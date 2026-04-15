import telebot
import logging
from bin_info_v1 import bin_info
from sk_check import check_key
from braintree_Api import main as braintree_main

# --- CONFIGURATION ---
TOKEN = "8662492230:AAHerwQ0PlavJ3rwn7zxsE6g-MnmJbJqXrg" 
admin_id = 1630132104 

bot = telebot.TeleBot(TOKEN, parse_mode="HTML")

# Logging setup takki terminal pe dikhe kya ho raha hai
logging.basicConfig(level=logging.INFO)

# --- START COMMAND ---
@bot.message_handler(commands=['start'])
def start(message):
    user_first_name = message.from_user.first_name
    welcome_msg = (
        f"<b>Hey {user_first_name}! Welcome to Black Knowledge Bot</b>\n\n"
        "✨ <b>Main Commands:</b>\n"
        "💳 <code>/chk card|mm|yy|cvv</code> - Braintree Check\n"
        "🔍 <code>/bin 444444</code> - BIN Lookup\n"
        "🔑 <code>/sk sk_live_xxx</code> - SK Key Check\n\n"
        "📢 <b>Channel:</b> @BLACK_KNOWLEDGE_190"
    )
    bot.reply_to(message, welcome_msg)

# --- BIN LOOKUP ---
@bot.message_handler(commands=['bin'])
def bin_handler(message):
    text = message.text.split()
    if len(text) < 2:
        return bot.reply_to(message, "❌ <b>BIN missing!</b> Example: <code>/bin 444444</code>")
    
    status = bot.reply_to(message, "🔍 <b>Searching BIN...</b>")
    try:
        # Aapki file bin_info_v1.py ka function call
        res = bin_info(text[1][:6])
        bot.edit_message_text(f"📌 <b>BIN RESULT:</b>\n\n<code>{res}</code>", message.chat.id, status.message_id)
    except Exception as e:
        bot.edit_message_text(f"❌ <b>Error:</b> {str(e)}", message.chat.id, status.message_id)

# --- SK CHECK ---
@bot.message_handler(commands=['sk'])
def sk_handler(message):
    text = message.text.split()
    if len(text) < 2:
        return bot.reply_to(message, "❌ <b>SK Key missing!</b>")
    
    status = bot.reply_to(message, "🔑 <b>Checking Key...</b>")
    try:
        # Aapki file sk_check.py ka function call
        res = check_key(text[1])
        bot.edit_message_text(f"📝 <b>SK RESULT:</b>\n\n<code>{res}</code>", message.chat.id, status.message_id)
    except Exception as e:
        bot.edit_message_text("❌ <b>Key Dead ya Invalid hai.</b>", message.chat.id, status.message_id)

# --- CARD CHECK (BRAINTREE) ---
@bot.message_handler(commands=['chk'])
def chk_handler(message):
    text = message.text.split()
    if len(text) < 2:
        return bot.reply_to(message, "❌ <b>Format:</b> <code>/chk card|mm|yy|cvv</code>")
    
    status = bot.reply_to(message, "⏳ <b>Checking Card...</b>")
    try:
        # Aapki file braintree_Api.py ka main function call
        # Ye function card data string leta hai
        res = braintree_main(text[1])
        bot.edit_message_text(f"💳 <b>GATE: BRAINTREE</b>\n\n<code>{res}</code>", message.chat.id, status.message_id)
    except Exception as e:
        bot.edit_message_text("❌ <b>Gateway Timeout ya Card Declined.</b>", message.chat.id, status.message_id)

# --- RUNNING THE BOT ---
if __name__ == "__main__":
    print("🚀 Black Knowledge Bot is Running...")
    try:
        # Admin ko alert bhejna
        bot.send_message(admin_id, "✅ <b>Master, the bot is now Live!</b>")
        bot.infinity_polling()
    except Exception as e:
        print(f"❌ Crash Error: {e}")
        
