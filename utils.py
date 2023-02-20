import json


def load_json(filename):
    with open(filename, encoding='utf-8') as file:
        data = json.load(file)
    return data

def get_posts_by_user(user_name, posts):
    user_posts = []
    for post in posts:
        if post['poster_name'] == user_name:
            user_posts.append(post)
    return user_posts

def get_text(posts):
    for user in posts:
        user["content50"] = user["content"][0:51] + '...'
    return posts

def get_comments_by_post_id(post_id, comments):
    feedback = []

    for comment in comments:
        if comment['post_id'] == post_id:
            feedback.append(comment)
    return feedback

def search_for_posts(query, posts):
    posts_word = []
    for post in posts:
        if query in post['content']:
            posts_word.append(post)
    return posts_word

def get_post_by_pk(pk, posts):
    for post in posts:
        if post['pk'] == pk:
            return post

# load_json('data/posts.json') - возвращает все посты, аналогично get_posts_all()
# get_posts_by_user('leo', load_json('data/posts.json'))) - выводит все посты от пользователя
# get_comments_by_post_id(1, load_json('data/comments.json')) - выводит все комментарии
# search_for_posts('кот', load_json('data/posts.json')) - вывод постов по ключевому слову
# get_post_by_pk(1, load_json('data/posts.json')) - вывод поста по порядковому элементу