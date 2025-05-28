# 🤖 Gemini Multi-Turn Chat (Console-Based)

This project is a simple Python script that demonstrates how to build a **multi-turn chatbot using Google's Gemini API**. It maintains conversation context between turns and allows basic control over model behavior like temperature.

---

## 🚀 What This Script Does

- Initializes a Gemini chat session using the `google.generativeai` library.
- Prompts the user for two or more inputs and maintains the conversation context.
- Sends all messages to the Gemini model with preserved history.
- Prints the model's final response after the last user input.
- Supports setting the model temperature for more or less creativity.

---

## ⚙️ How to Run

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/gemini-multi-turn-chat.git
cd gemini-multi-turn-chat
```
### 2. Create and Activate a Virtual Environment (Optional but Recommended)
```bash
python -m venv venv
venv\Scripts\activate  # On Windows
#Or
source venv/bin/activate  # On macOS/Linux
```
### 3. Install Requirements
```bash
pip install -r requirements.txt
```
### 4. Add Your Gemini API Key
Create a .env file in the root folder and add your API key like this:
```bash
GEMINI_API_KEY=your-api-key-here
```
### You can get your Gemini API key from: https://makersuite.google.com/app/apikey

### ▶️ Run the Script
```bash
python gemini_chat.py
```
### You’ll see prompts like:
```bash
Set temperature (e.g. 0.5 for balanced response): 0.7
You: What is the future of AI?
You: And what jobs might be most affected?
Gemini: The future of AI is evolving rapidly, and certain industries...
```
## 🧪 Features
🔁 Maintains multi-turn conversation context

🎛️ Allows adjusting temperature for creativity level

📦 Uses .env for secure API key handling

🧼 No GUI needed — console only
