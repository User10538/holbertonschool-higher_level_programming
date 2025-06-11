from flask import Flask, jsonify, request
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import (
    JWTManager, create_access_token, jwt_required,
    get_jwt_identity, get_jwt
)
from datetime import timedelta

# Flask setup
app = Flask(__name__)
auth = HTTPBasicAuth()

app.config['JWT_SECRET_KEY'] = 'super-secret-key'  # Use env var in production!
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = timedelta(hours=1)
jwt = JWTManager(app)

# In-memory user database
users = {
    "user1": {"username": "user1", "password": generate_password_hash("password"), "role": "user"},
    "admin1": {"username": "admin1", "password": generate_password_hash("password"), "role": "admin"}
}

# Basic Auth verification
@auth.verify_password
def verify_password(username, password):
    if username in users and check_password_hash(users[username]['password'], password):
        return username
    return None

@auth.error_handler
def handle_auth_error():
    return jsonify({"error": "Unauthorized access"}), 401

# Route: Basic Auth Protected
@app.route('/basic-protected')
@auth.login_required
def basic_protected():
    return "Basic Auth: Access Granted"

# Route: JWT Login
@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")

    if username not in users or not check_password_hash(users[username]['password'], password):
        return jsonify({"error": "Invalid credentials"}), 401

    access_token = create_access_token(identity={
        "username": username,
        "role": users[username]['role']
    })
    return jsonify(access_token=access_token)

# Route: JWT Protected
@app.route('/jwt-protected')
@jwt_required()
def jwt_protected():
    identity = get_jwt_identity()
    return f"JWT Auth: Access Granted for {identity['username']}"

# Route: Admin-only
@app.route('/admin-only')
@jwt_required()
def admin_only():
    identity = get_jwt_identity()
    if identity['role'] != 'admin':
        return jsonify({"error": "Admin access required"}), 403
    return "Admin Access: Granted"

# JWT Error Handlers
@jwt.unauthorized_loader
def handle_unauthorized_error(err):
    return jsonify({"error": "Missing or invalid token"}), 401

@jwt.invalid_token_loader
def handle_invalid_token_error(err):
    return jsonify({"error": "Invalid token"}), 401

@jwt.expired_token_loader
def handle_expired_token_error(jwt_header, jwt_payload):
    return jsonify({"error": "Token has expired"}), 401

@jwt.revoked_token_loader
def handle_revoked_token_error(jwt_header, jwt_payload):
    return jsonify({"error": "Token has been revoked"}), 401

@jwt.needs_fresh_token_loader
def handle_needs_fresh_token_error(jwt_header, jwt_payload):
    return jsonify({"error": "Fresh token required"}), 401

# Entry point
if __name__ == '__main__':
    app.run(debug=True)
