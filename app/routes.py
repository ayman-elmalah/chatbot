from flask import Blueprint, render_template, request, jsonify, make_response
import uuid
from app.models.user import User
from app import db

# Blueprint for UI routes
ui_bp = Blueprint("ui", __name__)

@ui_bp.route("/")
def index():
    """Render the chatbot UI."""
    # Check for session ID in cookies
    session_id = request.cookies.get("session_id")

    # Print the session_id for debugging purposes
    print(f"Session ID from cookies: {session_id}")

    if not session_id:
        # Generate a new unique session ID
        session_id = str(uuid.uuid4())

        # Create a new user in the database with this session ID
        new_user = User(session_id=session_id)
        db.session.add(new_user)
        db.session.commit()

        # Set the session ID in cookies
        response = make_response(render_template("index.html"))
        response.set_cookie("session_id", session_id, httponly=True, secure=True)
        print(f"New session ID generated: {session_id}")
        return response

    # If session ID exists, just render the page
    return render_template("index.html")

@ui_bp.route("/api/message", methods=["POST"])
def message():
    """Handle user messages."""
    user_message = request.json.get("message", "")
    # Mock response for now
    bot_response = f"You said: {user_message}"
    return jsonify({"response": bot_response})
