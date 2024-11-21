from flask import Blueprint, render_template, request, jsonify

# Blueprint for UI routes
ui_bp = Blueprint("ui", __name__)

@ui_bp.route("/")
def index():
    """Render the chatbot UI."""
    return render_template("index.html")

@ui_bp.route("/api/message", methods=["POST"])
def message():
    """Handle user messages."""
    user_message = request.json.get("message", "")
    # Mock response for now
    bot_response = f"You said: {user_message}"
    return jsonify({"response": bot_response})
