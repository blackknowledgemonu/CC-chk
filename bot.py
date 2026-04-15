import telebot
import logging
from bin_info_v1 import bin_info  # Aapki file ka sahi function name
from sk_check import check_key
from braintree_Api import main as braintree_chk

# --- CONFIGURATION ---
TOKEN = "8662492230:AAHerwQ0PlavJ3rwn7zxsE6g-MnmJbJqXrg" # Apna token yahan replace karein
admin_id = 1630132104 

bot = telebot.TeleBot(TOKEN, parse_mode="HTML")
logging.basicConfig(level=logging.INFO)

# --- START COMMAND ---
@bot.message_handler(commands=['start'])
def start(message):
    welcome = (
        "<b>🔥 Black Knowledge Multi-Bot V1</b>\n\n"
        "Status: <code>Online ✅</code>\n"
        "Owner: @BLACK_KNOWLEDGE_190\n\n"
        "<b>Commands:</b>\n"
        "💳 /chk <code>card|mm|yy|cvv</code>\n"
        "🔍 /bin <code>444444</code>\n"
        "🔑 /sk <code>sk_live_xxx</code>"
    )
    bot.reply_to(message, welcome)

# --- BIN LOOKUP ---
@bot.message_handler(commands=['bin'])
def bin_handler(message):
    args = message.text.split()
    if len(args) < 2:
        return bot.reply_to(message, "❌ BIN dijiye. Example: <code>/bin 444444</code>")
    
    sent = bot.reply_to(message, "🔍 <b>Searching BIN...</b>")
    try:
        # Aapki 'bin_info_v1.py' file ka function call
        res = bin_info(args[1][:6])
        bot.edit_message_text(f"📌 <b>BIN Result:</b>\n\n<code>{res}</code>", message.chat.id, sent.message_id)
    except Exception as e:
        bot.edit_message_text(f"❌ Error: {str(e)}", message.chat.id, sent.message_id)

# --- SK KEY CHECK ---
@bot.message_handler(commands=['sk'])
def sk_handler(message):
    args = message.text.split()
    if len(args) < 2:
        return bot.reply_to(message, "❌ Key missing!")
    
    sent = bot.reply_to(message, "🔑 <b>Checking Key...</b>")
    try:
        res = check_key(args[1])
        bot.edit_message_text(f"📝 <b>SK Result:</b>\n\n<code>{res}</code>", message.chat.id, sent.message_id)
    except Exception as e:
        bot.edit_message_text("❌ Key Invalid ya API Error.", message.chat.id, sent.message_id)

# --- CHECK CARD (BRAINTREE/STRIPE) ---
@bot.message_handler(commands=['chk'])
def chk_handler(message):
    args = message.text.split()
    if len(args) < 2:
        return bot.reply_to(message, "❌ Format: <code>/chk card|mm|yy|cvv</code>")
    
    sent = bot.reply_to(message, "⏳ <b>Processing...</b>")
    try:
        # Aapki braintree_Api.py ka main function call
        res = braintree_chk(args[1])
        bot.edit_message_text(f"💳 <b>Gate: Braintree</b>\n\n<code>{res}</code>", message.chat.id, sent.message_id)
    except Exception as e:
        bot.edit_message_text("❌ Card decline ya Gateway error.", message.chat.id, sent.message_id)

# --- RUN BOT ---
if __name__ == "__main__":
    print("✅ Bot Started Successfully!")
    bot.send_message(admin_id, "🚀 <b>Bot is Live, Master!</b>")
    bot.infinity_polling()
    
