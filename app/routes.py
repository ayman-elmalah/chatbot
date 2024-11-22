from flask import Blueprint, render_template, request, jsonify, make_response
import uuid
from app.models.user import User
from app.models.message import Message
from app import db
from app.services.message_service import handle_message_service

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

@ui_bp.route("/api/messages", methods=["GET"])
def get_messages():
    """Retrieve all messages for the current session."""
    session_id = request.cookies.get("session_id")

    if not session_id:
        return jsonify({"error": "Session not found"}), 400

    # Find the user by session_id
    user = User.query.filter_by(session_id=session_id).first()

    if not user:
        return jsonify({"error": "User not found"}), 404

    # Retrieve messages for the user
    messages = Message.query.filter_by(user_id=user.id).order_by(Message.id).all()

    # Convert messages to a serializable format
    serialized_messages = [
        {
            "text": message.text,
            "type": message.type,
            "timestamp": message.timestamp.isoformat(),
        }
        for message in messages
    ]

    return jsonify(serialized_messages), 200

@ui_bp.route("/api/message", methods=["POST"])
def message():
    """Handle user messages."""
    # Get the message from the request
    user_message = request.json.get("message", "")

    # Get the session ID from cookies
    session_id = request.cookies.get("session_id")

    if not session_id:
        return jsonify({"error": "Session not found"}), 400

    # Find the user
    user = User.query.filter_by(session_id=session_id).first()
    if not user:
        return jsonify({"error": "User not found"}), 404

    try:
        ai_response = handle_message_service(user.id, user_message)
        return jsonify({"response": ai_response}), 200
    except Exception as e:
        return jsonify({"error": "Failed to process the message", "details": str(e)}), 500
