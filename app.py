import datetime
import os
import random
import re
import string
import uuid

from flask import Flask, request, render_template, abort, redirect
from extensions import db
from markupsafe import escape
from models.models import Link
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(app.instance_path, 'database.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

@app.route('/', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        original_url = request.form['url']
        if is_url(original_url):
            short_code = random_short_code()
            link = create_link(original_url, short_code)
            add_link_database(link)


            new_short_url = generate_shorten_url(short_code)
            return render_template("index.html", operation_completed=True, link=new_short_url)
        else:
            return f'<p>IS NOT A LINK</p>'
    else:
        return render_template("index.html")


@app.route('/r/<path:shortcode>')
def handle_redirect(shortcode):
    link = Link.query.filter_by(short_code=f'{escape(shortcode)}').first()
    if link:
        return redirect(link.original_url)
    return abort(404)


def generate_shorten_url(code):
    PAGE_PATH = 'http://127.0.0.1:5000/r/'
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


def random_short_code():
    letters = ''.join(random.choices(string.ascii_letters, k=4))
    nums = str(uuid.uuid4().clock_seq_low) + str(uuid.uuid4().clock_seq_hi_variant)
    code = letters + nums
    return code


def is_url(string) -> bool:
    pattern = r'^(https?:\/\/)?([a-zA-Z0-9-]+\.)+[a-zA-Z]{2,}(\/\S*)?$'
    return re.match(pattern, string) is not None


with app.app_context():
    db.create_all()











