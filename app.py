from logging import debug
from flask import Flask, render_template, request
from flask_cors import CORS
from models import get_posts, create_post

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    template = "index.html"

    if request.method == 'GET':
        pass

    if request.method == 'POST':
        form_name = request.form.get('user_name')
        form_post = request.form.get('user_post')

        create_post(form_name, form_post)

    user_posts = get_posts()

    print(user_posts)

    return render_template(template, user_posts=user_posts)


if __name__ == "__main__":
    app.run(debug=True)
