import telebot, time, os, asyncio, datetime, re, json, threading, functools
from telebot import types
import random, string
from datetime import datetime, timedelta

# —————————— FIXED IMPORTS —————————— #
try:
    import braintree as official_bt
except ImportError:
    print("⚠️ Official braintree library not found!")

try:
    # Ensure your file is named 'my_braintree.py' on GitHub
    from my_braintree import process_card_b 
    from braintree_dual_checker import ali1
    from check_bins_fun import extract_bins
except ImportError as e:
    print(f"⚠️ Missing Local File: {e}")

# —————————— BOT CONFIGURATION —————————— #
TOKEN = "8662492230:AAHerwQ0PlavJ3rwn7zxsE6g-MnmJbJqXrg"
admin_id = 1677950104
bot = telebot.TeleBot(TOKEN, parse_mode='html')

# —————————— INITIALIZE DATA —————————— #
def initialize_json(filename, default_data):
    if not os.path.exists(filename):
        with open(filename, 'w') as f:
            json.dump(default_data, f, indent=4)

json_list = ['data.json', 'free.json', 'banned_users.json', 'credits.json', 'user_proxies.json']
for f in json_list:
    initialize_json(f, {} if 'json' in f else [])

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

# —————————— COMMAND HANDLERS —————————— #
@bot.message_handler(commands=['start'])
def start_cmd(message):
    try:
        bot.send_video(
            message.chat.id,
            video="https://t.me/cccjwowowow/85",
            caption="<b>𝘄𝗲𝗹𝗰𝗼𝗺𝗲 𝘁𝗼 𝘁𝗵𝗲 𝗯𝗼𝘁 ❤️🇪🇬</b>\n\nStatus: 🟢 <code>Online</code>\nAdmin ID: <code>1677950104</code>",
            reply_markup=main_menu()
        )
    except Exception:
        bot.send_message(message.chat.id, "<b>Bot is Online! ❤️</b>", reply_markup=main_menu())

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
            bot.edit_message_caption(
                caption="👑 <b>Admin Control Panel</b>\n\n/admin - Control Panel\n/gates - Gates Status\n/grant - Add Credits", 
                chat_id=call.message.chat.id, 
                message_id=call.message.message_id, 
                reply_markup=main_menu()
            )
        else:
            bot.answer_callback_query(call.id, "❌ Only Owner Access!", show_alert=True)

# —————————— START THE BOT —————————— #
if __name__ == '__main__':
    print("🚀 Bot starting on Render...")
    try:
        bot.send_message(admin_id, "✅ <b>Bot is now ONLINE!</b>\nIndentation fixed.")
    except Exception as e:
        print(f"Startup notice failed: {e}")
    
    bot.infinity_polling(none_stop=True)
          
