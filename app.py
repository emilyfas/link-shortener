import os
import re

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
            return f'<p>VALID LINK</p>'
        else:
            return f'<p>IS NOT A LINK</p>'
    else:
        return render_template("index.html")


def is_url(string) -> bool:
    pattern = r'^(https?:\/\/)?([a-zA-Z0-9-]+\.)+[a-zA-Z]{2,}(\/\S*)?$'
    return re.match(pattern, string) is not None


from models.models import Link

with app.app_context():
    db.create_all()











