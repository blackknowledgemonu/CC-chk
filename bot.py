import telebot, time, os, re, json, random, threading
from telebot import types
import requests

# —————————— IMPORT YOUR FILE LOGIC —————————— #
try:
    from my_braintree import process_card_b 
    from braintree_dual_checker import ali1
    from check_bins_fun import extract_bins
except ImportError as e:
    print(f"⚠️ Error: Kuch files missing hain: {e}")

# —————————— BOT SETTINGS —————————— #
TOKEN = "8662492230:AAHerwQ0PlavJ3rwn7zxsE6g-MnmJbJqXrg"
admin_id = 1677950104
bot = telebot.TeleBot(TOKEN, parse_mode='html')

# —————————— HELPER FUNCTIONS —————————— #
def get_cards(text):
    return re.findall(r'\d{15,16}[\s|:|/|-]\d{1,2}[\s|:|/|-]\d{2,4}[\s|:|/|-]\d{3,4}', text)

# —————————— COMMANDS —————————— #

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(
        types.InlineKeyboardButton("👑 OWNER", callback_data="admin"),
        types.InlineKeyboardButton("💳 CC CHECK", callback_data="cc")
    )
    bot.send_message(message.chat.id, "<b>Bot is Online! ❤️🇪🇬</b>\nSaare commands active hain.", reply_markup=markup)

# 1. Check Card (/chk, /str, /chk3)
@bot.message_handler(commands=['chk', 'str', 'chk3'])
def check_handler(message):
    cards = get_cards(message.text)
    if not cards:
        return bot.reply_to(message, "❌ Format: <code>/chk cc|mm|yy|cvv</code>")
    
    cc = cards[0]
    status_msg = bot.reply_to(message, f"⌛ <b>Checking:</b> <code>{cc}</code>")
    
    try:
        # Aapki file 'braintree_dual_checker.py' ka logic call ho raha hai
        result = ali1(cc) 
        bot.edit_message_text(f"<b>💳 RESULT</b>\n\n<code>{result}</code>", message.chat.id, status_msg.message_id)
    except Exception as e:
        bot.edit_message_text(f"❌ Error: {str(e)}", message.chat.id, status_msg.message_id)

# 2. BIN Lookup (/bin)
@bot.message_handler(commands=['bin'])
def bin_handler(message):
    try:
        bin_num = re.findall(r'\d{6}', message.text)[0]
        # Aapki file 'check_bins_fun.py' ka logic call ho raha hai
        data = extract_bins(bin_num)
        bot.reply_to(message, f"<b>🔍 BIN INFO</b>\n\n<code>{data}</code>")
    except:
        bot.reply_to(message, "❌ Use: <code>/bin 458456</code>")

# 3. Filter BIN from File (/filter)
@bot.message_handler(commands=['filter'])
def filter_handler(message):
    try:
        args = message.text.split(' ')
        target_bin = args[1]
        bot.reply_to(message, f"📥 Ab wo combo file bhejo jisme se <code>{target_bin}</code> filter karna hai.")
    except:
        bot.reply_to(message, "❌ Format: <code>/filter 458456</code>")

# 4. Combo Len (/len)
@bot.message_handler(commands=['len'])
def len_handler(message):
    bot.reply_to(message, "📊 Combo file bhejiye lines check karne ke liye.")

# 5. File Handling (For /file, /filter, /mix)
@bot.message_handler(content_types=['document'])
def handle_file(message):
    file_info = bot.get_file(message.document.file_id)
    downloaded_file = bot.download_file(file_info.file_path)
    content = downloaded_file.decode('utf-8')
    
    cards = get_cards(content)
    bot.reply_to(message, f"✅ <b>File Received!</b>\nTotal Cards Found: <code>{len(cards)}</code>\nProcessing Start...")

# —————————— CALLBACKS —————————— #
@bot.callback_query_handler(func=lambda call: True)
def calls(call):
    if call.data == "cc":
        bot.answer_callback_query(call.id, "Send /chk command to check cards.")
    elif call.data == "admin":
        if call.from_user.id == admin_id:
            bot.send_message(call.message.chat.id, "👑 <b>Admin Panel Active.</b>")
        else:
            bot.answer_callback_query(call.id, "❌ Not Owner!", show_alert=True)

# —————————— START —————————— #
if __name__ == '__main__':
    print("🚀 Bot with full logic is starting...")
    bot.infinity_polling(none_stop=True)
