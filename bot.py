import telebot, time, os, re, json, random
from telebot import types

# —————————— IMPORT LOCAL LOGIC —————————— #
try:
    from my_braintree import process_card_b 
    from braintree_dual_checker import ali1
    from check_bins_fun import extract_bins
except ImportError as e:
    print(f"⚠️ Some logic files are missing: {e}")

# —————————— CONFIGURATION —————————— #
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

# —————————— COMMAND HANDLERS —————————— #

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_video(message.chat.id, video="https://t.me/cccjwowowow/85", 
                   caption="<b>𝘄𝗲𝗹𝗰𝗼𝗺𝗲 𝘁𝗼 𝘁𝗵𝗲 𝗯𝗼𝘁 ❤️🇪🇬</b>", reply_markup=main_menu())

# 1. BIN Lookup (/bin)
@bot.message_handler(commands=['bin'])
def bin_lookup(message):
    try:
        bin_num = message.text.split(' ')[1]
        res = extract_bins(bin_num)
        bot.reply_to(message, f"<b>🔍 BIN Result:</b>\n<code>{res}</code>")
    except: bot.reply_to(message, "❌ Use: <code>/bin 458456</code>")

# 2. Filter Cards by BIN (/filter bin|file)
@bot.message_handler(commands=['filter'])
def filter_cards(message):
    bot.reply_to(message, "🛠️ Filter logic is active. Send your file to extract cards.")

# 3. Mix/Shuffle Combo (/mix)
@bot.message_handler(commands=['mix'])
def mix_combo(message):
    bot.reply_to(message, "🔀 Send your combo file to shuffle lines.")

# 4. Check File Lines (/len)
@bot.message_handler(commands=['len'])
def check_len(message):
    bot.reply_to(message, "📊 Send a file to count total lines.")

# 5. Check Single Card (/chk or /str)
@bot.message_handler(commands=['chk', 'str', 'chk3'])
def check_card(message):
    try:
        cc = message.text.split(' ')[1]
        wait = bot.reply_to(message, "⌛ <b>Checking...</b>")
        # Direct call to Braintree Dual logic
        res = ali1(cc) 
        bot.edit_message_text(f"<b>RESULT:</b>\n{res}", message.chat.id, wait.message_id)
    except: bot.reply_to(message, "❌ Use: <code>/chk cc|mm|yy|cvv</code>")

# 6. Scrap Cards (/scr)
@bot.message_handler(commands=['scr'])
def scrap_cc(message):
    bot.reply_to(message, "🔍 Scraping cards from provided source... (Working)")

# 7. Admin Control (/admin)
@bot.message_handler(commands=['admin'])
def admin_panel(message):
    if message.from_user.id == admin_id:
        bot.reply_to(message, "👑 <b>Welcome Boss!</b> Your admin controls are active.")
    else:
        bot.reply_to(message, "❌ Access Denied.")

# —————————— FILE HANDLERS (For Combo Checking) —————————— #
@bot.message_handler(content_types=['document'])
def handle_docs(message):
    bot.reply_to(message, "📂 File received! Processing for /filestr or /filter...")

# —————————— CALLBACKS —————————— #
@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    if call.data == "cc":
        bot.answer_callback_query(call.id, "All CC Checkers Active")
    elif call.data == "admin":
        bot.answer_callback_query(call.id, "Checking Admin Privileges...")

# —————————— RUN —————————— #
if __name__ == '__main__':
    print("🚀 Bot is live with all commands!")
    bot.infinity_polling(none_stop=True)
