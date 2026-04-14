import telebot, time, os, re, json, threading
from telebot import types

# —————————— INTEGRATING YOUR 300+ FILES —————————— #
try:
    from braintree_Api import main as api
    from bin_info_v1 import bin_info
    from paypal import process_card_p
    from stripe import process_card as stripe_chk
    from braintree import process_card_b
    from braintree_dual_checker import ali1
    from binlookup import get_bin_info
    from check_bins_fun import extract_bins
    # Note: Agar koi file missing hui to niche error handle ho jayega
except ImportError as e:
    print(f"⚠️ Warning: Kuch logic files missing hain: {e}")

# —————————— BOT SETTINGS —————————— #
TOKEN = "8662492230:AAHerwQ0PlavJ3rwn7zxsE6g-MnmJbJqXrg"
admin_id = 1677950104
bot = telebot.TeleBot(TOKEN, parse_mode='html')

def get_cards(text):
    return re.findall(r'\d{15,16}[\s|:|/|-]\d{1,2}[\s|:|/|-]\d{2,4}[\s|:|/|-]\d{3,4}', text)

# —————————— COMMAND HANDLERS —————————— #

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "<b>𝗕𝗼𝘁 𝗶𝘀 𝗢𝗻𝗹𝗶𝗻𝗲 ✅</b>\nSaare gateways (Braintree/Stripe) connect ho gaye hain.")

# 1. Braintree Gate (/chk)
@bot.message_handler(commands=['chk'])
def chk_handler(message):
    cards = get_cards(message.text)
    if not cards: return bot.reply_to(message, "❌ Use: /chk cc|mm|yy|cvv")
    
    sent = bot.reply_to(message, "⏳ 𝗖𝗵𝗲𝗰𝗸𝗶𝗻𝗴 (𝗕𝗿𝗮𝗶𝗻𝘁𝗿𝗲𝗲)...")
    try:
        # Aapki 'braintree_dual_checker.py' ka function
        res = ali1(cards[0]) 
        bot.edit_message_text(f"<b>𝗥𝗲𝘀𝘂𝗹𝘁:</b>\n{res}", message.chat.id, sent.message_id)
    except Exception as e:
        bot.edit_message_text(f"❌ Error in ali1: {str(e)}", message.chat.id, sent.message_id)

# 2. Stripe Gate (/str)
@bot.message_handler(commands=['str'])
def str_handler(message):
    cards = get_cards(message.text)
    if not cards: return bot.reply_to(message, "❌ Use: /str cc|mm|yy|cvv")
    
    sent = bot.reply_to(message, "⏳ 𝗖𝗵𝗲𝗰𝗸𝗶𝗻𝗴 (𝗦𝘁𝗿𝗶𝗽𝗲)...")
    try:
        # Aapki 'stripe.py' ka function
        res = stripe_chk(cards[0]) 
        bot.edit_message_text(f"<b>𝗦𝘁𝗿𝗶𝗽𝗲 𝗥𝗲𝘀𝘂𝗹𝘁:</b>\n{res}", message.chat.id, sent.message_id)
    except Exception as e:
        bot.edit_message_text(f"❌ Error in Stripe: {str(e)}", message.chat.id, sent.message_id)

# 3. BIN Lookup (/bin)
@bot.message_handler(commands=['bin'])
def bin_handler(message):
    try:
        bin_num = re.findall(r'\d{6}', message.text)[0]
        # Aapki 'bin_info_v1.py' ka function
        res = bin_info(bin_num)
        bot.reply_to(message, f"<b>🔍 BIN INFO:</b>\n\n<code>{res}</code>")
    except:
        bot.reply_to(message, "❌ Example: /bin 458456")

# 4. Admin Control (/admin)
@bot.message_handler(commands=['admin'])
def admin_cmd(message):
    if message.from_user.id == admin_id:
        bot.reply_to(message, "👑 Admin Panel Access Granted.")
    else:
        bot.reply_to(message, "❌ Access Denied.")

# —————————— RUN —————————— #
if __name__ == '__main__':
    print("🚀 Bot is live and linked with all files!")
    bot.infinity_polling(none_stop=True)
    
