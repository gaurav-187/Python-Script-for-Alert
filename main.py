from flask import Flask, request
import requests

app = Flask(__name__)

BOT_TOKEN = "8000527359:AAHCRanNCeJwcDBg9smYBnhKwpxPutJ-nsM"
CHAT_ID = "1215751286"

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.get_json()
    symbol = data.get('symbol', 'N/A')
    price = data.get('price', 'N/A')
    time = data.get('time', 'N/A')
    message = f"📈 BUY SIGNAL ALERT\n\n📊 Symbol: {symbol}\n💰 Price: {price}\n🕒 Time: {time}"
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    r = requests.post(url, json={'chat_id': CHAT_ID, 'text': message})
    return ("Alert sent to Telegram", 200) if r.ok else (r.text, 500)

if __name__ == '__main__':
    app.run(port=5000)
