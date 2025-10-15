from flask import Flask, request, jsonify
from flask_cors import CORS
import openai

app = Flask(__name__)
CORS(app)  # Allow cross-origin requests from frontend

# Replace with your OpenAI API key
openai.api_key = "YOUR_OPENAI_API_KEY"

@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.json.get("message", "").lower()

    # Check for personal question about creator
    if "who made you" in user_message or "creator" in user_message or "owner" in user_message:
        reply = "I was created by Abhinav Kumar Prem. 💻"
    else:
        # Normal ChatGPT response
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are GENBOT V7, a helpful chatbot."},
                {"role": "user", "content": user_message}
            ]
        )
        reply = response['choices'][0]['message']['content']

    return jsonify({"reply": reply})

if __name__ == "__main__":
    app.run(debug=True)
