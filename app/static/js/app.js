const messagesDiv = document.getElementById("messages");
const form = document.getElementById("chat-form");
const userInput = document.getElementById("user-input");

// Function to append a message to the chat
function appendMessage(text, type) {
    const messageDiv = document.createElement("div");
    messageDiv.classList.add(type === "user" ? "user" : "ai");
    messageDiv.textContent = text;
    messagesDiv.appendChild(messageDiv);
}

// Fetch existing messages on page load
async function fetchMessages() {
    try {
        const response = await fetch("/api/messages");
        if (!response.ok) throw new Error("Failed to fetch messages");
        const messages = await response.json();

        // Append each message to the chat
        messages.forEach((message) => {
            appendMessage(message.text, message.type);
        });

        // Scroll to the bottom of the chat
        messagesDiv.scrollTop = messagesDiv.scrollHeight;
    } catch (error) {
        console.error("Error fetching messages:", error);
    }
}

// Submit handler for sending new messages
form.addEventListener("submit", async (e) => {
    e.preventDefault();

    const userMessage = userInput.value.trim();
    if (!userMessage) return;

    // Clear input immediately
    userInput.value = "";

    // Add user message to chat
    appendMessage(userMessage, "user");

    // Send to backend
    try {
        const response = await fetch("/api/message", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ message: userMessage }),
        });

        if (!response.ok) throw new Error("Failed to send message");
        const data = await response.json();

        // Add bot response to chat
        appendMessage(data.response, "ai");
    } catch (error) {
        console.error("Error sending message:", error);
    }

    // Clear input and scroll to the bottom
    userInput.value = "";
    messagesDiv.scrollTop = messagesDiv.scrollHeight;
});

// Load existing messages on page load
fetchMessages();
