from flask import Flask, request, jsonify, session
import sqlite3
from functools import wraps

app = Flask(__name__)
app.secret_key = "supersecretkey"  # Required for session

# ---------------------------
# Database Setup
# ---------------------------

import sqlite3

conn = sqlite3.connect("users.db")
cursor = conn.cursor()

cursor.execute("SELECT * FROM users")
rows = cursor.fetchall()

print("ID | Username | Password")
print("-" * 30)

for row in rows:
    print(row)

conn.close()

# def init_db():
#     conn = sqlite3.connect("users.db")
#     cursor = conn.cursor()

#     cursor.execute("""
#     CREATE TABLE IF NOT EXISTS users (
#         id INTEGER PRIMARY KEY AUTOINCREMENT,
#         username TEXT UNIQUE,
#         password TEXT
#     )
#     """)
    
#     conn.commit()
#     conn.close()

# init_db()


# ---------------------------
# Login Decorator
# ---------------------------
def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if "user" not in session:
            return jsonify({"message": "Unauthorized! Please login."}), 401
        return f(*args, **kwargs)
    return decorated_function


# ---------------------------
# Register API
# ---------------------------
@app.route("/register", methods=["POST"])
def register():
    data = request.get_json()
    username = data["username"]
    password = data["password"]

    try:
        conn = sqlite3.connect("users.db")
        cursor = conn.cursor()
        cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
        conn.commit()
        conn.close()

        return jsonify({"message": "User registered successfully"})
    
    except sqlite3.IntegrityError:
        return jsonify({"message": "User already exists"}), 400


# ---------------------------
# Login API
# ---------------------------
@app.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    username = data["username"]
    password = data["password"]

    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password))
    user = cursor.fetchone()
    conn.close()

    if user:
        session["user"] = username
        return jsonify({"message": "Login successful"})
    else:
        return jsonify({"message": "Invalid credentials"}), 401


# ---------------------------
# Protected Route
# ---------------------------
@app.route("/dashboard")
@login_required
def dashboard():
    return jsonify({"message": f"Welcome {session['user']}!"})


# ---------------------------
# Logout API
# ---------------------------
@app.route("/logout")
@login_required
def logout():
    session.pop("user", None)
    return jsonify({"message": "Logged out successfully"})


# ---------------------------
# Run Server
# ---------------------------
if __name__ == "__main__":
    app.run(debug=True)