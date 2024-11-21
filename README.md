# Chatbot Project

This project is a scalable chatbot built using Flask. It provides an interactive interface for users to communicate with a chatbot. The chatbot is designed to be easily extendable, and integrated with AI capabilities for enhanced user experiences. This project serves as the front-end interface for interacting with a backend service, and it can be expanded to include AI-driven conversations powered by services like OpenAI or Langchain.

## Table of Contents
1. [Project Overview](#project-overview)
2. [Technologies Used](#technologies-used)
3. [Installation Guide](#installation-guide)
4. [Running the Application](#running-the-application)

## Project Overview

This project serves as a user interface for a chatbot. It allows users to input messages and receive responses from the chatbot, providing a foundation for integrating AI capabilities. 

### Current Features:
- Simple UI to interact with the chatbot.
- Integration with **AI models** like OpenAI's GPT or Langchain for advanced conversational abilities.
- The backend will process and generate responses using the AI model, enabling dynamic, context-aware conversations.
- Potential future integrations with voice recognition or other AI-driven features to enhance the interaction experience.

## Technologies Used

- **Flask**: Web framework for building the web application.
- **HTML/CSS**: For building the front-end UI.
- **JavaScript**: For dynamic interaction with the UI (AJAX).
- **AI Integration**: Integration with AI technologies such as Langchain and OpenAI for enhanced conversational AI features.

## Installation Guide

Follow these steps to set up the project on your local machine:

### Prerequisites:
- Python 3.x
- pip (Python package installer)

### 1. Clone the repository:
```bash
git clone https://github.com/ayman-elmalah/chatbot.git && cd chatbot
```

### 2. Install Dependencies:
Once your virtual environment is activated, install the required dependencies from `requirements.txt`:

```bash
pip install -r requirements.txt
```

### 3. Set Up the Environment Variables:
Make sure you have a `.env` file in the root of your project. You can use the `.env.example` file as a template. Here's an example:

```bash
cp .env.example .env
```


Ensure you replace all keys` with your own values.

---

## Running the Application

### 1. Run the Application:
Once the dependencies are installed and environment variables are set, you can start the Flask development server.

```bash
python3 run.py
```

Flask will start the application on the port specified in the `.env` file (default is 5000 if not set).

### 2. Access the Chatbot UI:
Open your browser and navigate to `http://localhost:5000` (or the port specified in your `.env` file) to interact with the chatbot UI.
