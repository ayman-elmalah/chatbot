from datetime import datetime
from langchain_openai import ChatOpenAI
from app.models.message import Message
from app import db
from langchain.memory import ConversationBufferMemory

# Initialize the AI model
model = ChatOpenAI(model="gpt-3.5-turbo")


# Initialize the memory to store the conversation
def initialize_memory(user_id):
    # Fetch conversation history for the user from the database
    messages = Message.query.filter_by(user_id=user_id).order_by(Message.id).all()

    # Initialize ConversationBufferMemory
    memory = ConversationBufferMemory(memory_key="chat_history")

    # Add system and user messages to memory (SystemMessage could be set depending on your app's logic)
    for message in messages:
        if message.type == 'user':
            memory.save_context({"input": message.text},
                                {"output": ""})  # Just save user input, AI response will be added after
        elif message.type == 'ai':
            memory.save_context({"input": ""}, {"output": message.text})  # Save AI response here

    return memory


def handle_message_service(user_id, user_message):
    """Service to handle message logic."""

    # Save user message to the database
    user_message_entry = Message(
        text=user_message,
        type='user',
        user_id=user_id,
        timestamp=datetime.now()
    )
    db.session.add(user_message_entry)
    db.session.commit()

    # Initialize memory
    memory = initialize_memory(user_id)

    # Save user message to memory (similar to adding it to the conversation history)
    memory.save_context({"input": user_message}, {"output": ""})

    # Extract the list of messages from the memory
    messages = memory.buffer_as_messages  # Get the conversation history as a list of messages

    # Get AI response using the messages list
    ai_response = model.invoke(messages)

    # Save AI response to memory (this will add the AI response after the user message)
    memory.save_context({"input": ""}, {"output": ai_response.content})

    # Save AI response to the database
    ai_message_entry = Message(
        text=ai_response.content,
        type='ai',
        user_id=user_id,
        timestamp=datetime.now()
    )
    db.session.add(ai_message_entry)
    db.session.commit()

    # Return the AI response
    return ai_response.content
