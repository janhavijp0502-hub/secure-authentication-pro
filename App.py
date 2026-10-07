from flask import Flask, request, render_template_string, redirect, session
from werkzeug.security import generate_password_hash, check_password_hash
import time

app = Flask(__name__)
app.secret_key = "change-this-secret-key"

# Secure session settings
app.config["SESSION_COOKIE_HTTPONLY"] = True
app.config["SESSION_COOKIE_SAMESITE"] = "Lax"
app.config["PERMANENT_SESSION_LIFETIME"] = 300

users = {}
login_attempts = {}

HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>Secure Authentication</title>
</head>
<body>
    <h1>Secure Authentication Project</h1>

    {% if user %}
        <h3>Welcome, {{ user }}</h3>
        <a href="/logout">Logout</a>
    {% else %}
        <h3>Register</h3>
        <form method="POST" action="/register">
            <input name="username" placeholder="Username" required>
            <input name="password" type="password"
                   placeholder="Password" required>
            <button>Register</button>
        </form>

        <h3>Login</h3>
        <form method="POST" action="/login">
            <input name="username" placeholder="Username" required>
            <input name="password" type="password"
                   placeholder="Password" required>
            <button>Login</button>
        </form>

        {% if message %}
            <p>{{ message }}</p>
        {% endif %}
    {% endif %}
</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(
        HTML,
        user=session.get("username"),
        message=None
    )

@app.route("/register", methods=["POST"])
def register():
    username = request.form.get("username", "").strip()
    password = request.form.get("password", "")

    # Server-side validation
    if len(username) < 3 or len(username) > 30:
        return render_template_string(
            HTML, user=None,
            message="Invalid username."
        )

    if len(password) < 8:
        return render_template_string(
            HTML, user=None,
            message="Password must contain at least 8 characters."
        )

    if username in users:
        return render_template_string(
            HTML, user=None,
            message="Registration failed."
        )

    # Password hashing
    users[username] = generate_password_hash(password)

    return redirect("/")

@app.route("/login", methods=["POST"])
def login():
    username = request.form.get("username", "").strip()
    password = request.form.get("password", "")

    ip = request.remote_addr or "
