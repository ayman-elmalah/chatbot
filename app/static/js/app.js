const messagesDiv = document.getElementById("messages");
const form = document.getElementById("chat-form");
const userInput = document.getElementById("user-input");

form.addEventListener("submit", async (e) => {
    e.preventDefault();

    const userMessage = userInput.value;

    // Add user message to chat
    const userMessageDiv = document.createElement("div");
    userMessageDiv.textContent = `You: ${userMessage}`;
    messagesDiv.appendChild(userMessageDiv);

    // Send to backend
    const response = await fetch("/api/message", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ message: userMessage }),
    });
    const data = await response.json();

    // Add bot response to chat
    const botMessageDiv = document.createElement("div");
    botMessageDiv.textContent = `Bot: ${data.response}`;
    messagesDiv.appendChild(botMessageDiv);

    // Clear input
    userInput.value = "";
    messagesDiv.scrollTop = messagesDiv.scrollHeight;
});
