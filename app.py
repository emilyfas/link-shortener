import datetime
import os
import random
import re
import string
import uuid

from flask import Flask, request, render_template
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
            '''
            link = create_link(original_url)
            add_link_database(link)
            return render_template("index.html", links = Link.query.all())
            '''
            return f'<p>IS A LINK</p>'
        else:
            return f'<p>IS NOT A LINK</p>'
    else:
        return f'<a href="{generate_shorten_url(random_short_code())}" target="_blank">link</a>'
        # return render_template("index.html")


@app.route('/redirect/<path:shortenurl>')
def redirect(shortenurl):
    return f'CODIGO: {escape(shortenurl)}'



def generate_shorten_url(code):
    PAGE_PATH = 'http://127.0.0.1:5000/redirect/'
    shorten_url = PAGE_PATH + code
    return shorten_url


def add_link_database(link:Link):
    db.session.add(link)
    db.session.commit()


def create_link(url) -> Link:
    return Link(
        original_url = url,
        short_code = random_short_code(),
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











