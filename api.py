import os
import requests
from flask import Flask, request, jsonify

app = Flask(__name__)

OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")
OPENROUTER_URL = "https://openrouter.ai/api/v1/chat/completions"


@app.route("/chat", methods=["GET"])
def call_openrouter_chat_model():
    try:
        # Read inputs
        user_input = request.args.get("input")
        model_id = request.args.get("model_id")

        print("🟢 Received request:", user_input, model_id)

        headers = {
            "Authorization": f"Bearer {OPENROUTER_API_KEY}",
            "Content-Type": "application/json"
        }

        payload = {
            "model": model_id,
            "messages": [
                {"role": "user", "content": user_input}
            ]
        }

        print("📤 Sending payload to OpenRouter:", payload)

        response = requests.post(
            OPENROUTER_URL,
            json=payload,
            headers=headers
        )

        print("📥 OpenRouter returned status:", response.status_code)
        print("📥 OpenRouter raw response:", response.text)

        data = response.json()

        # -----------------------------
        # SAFE EXTRACTION OF BOT REPLY
        # -----------------------------
        bot_reply = None

        # Standard OpenAI/OpenRouter format
        if "choices" in data:
            try:
                bot_reply = data["choices"][0]["message"]["content"]
            except Exception:
                bot_reply = None

        # Alternative simple format
        elif "output_text" in data:
            bot_reply = data["output_text"]

        # If still no reply, return error
        if bot_reply is None:
            return jsonify({
                "error": "Model response missing expected fields.",
                "raw_response": data
            }), 500

        output = jsonify({"ack": bot_reply})
        output.headers.add("Access-Control-Allow-Origin", "*")
        return output

    except Exception as e:
        print("❌ ERROR:", str(e))
        return jsonify({"error": str(e)}), 500


@app.route("/ping", methods=["GET"])
def ping():
    output = jsonify({"ack": "pong"})
    output.headers.add("Access-Control-Allow-Origin", "*")
    return output


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5001))
    app.run(debug=True, host="0.0.0.0", port=port)
