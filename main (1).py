from flask import Flask, request, jsonify
import openai

app = Flask(__name__)

# ⚠️ Your OpenAI API key (use only in private environments)
import os
openai.api_key = os.environ.get("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")

@app.route('/analyze', methods=['POST'])
def analyze():
    data = request.json
    coin = data.get('coin', 'BTC').upper()

    prompt = f"""Give a short crypto analysis for {coin}:
- Market trend
- RSI estimate
- MACD signal
- Suggested entry price
- Stop-loss value
- Risk level (Low, Medium, High)

Format it cleanly for traders."""

    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "user", "content": prompt}
            ]
        )
        result = response['choices'][0]['message']['content']
        return jsonify({"coin": coin, "analysis": result})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/', methods=['GET'])
def home():
    return jsonify({
        "message": "✅ Crypto AI Backend is live. Use POST /analyze with JSON like {\"coin\": \"BTC\"}."
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
