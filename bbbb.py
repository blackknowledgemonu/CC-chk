#   /admin - 𝗮𝗱𝗺𝗶𝗻 𝗰𝗼𝗻𝘁𝗿𝗼𝗹
#   /gates - 𝗴𝗮𝘁𝗲𝘄𝗮𝘆 𝗰𝗼𝗻𝘁𝗿𝗼𝗹
#   /search - 𝗴𝗼𝗼𝗴𝗹𝗲 𝘀𝗰𝗿𝗮𝗽 𝗳𝗼𝗿 𝗴𝗮𝘁𝗲𝘀
#   /bin - 𝗕𝗜𝗡 𝗹𝗼𝗼𝗸𝘂𝗽
#   /cb - 𝗰𝗵𝗲𝗰𝗸 𝗳𝗶𝗹𝗲 𝗯𝗶𝗻𝘀
#   /len - 𝗵𝗼𝘄 𝗺𝗮𝗻𝘆 𝗳𝗶𝗹𝗲 𝗹𝗶𝗻𝗲𝘀
#   /mix - 𝘀𝗵𝘂𝗳𝗳𝗹𝗲 𝗮𝗻𝗱 𝗺𝗶𝘅 𝗰𝗼𝗺𝗯𝗼 𝗹𝗶𝗻𝗲𝘀
#   /filter - 𝗲𝘅𝘁𝗿𝗮𝗰𝘁 𝗰𝗮𝗿𝗱𝘀 𝘄𝗶𝘁𝗵 𝘀𝗽𝗲𝗰𝗶𝗳𝗶𝗰 𝗯𝗶𝗻
#   /genf - 𝗴𝗲𝗻𝗿𝗮𝘁𝗲 𝗰𝗼𝗺𝗯𝗼 𝗳𝗶𝗹𝗲
#   /gen - 𝗴𝗲𝗻𝗿𝗮𝘁𝗲 𝟭𝟬 𝗰𝗮𝗿𝗱𝘀
#   /scr - 𝘀𝗰𝗿𝗮𝗽 𝗰𝗮𝗿𝗱𝘀
#   /sk - 𝗰𝗵𝗲𝗰𝗸 𝘀𝗸 𝗸𝗲𝘆
#   /chk - 𝗰𝗵𝗲𝗰𝗸 𝘀𝗶𝗻𝗴𝗹𝗲 𝗰𝗮𝗿𝗱 𝘄𝗶𝘁𝗵 𝗯𝗿𝗮𝗶𝗻𝘁𝗿𝗲𝗲
#   /str - 𝗰𝗵𝗲𝗰𝗸 𝘀𝗶𝗻𝗴𝗹𝗲 𝗰𝗮𝗿𝗱 𝘄𝗶𝘁𝗵 𝘀𝘁𝗿𝗶𝗽𝗲
#   /filestr - 𝗰𝗵𝗲𝗰𝗸 𝗰𝗼𝗺𝗯𝗼 𝗳𝗶𝗹𝗲 𝘄𝗶𝘁𝗵 𝘀𝘁𝗿𝗶𝗽𝗲
#   /file - 𝗰𝗵𝗲𝗰𝗸 𝗰𝗼𝗺𝗯𝗼 𝗳𝗶𝗹𝗲 𝘄𝗶𝘁𝗵 𝗯𝗿𝗮𝗶𝗻𝘁𝗿𝗲𝗲
#   /start - 𝘀𝘁𝗮𝗿𝘁 𝘁𝗵𝗲 𝗯𝗼𝘁
#———–———–———–———–———–———#
#pylint:disable=W0603
#pylint:disable=W0703
#pylint:disable=W0622
#———–———–———–———–———–———#
import telebot, time, os, asyncio, datetime, re
from telebot import types
#———–———–———–———–———–———#
# Make sure you have these local modules in the same directory
from braintree_Api import main as api
from bin_info_v1 import bin_info
from paypal import process_card_p
from stripe import process_card
from braintree import process_card_b
from genfun import gen_card
from search import perform_search
from len_fun import count_lines
from mix_fun import mix_lines
from filter_fun import filter
from sk_check import check_key
from binlookup import get_bin_info
from check_bins_fun import extract_bins
from scrap_fun import get_last_messages,save_to_file
#———–———–———–———–———–———#
from telebot.types import LabeledPrice
import random, string, json, threading
from datetime import datetime, timedelta
#———–———–———–———–———–———#
bot = telebot.TeleBot("7040898503:AAGHQ-8s55l3SELZexgVYk2p94utaXdS4ng", parse_mode='html')
admin_id = 1861702459

bot.send_message(admin_id,"𝗯𝗼𝘁 𝘀𝘁𝗮𝗿𝘁𝗲𝗱")
iD = ["1861702459","",""] # This list is no longer used for command access
bot_working = True
is_card_checking = False

# --- Gateway Status Dictionary ---
gate_status = {
    'chk': True,      # Braintree single
    'str': True,      # Stripe single
    'pay': True,      # PayPal single
    'filestr': True,  # Stripe file
    'file': True,     # Braintree file
    'filep': True,    # PayPal file
}

# Ensure data.json file exists
if not os.path.exists('data.json'):
    with open('data.json', 'w') as f:
        json.dump({}, f)

# ——————————— Subscription Check Function ——————————— #
def check_subscription(user_id):
    if user_id == admin_id:
        return True, "𝗮𝗱𝗺𝗶𝗻"
    try:
        with open('data.json', 'r') as file:
            data = json.load(file)
        user_id_str = str(user_id)
        if user_id_str in data:
            user_data = data[user_id_str]
            expiry_time_str = user_data.get('timer')
            if expiry_time_str:
                expiry_time = datetime.strptime(expiry_time_str, '%Y-%m-%d %H:%M')
                if datetime.now() < expiry_time:
                    return True, f"𝘀𝘂𝗯𝘀𝗰𝗿𝗶𝗽𝘁𝗶𝗼𝗻 𝘃𝗮𝗹𝗶𝗱 𝘂𝗻𝘁𝗶𝗹 {expiry_time_str}"
                else:
                    del data[user_id_str]
                    with open('data.json', 'w') as f:
                        json.dump(data, f, indent=4)
                    return False, "𝘀𝘂𝗯𝘀𝗰𝗿𝗶𝗽𝘁𝗶𝗼𝗻 𝗲𝘅𝗽𝗶𝗿𝗲𝗱"
        return False, "𝗻𝗼𝘁 𝘀𝘂𝗯𝘀𝗰𝗿𝗶𝗯𝗲𝗱"
    except (FileNotFoundError, json.JSONDecodeError):
        return False, "𝗲𝗿𝗿𝗼𝗿 𝗰𝗵𝗲𝗰𝗸𝗶𝗻𝗴 𝘀𝘂𝗯𝘀𝗰𝗿𝗶𝗽𝘁𝗶𝗼𝗻"

def create_buy_keyboard():
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("💰 𝗯𝘂𝘆 𝘀𝘂𝗯𝘀𝗰𝗿𝗶𝗽𝘁𝗶𝗼𝗻", callback_data="Buy"))
    return markup
#—————–————–———————––———#
if not os.path.exists("Temps"):
	os.makedirs("Temps")
#—————–————–———————––———#
def create_main_menu_keyboard():
	markup = types.InlineKeyboardMarkup()
	
	markup.add(types.InlineKeyboardButton("𝗮𝗱𝗺𝗶𝗻", callback_data="admin"),types.InlineKeyboardButton("𝗼𝘁𝗵𝗲𝗿", callback_data="other"))
	markup.add(types.InlineKeyboardButton("𝗰𝗰 𝗰𝗵𝗲𝗰𝗸", callback_data="cc"))
	markup.add(types.InlineKeyboardButton("𝘀𝗰𝗿𝗮𝗽", callback_data="scr"))
	markup.add(types.InlineKeyboardButton("𝗰𝗼𝗺𝗯𝗼 𝗵𝗲𝗹𝗽𝗲𝗿", callback_data="combo"))
	markup.add(types.InlineKeyboardButton("💰 𝗯𝘂𝘆 𝘀𝘂𝗯𝘀𝗰𝗿𝗶𝗽𝘁𝗶𝗼𝗻", callback_data="Buy"))
	return markup

def create_back_button_keyboard():
	markup = types.InlineKeyboardMarkup()
	markup.add(types.InlineKeyboardButton("𝗯𝗮𝗰𝗸", callback_data="back"))
	return markup
#—————–————–———————––———#
@bot.message_handler(commands=['start'])
def send_main_menu(message):
    is_subscribed, status = check_subscription(message.from_user.id)
    final_caption = f"""
𝘄𝗲𝗹𝗰𝗼𝗺𝗲 𝘁𝗼 𝘁𝗵𝗲 𝗯𝗼𝘁, 𝗽𝗹𝗲𝗮𝘀𝗲 𝗰𝗵𝗼𝗼𝘀𝗲 𝗳𝗿𝗼𝗺 𝘁𝗵𝗲 𝗼𝗽𝘁𝗶𝗼𝗻𝘀 𝗯𝗲𝗹𝗼𝘄.

📝 𝘆𝗼𝘂𝗿 𝘀𝘂𝗯𝘀𝗰𝗿𝗶𝗽𝘁𝗶𝗼𝗻 𝘀𝘁𝗮𝘁𝘂𝘀: {status}
"""
    
    # الخطوة 1: إرسال الفيديو مع رمز مؤقت كتعليق للحصول على message_id
    sent_message = bot.send_video(message.chat.id, video="https://t.me/cccjwowowow/85", caption="⏳")
    
    # الخطوة 2: حلقة لتعديل التعليق وتحقيق تأثير الكتابة
    current_caption = ""
    for char in final_caption:
        current_caption += char
        try:
            # قم بالتعديل فقط إذا كان النص مختلفًا لتجنب الأخطاء
            if current_caption != sent_message.caption:
                bot.edit_message_caption(
                    caption=current_caption,
                    chat_id=message.chat.id,
                    message_id=sent_message.message_id
                )
                time.sleep(0.0001)  # يمكنك تعديل هذه القيمة لزيادة أو إبطاء سرعة الكتابة
        except telebot.apihelper.ApiTelegramException as e:
            # تجاهل الخطأ إذا كان "message is not modified"
            if 'message is not modified' in str(e):
                pass
            else:
                raise

    # الخطوة 3: بعد انتهاء الكتابة، قم بتعديل الرسالة لإضافة الأزرار
    bot.edit_message_reply_markup(
        chat_id=message.chat.id,
        message_id=sent_message.message_id,
        reply_markup=create_main_menu_keyboard()
    )




@bot.callback_query_handler(func=lambda call: call.data == "admin")
def admin_callback(call):
	chat_id = call.message.chat.id
	message_id = call.message.message_id
	if chat_id == admin_id:
		bot.edit_message_caption("""
#———–———–——————–——#
#   /admin - 𝗯𝗼𝘁 𝘀𝘁𝗮𝘁𝘂𝘀 𝗰𝗼𝗻𝘁𝗿𝗼𝗹
#   /gates - 𝗴𝗮𝘁𝗲𝘄𝗮𝘆 𝗰𝗼𝗻𝘁𝗿𝗼𝗹
#   /grant - 𝗴𝗿𝗮𝗻𝘁 𝘀𝘂𝗯𝘀𝗰𝗿𝗶𝗽𝘁𝗶𝗼𝗻
#   /listusers - 𝗹𝗶𝘀𝘁 𝘀𝘂𝗯𝘀𝗰𝗿𝗶𝗯𝗲𝗿𝘀
#   /broadcast - 𝗯𝗿𝗼𝗮𝗱𝗰𝗮𝘀𝘁 𝗺𝗲𝘀𝘀𝗮𝗴𝗲
#———–———–——————–——#
		""",chat_id, message_id, reply_markup=create_back_button_keyboard())
	else:
		bot.answer_callback_query(call.id, text="𝘆𝗼𝘂 𝗮𝗿𝗲 𝗻𝗼𝘁 𝗮𝗻 𝗮𝗱𝗺𝗶𝗻.", show_alert=True)

@bot.callback_query_handler(func=lambda call: call.data == "cc")
def cards_callback(call):
	chat_id = call.message.chat.id
	message_id = call.message.message_id
	bot.edit_message_caption("""
#———–———–——————–——#
#   /chk - 𝗰𝗵𝗲𝗰𝗸 𝘀𝗶𝗻𝗴𝗹𝗲 𝗰𝗮𝗿𝗱 𝘄𝗶𝘁𝗵 𝗯𝗿𝗮𝗶𝗻𝘁𝗿𝗲𝗲
#   /str - 𝗰𝗵𝗲𝗰𝗸 𝘀𝗶𝗻𝗴𝗹𝗲 𝗰𝗮𝗿𝗱 𝘄𝗶𝘁𝗵 𝘀𝘁𝗿𝗶𝗽𝗲
#   /file - 𝗰𝗵𝗲𝗰𝗸 𝗰𝗼𝗺𝗯𝗼 𝗳𝗶𝗹𝗲 𝘄𝗶𝘁𝗵 𝗯𝗿𝗮𝗶𝗻𝘁𝗿𝗲𝗲
#   /filestr - 𝗰𝗵𝗲𝗰𝗸 𝗰𝗼𝗺𝗯𝗼 𝗳𝗶𝗹𝗲 𝘄𝗶𝘁𝗵 𝘀𝘁𝗿𝗶𝗽𝗲
#———–———–——————–——#
	""", chat_id, message_id, reply_markup=create_back_button_keyboard())

@bot.callback_query_handler(func=lambda call: call.data == "scr")
def scarp_callback(call):
	chat_id = call.message.chat.id
	message_id = call.message.message_id
	bot.edit_message_caption("""
#———–———–——————–——#
#   /scr - 𝘀𝗰𝗿𝗮𝗽 𝗰𝗮𝗿𝗱𝘀
#———–———–——————–——#
	""", chat_id, message_id, reply_markup=create_back_button_keyboard())

@bot.callback_query_handler(func=lambda call: call.data == "combo")
def combo_callback(call):
	chat_id = call.message.chat.id
	message_id = call.message.message_id
	bot.edit_message_caption("""
#———–———–——————–——#
#   /cb - 𝗰𝗵𝗲𝗰𝗸 𝗳𝗶𝗹𝗲 𝗯𝗶𝗻𝘀
#   /len - 𝗵𝗼𝘄 𝗺𝗮𝗻𝘆 𝗳𝗶𝗹𝗲 𝗹𝗶𝗻𝗲𝘀
#   /mix - 𝘀𝗵𝘂𝗳𝗳𝗹𝗲 𝗰𝗼𝗺𝗯𝗼 𝗹𝗶𝗻𝗲𝘀
#   /filter - 𝗲𝘅𝘁𝗿𝗮𝗰𝘁 𝗰𝗮𝗿𝗱𝘀 𝘄𝗶𝘁𝗵 𝘀𝗽𝗲𝗰𝗶𝗳𝗶𝗰 𝗯𝗶𝗻
#   /genf - 𝗴𝗲𝗻𝗲𝗿𝗮𝘁𝗲 𝗰𝗼𝗺𝗯𝗼 𝗳𝗶𝗹𝗲
#   /gen - 𝗴𝗲𝗻𝗲𝗿𝗮𝘁𝗲 𝟭𝟬 𝗰𝗮𝗿𝗱𝘀
#———–———–——————–——#
	""", chat_id, message_id, reply_markup=create_back_button_keyboard())

@bot.callback_query_handler(func=lambda call: call.data == "other")
def other_callback(call):
	chat_id = call.message.chat.id
	message_id = call.message.message_id
	bot.edit_message_caption("""
#———–———–——————–——#
#   /search - 𝗴𝗼𝗼𝗴𝗹𝗲 𝘀𝗰𝗿𝗮𝗽 𝗳𝗼𝗿 𝗴𝗮𝘁𝗲𝘀
#   /sk - 𝗰𝗵𝗲𝗰𝗸 𝘀𝗸 𝗸𝗲𝘆
#   /bin - 𝗕𝗜𝗡 𝗹𝗼𝗼𝗸𝘂𝗽
#———–———–——————–——#
	""", chat_id, message_id, reply_markup=create_back_button_keyboard())

@bot.callback_query_handler(func=lambda call: call.data == "back")
def back_callback(call):
    chat_id = call.message.chat.id
    message_id = call.message.message_id
    is_subscribed, status = check_subscription(chat_id)
    welcome_message = f"""
𝘄𝗲𝗹𝗰𝗼𝗺𝗲 𝘁𝗼 𝘁𝗵𝗲 𝗯𝗼𝘁, 𝗽𝗹𝗲𝗮𝘀𝗲 𝗰𝗵𝗼𝗼𝘀𝗲 𝗳𝗿𝗼𝗺 𝘁𝗵𝗲 𝗼𝗽𝘁𝗶𝗼𝗻𝘀 𝗯𝗲𝗹𝗼𝘄.

📝 𝘆𝗼𝘂𝗿 𝘀𝘂𝗯𝘀𝗰𝗿𝗶𝗽𝘁𝗶𝗼𝗻 𝘀𝘁𝗮𝘁𝘂𝘀: {status}
"""
    bot.edit_message_caption(welcome_message, chat_id, message_id, reply_markup=create_main_menu_keyboard())

#—————–————–———————––———#
@bot.message_handler(commands=['admin'])
def admin_command(message):
	if message.from_user.id == admin_id:
		keyboard = telebot.types.InlineKeyboardMarkup()
		if bot_working:
			status_text = "𝘁𝗵𝗲 𝗯𝗼𝘁 𝗶𝘀 𝘄𝗼𝗿𝗸𝗶𝗻𝗴 ✅"
			button_text = "𝘀𝗲𝘁 𝗯𝗼𝘁 𝗮𝘀 𝗻𝗼𝘁 𝘄𝗼𝗿𝗸𝗶𝗻𝗴 ❌"
		else:
			status_text = "𝘁𝗵𝗲 𝗯𝗼𝘁 𝗶𝘀 𝗻𝗼𝘁 𝘄𝗼𝗿𝗸𝗶𝗻𝗴 ❌"
			button_text = "𝘀𝗲𝘁 𝗯𝗼𝘁 𝗮𝘀 𝘄𝗼𝗿𝗸𝗶𝗻𝗴 ✅"
		
		keyboard.add(telebot.types.InlineKeyboardButton(text=button_text, callback_data='toggle_status'))
		bot.send_message(message.chat.id, status_text, reply_markup=keyboard)
	else:
		pass

@bot.callback_query_handler(func=lambda call: call.data == 'toggle_status')
def toggle_status_callback(call):
    if call.from_user.id != admin_id: return
    global bot_working
    bot_working = not bot_working
    if bot_working:
        new_status = "𝘁𝗵𝗲 𝗯𝗼𝘁 𝗶𝘀 𝘄𝗼𝗿𝗸𝗶𝗻𝗴 ✅"
        new_button_text = "𝘀𝗲𝘁 𝗯𝗼𝘁 𝗮𝘀 𝗻𝗼𝘁 𝘄𝗼𝗿𝗸𝗶𝗻𝗴 ❌"
    else:
        new_status = "𝘁𝗵𝗲 𝗯𝗼𝘁 𝗶𝘀 𝗻𝗼𝘁 𝘄𝗼𝗿𝗸𝗶𝗻𝗴 ❌"
        new_button_text = "𝘀𝗲𝘁 𝗯𝗼𝘁 𝗮𝘀 𝘄𝗼𝗿𝗸𝗶𝗻𝗴 ✅"
    
    keyboard = telebot.types.InlineKeyboardMarkup()
    keyboard.add(telebot.types.InlineKeyboardButton(text=new_button_text, callback_data='toggle_status'))
    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=new_status, reply_markup=keyboard)


# --- Gateway Control Function ---
def create_gates_keyboard():
    markup = types.InlineKeyboardMarkup()
    for gate, status in gate_status.items():
        text = f"/{gate} : {'✅ 𝗲𝗻𝗮𝗯𝗹𝗲𝗱' if status else '❌ 𝗱𝗶𝘀𝗮𝗯𝗹𝗲𝗱'}"
        callback_data = f"toggle_{gate}"
        markup.add(types.InlineKeyboardButton(text, callback_data=callback_data))
    return markup

@bot.message_handler(commands=['gates'])
def gates_command(message):
    if message.from_user.id == admin_id:
        bot.send_message(message.chat.id, "𝗴𝗮𝘁𝗲𝘄𝗮𝘆 𝗰𝗼𝗻𝘁𝗿𝗼𝗹 𝗽𝗮𝗻𝗲𝗹", reply_markup=create_gates_keyboard())

@bot.callback_query_handler(func=lambda call: call.data.startswith('toggle_'))
def toggle_gate_callback(call):
    if call.from_user.id == admin_id:
        gate = call.data.split('_')[1]
        if gate in gate_status:
            gate_status[gate] = not gate_status[gate]
            bot.edit_message_reply_markup(chat_id=call.message.chat.id,
                                          message_id=call.message.message_id,
                                          reply_markup=create_gates_keyboard())
            bot.answer_callback_query(call.id)
#—————–————–———————––———#

# ——————————— New Admin Commands (Implemented) ——————————— #
@bot.message_handler(commands=['grant'])
def grant_command(message):
    if message.from_user.id != admin_id:
        return

    try:
        parts = message.text.split()
        if len(parts) != 3:
            bot.reply_to(message, "𝘂𝘀𝗮𝗴𝗲: /grant <user_id> <hours>")
            return
            
        target_user_id = int(parts[1])
        hours = float(parts[2])

        with open('data.json', 'r') as file:
            data = json.load(file)

        expiry_time = datetime.now() + timedelta(hours=hours)
        expiry_time_str = expiry_time.strftime('%Y-%m-%d %H:%M')

        data[str(target_user_id)] = {'timer': expiry_time_str, 'plan': 'granted_vip'}

        with open('data.json', 'w') as file:
            json.dump(data, file, indent=4)

        bot.reply_to(message, f"✅ 𝘀𝘂𝗰𝗰𝗲𝘀𝘀𝗳𝘂𝗹𝗹𝘆 𝗴𝗿𝗮𝗻𝘁𝗲𝗱 𝗮 {hours}-𝗵𝗼𝘂𝗿 𝘀𝘂𝗯𝘀𝗰𝗿𝗶𝗽𝘁𝗶𝗼𝗻 𝘁𝗼 𝘂𝘀𝗲𝗿 {target_user_id}.")
        # Notify the user
        bot.send_message(target_user_id, f"🎉 𝘆𝗼𝘂 𝗵𝗮𝘃𝗲 𝗯𝗲𝗲𝗻 𝗴𝗿𝗮𝗻𝘁𝗲𝗱 𝗮 𝘀𝘂𝗯𝘀𝗰𝗿𝗶𝗽𝘁𝗶𝗼𝗻. 𝗶𝘁 𝗲𝘅𝗽𝗶𝗿𝗲𝘀 𝗼𝗻: {expiry_time_str}")
    except (IndexError, ValueError):
        bot.reply_to(message, "𝗶𝗻𝗰𝗼𝗿𝗿𝗲𝗰𝘁 𝗳𝗼𝗿𝗺𝗮𝘁. 𝘂𝘀𝗮𝗴𝗲: /grant <user_id> <hours>")
    except Exception as e:
        bot.reply_to(message, f"𝗮𝗻 𝗲𝗿𝗿𝗼𝗿 𝗼𝗰𝗰𝘂𝗿𝗿𝗲𝗱: {e}")

@bot.message_handler(commands=['listusers'])
def listusers_command(message):
    if message.from_user.id != admin_id:
        return
    
    try:
        with open('data.json', 'r') as file:
            data = json.load(file)

        user_list = ["𝘀𝘂𝗯𝘀𝗰𝗿𝗶𝗯𝗲𝗱 𝘂𝘀𝗲𝗿𝘀 𝗹𝗶𝘀𝘁:\n\n"]
        count = 0
        for key, value in data.items():
            if key.isdigit():
                count += 1
                user_list.append(f"𝗶𝗱: {key} | 𝗲𝘅𝗽𝗶𝗿𝗲𝘀: {value.get('timer', 'N/A')}")

        if count == 0:
            bot.reply_to(message, "𝗻𝗼 𝘀𝘂𝗯𝘀𝗰𝗿𝗶𝗯𝗲𝗱 𝘂𝘀𝗲𝗿𝘀 𝗳𝗼𝘂𝗻𝗱.")
            return

        file_content = "\n".join(user_list)
        file_path = "subscribed_users.txt"
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(file_content)
        
        with open(file_path, 'rb') as f:
            bot.send_document(message.chat.id, f, caption=f"𝘁𝗼𝘁𝗮𝗹 𝘀𝘂𝗯𝘀𝗰𝗿𝗶𝗯𝗲𝗿𝘀: {count}")
        
        os.remove(file_path)
    except Exception as e:
        bot.reply_to(message, f"𝗮𝗻 𝗲𝗿𝗿𝗼𝗿 𝗼𝗰𝗰𝘂𝗿𝗿𝗲𝗱: {e}")

@bot.message_handler(commands=['broadcast'])
def broadcast_command(message):
    if message.from_user.id != admin_id:
        return

    try:
        broadcast_message = message.text.split(maxsplit=1)[1]
    except IndexError:
        bot.reply_to(message, "𝗽𝗹𝗲𝗮𝘀𝗲 𝘄𝗿𝗶𝘁𝗲 𝗮 𝗺𝗲𝘀𝘀𝗮𝗴𝗲 𝗮𝗳𝘁𝗲𝗿 𝘁𝗵𝗲 𝗰𝗼𝗺𝗺𝗮𝗻𝗱. 𝘂𝘀𝗮𝗴𝗲: /broadcast <your_message>")
        return

    try:
        with open('data.json', 'r') as file:
            data = json.load(file)
        
        user_ids = [key for key in data.keys() if key.isdigit()]
        
        if not user_ids:
            bot.reply_to(message, "𝗻𝗼 𝘀𝘂𝗯𝘀𝗰𝗿𝗶𝗯𝗲𝗿𝘀 𝘁𝗼 𝘀𝗲𝗻𝗱 𝗮 𝗺𝗲𝘀𝘀𝗮𝗴𝗲 𝘁𝗼.")
            return

        bot.reply_to(message, f"𝘀𝘁𝗮𝗿𝘁𝗶𝗻𝗴 𝗯𝗿𝗼𝗮𝗱𝗰𝗮𝘀𝘁 𝘁𝗼 {len(user_ids)} 𝘀𝘂𝗯𝘀𝗰𝗿𝗶𝗯𝗲𝗿𝘀...")
        
        success_count = 0
        fail_count = 0
        for user_id in user_ids:
            try:
                bot.send_message(int(user_id), broadcast_message)
                success_count += 1
                time.sleep(0.1) # To avoid Telegram rate limits
            except Exception as e:
                print(f"Failed to send to {user_id}: {e}")
                fail_count += 1
        
        bot.reply_to(message, f"𝗯𝗿𝗼𝗮𝗱𝗰𝗮𝘀𝘁 𝗳𝗶𝗻𝗶𝘀𝗵𝗲𝗱.\n\n- 𝘀𝘂𝗰𝗰𝗲𝘀𝘀𝗳𝘂𝗹𝗹𝘆 𝘀𝗲𝗻𝘁 𝘁𝗼: {success_count} 𝘂𝘀𝗲𝗿𝘀.\n- 𝗳𝗮𝗶𝗹𝗲𝗱 𝘁𝗼 𝘀𝗲𝗻𝗱 𝘁𝗼: {fail_count} 𝘂𝘀𝗲𝗿𝘀.")

    except Exception as e:
        bot.reply_to(message, f"𝗮𝗻 𝗲𝗿𝗿𝗼𝗿 𝗼𝗰𝗰𝘂𝗿𝗿𝗲𝗱 𝗱𝘂𝗿𝗶𝗻𝗴 𝗯𝗿𝗼𝗮𝗱𝗰𝗮𝘀𝘁: {e}")


# ——————————— Stars Payment System ——————————— #
@bot.callback_query_handler(func=lambda call: call.data == 'Buy')
def buy_callback(call):
    try:
        bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
    except Exception as e:
        print(f"Could not delete message: {e}")

    markup = types.InlineKeyboardMarkup(row_width=1)
    gate_btn = types.InlineKeyboardButton("𝟮 𝗵𝗼𝘂𝗿𝘀 » 𝟰𝟬 ⭐", callback_data="buy_2hour")
    lock_btn = types.InlineKeyboardButton("𝟭 𝗱𝗮𝘆 » 𝟭𝟬𝟬 ⭐", callback_data="buy_1day")
    unlock_btn = types.InlineKeyboardButton("𝟭 𝘄𝗲𝗲𝗸 » 𝟯𝟱𝟬 ⭐", callback_data="buy_1week")
    back_btn = types.InlineKeyboardButton("𝗯𝗮𝗰𝗸", callback_data="back")
    markup.add(gate_btn, lock_btn, unlock_btn, back_btn)
    
    msg = '''-
𝗰𝗵𝗼𝗼𝘀𝗲 𝗮 𝘀𝘂𝗶𝘁𝗮𝗯𝗹𝗲 𝘀𝘂𝗯𝘀𝗰𝗿𝗶𝗽𝘁𝗶𝗼𝗻 𝗽𝗹𝗮𝗻.

<a href='tg://user?id=1861702459'>(VENOM)</a>'''

    bot.send_video(
        chat_id=call.message.chat.id,
        video="https://t.me/cccjwowowow/85",
        caption=msg,
        reply_markup=markup
    )

def send_star_invoice(call, hours, cost, label):
    prices = [LabeledPrice(label=label, amount=int(cost))]
    bot.send_invoice(
        chat_id=call.message.chat.id,
        title=label,
        description=f"𝗽𝗮𝘆 {cost} 𝘀𝘁𝗮𝗿𝘀 𝗳𝗼𝗿 𝘀𝘂𝗯𝘀𝗰𝗿𝗶𝗽𝘁𝗶𝗼𝗻",
        provider_token="",  # put your provider token here
        currency="XTR",
        prices=prices,
        start_parameter="pay_with_stars",
        invoice_payload=f"Star-{hours}h",
    )

@bot.callback_query_handler(func=lambda call: call.data == 'buy_2hour')
def process_hour(call):
    send_star_invoice(call, 2, 40, "𝘀𝘂𝗯𝘀𝗰𝗿𝗶𝗽𝘁𝗶𝗼𝗻 𝟮 𝗵𝗼𝘂𝗿𝘀")

@bot.callback_query_handler(func=lambda call: call.data == 'buy_1day')
def process_day(call):
    send_star_invoice(call, 24, 100, "𝘀𝘂𝗯𝘀𝗰𝗿𝗶𝗽𝘁𝗶𝗼𝗻 𝟭 𝗱𝗮𝘆")

@bot.callback_query_handler(func=lambda call: call.data == 'buy_1week')
def process_week(call):
    send_star_invoice(call, 168, 350, "𝘀𝘂𝗯𝘀𝗰𝗿𝗶𝗽𝘁𝗶𝗼𝗻 𝟭 𝘄𝗲𝗲𝗸")

@bot.pre_checkout_query_handler(func=lambda query: True)
def checkout_handler(pre_checkout_query):
    bot.answer_pre_checkout_query(pre_checkout_query.id, ok=True)

@bot.message_handler(content_types=["successful_payment"])
def successful_payment(message):
    invoice = message.successful_payment.invoice_payload
    h_str = invoice.split('-')[1].replace('h', '')
    h = int(h_str)
    
    characters = string.ascii_uppercase + string.digits
    pas = 'venom-' + '-'.join([''.join(random.choices(characters, k=4)) for _ in range(3)])
    current_time = datetime.now()
    ig = current_time + timedelta(hours=h)
    plan = 'vip'
    
    ig_formatted = ig.strftime('%Y-%m-%d %H:%M')
    
    with open('data.json', 'r') as json_file:
        existing_data = json.load(json_file)
    new_data = {pas: {"plan": plan, "time": ig_formatted}}
    existing_data.update(new_data)
    with open('data.json', 'w') as json_file:
        json.dump(existing_data, json_file, ensure_ascii=False, indent=4)
    msg = f'''<b>
✅ 𝗽𝗮𝘆𝗺𝗲𝗻𝘁 𝗱𝗼𝗻𝗲 𝘀𝘂𝗰𝗰𝗲𝘀𝘀𝗳𝘂𝗹𝗹𝘆

𝗵𝗲𝗿𝗲 𝗶𝘀 𝘆𝗼𝘂𝗿 𝗸𝗲𝘆 
𝘆𝗼𝘂 𝗰𝗮𝗻 𝗿𝗲𝗱𝗲𝗲𝗺 𝗶𝘁 𝗼𝗿 𝘀𝗲𝗻𝗱 𝗶𝘁 𝗮𝘀 𝗮 𝗴𝗶𝗳𝘁.

├ 𝘀𝘁𝗮𝘁𝘂𝘀 » {plan}
├ 𝗲𝘅𝗽𝗶𝗿𝗲𝘀 𝗼𝗻 » {ig_formatted}
├ 𝗸𝗲𝘆   <code>{pas}</code>	
├ 𝘂𝘀𝗮𝗴𝗲: /redeem [KEY]
</b>'''
    bot.send_message(message.chat.id, msg, parse_mode="HTML")

# ——————————— /redeem and /code Commands ——————————— #
@bot.message_handler(func=lambda message: message.text.lower().startswith('.redeem') or message.text.lower().startswith('/redeem'))
def redeem_key(message):
    def my_function():
        try:
            key = message.text.split(' ')[1]
            with open('data.json', 'r') as file:
                json_data = json.load(file)
            if key not in json_data:
                raise KeyError(f'Code {key} not found')
            timer = json_data[key]['time']
            typ = json_data[key]['plan']
            
            expiry_time = datetime.strptime(timer, '%Y-%m-%d %H:%M')
            if datetime.now() >= expiry_time:
                bot.reply_to(message, '<b>❌ 𝘁𝗵𝗶𝘀 𝗸𝗲𝘆 𝗵𝗮𝘀 𝗲𝘅𝗽𝗶𝗿𝗲𝗱 𝗮𝗻𝗱 𝗰𝗮𝗻𝗻𝗼𝘁 𝗯𝗲 𝗿𝗲𝗱𝗲𝗲𝗺𝗲𝗱.</b>', parse_mode="HTML")
                return
                
            json_data[str(message.from_user.id)] = {'timer': timer, 'plan': typ}
            del json_data[key] 
            
            with open('data.json', 'w') as file:
                json.dump(json_data, file, indent=4)

            msg = f'''<b>✅ 𝗸𝗲𝘆 𝗿𝗲𝗱𝗲𝗲𝗺𝗲𝗱 𝘀𝘂𝗰𝗰𝗲𝘀𝘀𝗳𝘂𝗹𝗹𝘆!
» 𝗲𝘅𝗽𝗶𝗿𝗲𝘀 𝗼𝗻: {timer}
» 𝗽𝗹𝗮𝗻: {typ}</b>'''
            bot.reply_to(message, msg, parse_mode="HTML")
        except KeyError:
            bot.reply_to(message, '<b>❌ 𝗶𝗻𝗰𝗼𝗿𝗿𝗲𝗰𝘁 𝗰𝗼𝗱𝗲 𝗼𝗿 𝗮𝗹𝗿𝗲𝗮𝗱𝘆 𝗿𝗲𝗱𝗲𝗲𝗺𝗲𝗱</b>', parse_mode="HTML")
        except Exception as e:
            bot.reply_to(message, f'<b>𝗲𝗿𝗿𝗼𝗿: {e}</b>', parse_mode="HTML")
    threading.Thread(target=my_function).start()

@bot.message_handler(commands=["code"])
def code(message):
    def my_function():
        if message.from_user.id != admin_id:
            return
        try:
            h = float(message.text.split(' ')[1])
            with open('data.json', 'r') as json_file:
                existing_data = json.load(json_file)
            characters = string.ascii_uppercase + string.digits
            pas = 'venom-' + '-'.join([''.join(random.choices(characters, k=4)) for _ in range(3)])
            current_time = datetime.now()
            ig = current_time + timedelta(hours=h)
            plan = 'vip'
            ig_formatted = ig.strftime('%Y-%m-%d %H:%M')
            
            new_data = {pas: {"plan": plan, "time": ig_formatted}}
            existing_data.update(new_data)
            with open('data.json', 'w') as json_file:
                json.dump(existing_data, json_file, ensure_ascii=False, indent=4)
            msg = f'''<b>
✅ 𝗸𝗲𝘆 𝗰𝗿𝗲𝗮𝘁𝗲𝗱

├ 𝘀𝘁𝗮𝘁𝘂𝘀 » {plan}
├ 𝗲𝘅𝗽𝗶𝗿𝗲𝘀 𝗼𝗻 » {ig_formatted}
├ 𝗸𝗲𝘆   <code>{pas}</code>	
├ 𝘂𝘀𝗮𝗴𝗲: /redeem [KEY]
</b>'''
            bot.reply_to(message, msg, parse_mode="HTML")
        except Exception as e:
            bot.reply_to(message, f"𝗲𝗿𝗿𝗼𝗿: {e}", parse_mode="HTML")
    threading.Thread(target=my_function).start()

# ——————————— User Commands (Free) ——————————— #
@bot.message_handler(commands=['me'])
def me_command(message):
    commands_list = """
<b>𝗯𝗼𝘁 𝗰𝗼𝗺𝗺𝗮𝗻𝗱 𝗹𝗶𝘀𝘁:</b>

<b>/admin</b> - <code>𝗮𝗱𝗺𝗶𝗻 𝗰𝗼𝗻𝘁𝗿𝗼𝗹 𝗽𝗮𝗻𝗲𝗹</code>
<b>/gates</b> - <code>𝗴𝗮𝘁𝗲𝘄𝗮𝘆 𝗰𝗼𝗻𝘁𝗿𝗼𝗹</code>
<b>/search</b> - <code>𝗴𝗼𝗼𝗴𝗹𝗲 𝘀𝗰𝗿𝗮𝗽 𝗳𝗼𝗿 𝗴𝗮𝘁𝗲𝘀</code>
<b>/bin</b> - <code>𝗯𝗶𝗻 𝗹𝗼𝗼𝗸𝘂𝗽</code>
<b>/cb</b> - <code>𝗰𝗵𝗲𝗰𝗸 𝗳𝗶𝗹𝗲 𝗯𝗶𝗻𝘀</code>
<b>/len</b> - <code>𝗰𝗼𝘂𝗻𝘁 𝗳𝗶𝗹𝗲 𝗹𝗶𝗻𝗲𝘀</code>
<b>/mix</b> - <code>𝘀𝗵𝘂𝗳𝗳𝗹𝗲 𝗰𝗼𝗺𝗯𝗼 𝗹𝗶𝗻𝗲𝘀</code>
<b>/filter</b> - <code>𝗲𝘅𝘁𝗿𝗮𝗰𝘁 𝗰𝗮𝗿𝗱𝘀 𝘄𝗶𝘁𝗵 𝘀𝗽𝗲𝗰𝗶𝗳𝗶𝗰 𝗯𝗶𝗻</code>
<b>/genf</b> - <code>𝗴𝗲𝗻𝗲𝗿𝗮𝘁𝗲 𝗰𝗼𝗺𝗯𝗼 𝗳𝗶𝗹𝗲</code>
<b>/gen</b> - <code>𝗴𝗲𝗻𝗲𝗿𝗮𝘁𝗲 𝟭𝟬 𝗰𝗮𝗿𝗱𝘀</code>
<b>/scr</b> - <code>𝘀𝗰𝗿𝗮𝗽 𝗰𝗮𝗿𝗱𝘀 𝗳𝗿𝗼𝗺 𝗰𝗵𝗮𝗻𝗻𝗲𝗹𝘀</code>
<b>/sk</b> - <code>𝗰𝗵𝗲𝗰𝗸 𝘀𝗸 𝗸𝗲𝘆</code>
<b>/profile</b> - <code>𝘃𝗶𝗲𝘄 𝘆𝗼𝘂𝗿 𝗽𝗿𝗼𝗳𝗶𝗹𝗲 𝗮𝗻𝗱 𝘀𝘂𝗯𝘀𝗰𝗿𝗶𝗽𝘁𝗶𝗼𝗻</code>
<b>/start</b> - <code>𝘀𝘁𝗮𝗿𝘁 𝘁𝗵𝗲 𝗯𝗼𝘁</code>

<b>--- 𝗣𝗿𝗲𝗺𝗶𝘂𝗺 𝗖𝗼𝗺𝗺𝗮𝗻𝗱𝘀 ---</b>
<b>/chk</b> - <code>𝗰𝗵𝗲𝗰𝗸 𝗰𝗮𝗿𝗱 𝘄𝗶𝘁𝗵 𝗯𝗿𝗮𝗶𝗻𝘁𝗿𝗲𝗲</code>
<b>/pay</b> - <code>𝗰𝗵𝗲𝗰𝗸 𝗰𝗮𝗿𝗱 𝘄𝗶𝘁𝗵 𝗽𝗮𝘆𝗽𝗮𝗹</code>
<b>/file</b> - <code>𝗰𝗵𝗲𝗰𝗸 𝗰𝗼𝗺𝗯𝗼 𝗳𝗶𝗹𝗲 𝘄𝗶𝘁𝗵 𝗯𝗿𝗮𝗶𝗻𝘁𝗿𝗲𝗲</code>
<b>/filestr</b> - <code>𝗰𝗵𝗲𝗰𝗸 𝗰𝗼𝗺𝗯𝗼 𝗳𝗶𝗹𝗲 𝘄𝗶𝘁𝗵 𝘀𝘁𝗿𝗶𝗽𝗲</code>
    """
    bot.reply_to(message, commands_list, parse_mode="HTML")

@bot.message_handler(commands=['profile'])
def profile_command(message):
    is_subscribed, status = check_subscription(message.from_user.id)
    
    try:
        user_id = message.from_user.id
        profile_text = f"""
<b>𝘆𝗼𝘂𝗿 𝗽𝗿𝗼𝗳𝗶𝗹𝗲:</b>

- <b>𝘂𝘀𝗲𝗿 𝗶𝗱:</b> <code>{user_id}</code>
- <b>𝘀𝘂𝗯𝘀𝗰𝗿𝗶𝗽𝘁𝗶𝗼𝗻 𝘀𝘁𝗮𝘁𝘂𝘀:</b> {status.capitalize()}
        """
        bot.reply_to(message, profile_text, parse_mode="HTML")
    except Exception as e:
        bot.reply_to(message, f"𝗮𝗻 𝗲𝗿𝗿𝗼𝗿 𝗼𝗰𝗰𝘂𝗿𝗿𝗲𝗱: {e}")

@bot.message_handler(commands=['search'])
def search_command(message):
    if bot_working:
        chat_id = message.chat.id
        initial_message = bot.reply_to(message, "𝘀𝗲𝗮𝗿𝗰𝗵 𝘀𝘁𝗮𝗿𝘁𝗲𝗱...⏳")
        args = message.text.split()[1:]
        if len(args) != 3:
            bot.edit_message_text(chat_id=chat_id, message_id=initial_message.message_id, text="𝗽𝗹𝗲𝗮𝘀𝗲 𝗽𝗿𝗼𝘃𝗶𝗱𝗲 𝘁𝗵𝗿𝗲𝗲 𝗮𝗿𝗴𝘂𝗺𝗲𝗻𝘁𝘀 𝗶𝗻 𝘁𝗵𝗲 𝗳𝗼𝗿𝗺𝗮𝘁: \n/search [payment] [name] [domain]")
            return
        
        v1, v2, v3 = args
        result = perform_search(v1, v2, v3)
        bot.edit_message_text(chat_id=chat_id, message_id=initial_message.message_id, text=result,disable_web_page_preview=True)
    else:
        pass

@bot.message_handler(commands=['bin'])
def bin_lookup_command(message):
    if bot_working:
        chat_id = message.chat.id
        try:
            initial_message = bot.reply_to(message, "𝗹𝗼𝗼𝗸𝘂𝗽 𝘀𝘁𝗮𝗿𝘁𝗲𝗱...⏳")
            biN = message.text.split()[1]
            bin_inf = bin_info(biN)
            bot.edit_message_text(chat_id=chat_id, message_id=initial_message.message_id, text=bin_inf)
        except Exception as ex:
            bot.edit_message_text(chat_id=chat_id, message_id=initial_message.message_id, text=f"𝗮𝗻 𝗲𝗿𝗿𝗼𝗿 𝗼𝗰𝗰𝘂𝗿𝗿𝗲𝗱: {str(ex)}")
    else:
        pass

@bot.message_handler(commands=['cb'])
def handle_bins_command(message):
    if bot_working:
        try:
            bins_count = extract_bins(message,bot)
            if bins_count is not None:
                chunk_size = 285
                bins_chunks = [list(bins_count.keys())[i:i + chunk_size] for i in range(0, len(bins_count), chunk_size)]
                for bins_chunk in bins_chunks:
                    chunk_response = "\n".join([f"{bin} =>> {bins_count[bin]}" for bin in bins_chunk])
                    bot.reply_to(message, chunk_response)
            else:
                bot.reply_to(message, "𝗽𝗹𝗲𝗮𝘀𝗲 𝗿𝗲𝗽𝗹𝘆 𝘁𝗼 𝗮 𝗰𝗼𝗺𝗯𝗼 𝗳𝗶𝗹𝗲 𝘁𝗼 𝗴𝗲𝘁 𝘁𝗵𝗲 𝗯𝗶𝗻𝘀 𝗶𝘁 𝗰𝗼𝗻𝘁𝗮𝗶𝗻𝘀.")
        except Exception as e:
            bot.reply_to(message, str(e))
    else:
        pass

@bot.message_handler(commands=['len'])
def handle_len_command(message):
    if bot_working:
        chat_id = message.chat.id
        initial_message = bot.reply_to(message, "𝗰𝗼𝘂𝗻𝘁 𝘀𝘁𝗮𝗿𝘁𝗲𝗱...⏳")
        response = count_lines(message,bot)
        bot.edit_message_text(chat_id=chat_id, message_id=initial_message.message_id, text=response)
    else:
        pass

@bot.message_handler(commands=['mix'])
def handle_mix_command(message):
    if not bot_working: return

    chat_id = message.chat.id
    if not (message.reply_to_message and message.reply_to_message.document):
        bot.reply_to(message, "𝗽𝗹𝗲𝗮𝘀𝗲 𝗿𝗲𝗽𝗹𝘆 𝘁𝗼 𝗮 𝗱𝗼𝗰𝘂𝗺𝗲𝗻𝘁 𝘁𝗼 𝘂𝘀𝗲 𝘁𝗵𝗶𝘀 𝗰𝗼𝗺𝗺𝗮𝗻𝗱.")
        return

    initial_message = None
    try:
        initial_message = bot.reply_to(message, "𝗺𝗶𝘅 𝘀𝘁𝗮𝗿𝘁𝗲𝗱...⏳")
        file_info = bot.get_file(message.reply_to_message.document.file_id)
        downloaded_file = bot.download_file(file_info.file_path)
        shuffled_content = mix_lines(downloaded_file)
        
        temp_file_path = os.path.join("Temps", 'shuffled_lines.txt')
        with open(temp_file_path, 'w', encoding='utf-8') as shuffled_file:
            shuffled_file.write(shuffled_content)
            
        with open(temp_file_path, 'rb') as shuffled_file:
            bot.delete_message(message_id=initial_message.message_id, chat_id=chat_id)
            bot.send_document(message.chat.id, shuffled_file)
            
        os.remove(temp_file_path)
        
    except Exception as e:
        if initial_message:
            bot.edit_message_text(chat_id=chat_id, message_id=initial_message.message_id, text=f"𝗮𝗻 𝗲𝗿𝗿𝗼𝗿 𝗼𝗰𝗰𝘂𝗿𝗿𝗲𝗱: {str(e)}")
        else:
            bot.reply_to(message, f"𝗮𝗻 𝗲𝗿𝗿𝗼𝗿 𝗼𝗰𝗰𝘂𝗿𝗿𝗲𝗱: {str(e)}")

@bot.message_handler(commands=['filter'])
def handle_filter(message):
    if bot_working:
        command_parts = message.text.split()
        chat_id = message.chat.id
        initial_message = bot.reply_to(message, "𝗳𝗶𝗹𝘁𝗲𝗿 𝘀𝘁𝗮𝗿𝘁𝗲𝗱...⏳")
        if len(command_parts) != 2:
            bot.edit_message_text(chat_id=chat_id, message_id=initial_message.message_id, text="𝗶𝗻𝘃𝗮𝗹𝗶𝗱 𝗰𝗼𝗺𝗺𝗮𝗻𝗱 𝗳𝗼𝗿𝗺𝗮𝘁. 𝗽𝗹𝗲𝗮𝘀𝗲 𝘂𝘀𝗲 '/filter <bin_to_search>'",parse_mode='None')
            return
        value = command_parts[1]
        fun_call = filter(bot, value, message)
        filtered_lines = fun_call[0]
        if filtered_lines:
            file_name = f'Temps/{value}.txt'
            with open(file_name, 'w') as output_file:
                output_file.write('\n'.join(filtered_lines))
            with open(file_name, 'rb') as file_to_send:
                bot.delete_message(message_id=initial_message.message_id,chat_id=chat_id)
                bot.send_document(message.chat.id, file_to_send, caption=f"𝗰𝗮𝗿𝗱𝘀 𝗳𝗼𝘂𝗻𝗱 => {fun_call[1]}")
            os.remove(file_name)
        else:
            bot.edit_message_text(chat_id=chat_id, message_id=initial_message.message_id, text="𝗻𝗼 𝗹𝗶𝗻𝗲𝘀 𝗳𝗼𝘂𝗻𝗱 𝘄𝗶𝘁𝗵 𝘁𝗵𝗮𝘁 𝗯𝗶𝗻 𝗶𝗻 𝘁𝗵𝗲 𝗳𝗶𝗹𝗲, 𝗼𝗿 𝘆𝗼𝘂 𝗱𝗶𝗱𝗻'𝘁 𝗿𝗲𝗽𝗹𝘆 𝘁𝗼 𝗮 𝗳𝗶𝗹𝗲.")
    else:
        pass

@bot.message_handler(commands=['genf'])
def generate_cards_file(message):
    if bot_working:
        chat_id = message.chat.id
        try:
            initial_message = bot.reply_to(message, "𝗴𝗲𝗻𝗲𝗿𝗮𝘁𝗶𝗻𝗴 𝘀𝘁𝗮𝗿𝘁𝗲𝗱...⏳")
            start_time = datetime.now()
            command_args = message.text.split()[1:]
            a = command_args[0] if len(command_args) > 0 else ""
            e = int(command_args[1]) if len(command_args) > 1 else 5000
            b = command_args[2] if len(command_args) > 2 else ""
            c = command_args[3] if len(command_args) > 3 else ""
            d = command_args[4] if len(command_args) > 4 else ""
            cards_data = ""
            f = 0
            while f < e:
                card_number, exp_m, exp_y, cvv = gen_card(a, b, c, d)
                cards_data += f"{card_number}|{exp_m}|{exp_y}|{cvv}\n"
                f += 1
            file_name = "generated_cards.txt"
            with open(file_name, "w") as file:
                file.write(cards_data)
            end_time = datetime.now()
            time_taken_seconds = (end_time - start_time).total_seconds()
            time_taken_formatted = "{:.2f}".format(time_taken_seconds)
            with open(file_name, "rb") as file:
                bin_inf = bin_info(a)
                bot.delete_message(message_id=initial_message.message_id,chat_id=chat_id)
                bot.send_document(message.chat.id, file, caption=f"𝗰𝗼𝘂𝗻𝘁 =>> {e}\n{bin_inf}\n𝘁𝗼𝗼𝗸 =>>{time_taken_formatted}s")
            os.remove(file_name)
        except Exception as ex:
            bot.edit_message_text(chat_id=chat_id, message_id=initial_message.message_id, text=f"𝗮𝗻 𝗲𝗿𝗿𝗼𝗿 𝗼𝗰𝗰𝘂𝗿𝗿𝗲𝗱: {str(ex)}")
    else:
        pass

@bot.message_handler(commands=['gen'])
def generate_card(message):
    if bot_working:
        chat_id = message.chat.id
        try:
            initial_message = bot.reply_to(message, "𝗴𝗲𝗻𝗲𝗿𝗮𝘁𝗶𝗻𝗴 𝘀𝘁𝗮𝗿𝘁𝗲𝗱...⏳")
            card_info = message.text.split('/gen ', 1)[1]
            def multi_explode(delimiters, string):
                pattern = '|'.join(map(re.escape, delimiters))
                return re.split(pattern, string)
        
            split_values = multi_explode([":", "|", "⋙", " ", "/"], card_info)
            bin_value = ""
            mes_value = ""
            ano_value = ""
            cvv_value = ""
            
            if len(split_values) >= 1:
                bin_value = re.sub(r'[^0-9]', '', split_values[0])
            if len(split_values) >= 2:
                mes_value = re.sub(r'[^0-9]', '', split_values[1])
            if len(split_values) >= 3:
                ano_value = re.sub(r'[^0-9]', '', split_values[2])
            if len(split_values) >= 4:
                cvv_value = re.sub(r'[^0-9]', '', split_values[3])
            cards_data = ""
            f = 0
            while f < 10:
                card_number, exp_m, exp_y, cvv = gen_card(bin_value, mes_value, ano_value, cvv_value)
                cards_data += f"<code>{card_number}|{exp_m}|{exp_y}|{cvv}</code>\n"
                f += 1
            bot.edit_message_text(chat_id=chat_id, message_id=initial_message.message_id, text=cards_data)
        except Exception as e:
            bot.edit_message_text(chat_id=chat_id, message_id=initial_message.message_id, text=f"𝗮𝗻 𝗲𝗿𝗿𝗼𝗿 𝗼𝗰𝗰𝘂𝗿𝗿𝗲𝗱: {e}")
    else:
        pass

@bot.message_handler(commands=['scr'])
def send_last_messages(message):
    if bot_working:
        chat_id = message.chat.id
        initial_message = bot.reply_to(message, "𝘀𝗰𝗿𝗮𝗽𝗶𝗻𝗴 𝘀𝘁𝗮𝗿𝘁𝗲𝗱...⏳")
        start_time = datetime.now()
        command_parts = message.text.split()
        if len(command_parts) == 3 and command_parts[0] == '/scr':
            
            username = command_parts[1]
            limit = int(command_parts[2])
            try:
                username = int(username)
            except ValueError:
                pass
            loop = asyncio.new_event_loop()
            asyncio.set_event_loop(loop)
            messages_text = loop.run_until_complete(get_last_messages(username, limit))
            save_to_file(messages_text)
            file_len = len(messages_text.split('\n'))
            end_time = datetime.now()
            time_taken_seconds = (end_time - start_time).total_seconds()
            time_taken_formatted = "{:.2f}".format(time_taken_seconds)
            captain_info = f"𝗰𝗮𝗿𝗱𝘀 = {file_len}\n𝘁𝗼𝗼𝗸 = {time_taken_formatted}s\n𝘀𝗼𝘂𝗿𝗰𝗲 = {command_parts[1]}"
            with open('combo.txt', 'rb') as file:
                bot.delete_message(message_id=initial_message.message_id,chat_id=chat_id)
                bot.send_document(message.chat.id, file,caption=captain_info)
        else:
            bot.edit_message_text(chat_id=chat_id, message_id=initial_message.message_id, text="𝗶𝗻𝘃𝗮𝗹𝗶𝗱 𝗰𝗼𝗺𝗺𝗮𝗻𝗱 𝗳𝗼𝗿𝗺𝗮𝘁. 𝘂𝘀𝗲 /scr [username/id] [limit]")
    else:
        pass

@bot.message_handler(commands=['sk'])
def handle_sk_message(message):
    if bot_working:
        chat_id = message.chat.id
        command_parts = message.text.split()
        initial_message = bot.reply_to(message, "𝗰𝗵𝗲𝗰𝗸𝗶𝗻𝗴 𝘀𝘁𝗮𝗿𝘁𝗲𝗱...⏳")
        if len(command_parts) != 2:
            bot.edit_message_text(chat_id=chat_id, message_id=initial_message.message_id, text= "𝗶𝗻𝘃𝗮𝗹𝗶𝗱 𝗰𝗼𝗺𝗺𝗮𝗻𝗱 𝗳𝗼𝗿𝗺𝗮𝘁. 𝗽𝗹𝗲𝗮𝘀𝗲 𝘂𝘀𝗲 '/sk <sk_key>'",parse_mode='none')
            return
        sk = command_parts[1]
        result = check_key(sk)
        bot.edit_message_text(chat_id=chat_id, message_id=initial_message.message_id, text=result)
    else:
        pass

@bot.message_handler(commands=['str'])
def stripe_chk_command(message):
    if bot_working:
        if not gate_status['str']:
            bot.reply_to(message, "❗️ 𝘁𝗵𝗶𝘀 𝗴𝗮𝘁𝗲𝘄𝗮𝘆 𝗶𝘀 𝗰𝘂𝗿𝗿𝗲𝗻𝘁𝗹𝘆 𝗱𝗶𝘀𝗮𝗯𝗹𝗲𝗱.")
            return
        chat_id = message.chat.id
        try:
            card_details = message.text.split(' ')
            if len(card_details) != 2:bot.send_message(message.chat.id, "𝗶𝗻𝘃𝗮𝗹𝗶𝗱 𝗰𝗼𝗺𝗺𝗮𝗻𝗱 𝗳𝗼𝗿𝗺𝗮𝘁. 𝗽𝗹𝗲𝗮𝘀𝗲 𝘂𝘀𝗲 '/str <card>'",parse_mode='none');return
            card_details = message.text.split(' ')[1]
            initial_message = bot.reply_to(message, "𝗰𝗵𝗲𝗰𝗸𝗶𝗻𝗴 𝘀𝘁𝗮𝗿𝘁𝗲𝗱, 𝗽𝗹𝗲𝗮𝘀𝗲 𝘄𝗮𝗶𝘁 ⌛")
            edited_message = process_card(card_details)[4]
            bot.edit_message_text(chat_id=chat_id, message_id=initial_message.message_id, text=edited_message)
        except Exception as e:
            bot.send_message(chat_id=chat_id, text="𝗮𝗻 𝗲𝗿𝗿𝗼𝗿 𝗼𝗰𝗰𝘂𝗿𝗿𝗲𝗱: " + str(e))
    else:
        pass

@bot.message_handler(commands=['filep'])
def payal_file_command(message):
    if bot_working:
        if not gate_status['filep']:
            bot.reply_to(message, "❗️ 𝘁𝗵𝗶𝘀 𝗴𝗮𝘁𝗲𝘄𝗮𝘆 𝗶𝘀 𝗰𝘂𝗿𝗿𝗲𝗻𝘁𝗹𝘆 𝗱𝗶𝘀𝗮𝗯𝗹𝗲𝗱.")
            return
        bot.reply_to(message,"𝘀𝗲𝗻𝗱 𝘁𝗵𝗲 𝗰𝗼𝗺𝗯𝗼 𝗳𝗶𝗹𝗲.")
        bot.register_next_step_handler(message, handle_paypal_file)
    else:
        pass
        
# ——————————— Premium Commands (Subscription Required) ——————————— #
@bot.message_handler(commands=['chk'])
def brinetree_chk_command(message):
    is_subscribed, _ = check_subscription(message.from_user.id)
    if not is_subscribed:
        bot.reply_to(message, "𝘆𝗼𝘂 𝗺𝘂𝘀𝘁 𝗵𝗮𝘃𝗲 𝗮𝗻 𝗮𝗰𝘁𝗶𝘃𝗲 𝘀𝘂𝗯𝘀𝗰𝗿𝗶𝗽𝘁𝗶𝗼𝗻 𝘁𝗼 𝘂𝘀𝗲 𝘁𝗵𝗶𝘀 𝗰𝗼𝗺𝗺𝗮𝗻𝗱.", reply_markup=create_buy_keyboard())
        return
        
    if bot_working:
        if not gate_status['chk']:
            bot.reply_to(message, "❗️ 𝘁𝗵𝗶𝘀 𝗴𝗮𝘁𝗲𝘄𝗮𝘆 𝗶𝘀 𝗰𝘂𝗿𝗿𝗲𝗻𝘁𝗹𝘆 𝗱𝗶𝘀𝗮𝗯𝗹𝗲𝗱.")
            return
        chat_id = message.chat.id
        try:
            card_details = message.text.split(' ')
            if len(card_details) != 2:bot.send_message(message.chat.id, "𝗶𝗻𝘃𝗮𝗹𝗶𝗱 𝗰𝗼𝗺𝗺𝗮𝗻𝗱 𝗳𝗼𝗿𝗺𝗮𝘁. 𝗽𝗹𝗲𝗮𝘀𝗲 𝘂𝘀𝗲 '/chk <card>'",parse_mode='none');return
            card_details = message.text.split(' ')[1]
            initial_message = bot.reply_to(message, "𝗰𝗵𝗲𝗰𝗸𝗶𝗻𝗴 𝘀𝘁𝗮𝗿𝘁𝗲𝗱, 𝗽𝗹𝗲𝗮𝘀𝗲 𝘄𝗮𝗶𝘁 ⌛")
            edited_message = process_card_b(card_details)[4]
            bot.edit_message_text(chat_id=chat_id, message_id=initial_message.message_id, text=edited_message)
        except Exception as e:
            bot.send_message(chat_id=chat_id, text="𝗮𝗻 𝗲𝗿𝗿𝗼𝗿 𝗼𝗰𝗰𝘂𝗿𝗿𝗲𝗱: " + str(e))
    else:
        pass

@bot.message_handler(commands=['pay'])
def paypal_chk_command(message):
    is_subscribed, _ = check_subscription(message.from_user.id)
    if not is_subscribed:
        bot.reply_to(message, "𝘆𝗼𝘂 𝗺𝘂𝘀𝘁 𝗵𝗮𝘃𝗲 𝗮𝗻 𝗮𝗰𝘁𝗶𝘃𝗲 𝘀𝘂𝗯𝘀𝗰𝗿𝗶𝗽𝘁𝗶𝗼𝗻 𝘁𝗼 𝘂𝘀𝗲 𝘁𝗵𝗶𝘀 𝗰𝗼𝗺𝗺𝗮𝗻𝗱.", reply_markup=create_buy_keyboard())
        return
        
    if bot_working:
        if not gate_status['pay']:
            bot.reply_to(message, "❗️ 𝘁𝗵𝗶𝘀 𝗴𝗮𝘁𝗲𝘄𝗮𝘆 𝗶𝘀 𝗰𝘂𝗿𝗿𝗲𝗻𝘁𝗹𝘆 𝗱𝗶𝘀𝗮𝗯𝗹𝗲𝗱.")
            return
        chat_id = message.chat.id
        try:
            card_details = message.text.split(' ')
            if len(card_details) != 2:
                bot.send_message(message.chat.id, "𝗶𝗻𝘃𝗮𝗹𝗶𝗱 𝗰𝗼𝗺𝗺𝗮𝗻𝗱 𝗳𝗼𝗿𝗺𝗮𝘁. 𝗽𝗹𝗲𝗮𝘀𝗲 𝘂𝘀𝗲 '/pay <card>'", parse_mode='none')
                return
            card_details = message.text.split(' ')[1]
            initial_message = bot.reply_to(message, "𝗰𝗵𝗲𝗰𝗸𝗶𝗻𝗴 𝘀𝘁𝗮𝗿𝘁𝗲𝗱, 𝗽𝗹𝗲𝗮𝘀𝗲 𝘄𝗮𝗶𝘁 ⌛")
            for _ in range (5):
                try:
                    result = process_card_p(card_details)
                    card = result[4]
                    bin_inf = bin_info(result[0])
                    edited_message = (f"{card}")
                    edited_message = edited_message.replace("bin_info",f"═════『 𝗕𝗜𝗡 𝗜𝗡𝗙𝗢 』═════\n{bin_inf}")
                    print(edited_message)
                    bot.edit_message_text(chat_id=chat_id, message_id=initial_message.message_id, text=edited_message)
                    break
                except Exception:pass
        except Exception as e:
            bot.send_message(chat_id=chat_id, text="𝗮𝗻 𝗲𝗿𝗿𝗼𝗿 𝗼𝗰𝗰𝘂𝗿𝗿𝗲𝗱: " + str(e))
    else:
        pass

@bot.message_handler(commands=['filestr'])
def stripe_fill_command(message):
    is_subscribed, _ = check_subscription(message.from_user.id)
    if not is_subscribed:
        bot.reply_to(message, "𝘆𝗼𝘂 𝗺𝘂𝘀𝘁 𝗵𝗮𝘃𝗲 𝗮𝗻 𝗮𝗰𝘁𝗶𝘃𝗲 𝘀𝘂𝗯𝘀𝗰𝗿𝗶𝗽𝘁𝗶𝗼𝗻 𝘁𝗼 𝘂𝘀𝗲 𝘁𝗵𝗶𝘀 𝗰𝗼𝗺𝗺𝗮𝗻𝗱.", reply_markup=create_buy_keyboard())
        return

    global is_card_checking
    if bot_working:
        if not gate_status['filestr']:
            bot.reply_to(message, "❗️ 𝘁𝗵𝗶𝘀 𝗴𝗮𝘁𝗲𝘄𝗮𝘆 𝗶𝘀 𝗰𝘂𝗿𝗿𝗲𝗻𝘁𝗹𝘆 𝗱𝗶𝘀𝗮𝗯𝗹𝗲𝗱.")
            return
        
        bot.reply_to(message,"𝘀𝗲𝗻𝗱 𝘁𝗵𝗲 𝗰𝗼𝗺𝗯𝗼 𝗳𝗶𝗹𝗲.")
        bot.register_next_step_handler(message, handle_stripe_file)
    else:
        pass

@bot.message_handler(commands=['file'])
def brintree_file_command(message):
    is_subscribed, _ = check_subscription(message.from_user.id)
    if not is_subscribed:
        bot.reply_to(message, "𝘆𝗼𝘂 𝗺𝘂𝘀𝘁 𝗵𝗮𝘃𝗲 𝗮𝗻 𝗮𝗰𝘁𝗶𝘃𝗲 𝘀𝘂𝗯𝘀𝗰𝗿𝗶𝗽𝘁𝗶𝗼𝗻 𝘁𝗼 𝘂𝘀𝗲 𝘁𝗵𝗶𝘀 𝗰𝗼𝗺𝗺𝗮𝗻𝗱.", reply_markup=create_buy_keyboard())
        return
        
    global is_card_checking
    if bot_working:
        if not gate_status['file']:
            bot.reply_to(message, "❗️ 𝘁𝗵𝗶𝘀 𝗴𝗮𝘁𝗲𝘄𝗮𝘆 𝗶𝘀 𝗰𝘂𝗿𝗿𝗲𝗻𝘁𝗹𝘆 𝗱𝗶𝘀𝗮𝗯𝗹𝗲𝗱.")
            return
        bot.reply_to(message,"𝘀𝗲𝗻𝗱 𝘁𝗵𝗲 𝗰𝗼𝗺𝗯𝗼 𝗳𝗶𝗹𝗲.")
        bot.register_next_step_handler(message, handle_braintree_file)
    else:
        pass

# ——————————— File Handlers and Callbacks ——————————— #
def handle_stripe_file(message):
    global is_card_checking
    if not message.document:
        bot.reply_to(message, "𝗽𝗹𝗲𝗮𝘀𝗲 𝘀𝗲𝗻𝗱 𝗮 𝗳𝗶𝗹𝗲.")
        return
        
    is_card_checking = True
    try:
        file_info = bot.get_file(message.document.file_id)
        downloaded_file = bot.download_file(file_info.file_path)
        file_content = downloaded_file.decode('utf-8')
        card_lines = file_content.strip().split('\n')
        msg = bot.send_message(chat_id=message.chat.id,text="𝗰𝗵𝗲𝗰𝗸𝗶𝗻𝗴 𝘀𝘁𝗮𝗿𝘁𝗲𝗱, 𝗽𝗹𝗲𝗮𝘀𝗲 𝘄𝗮𝗶𝘁 ⌛")
        
        not_working_cards, working_cards, cards_3D_secure, insufficient_founds, ccn_cards, live_cards = [], [], [], [], [], []
        
        for card in card_lines:
            if not is_card_checking: break
            result = process_card(card)
            num = result[3]
            lists_mapping = {
                1: working_cards, 2: live_cards, 3: insufficient_founds,
                4: ccn_cards, 5: not_working_cards, 6: cards_3D_secure
            }
            if num in lists_mapping:
                lists_mapping[num].append(card)
            
            msg_text = result[1]
            if result[2]:
                bot.send_message(message.chat.id,result[4])
            
            reply_markup = create_reply_markup_stripe(card, len(not_working_cards),len(live_cards), len(working_cards), len(cards_3D_secure) ,len(insufficient_founds),len(ccn_cards),msg_text,len(card_lines))
            try:
                bot.edit_message_text(
                    chat_id=message.chat.id, message_id=msg.message_id,
                    text="𝗰𝗵𝗲𝗰𝗸𝗶𝗻𝗴 𝗶𝗻 𝗽𝗿𝗼𝗴𝗿𝗲𝘀𝘀, 𝗽𝗹𝗲𝗮𝘀𝗲 𝘄𝗮𝗶𝘁...", reply_markup=reply_markup
                )
            except telebot.apihelper.ApiTelegramException:
                time.sleep(2)
        
        is_card_checking = False
        bot.send_message(message.chat.id, "𝗳𝗶𝗹𝗲 𝗰𝗵𝗲𝗰𝗸𝗶𝗻𝗴 𝗳𝗶𝗻𝗶𝘀𝗵𝗲𝗱.")
    except Exception as e:
        print(e)
        bot.send_message(message.chat.id, f"𝗮𝗻 𝗲𝗿𝗿𝗼𝗿 𝗼𝗰𝗰𝘂𝗿𝗿𝗲𝗱: {e}")
        is_card_checking = False

def create_reply_markup_stripe(current_card, num_not_working, num_live, num_working,num_cards_3D_secure, num_insufficient_founds, num_ccn, message_text, All):
    markup = types.InlineKeyboardMarkup()
    markup.row(types.InlineKeyboardButton(text=f"⌜ • {current_card} • ⌝", callback_data="current_card"))
    markup.row(types.InlineKeyboardButton(text=f" ⌯ {message_text} ⌯ ", callback_data="message"))
    markup.row(types.InlineKeyboardButton(text=f"𝗰𝗵𝗮𝗿𝗴𝗲𝗱: {num_working}", callback_data="working"),
               types.InlineKeyboardButton(text=f"𝗹𝗶𝘃𝗲: {num_live}", callback_data="live"))
    markup.row(types.InlineKeyboardButton(text=f"𝗶𝗻𝘀𝘂𝗳𝗳 𝗳𝘂𝗻𝗱𝘀: {num_insufficient_founds}", callback_data="no thing"),
               types.InlineKeyboardButton(text=f"𝗰𝗰𝗻: {num_ccn}", callback_data="no thing"))
    markup.row(types.InlineKeyboardButton(text=f"⌞ • 𝗮𝗹𝗹: {All} ┇ 𝗱𝗲𝗰𝗹𝗶𝗻𝗲𝗱: {num_not_working} ┇𝗼𝘁𝗽: {num_cards_3D_secure} • ⌟", callback_data="no thing"))
    markup.row(types.InlineKeyboardButton(text="〄 𝘀𝘁𝗼𝗽 〄", callback_data="stop"))
    return markup

def handle_braintree_file(message):
    global is_card_checking
    if not message.document:
        bot.reply_to(message, "𝗽𝗹𝗲𝗮𝘀𝗲 𝘀𝗲𝗻𝗱 𝗮 𝗳𝗶𝗹𝗲.")
        return
        
    is_card_checking = True
    try:
        file_info = bot.get_file(message.document.file_id)
        downloaded_file = bot.download_file(file_info.file_path)
        file_content = downloaded_file.decode('utf-8')
        card_lines = file_content.strip().split('\n')
        msg = bot.send_message(chat_id=message.chat.id,text="𝗰𝗵𝗲𝗰𝗸𝗶𝗻𝗴 𝘀𝘁𝗮𝗿𝘁𝗲𝗱, 𝗽𝗹𝗲𝗮𝘀𝗲 𝘄𝗮𝗶𝘁 ⌛")
        
        not_working_cards, working_cards, risk_cards, insufficient_founds, ccn_cards, live_cards = [], [], [], [], [], []
        
        for card in card_lines:
            if not is_card_checking: break
            result = process_card_b(card)
            num = result[3]
            lists_mapping = {
                1: working_cards, 2: live_cards, 3: insufficient_founds,
                4: ccn_cards, 5: not_working_cards, 6: risk_cards
            }
            if num in lists_mapping:
                lists_mapping[num].append(card)
                
            msg_text = result[1]
            if result[2]:
                bot.send_message(message.chat.id,result[4])
                
            reply_markup = create_reply_markup_braintree(card, len(not_working_cards),len(live_cards), len(insufficient_founds),len(ccn_cards),msg_text,len(card_lines),len(risk_cards))
            try:
                bot.edit_message_text(
                    chat_id=message.chat.id, message_id=msg.message_id,
                    text="𝗰𝗵𝗲𝗰𝗸𝗶𝗻𝗴 𝗶𝗻 𝗽𝗿𝗼𝗴𝗿𝗲𝘀𝘀, 𝗽𝗹𝗲𝗮𝘀𝗲 𝘄𝗮𝗶𝘁...", reply_markup=reply_markup
                )
            except telebot.apihelper.ApiTelegramException:
                time.sleep(2)
        is_card_checking = False
        bot.send_message(message.chat.id, "𝗳𝗶𝗹𝗲 𝗰𝗵𝗲𝗰𝗸𝗶𝗻𝗴 𝗳𝗶𝗻𝗶𝘀𝗵𝗲𝗱.")
    except Exception as e:
        print(e)
        bot.send_message(message.chat.id, f"𝗮𝗻 𝗲𝗿𝗿𝗼𝗿 𝗼𝗰𝗰𝘂𝗿𝗿𝗲𝗱: {e}")
        is_card_checking = False

def create_reply_markup_braintree(current_card, num_not_working, num_live,  num_insufficient_founds, num_ccn, message_text, All,num_risk):
    markup = types.InlineKeyboardMarkup()
    markup.row(types.InlineKeyboardButton(text=f"⌜ • {current_card} • ⌝", callback_data="current_card"))
    markup.row(types.InlineKeyboardButton(text=f" ⌯ {message_text} ⌯ ", callback_data="message"))
    markup.row(types.InlineKeyboardButton(text=f"𝗹𝗶𝘃𝗲: {num_live}", callback_data="live"))
    markup.row(types.InlineKeyboardButton(text=f"𝗶𝗻𝘀𝘂𝗳𝗳 𝗳𝘂𝗻𝗱𝘀: {num_insufficient_founds}", callback_data="no thing"),
               types.InlineKeyboardButton(text=f"𝗰𝗰𝗻: {num_ccn}", callback_data="no thing"))
    markup.row(types.InlineKeyboardButton(text=f"⌞ • 𝗮𝗹𝗹: {All} ┇ 𝗱𝗲𝗰𝗹𝗶𝗻𝗲𝗱: {num_not_working} ┇𝗿𝗶𝘀𝗸: {num_risk} • ⌟", callback_data="no thing"))
    markup.row(types.InlineKeyboardButton(text="〄 𝘀𝘁𝗼𝗽 〄", callback_data="stop"))
    return markup
    
def handle_paypal_file(message):
    global is_card_checking
    if not message.document:
        bot.reply_to(message, "𝗽𝗹𝗲𝗮𝘀𝗲 𝘀𝗲𝗻𝗱 𝗮 𝗳𝗶𝗹𝗲.")
        return

    is_card_checking = True
    try:
        file_info = bot.get_file(message.document.file_id)
        downloaded_file = bot.download_file(file_info.file_path)
        file_content = downloaded_file.decode('utf-8')
        card_lines = file_content.strip().split('\n')
        msg = bot.send_message(chat_id=message.chat.id, text="𝗰𝗵𝗲𝗰𝗸𝗶𝗻𝗴 𝘀𝘁𝗮𝗿𝘁𝗲𝗱, 𝗽𝗹𝗲𝗮𝘀𝗲 𝘄𝗮𝗶𝘁 ⌛")
        
        not_working_cards, working_cards, risk_cards, insufficient_founds, ccn_cards = [], [], [], [], []

        for card in card_lines:
            if not is_card_checking: break
            
            result = process_card_p(card)
            num = result[3]
            lists_mapping = {
                1: working_cards, 2: insufficient_founds, 3: ccn_cards,
                4: not_working_cards, 5: risk_cards
            }
            if num in lists_mapping:
                lists_mapping[num].append(card)

            msg_text = result[1]
            if result[2]:
                bot.send_message(message.chat.id, result[4])

            reply_markup = create_reply_markup_paypal(card, len(not_working_cards), len(working_cards), len(insufficient_founds), len(ccn_cards), msg_text, len(card_lines), len(risk_cards))
            try:
                bot.edit_message_text(
                    chat_id=message.chat.id, message_id=msg.message_id,
                    text="𝗰𝗵𝗲𝗰𝗸𝗶𝗻𝗴 𝗶𝗻 𝗽𝗿𝗼𝗴𝗿𝗲𝘀𝘀, 𝗽𝗹𝗲𝗮𝘀𝗲 𝘄𝗮𝗶𝘁...", reply_markup=reply_markup
                )
            except telebot.apihelper.ApiTelegramException:
                time.sleep(2)
        
        is_card_checking = False
        bot.send_message(message.chat.id, "𝗳𝗶𝗹𝗲 𝗰𝗵𝗲𝗰𝗸𝗶𝗻𝗴 𝗳𝗶𝗻𝗶𝘀𝗵𝗲𝗱.")
    except Exception as e:
        print(e)
        bot.send_message(message.chat.id, f"𝗮𝗻 𝗲𝗿𝗿𝗼𝗿 𝗼𝗰𝗰𝘂𝗿𝗿𝗲𝗱: {e}")
        is_card_checking = False

def create_reply_markup_paypal(current_card, num_not_working, num_working,  num_insufficient_founds, num_ccn, message_text, All,num_risk):
    markup = types.InlineKeyboardMarkup()
    markup.row(types.InlineKeyboardButton(text=f"⌜ • {current_card} • ⌝", callback_data="current_card"))
    markup.row(types.InlineKeyboardButton(text=f" ⌯ {message_text} ⌯ ", callback_data="message"))
    markup.row(types.InlineKeyboardButton(text=f"𝗹𝗶𝘃𝗲: {num_working}", callback_data="live"))
    markup.row(types.InlineKeyboardButton(text=f"𝗶𝗻𝘀𝘂𝗳𝗳𝗶𝗰𝗶𝗲𝗻𝘁 𝗳𝘂𝗻𝗱𝘀: {num_insufficient_founds}", callback_data="no thing"),
               types.InlineKeyboardButton(text=f"𝗰𝗰𝗻: {num_ccn}", callback_data="no thing"))
    markup.row(types.InlineKeyboardButton(text=f"⌞ • 𝗮𝗹𝗹: {All} ┇ 𝗱𝗲𝗰𝗹𝗶𝗻𝗲𝗱: {num_not_working} ┇𝗼𝘁𝗽: {num_risk} • ⌟", callback_data="no thing"))
    markup.row(types.InlineKeyboardButton(text="〄 𝘀𝘁𝗼𝗽 〄", callback_data="stop"))
    return markup

@bot.callback_query_handler(func=lambda call: call.data == "stop")
def stop_checking_callback(call):
    global is_card_checking
    is_card_checking = False
    bot.answer_callback_query(call.id, text="𝗰𝗮𝗿𝗱 𝗰𝗵𝗲𝗰𝗸𝗶𝗻𝗴 𝘀𝘁𝗼𝗽𝗽𝗲𝗱.")
    bot.edit_message_text("𝗰𝗮𝗿𝗱 𝗰𝗵𝗲𝗰𝗸𝗶𝗻𝗴 𝘄𝗮𝘀 𝘀𝘁𝗼𝗽𝗽𝗲𝗱 𝗯𝘆 𝘁𝗵𝗲 𝘂𝘀𝗲𝗿.", chat_id=call.message.chat.id, message_id=call.message.message_id)


@bot.callback_query_handler(func=lambda call: call.data in ["current_card", "message", "working", "live", "no thing"])
def do_nothing_callback(call):
    bot.answer_callback_query(call.id)

#—————–————–———————––———#
# Main polling loop with error handling
#—————–————–———————––———#
if __name__ == '__main__':
    while True:
        try:
            print("𝗯𝗼𝘁 𝗶𝘀 𝗿𝘂𝗻𝗻𝗶𝗻𝗴...")
            bot.polling(none_stop=True)
        except Exception as e:
            error_message = f"❗️ 𝗯𝗼𝘁 𝗰𝗿𝗮𝘀𝗵𝗲𝗱 𝘄𝗶𝘁𝗵 𝗲𝗿𝗿𝗼𝗿: {e}\n\n🕒 𝘁𝗶𝗺𝗲: {datetime.now()}"
            print(error_message)
            
            with open("error.txt", "a", encoding='utf-8') as error_file:
                error_file.write(f"{error_message}\n" + "="*50 + "\n")
            
            try:
                bot.send_message(admin_id, error_message)
            except Exception as admin_notify_error:
                print(f"could not notify admin: {admin_notify_error}")
            
            time.sleep(5)