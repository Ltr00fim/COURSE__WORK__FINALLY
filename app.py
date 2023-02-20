from flask import Flask, render_template, request, jsonify
from utils import *
import logging


app = Flask(__name__)
logging.basicConfig(level=logging.INFO, filename="api.log")

@app.route('/')
@app.route('/skyprogram/', methods=["POST", "GET"])
def index():
    logging.info("Главная страница запрошена")
    return render_template("index.html", posts=get_text(load_json('data/posts.json')))


@app.route("/skyprogram/post/<post_id>", methods=["POST", "GET"])
def post(post_id):
    logging.info(f"Страница поста {post_id} запрошена")

    need_post = get_post_by_pk(int(post_id), load_json('data/posts.json'))
    need_comments = get_comments_by_post_id(int(post_id), load_json('data/comments.json'))
    return render_template('post.html', post=need_post, comments=need_comments, len_comments=len(need_comments))


@app.route("/skyprogram/search/", methods=["POST", "GET"])
def search():
    word = request.form.get('find')
    posts = get_text(search_for_posts(word, load_json('data/posts.json')))
    number = len(posts)

    logging.info(f"Страница поиска по слову {word} запрошена")

    return render_template('search.html', posts=posts, number=number)

@app.route("/skyprogram/user-feed/<user_name>")
def user_feed(user_name):
    logging.info(f"Страница постов пользователя {user_name} запрошена")

    posts = get_text(get_posts_by_user(user_name, load_json('data/posts.json')))
    return render_template('user-feed.html', posts=posts)

@app.errorhandler(404)
def not_found_error(error):
    logging.info("Ошибка 404")

    return "<h1>sorry, mistake</h1>", 404


@app.errorhandler(500)
def internal_error(error):
    logging.info("Ошибка 500")

    return "<h1>sorry, mistake</h1>", 500

@app.route("/api/posts/")
def api():
    logging.info("Страница API всех постов запрошена")
    return jsonify(load_json('data/posts.json'))

@app.route("/api/posts/<int:post_id>")
def api_one(post_id):
    logging.info(f"Страница API поста {post_id} запрошена")
    return jsonify(load_json('data/posts.json')[post_id-1])

if __name__ == '__main__':
    app.run(debug=True)