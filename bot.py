import telebot, time, os, re, json, threading, random
from telebot import types
import requests

# —————————— IMPORT LOCAL LOGIC —————————— #
try:
    # Aapki local files se functions connect kar rahe hain
    from my_braintree import process_card_b 
    from braintree_dual_checker import ali1
    from check_bins_fun import extract_bins
except ImportError as e:
    print(f"⚠️ Warning: Kuch files GitHub par missing hain: {e}")

# —————————— BOT SETTINGS —————————— #
TOKEN = "8662492230:AAHerwQ0PlavJ3rwn7zxsE6g-MnmJbJqXrg"
admin_id = 1677950104
bot = telebot.TeleBot(TOKEN, parse_mode='html')

# —————————— HELPER: CARD EXTRACTOR —————————— #
def get_cards(text):
    # Yeh function text me se CC|MM|YY|CVV nikalta hai
    return re.findall(r'\d{15,16}[\s|:|/|-]\d{1,2}[\s|:|/|-]\d{2,4}[\s|:|/|-]\d{3,4}', text)

# —————————— COMMAND HANDLERS —————————— #

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(
        types.InlineKeyboardButton("👑 OWNER", callback_data="admin"),
        types.InlineKeyboardButton("💳 CC CHECK", callback_data="cc")
    )
    bot.send_message(
        message.chat.id, 
        "<b>𝗕𝗼𝘁 𝗶𝘀 𝗢𝗻𝗹𝗶𝗻𝗲! ❤️🇪🇬</b>\n\nSaare commands active hain.\nExample: <code>/chk cc|mm|yy|cvv</code>", 
        reply_markup=markup
    )

# 1. 💳 CC CHECKER (/chk, /str, /chk3)
@bot.message_handler(commands=['chk', 'str', 'chk3'])
def check_cc(message):
    cards = get_cards(message.text)
    if not cards:
        return bot.reply_to(message, "❌ <b>Format Galat Hai!</b>\nUse: <code>/chk cc|mm|yy|cvv</code>")
    
    cc = cards[0]
    initial_msg = bot.reply_to(message, f"⌛ 𝗖𝗵𝗲𝗰𝗸𝗶𝗻𝗴: <code>{cc}</code>")
    
    try:
        # Aapki braintree_dual_checker.py file ka function call ho raha hai
        result = ali1(cc) 
        bot.edit_message_text(f"<b>💳 𝗖𝗖 𝗥𝗘𝗦𝗨𝗟𝗧</b>\n\n{result}", message.chat.id, initial_msg.message_id)
    except Exception as e:
        bot.edit_message_text(f"⚠️ 𝗘𝗿𝗿𝗼𝗿: {str(e)}", message.chat.id, initial_msg.message_id)

# 2. 🔍 BIN LOOKUP (/bin)
@bot.message_handler(commands=['bin'])
def bin_info(message):
    try:
        bin_num = re.findall(r'\d{6}', message.text)[0]
        # Aapki check_bins_fun.py file se data nikal rahe hain
        data = extract_bins(bin_num)
        bot.reply_to(message, f"<b>🔍 𝗕𝗜𝗡 𝗜𝗡𝗙𝗢</b>\n\n<code>{data}</code>")
    except:
        bot.reply_to(message, "❌ BIN format galat hai. Example: <code>/bin 458456</code>")

# 3. 📂 FILE/COMBO CHECKING (/file, /filestr)
@bot.message_handler(content_types=['document'])
def handle_combo(message):
    file_info = bot.get_file(message.document.file_id)
    downloaded_file = bot.download_file(file_info.file_path)
    
    try:
        content = downloaded_file.decode('utf-8')
        cards = get_cards(content)
        
        if not cards:
            return bot.reply_to(message, "❌ File me koi cards nahi mile.")
        
        bot.reply_to(message, f"✅ <b>File Received!</b>\nTotal Cards: <code>{len(cards)}</code>\nChecking start kar raha hoon...")
        
        # Yahan aap loop laga kar cards check kar sakte hain
    except Exception as e:
        bot.reply_to(message, f"⚠️ File error: {str(e)}")

# 4. ⚙️ TOOLS (/mix, /len, /filter)
@bot.message_handler(commands=['len'])
def count_lines(message):
    bot.reply_to(message, "📊 Combo file bhejiye count karne ke liye.")

@bot.message_handler(commands=['filter'])
def filter_bin(message):
    bot.reply_to(message, "🛠️ Specific BIN filter karne ke liye file ke sath <code>/filter 458456</code> likhein.")

# —————————— ADMIN & CALLBACKS —————————— #

@bot.callback_query_handler(func=lambda call: True)
def handle_clicks(call):
    if call.data == "cc":
        bot.answer_callback_query(call.id, "Send CC details with /chk")
    elif call.data == "admin":
        if call.from_user.id == admin_id:
            bot.send_message(call.message.chat.id, "👑 <b>Welcome Boss!</b> Admin commands active.")
        else:
            bot.answer_callback_query(call.id, "❌ Not Owner!", show_alert=True)

# —————————— START POLLING —————————— #
if __name__ == '__main__':
    print("▶️ Bot is running with ALL functions...")
    try:
        bot.send_message(admin_id, "✅ 𝗕𝗼𝘁 𝗶𝘀 𝗢𝗡𝗟𝗜𝗡𝗘 with Full Logic!")
    except: pass
    bot.infinity_polling(none_stop=True)
  
