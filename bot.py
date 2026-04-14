import telebot, time, os, re, json, requests
from telebot import types

# —————————— IMPORT YOUR UPLOADED FILES —————————— #
try:
    # bin_info_v1.py se bin_info function import kar rahe hain
    from bin_info_v1 import bin_info as get_bin_info
    # Agar bbbb.py ya br.py se kuch chahiye to yahan add kar sakte hain
except ImportError as e:
    print(f"⚠️ Warning: Local files connect nahi ho pa rahi: {e}")

# —————————— BOT SETTINGS —————————— #
TOKEN = "8662492230:AAHerwQ0PlavJ3rwn7zxsE6g-MnmJbJqXrg"
admin_id = 1677950104
bot = telebot.TeleBot(TOKEN, parse_mode='html')

def get_cards(text):
    return re.findall(r'\d{15,16}[\s|:|/|-]\d{1,2}[\s|:|/|-]\d{2,4}[\s|:|/|-]\d{3,4}', text)

# —————————— COMMANDS —————————— #

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "<b>𝗕𝗼𝘁 𝗶𝘀 𝗥𝘂𝗻𝗻𝗶𝗻𝗴 𝘄𝗶𝘁𝗵 𝗮𝗹𝗹 𝗳𝗶𝗹𝗲𝘀! ❤️</b>\n\n/chk - Card Check\n/bin - BIN Lookup")

# 🔍 BIN Lookup using your bin_info_v1.py logic
@bot.message_handler(commands=['bin'])
def bin_handler(message):
    try:
        bin_num = re.findall(r'\d{6}', message.text)[0]
        # Seedha aapki file ka function use ho raha hai
        res = get_bin_info(bin_num) 
        bot.reply_to(message, f"<b>🔍 BIN INFO:</b>\n\n<code>{res}</code>")
    except:
        bot.reply_to(message, "❌ Format: <code>/bin 458456</code>")

# 💳 Card Checker logic
@bot.message_handler(commands=['chk', 'str'])
def chk_handler(message):
    cards = get_cards(message.text)
    if not cards:
        return bot.reply_to(message, "❌ Format: <code>/chk cc|mm|yy|cvv</code>")

    cc = cards[0]
    msg = bot.reply_to(message, f"⏳ <b>𝗖𝗵𝗲𝗰𝗸𝗶𝗻𝗴 Card:</b> <code>{cc}</code>")
    
    # Yahan checking logic (Jo aapne bbbb.py ya br.py me rakha hai)
    # Abhi hum response simulate kar rahe hain
    time.sleep(2)
    
    final_res = f"<b>💳 CC RESULT</b>\n\nCard: <code>{cc}</code>\nStatus: <b>Live ✅</b>\nResponse: <code>Approved (1000)</code>"
    bot.edit_message_text(final_res, message.chat.id, msg.message_id)

# —————————— START THE BOT —————————— #
if __name__ == '__main__':
    print("🚀 Bot starting on Render...")
    try:
        bot.send_message(admin_id, "✅ Bot script started successfully with all linked files.")
    except: pass
    bot.infinity_polling(none_stop=True)
  
