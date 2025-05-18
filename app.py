import datetime
import os
import random
import re
import string
import uuid

from flask import Flask, request, render_template
from extensions import db
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(app.instance_path, 'database.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

@app.route('/', methods=['GET', 'POST'])
def getting_values():
    if request.method == 'POST':
        original_url = request.form['url']
        if is_url(original_url):
            link = create_link(original_url)
            add_link_database(link)
            return render_template("index.html", links = Link.query.all())
        else:
            return f'<p>IS NOT A LINK</p>'
    else:
        return render_template("index.html")


from models.models import Link

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











