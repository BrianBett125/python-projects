import google.generativeai as genai
import os

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-pro")

while True:
    prompt = input("You: ")
    if prompt.lower() in ["exit", "quit"]:
        break

    response = model.generate_content(prompt)
    print("Gemini:", response.text)
