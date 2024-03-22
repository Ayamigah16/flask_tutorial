from flask import Flask, url_for, request
from markupsafe import escape       # to prevent output info from injection

# app name as filename
app = Flask(__name__)

# route decorator for url triggering

@app.route("/user/<name>")
def show_user_profile(name):
    # show user rofile
    return f"User {escape(name)}"

@app.route("/")
def home():
    return "<h1>You are Welcome</h1>"

"""
Converter Types:
string, int, float, path, uuid
"""

@app.route("/post/<int:post_id>")
def show_post(post_id):
    # show post witha given id
    return f"Post {post_id}"

@app.route("/path/<path:subpath>")
def show_subpath(subpath):
    #show subpath after /path/
    return f"Subpath {escape(subpath)}"


# HTTP METHODS
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        pass ## return post method
    else:
        pass ##return get method

# Seprate HTTP views
@app.get('/login')
def login_get():
    return #show_the_login_form()

@app.post('/login')
def login_post():
    return #do_the_login()
# testing endpoints
# with app.test_request_context():
#     print(url_for('home'))
#     print(url_for("show_user_profile", name="Abraham Ayamigah"))
#     print(url_for("show_post", post_id=300))