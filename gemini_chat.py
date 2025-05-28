import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

genai.configure(api_key=GOOGLE_API_KEY)

model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    generation_config={
        "temperature": 0.7,
        "top_p": 1.0,
        "top_k": 1,
        "max_output_tokens": 2048,
    }
)

chat = model.start_chat(history=[])

print("💬 Gemini Multi-turn Chat\n(Type 'exit' to stop)\n")

while True:
    user_input = input("You: ")
    if user_input.lower() in {"exit", "quit"}:
        print("Ending chat. Goodbye!")
        break

    response = chat.send_message(user_input)
    print(f"Gemini: {response.text}")
