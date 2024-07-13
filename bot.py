from pyrogram import Client, filters
from flask import Flask, request

app = Flask(__name__)
bot = Client("my_bot", api_id="1623073", api_hash="a6f2f0a7b2022f8ca7717d9101c5ff5c", bot_token="7078609429:AAG5lAS82y_hNSiSVPvpJx6xRRHmYW7kbhc")

# Handle the /start command
@bot.on_message(filters.command("start"))
def start(client, message):
    message.reply_text("Hello! I'm a bot. How can I help you?")

# Echo any text message
@bot.on_message(filters.text & ~filters.command("start"))
def echo(client, message):
    message.reply_text(message.text)

# Set webhook
@app.route('/webhook', methods=['POST'])
def webhook():
    update = request.get_json()
    bot.process_update(update)
    return '', 200

if __name__ == "__main__":
    bot.start()
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
