const messagesDiv = document.getElementById("messages");
const form = document.getElementById("chat-form");
const userInput = document.getElementById("user-input");

// Function to append a message with a typing effect for AI response
function appendMessageWithTypingEffect(text, type) {
    const messageDiv = document.createElement("div");
    messageDiv.classList.add(type === "user" ? "user" : "ai");
    messagesDiv.appendChild(messageDiv);

    let index = 0;
    function typeNextCharacter() {
        if (index < text.length) {
            messageDiv.textContent += text.charAt(index);
            index++;
            setTimeout(typeNextCharacter, 10); // Adjust typing speed (30ms per character)
        } else {
            // Scroll to the bottom once typing is complete
            messagesDiv.scrollTop = messagesDiv.scrollHeight;
        }
    }
    typeNextCharacter();
}

// Function to append a message without a typing effect (e.g., for user messages)
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
        if (messages.length === 1 && messages[0].type === "ai") {
            // Apply typing effect if there's only one AI message
            appendMessageWithTypingEffect(messages[0].text, "ai");
        } else {
            messages.forEach((message) => {
                if (message.type === "ai") {
                    appendMessage(message.text, "ai");
                } else {
                    appendMessage(message.text, "user");
                }
            });
        }

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

        // Add bot response with typing effect
        appendMessageWithTypingEffect(data.response, "ai");
    } catch (error) {
        console.error("Error sending message:", error);
    }

    // Scroll to the bottom
    messagesDiv.scrollTop = messagesDiv.scrollHeight;
});

// Load existing messages on page load
fetchMessages();
