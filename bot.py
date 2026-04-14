import telebot, time, os, re, json, threading
from telebot import types

# —————————— LOCAL FILE IMPORTS —————————— #
try:
    # GitHub par ye files hona zaroori hai
    from my_braintree import process_card_b 
    from braintree_dual_checker import ali1
    from check_bins_fun import extract_bins
except ImportError as e:
    print(f"⚠️ Warning: Some local files are missing: {e}")

# —————————— BOT SETTINGS —————————— #
TOKEN = "8662492230:AAHerwQ0PlavJ3rwn7zxsE6g-MnmJbJqXrg"
admin_id = 1677950104
bot = telebot.TeleBot(TOKEN, parse_mode='html')

# —————————— KEYBOARDS —————————— #
def main_menu():
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(
        types.InlineKeyboardButton("👑 OWNER", callback_data="admin"),
        types.InlineKeyboardButton("💳 CC CHECK", callback_data="cc"),
        types.InlineKeyboardButton("🔍 SCRAP", callback_data="scr"),
        types.InlineKeyboardButton("⚙️ COMBO", callback_data="combo")
    )
    return markup

# —————————— COMMANDS —————————— #

@bot.message_handler(commands=['start'])
def start_cmd(message):
    bot.send_video(
        message.chat.id,
        video="https://t.me/cccjwowowow/85",
        caption="<b>𝘄𝗲𝗹𝗰𝗼𝗺𝗲 𝘁𝗼 𝘁𝗵𝗲 𝗯𝗼𝘁 ❤️🇪🇬</b>\n\nStatus: 🟢 <code>Online</code>\nAdmin ID: <code>1677950104</code>",
        reply_markup=main_menu()
    )

# 🔍 BIN Lookup Command (/bin 458456)
@bot.message_handler(commands=['bin'])
def bin_handler(message):
    try:
        bin_num = message.text.split(' ')[1]
        result = extract_bins(bin_num) # check_bins_fun.py call ho rahi hai
        bot.reply_to(message, f"<b>🔍 BIN LOOKUP</b>\n\n<code>{result}</code>")
    except:
        bot.reply_to(message, "❌ Format: <code>/bin 458456</code>")

# 💳 Braintree Dual Command (/chk3 cc|mm|yy|cvv)
@bot.message_handler(commands=['chk3'])
def chk_handler(message):
    try:
        cc_data = message.text.split(' ')[1]
        msg = bot.reply_to(message, "⌛ <b>Checking your card... Please wait.</b>")
        
        # braintree_dual_checker.py se ali1 function call ho raha hai
        response = ali1(cc_data) 
        bot.edit_message_text(f"<b>💳 CC RESULT:</b>\n\n<code>{response}</code>", message.chat.id, msg.message_id)
    except:
        bot.reply_to(message, "❌ Format: <code>/chk3 cc|mm|yy|cvv</code>")

# —————————— CALLBACK HANDLERS —————————— #

@bot.callback_query_handler(func=lambda call: True)
def handle_callbacks(call):
    if call.data == "cc":
        bot.edit_message_caption(
            caption="─────── 💳 <b>Card Check Menu</b> ───────\n\n/chk3 - Braintree Dual\n/str - Stripe Charge\n/bin - BIN Lookup", 
            chat_id=call.message.chat.id, 
            message_id=call.message.message_id, 
            reply_markup=main_menu()
        )
    elif call.data == "admin":
        if call.from_user.id == admin_id:
            bot.answer_callback_query(call.id, "Welcome Boss!", show_alert=False)
        else:
            bot.answer_callback_query(call.id, "❌ Only Owner Access!", show_alert=True)

# —————————— START —————————— #
if __name__ == '__main__':
    print("🚀 All functions integrated! Bot is starting...")
    bot.infinity_polling(none_stop=True)
