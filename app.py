import datetime
import os
import random
import re
import string
import uuid

from flask import Flask, request, render_template, abort, redirect
from extensions import db
from models.models import Link
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(app.instance_path, 'database.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

def is_url(txt) -> bool:
    if txt is None or not isinstance(txt, str):
        return False
    pattern = r"^(https?:\/\/)?([\da-z\.-]+)\.([a-z\.]{2,6})([\/\w\.-]*)*\/?$"
    return re.match(pattern, txt) is not None


def random_short_code():
    while True:
        letters = ''.join(random.choices(string.ascii_letters, k=4))
        nums = str(uuid.uuid4().clock_seq_low) + str(uuid.uuid4().clock_seq_hi_variant)
        code = letters + nums

        if not Link.query.filter_by(short_code=code).first():
            return code


def has_link_expired(link):
    creation_time = link.creation_date
    current_time = datetime.datetime.now()
    return current_time - creation_time > datetime.timedelta(days=7)


def generate_shorten_url(code):
    PAGE_PATH = request.host_url + 'r/'
    shorten_url = PAGE_PATH + code
    return shorten_url


def add_link_database(link:Link):
    db.session.add(link)
    db.session.commit()


def create_link(url, short_code) -> Link:
    return Link(
        original_url = url,
        short_code = short_code,
        creation_date = datetime.datetime.now()
    )


@app.route('/', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        original_url = request.form['url']
        if not original_url.strip():
            return render_template("index.html", operation_completed=False, error='Campo vazio!')
        if is_url(original_url):
            short_code = random_short_code()
            link = create_link(original_url, short_code)
            new_short_url = generate_shorten_url(short_code)
            add_link_database(link)
            return render_template("index.html", operation_completed=True, new_short_url=new_short_url, original_url= original_url)
        else:
            return render_template("index.html", operation_completed=False, error='Link Invalido!')
    else:
        return render_template("index.html")


@app.route('/r/<path:shortcode>')
def handle_redirect(shortcode):
    link = Link.query.filter_by(short_code=f'{shortcode}').first()
    if link:
        if has_link_expired(link):
            return render_template("link_expired.html")
        return redirect(link.original_url)
    return abort(404)


@app.route('/sobre')
def about_page():
    return render_template("about.html")


@app.route('/contato')
def contact_page():
    return render_template("contact.html")

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

with app.app_context():
    db.create_all()

