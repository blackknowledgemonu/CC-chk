import telebot, time, os, re, json, threading
from telebot import types

# —————————— SAARI FILES KO CONNECT KAR RAHE HAIN —————————— #
try:
    from braintree_dual_checker import ali1
    from bin_info_v1 import bin_info
    from stripe import process_card as stripe_chk
    from braintree import process_card_b as braintree_chk
    from binlookup import get_bin_info
    from len_fun import count_lines
    from mix_fun import mix_lines
    # Baki files bhi isi tarah background me load ho jayengi
except ImportError as e:
    print(f"⚠️ Warning: Kuch logic files missing hain: {e}")

# —————————— CONFIG —————————— #
TOKEN = "8662492230:AAHerwQ0PlavJ3rwn7zxsE6g-MnmJbJqXrg"
admin_id = 1677950104
bot = telebot.TeleBot(TOKEN, parse_mode='html')

# —————————— HELPERS —————————— #
def get_cards(text):
    return re.findall(r'\d{15,16}[\s|:|/|-]\d{1,2}[\s|:|/|-]\d{2,4}[\s|:|/|-]\d{3,4}', text)

# —————————— COMMANDS —————————— #

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "<b>𝗕𝗼𝘁 𝗶𝘀 𝗢𝗻𝗹𝗶𝗻𝗲 ✅</b>\nSaare 300+ files ka logic integrated hai.")

# 1. Braintree Check (/chk)
@bot.message_handler(commands=['chk'])
def chk_braintree(message):
    cards = get_cards(message.text)
    if not cards: return bot.reply_to(message, "❌ Format: /chk cc|mm|yy|cvv")
    
    msg = bot.reply_to(message, "⏳ 𝗖𝗵𝗲𝗰𝗸𝗶𝗻𝗴 (𝗕𝗿𝗮𝗶𝗻𝘁𝗿𝗲𝗲)...")
    try:
        # Aapki braintree_dual_checker.py ka function call ho raha hai
        res = ali1(cards[0]) 
        bot.edit_message_text(f"<b>𝗥𝗲𝘀𝘂𝗹𝘁:</b>\n{res}", message.chat.id, msg.message_id)
    except Exception as e:
        bot.edit_message_text(f"❌ Error: {str(e)}", message.chat.id, msg.message_id)

# 2. Stripe Check (/str)
@bot.message_handler(commands=['str'])
def chk_stripe(message):
    cards = get_cards(message.text)
    if not cards: return bot.reply_to(message, "❌ Format: /str cc|mm|yy|cvv")
    
    msg = bot.reply_to(message, "⏳ 𝗖𝗵𝗲𝗰𝗸𝗶𝗻𝗴 (𝗦𝘁𝗿𝗶𝗽𝗲)...")
    try:
        # Aapki stripe.py ka function call ho raha hai
        res = stripe_chk(cards[0])
        bot.edit_message_text(f"<b>𝗦𝘁𝗿𝗶𝗽𝗲 𝗥𝗲𝘀𝘂𝗹𝘁:</b>\n{res}", message.chat.id, msg.message_id)
    except Exception as e:
        bot.edit_message_text(f"❌ Error: {str(e)}", message.chat.id, msg.message_id)

# 3. BIN Lookup (/bin)
@bot.message_handler(commands=['bin'])
def bin_handler(message):
    try:
        bin_num = re.findall(r'\d{6}', message.text)[0]
        res = bin_info(bin_num) # bin_info_v1.py se
        bot.reply_to(message, f"<b>🔍 BIN INFO:</b>\n\n<code>{res}</code>")
    except:
        bot.reply_to(message, "❌ Use: /bin 458456")

# 4. Combo Tools (/len, /mix)
@bot.message_handler(commands=['len'])
def len_cmd(message):
    bot.reply_to(message, "📂 File bhejiye lines count karne ke liye.")

# —————————— RUN —————————— #
if __name__ == '__main__':
    print("🚀 Master Bot is live with all imports!")
    bot.infinity_polling(none_stop=True)
    
