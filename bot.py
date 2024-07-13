from pyrogram import Client, filters
from flask import Flask, request

app = Flask(__name__)
bot = Client("my_bot", api_id="YOUR_API_ID", api_hash="YOUR_API_HASH", bot_token="YOUR_BOT_TOKEN")

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
