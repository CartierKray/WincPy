import os

from flask import Flask, redirect, render_template, request, session, url_for
from helpers import get_users, hash_password

__winc_id__ = "8fd255f5fe5e40dcb1995184eaa26116"
__human_name__ = "authentication"

app = Flask(__name__)

app.secret_key = os.urandom(16)


@app.route("/home")
def redirect_index():
    return redirect(url_for("index"))


@app.route("/")
def index():
    return render_template("index.html", title="Index")


@app.route("/about")
def about():
    return render_template("about.html", title="About")


@app.route("/lon")
def lon():
    return render_template("lon.html", title="League of Nations")


@app.route("/login", methods=["GET", "POST"])
def login():
    title = "Login"
    if request.method == "GET":
        error = request.args.get("error")
        return render_template("login.html", error=error, title=title)

    elif request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        users = get_users()

        if username in users:
            hashed_password = users[username]
            if hash_password(password) == hashed_password:
                # Store the username in the session
                session["username"] = username
                return redirect(url_for("dashboard"))

        return redirect(url_for("login", error=True))


@app.route("/dashboard")
def dashboard():
    if "username" in session:
        username = session["username"]

        # Customize the content based on the logged-in user
        if username == "Alice":
            greeting = "Hello, Alice!"
            additional_content = "This is Alice's dashboard."
        elif username == "Bob":
            greeting = "Hello, Bob!"
            additional_content = "This is Bob's dashboard."
        else:
            greeting = "Hello, User!"
            additional_content = "This is the default dashboard."

        return render_template("dashboard.html", greeting=greeting, additional_content=additional_content)
    else:
        return redirect(url_for("login"))


@app.route("/logout", methods=["GET", "POST"])
def logout():
    session.pop("username", None) # Remove the 'username' entry from the session
    return redirect(url_for("index")) # Redirect to the index route after logout

if __name__ == "__main__":
    app.run()