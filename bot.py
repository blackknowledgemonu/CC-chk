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
yboardButton("👑 OWNER", callback_data="admin"),
        types.InlineKeyboardButton("💳 CC CHECK", callback_data="cc"),
        types.InlineKeyboardButton("🔍 SCRAP", callback_data="scr"),
        types.InlineKeyboardButton("⚙️ COMBO", callback_data="combo")
    )
    return markup

# —————————— HANDLERS —————————— #
@bot.message_handler(commands=['start'])
def start_cmd(message):
    bot.send_video(
        message.chat.id,
        video="https://t.me/cccjwowowow/85",
        caption="<b>𝘄𝗲𝗹𝗰𝗼𝗺𝗲 𝘁𝗼 𝘁𝗵𝗲 𝗯𝗼𝘁 ❤️🇪🇬</b>\n\nStatus: 🟢 <code>Online</code>\nAdmin ID: <code>1677950104</code>",
        reply_markup=main_menu()
    )

@bot.callback_query_handler(func=lambda call: True)
def handle_callbacks(call):
    if call.data == "cc":
        bot.edit_message_caption("─────── 💳 <b>Card Check Menu</b> ───────\n\n/chk3 - Braintree Dual\n/str - Stripe Charge\n/bin - BIN Lookup", 
                                 call.message.chat.id, call.message.message_id, reply_markup=main_menu())
    
    elif call.data == "admin":
        if call.from_user.id == admin_id:
            bot.edit_message_caption("👑 <b>Admin Control Panel</b>\n\n/admin - Control\n/gates - Control Gates\n/grant - Add Credits", 
                                     call.message.chat.id, call.message.message_id, reply_markup=main_menu())
        else:
            bot.answer_callback_query(call.id, "❌ Only Owner Access!", show_alert=True)

# —————————— START THE BOT —————————— #
if __name__ == '__main__':
    print("🚀 Bot starting on Render...")
    try:
        # Admin ko alert bhejte hain startup par
        bot.send_message(admin_id, "✅ <b>Bot is now ONLINE!</b>\nAll conflicts and 'braintree_Api' errors are fixed.")
    except:
        pass
    bot.infinity_polling(none_stop=True)
        else:
            bot.answer_callback_query(call.id, "❌ Only Owner Access!", show_alert=True)

# —————————— START THE BOT —————————— #
if __name__ == '__main__':
    print("🚀 Bot starting on Render...")
    try:
        # Admin ko alert bhejte hain startup par
        bot.send_message(admin_id, "✅ <b>Bot is now ONLINE!</b>\nAll conflicts and 'braintree_Api' errors are fixed.")
    except:
        pass
    bot.infinity_polling(none_stop=True)
, timedelta

# —————————— FIXED IMPORTS & CONFLICT RESOLUTION —————————— #
# Official Braintree library (Conflict Fixed)
try:
    import braintree as official_bt_lib
except ImportError:
    print("⚠️ Official braintree library not found in requirements.txt")

# Aapki local files (Naming Conflict Fixed)
try:
    # Yaad rahe GitHub par file ka naam my_braintree.py hona chahiye
    from my_braintree import process_card_b 
    from braintree_dual_checker import ali1
    from check_bins_fun import extract_bins
except ImportError as e:
    print(f"⚠️ Local File Link Error: {e}")

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
def create_main_menu():
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(
        types.InlineKeyboardButton("👑 OWNER", callback_data="admin"),
        types.InlineKeyboardButton("💳 CC CHECK", callback_data="cc"),
        types.InlineKeyboardButton("🔍 SCRAP", callback_data="scr"),
        types.InlineKeyboardButton("⚙️ COMBO", callback_data="combo")
    )
    return markup

# —————————— HANDLERS —————————— #
@bot.message_handler(commands=['start'])
def start_cmd(message):
    bot.send_video(
        message.chat.id,
        video="https://t.me/cccjwowowow/85",
        caption="<b>𝘄𝗲𝗹𝗰𝗼𝗺𝗲 𝘁𝗼 𝘁𝗵𝗲 𝗯𝗼𝘁 ❤️🇪🇬</b>\n\nStatus: 🟢 <code>Online</code>\nAdmin ID: <code>1677950104</code>",
        reply_markup=create_main_menu()
    )

@bot.callback_query_handler(func=lambda call: True)
def handle_callbacks(call):
    if call.data == "cc":
        bot.edit_message_caption("─────── 💳 <b>Card Check Menu</b> ───────\n\n/chk3 - Braintree Dual\n/str - Stripe Charge\n/bin - BIN Lookup", 
                                 call.message.chat.id, call.message.message_id, reply_markup=create_main_menu())
    
    elif call.data == "admin":
        if call.from_user.id == admin_id:
            bot.edit_message_caption("👑 <b>Admin Control Panel</b>\n\n/admin - Control\n/gates - Control Gates\n/grant - Add Credits", 
                                     call.message.chat.id, call.message.message_id, reply_markup=create_main_menu())
        else:
            bot.answer_callback_query(call.id, "❌ Only Owner Access!", show_alert=True)

# —————————— START —————————— #
if __name__ == '__main__':
    print("🚀 Bot is booting up on Render...")
    try:
        bot.send_message(admin_id, "✅ <b>Bot is now ONLINE!</b>\nConflict resolved and modules linked.")
    except:
        pass
    bot.infinity_polling(none_stop=True)

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

# —————————— HANDLERS —————————— #
@bot.message_handler(commands=['start'])
def start_cmd(message):
    bot.send_video(
        message.chat.id,
        video="https://t.me/cccjwowowow/85",
        caption="<b>𝘄𝗲𝗹𝗰𝗼𝗺𝗲 𝘁𝗼 𝘁𝗵𝗲 𝗯𝗼𝘁 ❤️🇪🇬</b>\n\nStatus: 🟢 <code>Online</code>\nAdmin ID: <code>1677950104</code>",
        reply_markup=main_menu()
    )

@bot.callback_query_handler(func=lambda call: True)
def handle_callbacks(call):
    if call.data == "cc":
        bot.edit_message_caption("─────── 💳 <b>Card Check Menu</b> ───────\n\n/chk3 - Braintree Dual\n/str - Stripe Charge\n/bin - BIN Lookup", 
                                 call.message.chat.id, call.message.message_id, reply_markup=main_menu())
    
    elif call.data == "admin":
        if call.from_user.id == admin_id:
            bot.edit_message_caption("👑 <b>Admin Control Panel</b>\n\n/admin - Control\n/gates - Control Gates\n/grant - Add Credits", 
                                     call.message.chat.id, call.message.message_id, reply_markup=main_menu())
        else:
            bot.answer_callback_query(call.id, "❌ Only Owner Access!", show_alert=True)

# —————————— START —————————— #
if __name__ == '__main__':
    print("🚀 Bot is booting up on Render...")
    try:
        bot.send_message(admin_id, "✅ <b>Bot is now ONLINE!</b>\nAll conflicts resolved and modules linked.")
    except:
        pass
    bot.infinity_polling(none_stop=True)
(parts[2])

        with open('data.json', 'r') as file:
            data = json.load(file)

        expiry_time = datetime.now() + timedelta(hours=hours)
        expiry_time_str = expiry_time.strftime('%Y-%m-%d %H:%M')

        data[str(target_user_id)] = {'timer': expiry_time_str, 'plan': 'granted_vip'}

        with open('data.json', 'w') as file:
            json.dump(data, file, indent=4)

        bot.reply_to(message, f"✅ 𝘀𝘂𝗰𝗰𝗲𝘀𝘀𝗳𝘂𝗹ly 𝗴𝗿𝗮𝗻𝘁𝗲𝗱 𝗮 {hours}-𝗵𝗼𝘂𝗿 𝘀𝘂𝗯𝘀𝗰𝗿𝗶𝗽𝘁𝗶𝗼𝗻 𝘁𝗼 𝘂𝘀𝗲𝗿 {target_user_id}.")
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

#حذف اشتراك
@bot.message_handler(commands=['remove'])
def revoke_command(message):
    if message.from_user.id != admin_id:
        return

    try:
        parts = message.text.split()
        if len(parts) != 2:
            bot.reply_to(message, "𝘂𝘀𝗮𝗴𝗲: /remove <user_id>")
            return

        target_user_id = str(parts[1])

        with open('data.json', 'r') as file:
            data = json.load(file)

        if target_user_id in data:
            del data[target_user_id]

            with open('data.json', 'w') as file:
                json.dump(data, file, indent=4)

            bot.reply_to(message, f"❌ 𝘀𝘂𝗯𝘀𝗰𝗿𝗶𝗽𝘁𝗶𝗼𝗻 𝗿𝗲𝘃𝗼𝗸𝗲𝗱 𝗳𝗼𝗿 𝘂𝘀𝗲𝗿 {target_user_id}.")
            # Notify the user
            bot.send_message(int(target_user_id), "⚠️ 𝘆𝗼𝘂𝗿 𝘀𝘂𝗯𝘀𝗰𝗿𝗶𝗽𝘁𝗶𝗼𝗻 𝗵𝗮𝘀 𝗯𝗲𝗲𝗻 𝗿𝗲𝘃𝗼𝗸𝗲𝗱 𝗯𝘆 𝘁𝗵𝗲 𝗮𝗱𝗺𝗶𝗻.")
        else:
            bot.reply_to(message, f"𝗻𝗼 𝘀𝘂𝗯𝘀𝗰𝗿𝗶𝗽𝘁𝗶𝗼𝗻 𝗳𝗼𝘂𝗻𝗱 𝗳𝗼𝗿 𝘂𝘀𝗲𝗿 {target_user_id}.")
    except Exception as e:
        bot.reply_to(message, f"𝗮𝗻 𝗲𝗿𝗿𝗼𝗿 𝗼𝗰𝗰𝘂𝗿𝗿𝗲𝗱: {e}")


product_creation_steps = {}
@bot.message_handler(commands=['addproduct'])
def add_product_command(message):
    if message.from_user.id != admin_id: return
    try:
        parts = message.text.split(maxsplit=2)
        price = int(parts[1])
        name = parts[2]
        
        product_creation_steps[message.chat.id] = {'name': name, 'price': price}
        
        bot.reply_to(message, f"✅ Product details received.\nName: {name}\nPrice: {price} ⭐\n\nNow, please send the .txt file to be sold.")
        bot.register_next_step_handler(message, handle_product_file)
    except (IndexError, ValueError):
        bot.reply_to(message, "⚠️ Incorrect format. Use: /addproduct <price_in_stars> <Product Name>")

def handle_product_file(message):
    if message.from_user.id != admin_id: return
    try:
        if message.document and message.document.mime_type == 'text/plain':
            file_id = message.document.file_id
            product_info = product_creation_steps.pop(message.chat.id)
            with open('store.json', 'r+') as f:
                store_data = json.load(f)
                new_product = {
                    "product_id": f"prod_{int(time.time())}",
                    "name": product_info['name'],
                    "price": product_info['price'],
                    "file_id": file_id
                }
                store_data.append(new_product)
                f.seek(0)
                json.dump(store_data, f, indent=4)
            bot.reply_to(message, f"✅ Product '{product_info['name']}' has been successfully added to the store.")
        else:
            bot.reply_to(message, "❌ Please send a valid .txt file.")
    except Exception as e:
        bot.reply_to(message, f"An error occurred: {e}")

@bot.callback_query_handler(func=lambda call: call.data == "open_store")
def open_store_callback(call):
    with open('store.json', 'r') as f:
        products = json.load(f)
    if not products:
        bot.answer_callback_query(call.id, "The store is currently empty.", show_alert=True)
        return
    markup = types.InlineKeyboardMarkup()
    for product in products:
        button_text = f"Buy '{product['name']}' for {product['price']} ⭐"
        markup.add(types.InlineKeyboardButton(button_text, callback_data=f"buy_product_{product['product_id']}"))
    markup.add(types.InlineKeyboardButton("🔙 𝗕𝗮𝗰𝗸", callback_data="back"))
    bot.edit_message_caption(
        chat_id=call.message.chat.id,
        message_id=call.message.message_id,
        caption="🛒 𝗪𝗲𝗹𝗰𝗼𝗺𝗲 𝘁𝗼 𝘁𝗵𝗲 𝘀𝘁𝗼𝗿𝗲! 𝗦𝗲𝗹𝗲𝗰𝘁 𝗮𝗻 𝗶𝘁𝗲𝗺 𝘁𝗼 𝗽𝘂𝗿𝗰𝗵𝗮𝘀𝗲.",
        reply_markup=markup
    )

@bot.callback_query_handler(func=lambda call: call.data.startswith('buy_product_'))
def buy_product_callback(call):
    product_id = call.data.replace('buy_product_', '')
    user_id_str = str(call.from_user.id)
    with open('purchases.json', 'r') as f:
        purchases = json.load(f)
    if user_id_str in purchases and product_id in purchases[user_id_str]:
        bot.answer_callback_query(call.id, "You have already purchased this item.", show_alert=True)
        return
    with open('store.json', 'r') as f:
        products = json.load(f)
    product_to_buy = next((p for p in products if p['product_id'] == product_id), None)
    if product_to_buy:
        prices = [LabeledPrice(label=product_to_buy['name'], amount=int(product_to_buy['price']))]
        bot.send_invoice(
            chat_id=call.message.chat.id, title="Purchase from Store",
            description=f"Payment for '{product_to_buy['name']}'",
            provider_token="", # Your payment provider token here
            currency="XTR", prices=prices, start_parameter="pay_with_stars",
            invoice_payload=f"product-{product_id}"
        )
    else:
        bot.answer_callback_query(call.id, "Sorry, this product could not be found.", show_alert=True)


@bot.message_handler(content_types=["successful_payment"])
def successful_payment(message):
    invoice_payload = message.successful_payment.invoice_payload
    user = message.from_user
    chat_id = message.chat.id

    # --- Handle Instant Subscription Activation (No changes here) ---
    if invoice_payload.startswith("Star-"):
        h_str = invoice_payload.split('-')[1].replace('h', '')
        h = int(h_str)
        expiry_time = datetime.now() + timedelta(hours=h)
        plan = 'vip'
        expiry_time_formatted = expiry_time.strftime('%Y-%m-%d %H:%M')
        with open('data.json', 'r+') as f:
            existing_data = json.load(f)
            existing_data[str(user.id)] = {"plan": plan, "timer": expiry_time_formatted}
            f.seek(0)
            json.dump(existing_data, f, indent=4)
            f.truncate()
        msg = f'''<b>
✅ 𝗣𝗮𝘆𝗺𝗲𝗻𝘁 𝗦𝘂𝗰𝗰𝗲𝘀𝘀𝗳𝘂𝗹!
Your subscription has been activated directly on your account.
├ 𝗦𝘁𝗮𝘁𝘂𝘀 » {plan}
├ 𝗘𝘅𝗽𝗶𝗿𝗲𝘀 𝗼𝗻 » {expiry_time_formatted}
</b>'''
        bot.send_message(chat_id, msg, parse_mode="HTML")

    # --- NEW: Handle Store Purchase with AUTOMATIC DELETION ---
    elif invoice_payload.startswith("product-"):
        product_id = invoice_payload.split('-')[1]

        # 1. Open the store file for reading and modification
        with open('store.json', 'r+') as f:
            products = json.load(f)
            
            # 2. Find the product and its index
            product_to_deliver = None
            product_index = -1
            for i, p in enumerate(products):
                if p['product_id'] == product_id:
                    product_to_deliver = p
                    product_index = i
                    break
            
            if product_to_deliver:
                # 3. Deliver the file to the user
                bot.send_message(chat_id, f"✅ Payment successful for '{product_to_deliver['name']}'! Here is your file:")
                bot.send_document(chat_id, product_to_deliver['file_id'])

                # 4. Delete the product from the list
                if product_index != -1:
                    products.pop(product_index)
                
                # 5. Write the updated list (without the purchased item) back to the file
                f.seek(0)
                json.dump(products, f, indent=4)
                f.truncate()

                # Optional: Record the purchase for your own records
                with open('purchases.json', 'r+') as pf:
                    purchases = json.load(pf)
                    user_id_str = str(user.id)
                    if user_id_str not in purchases:
                        purchases[user_id_str] = []
                    purchases[user_id_str].append(product_id)
                    pf.seek(0)
                    json.dump(purchases, pf, indent=4)
            else:
                bot.send_message(chat_id, "❌ An error occurred while delivering your product. Please contact the admin.")
                bot.send_message(admin_id, f"⚠️ A payment was received for a product that could not be found (it may have been purchased simultaneously). Product ID: {product_id}, User ID: {user.id}")


@bot.message_handler(commands=['kill'])
def start_task(message):
    chat_id = message.chat.id
    
    # تحقق إذا كان المستخدم لديه مهمة تعمل بالفعل
    if active_tasks.get(chat_id):
        bot.reply_to(message, "⚠️ لديك مهمة تعمل بالفعل.")
        return

    active_tasks[chat_id] = True
    bot.reply_to(message, "🚀 المهمة بدأت، اكتب /stop لوقفها.")
    
    # يمكنك استبدال هذا اللوب بعملية فحص الملفات
    for i in range(1000):
        # تحقق إذا أعطى المستخدم أمر الإيقاف
        if not active_tasks.get(chat_id):
            bot.send_message(chat_id, "⛔ تم إيقاف المهمة يدويًا.")
            # لا تنس حذف المستخدم من القاموس عند انتهاء المهمة
            del active_tasks[chat_id] 
            return # استخدم return للخروج من الدالة تمامًا

        print(f"Task for {chat_id} is running, step {i+1}")
        time.sleep(2) # هذا يمثل عملية فحص بطاقة واحدة

    bot.send_message(chat_id, "✅ المهمة اكتملت بنجاح.")
    # لا تنس حذف المستخدم من القاموس عند انتهاء المهمة
    if active_tasks.get(chat_id):
        del active_tasks[chat_id]

@bot.message_handler(commands=['stop'])
def kill_task(message):
    chat_id = message.chat.id
    if active_tasks.get(chat_id):
        active_tasks[chat_id] = False
        bot.reply_to(message, "🛑 تم إرسال إشارة الإيقاف. ستتوقف المهمة خلال لحظات.")
    else:
        bot.reply_to(message, "لا توجد مهمة تعمل حاليًا لإيقافها.")


import time
#سرعه البوت
@bot.message_handler(commands=['ping', 'speed'])
@check_if_banned
@check_maintenance
def ping_command(message):
    start_time = time.time()
    sent = bot.reply_to(message, "⏳ 𝗽𝗶𝗻𝗴𝗶𝗻𝗴...")
    end_time = time.time()
    latency = (end_time - start_time) * 1000  # بالـ milliseconds

    bot.edit_message_text(
        chat_id=message.chat.id,
        message_id=sent.message_id,
        text=f"🏓 𝗣𝗼𝗻𝗴! 𝗟𝗮𝘁𝗲𝗻𝗰𝘆: {latency:.2f} 𝗺𝘀"
    )

# --- Reusable Broadcast Function ---
# --- Reusable Broadcast Function ---
def broadcast_to_all_users(message_text):
    """
    Sends a message to all users who have ever started the bot.
    Returns the count of successful and failed messages.
    """
    print("Starting broadcast...")
    success_count = 0
    fail_count = 0
    
    try:
        subscribed_users_ids = []
        free_users_ids = []

        # Get subscribed users from data.json
        try:
            with open('data.json', 'r') as file:
                data = json.load(file)
            subscribed_users_ids = [key for key in data.keys() if key.isdigit()]
        except (FileNotFoundError, json.JSONDecodeError):
            print("data.json not found or is empty.")

        # Get all users from free.json
        try:
            with open('free.json', 'r') as file:
                free_users_ids_int = json.load(file)
                free_users_ids = [str(uid) for uid in free_users_ids_int]
        except (FileNotFoundError, json.JSONDecodeError):
            print("free.json not found or is empty.")

        # Combine lists and remove duplicates
        all_user_ids = list(set(subscribed_users_ids + free_users_ids))

        if not all_user_ids:
            print("No users found to send a message to.")
            return 0, 0

        for user_id in all_user_ids:
            try:
                # Removed parse_mode to avoid errors with special characters
                bot.send_message(int(user_id), message_text) 
                success_count += 1
                time.sleep(0.1)  # To avoid hitting rate limits
            except Exception as e:
                print(f"Failed to send to {user_id}: {e}")
                fail_count += 1
        
        print(f"Broadcast finished. Success: {success_count}, Failed: {fail_count}")
        return success_count, fail_count

    except Exception as e:
        print(f"An error occurred during broadcast: {e}")
        return success_count, fail_count

@bot.message_handler(commands=['broadcast'])
def broadcast_command(message):
    if message.from_user.id != admin_id:
        return

    try:
        broadcast_message = message.text.split(maxsplit=1)[1]
    except IndexError:
        bot.reply_to(message, "𝗽𝗹𝗲𝗮𝘀𝗲 𝘄𝗿𝗶𝘁𝗲 𝗮 𝗺𝗲𝘀𝘀𝗮𝗴𝗲 𝗮𝗳𝘁𝗲𝗿 𝘁𝗵𝗲 𝗰𝗼𝗺𝗺𝗮𝗻𝗱. 𝘂𝘀𝗮𝗴𝗲: /broadcast <your_message>")
        return

    bot.reply_to(message, "⏳ 𝗦𝘁𝗮𝗿𝘁𝗶𝗻𝗴 𝗯𝗿𝗼𝗮𝗱𝗰𝗮𝘀𝘁...")
    
    success_count, fail_count = broadcast_to_all_users(broadcast_message)
    
    bot.reply_to(message, f"𝗯𝗿𝗼𝗮𝗱𝗰𝗮𝘀𝘁 𝗳𝗶𝗻𝗶𝘀𝗵𝗲𝗱.\n\n- ✅ 𝗦𝘂𝗰𝗰𝗲𝘀𝘀𝗳𝘂𝗹ly 𝘀𝗲𝗻𝘁 𝘁𝗼: {success_count} 𝘂𝘀𝗲𝗿𝘀.\n- ❌ 𝗙𝗮𝗶𝗹𝗲𝗱 𝘁𝗼 𝘀𝗲𝗻𝗱 𝘁𝗼: {fail_count} 𝘂𝘀𝗲𝗿𝘀.")


def format_stats(stats):
    return f"""
📊 <b>Progress</b> 📊

✅ CHARGE: {stats['CHARGE']}
🔰 3D/OTP: {stats['3D']}
💳 CCN: {stats['CCN']}
❌ Declined: {stats['DECLINED']}
⚡ Other: {stats['OTHER']}

📌 Total Checked: {stats['TOTAL']}
"""
#فردي
@bot.message_handler(commands=['pay5'])
@check_if_banned
@check_maintenance
@check_cooldown
def paypal5_command(message):
    if not gate_status['pay5']:
        bot.reply_to(message, "❗️ 𝘁𝗵𝗶𝘀 𝗴𝗮𝘁𝗲𝘄𝗮𝘆 𝗶𝘀 𝗰𝘂𝗿𝗿𝗲𝗻𝘁𝗹𝘆 𝗱𝗶𝘀𝗮𝗯𝗹𝗲𝗱.")
        return

    try:
        card = message.text.split()[1]
    except IndexError:
        bot.reply_to(message, "❌ Usage: /pay5 card|mm|yy|cvv")
        return

    bot.reply_to(message, "⏳ Checking PayPal $5...")
    success, response = process_card_paypal5(card)

    if "DECLINED" not in response:
        # Get BIN info and add it to the message
        card_number = card.split('|')[0]
        bin_number = card_number[:6]
        bin_info_text = bin_info(bin_number)

        final_response = f"{response}\n\n═════『 𝗕𝗜𝗡 𝗜𝗡𝗙𝗢 』═════\n{bin_info_text}"
        bot.send_message(message.chat.id, final_response, parse_mode="HTML")
    else:
        bot.send_message(message.chat.id, response, parse_mode="HTML")

# --------------------------
# أمر كومبو /payf (PREMIUM)
# --------------------------
@bot.message_handler(commands=['payf'])
@check_if_banned
@check_maintenance
def paypal5_combo_command(message):
    is_subscribed, _ = check_subscription(message.from_user.id)
    if not is_subscribed:
        bot.reply_to(message, "❌ 𝘆𝗼𝘂 𝗺𝘂𝘀𝘁 𝗵𝗮𝘃𝗲 𝗮 𝘀𝘂𝗯𝘀𝗰𝗿𝗶𝗽𝘁𝗶𝗼𝗻 𝘁𝗼 𝘂𝘀𝗲 𝘁𝗵𝗶𝘀 𝗰𝗼𝗺𝗺𝗮𝗻𝗱.", reply_markup=create_buy_keyboard())
        return

    if not gate_status.get('payf', True):
        bot.reply_to(message, "❗️ 𝘁𝗵𝗶𝘀 𝗴𝗮𝘁𝗲𝘄𝗮𝘆 𝗶𝘀 𝗰𝘂𝗿𝗿𝗲𝗻𝘁𝗹𝘆 𝗱𝗶𝘀𝗮𝗯𝗹𝗲𝗱.")
        return

    user_id = message.from_user.id
    active_tasks[user_id] = {"should_stop": False}

    bot.reply_to(message, "📂 𝗦𝗲𝗻𝗱 𝗺𝗲 𝘆𝗼𝘂𝗿 𝗰𝗼𝗺𝗯𝗼 𝗳𝗶𝗹𝗲 (.txt) 𝗳𝗼𝗿 𝗣𝗮𝘆𝗣𝗮𝗹 𝗖𝗵𝗲𝗰𝗸.")
    bot.register_next_step_handler(message, handle_paypal_file_upload_venom)


# ====== BLACK KNOWLEDGE PAYPAL DASHBOARD ======
def create_paypal_progress_keyboard(stats):
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.row(types.InlineKeyboardButton(text=f"💳 {stats['CURRENT_CARD']}", callback_data="ignore"))
    markup.row(types.InlineKeyboardButton(text=f"⚡ 𝗚𝗮𝘁𝗲: 𝗣𝗮𝘆𝗣𝗮𝗹 | 🧠 {stats['LAST_RESPONSE']}", callback_data="ignore"))
    markup.row(
        types.InlineKeyboardButton(text=f"✅ 𝗖𝗵𝗮𝗿𝗴𝗲𝗱: {stats.get('CHARGE', 0)}", callback_data="ignore"),
        types.InlineKeyboardButton(text=f"🔐 𝟯𝗗/𝗢𝗧𝗣: {stats.get('3D', 0)}", callback_data="ignore")
    )
    markup.row(
        types.InlineKeyboardButton(text=f"💰 𝗖𝗖𝗡: {stats.get('CCN', 0)}", callback_data="ignore"),
        types.InlineKeyboardButton(text=f"❌ 𝗗𝗲𝗰𝗹𝗶𝗻𝗲𝗱: {stats.get('DECLINED', 0)}", callback_data="ignore")
    )
    markup.row(types.InlineKeyboardButton(text=f"📊 𝗖𝗵𝗲𝗰𝗸𝗲𝗱: {stats.get('CHECKED', 0)}/{stats.get('TOTAL', 0)}", callback_data="ignore"))
    markup.row(types.InlineKeyboardButton(text="〄 𝙎𝙩𝙤𝙥 𝙑𝙀𝙉𝙊𝙈 〄", callback_data="stop_payf"))
    return markup


@bot.callback_query_handler(func=lambda call: call.data == "stop_payf")
def stop_payf_callback(call):
    user_id = call.from_user.id
    if user_id in active_tasks:
        active_tasks[user_id]["should_stop"] = True
        bot.answer_callback_query(call.id, "🛑 𝗦𝘁𝗼𝗽𝗽𝗶𝗻𝗴 𝗣𝗮𝘆𝗣𝗮𝗹 𝗖𝗵𝗲𝗰𝗸...")
    else:
        bot.answer_callback_query(call.id, "❌ No active check running.")


# ====== HANDLE FILE UPLOAD (VENOM STYLE) ======
def handle_paypal_file_upload_venom(message):
    if not message.document or message.document.mime_type != "text/plain":
        bot.reply_to(message, "❌ 𝗣𝗹𝗲𝗮𝘀𝗲 𝘀𝗲𝗻𝗱 𝗮 𝘃𝗮𝗹𝗶𝗱 .txt 𝗰𝗼𝗺𝗯𝗼 𝗳𝗶𝗹𝗲.")
        return

    user_id = message.from_user.id
    file_info = bot.get_file(message.document.file_id)
    downloaded_file = bot.download_file(file_info.file_path)

    temp_file = f"Temps/{user_id}_paypal.txt"
    with open(temp_file, "wb") as f:
        f.write(downloaded_file)

    try:
        with open(temp_file, "r", encoding="utf-8") as f:
            cards = [line.strip() for line in f if line.strip()]
    except Exception as e:
        bot.reply_to(message, f"❌ 𝗘𝗿𝗿𝗼𝗿 𝗿𝗲𝗮𝗱𝗶𝗻𝗴 𝗳𝗶𝗹𝗲: {e}")
        os.remove(temp_file)
        return

    total = len(cards)
    if total == 0:
        bot.reply_to(message, "⚠️ 𝗙𝗶𝗹𝗲 𝗶𝘀 𝗲𝗺𝗽𝘁𝘆 𝗼𝗿 𝗶𝗻𝘃𝗮𝗹𝗶𝗱.")
        os.remove(temp_file)
        return

    stats = {
        "CHARGE": 0, "3D": 0, "CCN": 0, "DECLINED": 0, "CHECKED": 0, "TOTAL": total,
        "CURRENT_CARD": "N/A", "LAST_RESPONSE": "Starting..."
    }

    status_msg = bot.send_message(
        message.chat.id,
        "⚡ <b>VENOM PayPal Combo Check Started...</b>",
        reply_markup=create_paypal_progress_keyboard(stats),
        parse_mode="HTML"
    )

    start_time = time.time()
    successful_results = []

    for card in cards:
        if active_tasks.get(user_id, {}).get("should_stop"):
            break

        stats["CHECKED"] += 1
        stats["CURRENT_CARD"] = card

        try:
            success, response = process_card_paypal5(card)
            stats["LAST_RESPONSE"] = response or "No Response"

            card_number = card.split('|')[0]
            bin_text = bin_info(card_number[:6])

            # ========= BLACK KNOWLEDGE RESPONSE SECTION =========
            if "CHARGE" in response:
                stats["CHARGE"] += 1
                msg = f"✅ 𝗖𝗵𝗮𝗿𝗴𝗲𝗱 (𝗣𝗮𝘆𝗣𝗮𝗹)\n━━━━━━━━━━━━━━━\n<code>{card}</code>\n🧠 {response}\n\n{bin_text}"
                successful_results.append(msg)
                bot.send_message(message.chat.id, msg, parse_mode="HTML")

            elif "3D" in response or "OTP" in response:
                stats["3D"] += 1
                msg = f"🔐 𝟯𝗗 𝗦𝗲𝗰𝘂𝗿𝗲/𝗢𝗧𝗣\n━━━━━━━━━━━━━━━\n<code>{card}</code>\n🧠 {response}\n\n{bin_text}"
                bot.send_message(message.chat.id, msg, parse_mode="HTML")

            elif "CCN" in response or "INVALID_SECURITY_CODE" in response:
                stats["CCN"] += 1
                msg = f"💳 𝗖𝗖𝗡 𝗖𝗮𝗿𝗱\n━━━━━━━━━━━━━━━\n<code>{card}</code>\n🧠 {response}\n\n{bin_text}"
                bot.send_message(message.chat.id, msg, parse_mode="HTML")

            elif any(x in response for x in ["EXISTING_ACCOUNT_RESTRICTED", "INVALID_BILLING_ADDRESS"]):
                stats["CCN"] += 1
                msg = f" 𝗢𝘁𝗵𝗲𝗿 𝗥𝗲𝘀𝗽𝗼𝗻𝘀𝗲\n━━━━━━━━━━━━━━━\n<code>{card}</code>\n🧠 {response}\n\n{bin_text}"
                bot.send_message(message.chat.id, msg, parse_mode="HTML")

            elif "DECLINED" in response:
                stats["DECLINED"] += 1
            else:
                stats["DECLINED"] += 1
            # ==========================================

        except Exception as e:
            stats["DECLINED"] += 1
            stats["LAST_RESPONSE"] = str(e)

        # تحديث العدادات أثناء الفحص BLACK KNOWLEDGE STYLE
        try:
            bot.edit_message_reply_markup(
                chat_id=message.chat.id,
                message_id=status_msg.message_id,
                reply_markup=create_paypal_progress_keyboard(stats)
            )
        except Exception:
            pass

        time.sleep(1.2)

    elapsed = round(time.time() - start_time, 2)
    os.remove(temp_file)
    if user_id in active_tasks:
        del active_tasks[user_id]

    summary_text = (
        f"✅ 𝗙𝗶𝗻𝗶𝘀𝗵𝗲𝗱 (𝗣𝗮𝘆𝗣𝗮𝗹)\n"
        f"━━━━━━━━━━━━━━━\n"
        f"📊 𝗖𝗵𝗲𝗰𝗸𝗲𝗱: {stats['CHECKED']}/{stats['TOTAL']}\n"
        f"✅ 𝗖𝗵𝗮𝗿𝗴𝗲𝗱: {stats['CHARGE']}\n"
        f"🔐 𝟯𝗗/𝗢𝗧𝗣: {stats['3D']}\n"
        f"💰 𝗖𝗖𝗡: {stats['CCN']}\n"
        f"❌ 𝗗𝗲𝗰𝗹𝗶𝗻𝗲𝗱: {stats['DECLINED']}\n"
        f"🕒 𝗧𝗶𝗺𝗲: {elapsed}s"
    )

    bot.edit_message_text(
        chat_id=message.chat.id,
        message_id=status_msg.message_id,
        text=summary_text,
        parse_mode="HTML"
    )

    if successful_results:
        live_file = f"Temps/{user_id}_PayPal_LIVE.txt"
        with open(live_file, "w", encoding="utf-8") as f:
            f.write("\n\n".join(successful_results))

        with open(live_file, "rb") as f:
            bot.send_document(message.chat.id, f, caption=f"✅ LIVE Results: {len(successful_results)}")
        os.remove(live_file)






@bot.message_handler(commands=['chgate'])
@check_if_banned
@check_maintenance
def check_gates_command(message):
    chat_id = message.chat.id
    initial_message = bot.reply_to(message, "🚦 𝗦𝘁𝗮𝗿𝘁𝗶𝗻𝗴 𝗵𝗲𝗮𝗹𝘁𝗵 𝗰𝗵𝗲𝗰𝗸 𝗳𝗼𝗿 𝗮𝗹𝗹 𝗴𝗮𝘁𝗲𝘀... ⏳")
    
    # Generate a fake card for testing all gates
    test_card = "4693080258964416|2|28|302"
    
    results = []
    
    # Check Braintree Single
    try:
        if gate_status['chk']:
            _ , response, _ , num, _ = process_card_b(test_card)
            status = "✅ 𝗪𝗼𝗿𝗸𝗶𝗻𝗴" if 'charge' in response.lower() else f"⚠️ 𝗥𝗲𝘀𝗽𝗼𝗻𝘀𝗲: {response}"
        else:
            status = "❌ 𝗗𝗶𝘀𝗮𝗯𝗹𝗲𝗱"
        results.append(f"<b>Braintree Single:</b> {status}")
    except Exception as e:
        results.append(f"<b>Braintree Single:</b> ❌ 𝗗𝗲𝗮𝗱/𝗘𝗿𝗿𝗼𝗿 - {str(e)}")

    # Check Stripe Single
    try:
        if gate_status['str']:
            _ , response, _ , num, _ = process_card(test_card)
            status = "✅ 𝗪𝗼𝗿𝗸𝗶𝗻𝗴" if 'charged' in response.lower() else f"⚠️ 𝗥𝗲𝘀𝗽𝗼𝗻𝘀𝗲: {response}"
        else:
            status = "❌ 𝗗𝗶𝘀𝗮𝗯𝗹𝗲𝗱"
        results.append(f"<b>Stripe Single:</b> {status}")
    except Exception as e:
        results.append(f"<b>Stripe Single:</b> ❌ 𝗗𝗲𝗮𝗱/𝗘𝗿𝗿𝗼𝗿 - {str(e)}")
        
    # Check PayPal Single
    try:
        if gate_status['pay']:
            _ , response, _ , num, _ = process_card_p(test_card)
            status = "✅ 𝗪𝗼𝗿𝗸𝗶𝗻𝗴" if 'passed' in response.lower() else f"⚠️ 𝗥𝗲𝘀𝗽𝗼𝗻𝘀𝗲: {response}"
        else:
            status = "❌ 𝗗𝗶𝘀𝗮𝗯𝗹𝗲𝗱"
        results.append(f"<b>PayPal Single:</b> {status}")
    except Exception as e:
        results.append(f"<b>PayPal Single:</b> ❌ 𝗗𝗲𝗮𝗱/𝗘𝗿𝗿𝗼𝗿 - {str(e)}")

    # Check PayPal $5 Single
    try:
        if gate_status['pay5']:
            _ , response = process_card_paypal5(test_card)
            status = "✅ 𝗪𝗼𝗿𝗸𝗶𝗻𝗴" if 'charge' in response.lower() else f"⚠️ 𝗥𝗲𝘀𝗽𝗼𝗻𝘀𝗲: {response}"
        else:
            status = "❌ 𝗗𝗶𝘀𝗮𝗯𝗹𝗲𝗱"
        results.append(f"<b>PayPal $5 Single:</b> {status}")
    except Exception as e:
        results.append(f"<b>PayPal $5 Single:</b> ❌ 𝗗𝗲𝗮𝗱/𝗘𝗿𝗿𝗼𝗿 - {str(e)}")
        
    # Check Shopify Single
    try:
        if gate_status['sh']:
            _ , response, ok = process_card_s(test_card, token=bot.token, ID=chat_id)
            status = "✅ 𝗪𝗼𝗿𝗸𝗶𝗻𝗴" if ok else f"⚠️ 𝗥𝗲𝘀𝗽𝗼𝗻𝘀𝗲: {response}"
        else:
            status = "❌ 𝗗𝗶𝘀𝗮𝗯𝗹𝗲𝗱"
        results.append(f"<b>Shopify Single:</b> {status}")
    except Exception as e:
        results.append(f"<b>Shopify Single:</b> ❌ 𝗗𝗲𝗮𝗱/𝗘𝗿𝗿𝗼𝗿 - {str(e)}")

    # Add more checks for file gates if needed...
    
    final_report = "<b>🚦 𝗚𝗮𝘁𝗲𝘀 𝗛𝗲𝗮𝗹𝘁𝗵 𝗖𝗵𝗲𝗰𝗸 𝗥𝗲𝗽𝗼𝗿𝘁 🚦</b>\n"
    final_report += "--------------------------------------\n"
    final_report += "\n".join(results)
    
    bot.edit_message_text(final_report, chat_id=chat_id, message_id=initial_message.message_id, parse_mode="HTML")


# تأكد من استيراد الدالتين ali1 و ali2 في بداية ملف bot.py من ملف الشيكر الخاص بهما
# from braintree_dual_checker import ali1, ali2 
# وتأكد من أن ملف braintree_dual_checker.py يحتوي على الدوال مُعدلة لترجع 3 قيم (is_live, response, proxy_info).

# تأكد من استيراد الدالتين ali1 و ali2 في بداية ملف bot.py:
# from braintree_dual_checker import ali1, ali2 
# وتأكد من استيراد دالة bin_info:
# from bin_info_v1 import bin_info 
# (أو من أي ملف تستخدمه للبحث عن BIN)

@bot.message_handler(commands=['chk3'])
@check_if_banned
@check_maintenance
@check_cooldown
def braintree_single_checker_command(message):
    if not gate_status.get('chk3', True): 
        bot.reply_to(message, "❗️ 𝘁𝗵𝗶𝘀 𝗴𝗮𝘁𝗲𝘄𝗮𝘆 𝗶𝘀 𝗰𝘂𝗿𝗿𝗲𝗻𝘁𝗹𝘆 𝗱𝗶𝘀𝗮𝗯𝗹𝗲𝗱.")
        return

    chat_id = message.chat.id
    
    try:
        start_time = time.time()
        card_details = message.text.split(' ', 1)[1]
        
        initial_message = bot.reply_to(message, "⏳ 𝗖𝗵𝗲𝗰𝗸𝗶𝗻𝗴 𝗰𝗮𝗿𝗱 𝗼𝗻 𝗕𝗿𝗮𝗶𝗻𝘁𝗿𝗲𝗲... 𝗽𝗹𝗲𝗮𝘀𝗲 𝘄𝗮𝗶𝘁.")
        
        # تشغيل ali1 فقط
        is_live_1, response_1, proxy_status_1 = ali1(card_details)
        
        end_time = time.time()
        
        # الرد النهائي
        final_live_status = is_live_1
        final_response = response_1
        main_proxy_info = proxy_status_1

        status_text = "Approved ✅" if final_live_status else "Declined ❌"
        
        # معلومات BIN
        card_number = card_details.split('|')[0]
        bin_number = card_number[:6]
        bin_data = bin_info(bin_number) 
        
        elapsed_time = round(end_time - start_time, 2)
        
        # حالة البروكسي (دائمًا "No Proxy Used")
        proxy_display = "Live ☁️"
        if "No Proxy Used" in main_proxy_info or "DECLINED" in final_response:
             proxy_display = "Declined ❌"
        
        # التقرير النهائي
        final_report = f"""
Brantree Auth Check

𝗖𝗖 : <code>{card_details}</code>
𝗦𝘁𝗮𝘁𝘂𝘀 : {status_text}
𝗥𝗲𝘀𝗽𝗼𝗻𝘀𝗲 : {final_response}
𝗚𝗮𝘁𝗲 : Brantree Auth

{bin_data}

𝗧/𝘁 : {elapsed_time}s | Proxy : {proxy_display}
"""

        
        bot.edit_message_text(chat_id=chat_id, message_id=initial_message.message_id, text=final_report, parse_mode="HTML")
        
    except IndexError:
        bot.reply_to(message, "⚠️ Correct usage: `/chk3 [card|mm|yy|cvc]`", parse_mode="Markdown")
    except Exception as e:
        bot.send_message(chat_id=chat_id, text=f"𝗮𝗻 𝗲𝗿𝗿𝗼𝗿 𝗼𝗰𝗰𝘂𝗿𝗿𝗲𝗱 𝗱𝘂𝗿𝗶𝗻𝗴 𝗰𝗵𝗲𝗰𝗸: {e}")


# =====================================================================

@bot.message_handler(commands=['filechk3'])
@check_if_banned
@check_maintenance
def braintree_file_checker(message):
    is_subscribed, _ = check_subscription(message.from_user.id)
    if not is_subscribed:
        bot.reply_to(message, "❌ 𝘆𝗼𝘂 𝗺𝘂𝘀𝘁 𝗵𝗮𝘃𝗲 𝗮 𝘀𝘂𝗯𝘀𝗰𝗿𝗶𝗽𝘁𝗶𝗼𝗻 𝘁𝗼 𝘂𝘀𝗲 𝘁𝗵𝗶𝘀 𝗰𝗼𝗺𝗺𝗮𝗻𝗱.", reply_markup=create_buy_keyboard())
        return

    if not gate_status.get('chk3', True):
        bot.reply_to(message, "❗️ 𝘁𝗵𝗶𝘀 𝗴𝗮𝘁𝗲𝘄𝗮𝘆 𝗶𝘀 𝗰𝘂𝗿𝗿𝗲𝗻𝘁𝗹𝘆 𝗱𝗶𝘀𝗮𝗯𝗹𝗲𝗱.")
        return

    user_id = message.from_user.id
    active_tasks[user_id] = {"should_stop": False}

    bot.reply_to(message, "📂 𝗦𝗲𝗻𝗱 𝗺𝗲 𝘆𝗼𝘂𝗿 𝗰𝗼𝗺𝗯𝗼 𝗳𝗶𝗹𝗲 (.txt) 𝗳𝗼𝗿 𝗕𝗿𝗮𝗶𝗻𝘁𝗿𝗲𝗲 𝗖𝗵𝗲𝗰𝗸.")
    bot.register_next_step_handler(message, handle_braintree_file_upload_venom)


# ====== BLACK KNOWLEDGE ======
def create_braintree_progress_keyboard(stats):
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.row(types.InlineKeyboardButton(text=f"💳 {stats['CURRENT_CARD']}", callback_data="ignore"))
    markup.row(types.InlineKeyboardButton(text=f"⚡ 𝗚𝗮𝘁𝗲: 𝗕𝗿𝗮𝗶𝗻𝘁𝗿𝗲𝗲 | 🧠 {stats['LAST_RESPONSE']}", callback_data="ignore"))
    markup.row(
        types.InlineKeyboardButton(text=f"✅ 𝗟𝗶𝘃𝗲: {stats.get('APV',0)}", callback_data="ignore"),
        types.InlineKeyboardButton(text=f"⚡ 𝗖𝗵𝗮𝗿𝗴𝗲𝗱: {stats.get('CHARGE',0)}", callback_data="ignore")
    )
    markup.row(
        types.InlineKeyboardButton(text=f"💰 𝗜𝗻𝘀𝘂𝗳𝗳 𝗙𝘂𝗻𝗱𝘀: {stats.get('CCN',0)}", callback_data="ignore"),
        types.InlineKeyboardButton(text=f"❌ 𝗗𝗲𝗰𝗹𝗶𝗻𝗲𝗱: {stats.get('DECLINED',0)}", callback_data="ignore")
    )
    markup.row(types.InlineKeyboardButton(text=f"📊 𝗖𝗵𝗲𝗰𝗸𝗲𝗱: {stats.get('CHECKED',0)}/{stats.get('TOTAL',0)}", callback_data="ignore"))
    markup.row(types.InlineKeyboardButton(text="〄 𝙎𝙩𝙤𝙥 𝙑𝙀𝙉𝙊𝙈 〄", callback_data="stop_chk3"))
    return markup


@bot.callback_query_handler(func=lambda call: call.data == "stop_chk3")
def stop_chk3_callback(call):
    user_id = call.from_user.id
    if user_id in active_tasks:
        active_tasks[user_id]["should_stop"] = True
        bot.answer_callback_query(call.id, "🛑 𝗦𝘁𝗼𝗽𝗽𝗶𝗻𝗴 𝗕𝗿𝗮𝗶𝗻𝘁𝗿𝗲𝗲 𝗖𝗵𝗲𝗰𝗸...")
    else:
        bot.answer_callback_query(call.id, "No active check running.")


# ====== معالجة رفع الملف + الفحص ======
def handle_braintree_file_upload_venom(message):
    if not message.document or message.document.mime_type != "text/plain":
        bot.reply_to(message, "❌ 𝗣𝗹𝗲𝗮𝘀𝗲 𝘀𝗲𝗻𝗱 𝗮 𝘃𝗮𝗹𝗶𝗱 .txt 𝗰𝗼𝗺𝗯𝗼 𝗳𝗶𝗹𝗲.")
        return

    user_id = message.from_user.id
    file_info = bot.get_file(message.document.file_id)
    downloaded_file = bot.download_file(file_info.file_path)

    temp_combo_path = f"Temps/{user_id}_combo.txt"
    with open(temp_combo_path, "wb") as f:
        f.write(downloaded_file)

    try:
        with open(temp_combo_path, "r", encoding="utf-8") as f:
            card_lines = [line.strip() for line in f if line.strip() and len(line.split('|')) >= 4]
    except Exception as e:
        bot.reply_to(message, f"❌ 𝗘𝗿𝗿𝗼𝗿 𝗿𝗲𝗮𝗱𝗶𝗻𝗴 𝗳𝗶𝗹𝗲: {e}")
        os.remove(temp_combo_path)
        return

    total_cards = len(card_lines)
    if total_cards == 0:
        bot.reply_to(message, "⚠️ 𝗙𝗶𝗹𝗲 𝗶𝘀 𝗲𝗺𝗽𝘁𝘆 𝗼𝗿 𝗶𝗻𝘃𝗮𝗹𝗶𝗱 𝗳𝗼𝗿𝗺𝗮𝘁.")
        os.remove(temp_combo_path)
        return

    stats = {
        "APV": 0, "CHARGE": 0, "CCN": 0, "DECLINED": 0,
        "TOTAL": total_cards, "CHECKED": 0,
        "CURRENT_CARD": "N/A", "LAST_RESPONSE": "Starting..."
    }

    status_msg = bot.send_message(
        message.chat.id,
        "🔍 𝗦𝘁𝗮𝗿𝘁𝗶𝗻𝗴 𝗕𝗿𝗮𝗶𝗻𝘁𝗿𝗲𝗲 𝗖𝗵𝗲𝗰𝗸...",
        reply_markup=create_braintree_progress_keyboard(stats)
    )

    start_time = time.time()
    successful_results = []

    for card in card_lines:
        if active_tasks.get(user_id, {}).get("should_stop"):
            break

        stats["CHECKED"] += 1
        stats["CURRENT_CARD"] = card

        try:
            is_live, response, proxy_status = ali1(card)
            stats["LAST_RESPONSE"] = response if response else "No response"

            if is_live:
                if "APPROVED" in response:
                    stats["APV"] += 1
                elif "CHARGE" in response:
                    stats["CHARGE"] += 1
                elif "CCN" in response:
                    stats["CCN"] += 1
                else:
                    stats["APV"] += 1

                card_number = card.split('|')[0]
                bin_data = bin_info(card_number[:6])

                full_result_message = f"""
𝗕𝗿𝗮𝗶𝗻𝘁𝗿𝗲𝗲 𝗖𝗵𝗲𝗰𝗸

𝗖𝗖 : <code>{card}</code>
𝗦𝘁𝗮𝘁𝘂𝘀 : ✅ Approved
𝗥𝗲𝘀𝗽𝗼𝗻𝘀𝗲 : {response}
𝗚𝗮𝘁𝗲 : Braintree Auth

{bin_data}

🕒 𝗧/𝘁 : {round(time.time() - start_time, 2)}s | Proxy : live ✅
"""
                successful_results.append(full_result_message)
                bot.send_message(message.chat.id, full_result_message, parse_mode="HTML")

            else:
                stats["DECLINED"] += 1
                stats["LAST_RESPONSE"] = response or "Declined ❌"

        except Exception as e:
            stats["DECLINED"] += 1
            stats["LAST_RESPONSE"] = str(e)

        # تحديث العدادات
        try:
            bot.edit_message_reply_markup(
                chat_id=message.chat.id,
                message_id=status_msg.message_id,
                reply_markup=create_braintree_progress_keyboard(stats)
            )
        except Exception:
            pass

        time.sleep(1)

    if user_id in active_tasks:
        del active_tasks[user_id]
    os.remove(temp_combo_path)

    elapsed = round(time.time() - start_time, 2)

    # إرسال الملخص النهائي BLACK KNOWLEDGE STYLE
    try:
        bot.edit_message_text(
            f"✅ 𝗙𝗶𝗻𝗶𝘀𝗵𝗲𝗱!\n📊 𝗖𝗵𝗲𝗰𝗸𝗲𝗱: {stats['CHECKED']}/{stats['TOTAL']}\n✅ 𝗟𝗶𝘃𝗲: {stats['APV']}\n⚡ 𝗖𝗵𝗮𝗿𝗴𝗲𝗱: {stats['CHARGE']}\n❌ 𝗗𝗲𝗰𝗹𝗶𝗻𝗲𝗱: {stats['DECLINED']}\n\n🕒 𝗧𝗶𝗺𝗲: {elapsed}s",
            chat_id=message.chat.id,
            message_id=status_msg.message_id,
            reply_markup=None,
            parse_mode="HTML"
        )
    except Exception:
        pass

    # إرسال ملف النتائج LIVE (لو وجد)
    if successful_results:
        final_file = f"Temps/{user_id}_Braintree_LIVE.txt"
        with open(final_file, "w", encoding="utf-8") as f:
            f.write("\n\n".join(successful_results))

        with open(final_file, "rb") as f:
            bot.send_document(message.chat.id, f, caption=f"✅ 𝗟𝗜𝗩𝗘 𝗥𝗲𝘀𝘂𝗹𝘁𝘀: {len(successful_results)}")

        os.remove(final_file)



import random
from datetime import date

# ========== الدالة ==========
def generate_paypal_info():
    first_names_male = ["Juan","Jose","Pedro","Mark","Michael","Antonio","Roberto","Francisco","Ricardo","Diego","Daniel"]
    first_names_female = ["Maria","Ana","Cristina","Angelica","Rosa","Luisa","Carmen","Sofia","Andrea","Beatriz","Clara"]
    middle_names = ["Santos","Reyes","Cruz","Bautista","Garcia","Lopez","Aquino","Torres","Flores","Morales","Gonzales"]
    last_names = ["Dela Cruz","Villanueva","Ramos","Fernandez","Domingo","Castillo","Mendoza","Navarro","Gutierrez","Alvarez"]
    cities = ["Manila","Quezon City","Davao City","Cebu City","Pasig","Taguig","Makati","Baguio","Iloilo"]
    provinces = ["Metro Manila","Cebu","Davao del Sur","Laguna","Pampanga","Bulacan","Batangas"]
    streets = ["Rizal Street","Bonifacio Avenue","Mabini St.","Katipunan Road","Roxas Blvd","Quezon Avenue"]
    email_domains = ["gmail.com","yahoo.com","outlook.com","hotmail.com","icloud.com","protonmail.com","gov.ph","up.edu.ph"]

    gender = random.choice(["Male", "Female"])
    nationality = "Filipino 🇵🇭"

    first = random.choice(first_names_male if gender == "Male" else first_names_female)
    middle = random.choice(middle_names)
    last = random.choice(last_names)
    full_name = f"{first} {middle} {last}"

    email_domain = random.choice(email_domains)
    email_user = f"{first.lower()}.{middle.lower()}.{last.replace(' ', '').lower()}{random.randint(10,99)}"
    email = f"{email_user}@{email_domain}"

    phone = f"+63 9{random.randint(10,99)}-{random.randint(100,999)}-{random.randint(1000,9999)}"
    passport_number = "E" + str(random.randint(1000000, 9999999))

    birth_year = random.randint(1975, 2005)
    birth_month = random.randint(1, 12)
    birth_day = random.randint(1, 28)
    birth_date = date(birth_year, birth_month, birth_day)
    today = date.today()
    age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))

    street = random.choice(streets) + f" No. {random.randint(10,999)}"
    postal = str(random.randint(1000, 9999))
    city = random.choice(cities)
    province = random.choice(provinces)
    barangay = f"{random.randint(1000, 9999)}00"

    return f"""
🌸 <b>𝗣𝗮𝘆𝗽𝗮𝗹 𝗜𝗻𝗳𝗼𝗿𝗺𝗮𝘁𝗶𝗼𝗻</b> 🌸

👤 <b>𝗡𝗮𝗺𝗲:</b> {full_name}
⚥ <b>𝗚𝗲𝗻𝗱𝗲𝗿:</b> {gender}
🌐 <b>𝗡𝗮𝘁𝗶𝗼𝗻𝗮𝗹𝗶𝘁𝘆:</b> {nationality}
📧 <b>𝗘𝗺𝗮𝗶𝗹:</b> {email}
📞 <b>𝗣𝗵𝗼𝗻𝗲:</b> {phone}
🏠 <b>𝗔𝗱𝗱𝗿𝗲𝘀𝘀:</b> {street}, {city}, {province}, {postal}
🆔 <b>𝗣𝗮𝘀𝘀𝗽𝗼𝗿𝘁:</b> {passport_number}
🏘 <b>𝗕𝗮𝗿𝗮𝗻𝗴𝗮𝘆 𝗗𝗶𝘀𝘁𝗿𝗶𝗰𝘁:</b> {barangay}
🎂 <b>𝗗𝗢𝗕:</b> {birth_date.strftime("%d-%m-%Y")} ({age} yrs)

👨‍💻 <b>𝗗𝗲𝘃:</b> <a href="https://t.me/dev_gax">@dev_gax</a>
"""

# ========== الأمر /if ==========
@bot.message_handler(commands=["if"])
def if_command(message):
    text = generate_paypal_info()
    bot.send_message(message.chat.id, text, parse_mode="HTML")


# --- NEW Admin Commands: Ban, Unban, Dashboard ---
@bot.message_handler(commands=['dashboard'])
def dashboard(message):
    if message.from_user.id != admin_id:
        return
        
    try:
        with open('free.json', 'r') as f:
            total_users = len(json.load(f))
    except (FileNotFoundError, json.JSONDecodeError):
        total_users = 0

    try:
        with open('data.json', 'r') as f:
            subscribed_users = len([k for k in json.load(f) if k.isdigit()])
    except (FileNotFoundError, json.JSONDecodeError):
        subscribed_users = 0

    bot_status_text = "𝗢𝗻𝗹𝗶𝗻𝗲 ✅" if bot_working else "𝗠𝗮𝗶𝗻𝘁𝗲𝗻𝗮𝗻𝗰𝗲 ⚠️"
    
    gates_status_text = ""
    for gate, status in gate_status.items():
        gates_status_text += f"    - `{gate}`: {'𝗘𝗻𝗮𝗯𝗹𝗲𝗱 ✅' if status else '𝗗𝗶𝘀𝗮𝗯𝗹𝗲𝗱 ❌'}\n"

    dashboard_text = f"""
📊 **𝗕𝗼𝘁 𝗗𝗮𝘀𝗵𝗯𝗼𝗮𝗿𝗱**

👥 **𝗧𝗼𝘁𝗮𝗹 𝗨𝘀𝗲𝗿𝘀:** `{total_users}`
⭐ **𝗔𝗰𝘁𝗶𝘃𝗲 𝗦𝘂𝗯𝘀𝗰𝗿𝗶𝗯𝗲𝗿𝘀:** `{subscribed_users}`

⚙️ **𝗕𝗼𝘁 𝗦𝘁𝗮𝘁𝘂𝘀:** {bot_status_text}

🕹️ **𝗚𝗮𝘁𝗲𝘄𝗮𝘆𝘀 𝗦𝘁𝗮𝘁𝘂𝘀:**
{gates_status_text}
"""
    bot.reply_to(message, dashboard_text, parse_mode="Markdown")

@bot.message_handler(commands=['ban', 'unban'])
def ban_unban_user(message):
    if message.from_user.id != admin_id:
        return
    try:
        command, user_id_str = message.text.split(maxsplit=1)
        user_to_modify = int(user_id_str)

        with open('banned_users.json', 'r+') as f:
            banned_list = json.load(f)

            if command == '/ban':
                if user_to_modify not in banned_list:
                    banned_list.append(user_to_modify)
                    reply_text = f"✅ 𝗨𝘀𝗲𝗿 `{user_to_modify}` 𝗵𝗮𝘀 𝗯𝗲𝗲𝗻 𝗯𝗮𝗻𝗻𝗲𝗱 𝘀𝘂𝗰𝗰𝗲𝘀𝘀𝗳𝘂𝗹ly."
                else:
                    reply_text = "⚠️ 𝗧𝗵𝗶𝘀 𝘂𝘀𝗲𝗿 𝗶𝘀 𝗮𝗹𝗿𝗲𝗮𝗱𝘆 𝗯𝗮𝗻𝗻𝗲𝗱."
            
            elif command == '/unban':
                if user_to_modify in banned_list:
                    banned_list.remove(user_to_modify)
                    reply_text = f"✅ 𝗨𝘀𝗲𝗿 `{user_to_modify}` 𝗵𝗮𝘀 𝗯𝗲𝗲𝗻 𝘂𝗻𝗯𝗮𝗻𝗻𝗲𝗱 𝘀𝘂𝗰𝗰𝗲𝘀𝘀𝗳𝘂𝗹ly."
                else:
                    reply_text = "⚠️ 𝗧𝗵𝗶𝘀 𝘂𝘀𝗲𝗿 𝗶𝘀 𝗻𝗼𝘁 𝗯𝗮𝗻𝗻𝗲𝗱."

            f.seek(0)
            f.truncate()
            json.dump(banned_list, f, indent=4)
            bot.reply_to(message, reply_text, parse_mode="Markdown")

    except (IndexError, ValueError):
        command_name = message.text.split()[0]
        bot.reply_to(message, f"𝗪𝗿𝗼𝗻𝗴 𝗳𝗼𝗿𝗺𝗮𝘁. 𝗨𝘀𝗮𝗴𝗲: `{command_name} <user_id>`", parse_mode="Markdown")




# ——————————— NEW All-in-One Checker Command ——————————— #
@bot.message_handler(commands=['ckall'])
@check_if_banned
@check_maintenance
@check_cooldown
def all_in_one_checker(message):
    is_subscribed, _ = check_subscription(message.from_user.id)
    if not is_subscribed:
        bot.reply_to(message, "This command is for subscribers only. 𝘆𝗼𝘂 𝗺𝘂𝘀𝘁 𝗵𝗮𝘃𝗲 𝗮𝗻 𝗮𝗰𝘁𝗶𝘃𝗲 𝘀𝘂𝗯𝘀𝗰𝗿𝗶𝗽𝘁𝗶𝗼𝗻.", reply_markup=create_buy_keyboard())
        return

    try:
        card_details = message.text.split(' ', 1)[1]
    except IndexError:
        bot.reply_to(message, "⚠️ Correct usage: `/checkall [card]`", parse_mode="Markdown")
        return

    initial_message = bot.reply_to(message, f"⏳ 𝗖𝗵𝗲𝗰𝗸𝗶𝗻𝗴 𝗰𝗮𝗿𝗱 <code>{card_details}</code> 𝗼𝗻 𝗮𝗹𝗹 𝗴𝗮𝘁𝗲𝘄𝗮𝘆𝘀... 𝗽𝗹𝗲𝗮𝘀𝗲 𝘄𝗮𝗶𝘁.")

    results = []

    # --- 1. Stripe Gateway ---
    if gate_status['str']:
        try:
            stripe_result = process_card(card_details)
            results.append(f"<b>- 𝗦𝘁𝗿𝗶𝗽𝗲 𝗚𝗮𝘁𝗲𝘄𝗮𝘆:</b> {stripe_result[1]}")
        except Exception as e:
            results.append(f"<b>- 𝗦𝘁𝗿𝗶𝗽𝗲 𝗚𝗮𝘁𝗲𝘄𝗮𝘆:</b> ⚠️ 𝗘𝗿𝗿𝗼𝗿: {e}")
    
    # --- 2. Braintree Gateway (Premium) ---
    if gate_status['chk']:
        try:
            braintree_result = process_card_b(card_details)
            results.append(f"<b>- 𝗕𝗿𝗮𝗶𝗻𝘁𝗿𝗲𝗲 𝗚𝗮𝘁𝗲𝘄𝗮𝘆:</b> {braintree_result[1]}")
        except Exception as e:
            results.append(f"<b>- 𝗕𝗿𝗮𝗶𝗻𝘁𝗿𝗲𝗲 𝗚𝗮𝘁𝗲𝘄𝗮𝘆:</b> ⚠️ 𝗘𝗿𝗿𝗼𝗿: {e}")

    # --- 3. Shopify Gateway ---
    if gate_status['sh']:
        try:
            cc, shopify_res, ok = process_card_s(card_details, token=bot.token, ID=message.chat.id)
            status_emoji = "✅" if ok else "❌"
            results.append(f"<b>- 𝗦𝗵𝗼𝗽𝗶𝗳𝘆 𝗚𝗮𝘁𝗲𝘄𝗮𝘆:</b> {status_emoji} {shopify_res}")
        except Exception as e:
            results.append(f"<b>- 𝗦𝗵𝗼𝗽𝗶𝗳𝘆 𝗚𝗮𝘁𝗲𝘄𝗮𝘆:</b> ⚠️ 𝗘𝗿𝗿𝗼𝗿: {e}")

    # --- 4. PayPal Gateway (Premium) ---
    if gate_status['pay']:
        try:
            paypal_result = process_card_p(card_details)
            results.append(f"<b>- 𝗣𝗮𝘆𝗣𝗮𝗹 𝗚𝗮𝘁𝗲𝘄𝗮𝘆:</b> {paypal_result[1]}")
        except Exception as e:
            results.append(f"<b>- 𝗣𝗮𝘆𝗣𝗮𝗹 𝗚𝗮𝘁𝗲𝘄𝗮𝘆:</b> ⚠️ 𝗘𝗿𝗿𝗼𝗿: {e}")
        
    final_report = f"<b>-- ✅ 𝗙𝘂𝗹𝗹 𝗖𝗵𝗲𝗰𝗸 𝗥𝗲𝗽𝗼𝗿𝘁 --</b>\n"
    final_report += f"<b>𝗖𝗮𝗿𝗱:</b> <code>{card_details}</code>\n"
    final_report += "--------------------------------------\n"
    final_report += "\n".join(results)

    bot.edit_message_text(final_report, chat_id=message.chat.id, message_id=initial_message.message_id, parse_mode="HTML")


# ——————————— Stars Payment System ——————————— #
@bot.callback_query_handler(func=lambda call: call.data == 'Buy')
def buy_callback(call):
    try:
        bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
    except Exception as e:
        print(f"Could not delete message: {e}")

    markup = types.InlineKeyboardMarkup(row_width=1)
    gate_btn = types.InlineKeyboardButton("𝟮 𝗵𝗼𝘂𝗿𝘀 » 20 ⭐", callback_data="buy_2hour")
    lock_btn = types.InlineKeyboardButton("𝟭 𝗱𝗮𝘆 » 75 ⭐", callback_data="buy_1day")
    unlock_btn = types.InlineKeyboardButton("𝟭 𝘄𝗲𝗲𝗸 » 275 ⭐", callback_data="buy_1week")
    back_btn = types.InlineKeyboardButton("𝗯𝗮𝗰𝗸", callback_data="back")
    markup.add(gate_btn, lock_btn, unlock_btn, back_btn)
    
    msg = '''-
𝗰𝗵𝗼𝗼𝘀𝗲 𝗮 𝘀𝘂𝗶𝘁𝗮𝗯𝗹𝗲 𝘀𝘂𝗯𝘀𝗰𝗿𝗶𝗽𝘁𝗶𝗼𝗻 𝗽𝗹𝗮𝗻.

<a href='tg://user?id=1677950104'>𝗼𝘄𝗻𝗲𝗿</a>'''

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
        provider_token="",
        currency="XTR",
        prices=prices,
        start_parameter="pay_with_stars",
        invoice_payload=f"Star-{hours}h",
    )

@bot.callback_query_handler(func=lambda call: call.data == 'buy_2hour')
def process_hour(call):
    send_star_invoice(call, 2, 20, "𝘀𝘂𝗯𝘀𝗰𝗿𝗶𝗽𝘁𝗶𝗼𝗻 𝟮 𝗵𝗼𝘂𝗿𝘀")

@bot.callback_query_handler(func=lambda call: call.data == 'buy_1day')
def process_day(call):
    send_star_invoice(call, 24, 75, "𝘀𝘂𝗯𝘀𝗰𝗿𝗶𝗽𝘁𝗶𝗼𝗻 𝟭 𝗱𝗮𝘆")

@bot.callback_query_handler(func=lambda call: call.data == 'buy_1week')
def process_week(call):
    send_star_invoice(call, 168, 275, "𝘀𝘂𝗯𝘀𝗰𝗿𝗶𝗽𝘁𝗶𝗼𝗻 𝟭 𝘄𝗲𝗲𝗸")

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
✅ 𝗽𝗮𝘆𝗺𝗲𝗻𝘁 𝗱𝗼𝗻𝗲 𝘀𝘂𝗰𝗰𝗲𝘀𝘀𝗳𝘂𝗹ly

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
@check_if_banned
@check_maintenance
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

            msg = f'''<b>✅ 𝗸𝗲𝘆 𝗿𝗲𝗱𝗲𝗲𝗺𝗲𝗱 𝘀𝘂𝗰𝗰𝗲𝘀𝘀𝗳𝘂𝗹ly!
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
    
# --- NEW User Commands for Credits/Referral ---
@bot.message_handler(commands=['credits'])
@check_if_banned
@check_maintenance
def referral(message):
    user_id = message.from_user.id
    
    with open('credits.json', 'r') as f:
        credits_data = json.load(f)
    
    user_credits = credits_data.get(str(user_id), {}).get("credits", 0)

    ref_link = f"https://t.me/{BOT_USERNAME}?start=ref_{user_id}"
    
    reply_text = f"""
🔗 **𝗬𝗼𝘂𝗿 𝗥𝗲𝗳𝗲𝗿𝗿𝗮𝗹 𝗦𝘆𝘀𝘁𝗲𝗺**

𝗜𝗻𝘃𝗶𝘁𝗲 𝘆𝗼𝘂𝗿 𝗳𝗿𝗶𝗲𝗻𝗱𝘀 𝘁𝗼 𝗷𝗼𝗶𝗻 𝘁𝗵𝗲 𝗯𝗼𝘁 𝘂𝘀𝗶𝗻𝗴 𝘁𝗵𝗲 𝗹𝗶𝗻𝗸 𝗯𝗲𝗹𝗼𝘄, 𝗮𝗻𝗱 𝗴𝗲𝘁 **10 𝗰𝗿𝗲𝗱𝗶𝘁𝘀** 𝗳𝗼𝗿 𝗲𝗮𝗰𝗵 𝗻𝗲𝘄 𝘂𝘀𝗲𝗿 𝘄𝗵𝗼 𝗷𝗼𝗶𝗻𝘀 𝘁𝗵𝗿𝗼𝘂𝗴𝗵 𝘆𝗼𝘂!

**𝗬𝗼𝘂𝗿 𝗿𝗲𝗳𝗲𝗿𝗿𝗮𝗹 𝗹𝗶𝗻𝗸:**
`{ref_link}`

🪙 **𝗬𝗼𝘂𝗿 𝗰𝘂𝗿𝗿𝗲𝗻𝘁 𝗯𝗮𝗹𝗮𝗻𝗰𝗲:** {user_credits} 𝗰𝗿𝗲𝗱𝗶𝘁𝘀.

𝗨𝘀𝗲 𝘆𝗼𝘂𝗿 𝗰𝗿𝗲𝗱𝗶𝘁𝘀 𝘁𝗼 𝗴𝗲𝘁 𝗮 𝗳𝗿𝗲𝗲 𝘀𝘂𝗯𝘀𝗰𝗿𝗶𝗽𝘁𝗶𝗼𝗻 𝘂𝘀𝗶𝗻𝗴 𝘁𝗵𝗲 𝗰𝗼𝗺𝗺𝗮𝗻𝗱:
`/redeem_credits <hours>`
(𝟱 𝗰𝗿𝗲𝗱𝗶𝘁𝘀 = 𝟭 𝗵𝗼𝘂𝗿 𝗼𝗳 𝘀𝘂𝗯𝘀𝗰𝗿𝗶𝗽𝘁𝗶𝗼𝗻)
"""
    bot.reply_to(message, reply_text, parse_mode="Markdown")

@bot.message_handler(commands=['redeem_credits'])
@check_if_banned
@check_maintenance
def redeem_credits(message):
    user_id = str(message.from_user.id)
    try:
        hours_to_redeem = int(message.text.split()[1])
        if hours_to_redeem <= 0:
            raise ValueError
        
        cost = hours_to_redeem * 5 # 5 credits per hour
        
        with open('credits.json', 'r+') as f:
            credits_data = json.load(f)
            user_credits = credits_data.get(user_id, {}).get("credits", 0)

            if user_credits >= cost:
                # Deduct credits
                credits_data[user_id]["credits"] -= cost
                
                # Grant subscription
                with open('data.json', 'r+') as data_f:
                    subscription_data = json.load(data_f)
                    expiry_time = datetime.now() + timedelta(hours=hours_to_redeem)
                    expiry_time_str = expiry_time.strftime('%Y-%m-%d %H:%M')
                    subscription_data[user_id] = {'timer': expiry_time_str, 'plan': 'credits_vip'}
                    
                    data_f.seek(0)
                    json.dump(subscription_data, data_f, indent=4)
                
                f.seek(0)
                json.dump(credits_data, f, indent=4)
                
                bot.reply_to(message, f"✅ 𝗦𝘂𝗰𝗰𝗲𝘀𝘀! 𝗬𝗼𝘂 𝗵𝗮𝘃𝗲 𝗿𝗲𝗱𝗲𝗲𝗺𝗲𝗱 `{cost}` 𝗰𝗿𝗲𝗱𝗶𝘁𝘀 𝗳𝗼𝗿 𝗮 `{hours_to_redeem}`-𝗵𝗼𝘂𝗿 𝘀𝘂𝗯𝘀𝗰𝗿𝗶𝗽𝘁𝗶𝗼𝗻.\n𝗬𝗼𝘂𝗿 𝘀𝘂𝗯𝘀𝗰𝗿𝗶𝗽𝘁𝗶𝗼𝗻 𝗲𝘅𝗽𝗶𝗿𝗲𝘀 𝗼𝗻: `{expiry_time_str}`", parse_mode="Markdown")
            else:
                bot.reply_to(message, f"❌ 𝗜𝗻𝘀𝘂𝗳𝗳𝗶𝗰𝗶𝗲𝗻𝘁 𝗰𝗿𝗲𝗱𝗶𝘁𝘀. 𝗬𝗼𝘂𝗿 𝗯𝗮𝗹𝗮𝗻𝗰𝗲 𝗶𝘀 `{user_credits}` 𝗰𝗿𝗲𝗱𝗶𝘁𝘀 𝗮𝗻𝗱 𝘆𝗼𝘂 𝗻𝗲𝗲𝗱 `{cost}`.", parse_mode="Markdown")

    except (IndexError, ValueError):
        bot.reply_to(message, "𝗪𝗿𝗼𝗻𝗴 𝗳𝗼𝗿𝗺𝗮𝘁. 𝗨𝘀𝗮𝗴𝗲: `/redeem_credits <hours>`\n𝗘𝘅𝗮𝗺𝗽𝗹𝗲: `/redeem_credits 24`", parse_mode="Markdown")


# ——————————— User Commands (Free) ——————————— #
@bot.message_handler(commands=['cmds', 'help'])
@check_if_banned
@check_maintenance
def me_command(message):
    is_admin = message.from_user.id == admin_id
    
    # User Commands Section
    commands_list = """
<b>𝗯𝗼𝘁 𝗰𝗼𝗺𝗺𝗮𝗻𝗱 𝗹𝗶𝘀𝘁</b>

<b>-- 𝗴𝗲𝗻𝗲𝗿𝗮𝗹 --</b>
<code>/start</code> - 𝘀𝘁𝗮𝗿𝘁 𝘁𝗵𝗲 𝗯𝗼𝘁
<code>/profile</code> - 𝘃𝗶𝗲𝘄 𝘆𝗼𝘂𝗿 𝗽𝗿𝗼𝗳𝗶𝗹𝗲
<code>/redeem_credits</code> - 𝗴𝗲𝘁 𝘀𝘂𝗯𝘀𝗰𝗿𝗶𝗽𝘁𝗶𝗼𝗻 𝘄𝗶𝘁𝗵 𝗰𝗿𝗲𝗱𝗶𝘁𝘀
<code>/redeem</code> - 𝗿𝗲𝗱𝗲𝗲𝗺 𝗮 𝘀𝘂𝗯𝘀𝗰𝗿𝗶𝗽𝘁𝗶𝗼𝗻 𝗸𝗲𝘆

<b>-- 𝗰𝗮𝗿𝗱 𝗰𝗵𝗲𝗰𝗸𝗲𝗿𝘀 --</b>
<code>/chk</code> - <code>𝗰𝗵𝗲𝗰𝗸 𝗰𝗮𝗿𝗱 (𝗯𝗿𝗮𝗶𝗻𝘁𝗿𝗲𝗲 - 𝗳𝗿𝗲𝗲)</code>
<code>/str</code> - <code>𝗰𝗵𝗲𝗰𝗸 𝗰𝗮𝗿𝗱 (𝘀𝘁𝗿𝗶𝗽𝗲 - 𝗳𝗿𝗲𝗲)</code>
<code>/pay</code> - <code>𝗰𝗵𝗲𝗰𝗸 𝗰𝗮𝗿𝗱 (𝗽𝗮𝘆𝗽𝗮𝗹 - 𝗳𝗿𝗲𝗲)</code>
<code>/pay5</code> - <code>𝗰𝗵𝗲𝗰𝗸 𝗰𝗮𝗿𝗱 (𝗽𝗮𝘆𝗽𝗮𝗹 𝟱$ - 𝗳𝗿𝗲𝗲)</code>
<code>/sh</code> - <code>𝗰𝗵𝗲𝗰𝗸 𝗰𝗮𝗿𝗱 (𝘀𝗵𝗼𝗽𝗶𝗳𝘆 - 𝗳𝗿𝗲𝗲)</code>
<code>/mass_chk</code> - <code>𝗰𝗵𝗲𝗰𝗸 𝟱 𝗰𝗮𝗿𝗱𝘀 𝘄𝗶𝘁𝗵 𝗯𝗿𝗮𝗶𝗻𝘁𝗿𝗲𝗲</code>
<code>/mass_str</code> - <code>𝗰𝗵𝗲𝗰𝗸 𝟱 𝗰𝗮𝗿𝗱𝘀 𝘄𝗶𝘁𝗵 𝘀𝘁𝗿𝗶𝗽𝗲</code>
<code>/mass_pay</code> - <code>𝗰𝗵𝗲𝗰𝗸 𝟱 𝗰𝗮𝗿𝗱𝘀 𝘄𝗶𝘁𝗵 𝗽𝗮𝘆𝗽𝗮𝗹</code>
<code>/mass_pay5</code> - <code>𝗰𝗵𝗲𝗰𝗸 𝟱 𝗰𝗮𝗿𝗱𝘀 𝘄𝗶𝘁𝗵 𝗣𝗮𝘆𝗣𝗮𝗹 𝟱$</code>
<code>/mass_sh</code> - <code>𝗰𝗵𝗲𝗰𝗸 𝟱 𝗰𝗮𝗿𝗱𝘀 𝘄𝗶𝘁𝗵 𝘀𝗵𝗼𝗽𝗶𝗳𝘆</code>
<code>/mass_chk3</code> - <code>𝗰𝗵𝗲𝗰𝗸 𝟱 𝗰𝗮𝗿𝗱𝘀 𝘄𝗶𝘁𝗵 𝗯𝗿𝗮𝗶𝗻𝘁𝗿𝗲𝗲 𝗱𝘂𝗮𝗹</code>
<code>/file</code> - <code>𝗰𝗵𝗲𝗰𝗸 𝗳𝗶𝗹𝗲 (𝗯𝗿𝗮𝗶𝗻𝘁𝗿𝗲𝗲 - 𝗽𝗿𝗲𝗺𝗶𝘂𝗺)</code>
<code>/filestr</code> - <code>𝗰𝗵𝗲𝗰𝗸 𝗳𝗶𝗹𝗲 (𝘀𝘁𝗿𝗶𝗽𝗲 - 𝗽𝗿𝗲𝗺𝗶𝘂𝗺)</code>
<code>/filep</code> - <code>𝗰𝗵𝗲𝗰𝗸 𝗰𝗼𝗺𝗯𝗼 𝗳𝗶𝗹𝗲 𝘄𝗶𝘁𝗵 𝗽𝗮𝘆𝗽𝗮𝗹 (𝗽𝗿𝗲𝗺𝗶𝘂𝗺)</code>
<code>/payf</code> - <code>𝗰𝗵𝗲𝗰𝗸 𝗰𝗼𝗺𝗯𝗼 𝗳𝗶𝗹𝗲 𝘄𝗶𝘁𝗵 𝗣𝗮𝘆𝗣𝗮𝗹 𝟱$ (𝗽𝗿𝗲𝗺𝗶𝘂𝗺)</code>
<code>/shf</code> - <code>𝗰𝗵𝗲𝗰𝗸 𝗰𝗼𝗺𝗯𝗼 𝗳𝗶𝗹𝗲 𝘄𝗶𝘁𝗵 𝘀𝗵𝗼𝗽𝗶𝗳𝘆 (𝗽𝗿𝗲𝗺𝗶𝘂𝗺)</code>

<b>-- 𝗰𝗮𝗿𝗱 & 𝗰𝗼𝗺𝗯𝗼 𝘁𝗼𝗼𝗹𝘀 --</b>
<code>/sk</code> - <code>𝗰𝗵𝗲𝗰𝗸 𝘀𝗸 𝗸𝗲𝘆</code>
<code>/bin</code> - <code>𝗯𝗶𝗻 𝗹𝗼𝗼𝗸𝘂𝗽</code>
<code>/gen</code> - <code>𝗴𝗲𝗻𝗲𝗿𝗮𝘁𝗲 𝟭𝟬 𝗰𝗮𝗿𝗱𝘀</code>
<code>/genf</code> - <code>𝗴𝗲𝗻𝗿𝗮𝘁𝗲 𝗮 𝗳𝗶𝗹𝗲 𝗼𝗳 𝗰𝗮𝗿𝗱𝘀</code>
<code>/mix</code> - <code>𝘀𝗵𝘂𝗳𝗳𝗹𝗲 𝗰𝗼𝗺𝗯𝗼 𝗹𝗶𝗻𝗲𝘀</code>
<code>/len</code> - <code>𝗰𝗼𝘂𝗻𝘁 𝗳𝗶𝗹𝗲 𝗹𝗶𝗻𝗲𝘀</code>
<code>/filter</code> - <code>𝗳𝗶𝗹𝘁𝗲𝗿 𝗰𝗮𝗿𝗱𝘀 𝗯𝘆 𝗯𝗶𝗻</code>
<code>/cb</code> - <code>𝗰𝗵𝗲𝗰𝗸 𝗯𝗶𝗻𝘀 𝗶𝗻 𝗮 𝗳𝗶𝗹𝗲</code>

<b>-- 𝘀𝗰𝗿𝗮𝗽𝗶𝗻𝗴 𝘁𝗼𝗼𝗹𝘀 --</b>
<code>/scr</code> - <code>𝘀𝗰𝗿𝗮𝗽 𝗰𝗮𝗿𝗱𝘀 𝗳𝗿𝗼𝗺 𝗰𝗵𝗮𝗻𝗻𝗲𝗹𝘀</code>
<code>/search</code> - <code>𝘀𝗲𝗮𝗿𝗰𝗵 𝗳𝗼𝗿 𝗽𝗮𝘆𝗺𝗲𝗻𝘁 𝗴𝗮𝘁𝗲𝘀</code>
<code>/fake</code> - <code>𝗚𝗘𝗡 𝗜𝗡𝗙𝗢𝗥𝗠𝗔𝗧𝗜𝗢𝗡</code>
"""
    
    # Admin Commands Section (only shown to admin)
    if is_admin:
        commands_list += """

<b>-- 𝗮𝗱𝗺𝗶𝗻 𝗰𝗼𝗺𝗺𝗮𝗻𝗱𝘀 --</b>
<code>/admin</code> - <code>𝗯𝗼𝘁 𝗼𝗻/𝗼𝗳𝗳 𝗰𝗼𝗻𝘁𝗿𝗼𝗹</code>
<code>/gates</code> - <code>𝗲𝗻𝗮𝗯𝗹𝗲/𝗱𝗶𝘀𝗮𝗯𝗹𝗲 𝗴𝗮𝘁𝗲𝘄𝗮𝘆𝘀</code>
<code>/dashboard</code> - <code>𝘃𝗶𝗲𝘄 𝗯𝗼𝘁 𝘀𝘁𝗮𝘁𝗶𝘀𝘁𝗶𝗰𝘀</code>
<code>/grant</code> - <code>𝗴𝗶𝘃𝗲 𝘀𝘂𝗯𝘀𝗰𝗿𝗶𝗽𝘁𝗶𝗼𝗻 𝘁𝗼 𝗮 𝘂𝘀𝗲𝗿</code>
<code>/code</code> - <code>𝗰𝗿𝗲𝗮𝘁𝗲 𝗮 𝘀𝘂𝗯𝘀𝗰𝗿𝗶𝗽𝘁𝗶𝗼𝗻 𝗸𝗲𝘆</code>
<code>/listusers</code> - <code>𝗹𝗶𝘀𝘁 𝗮𝗹𝗹 𝘀𝘂𝗯𝘀𝗰𝗿𝗶𝗯𝗲𝗱 𝘂𝘀𝗲𝗿𝘀</code>
<code>/broadcast</code> - <code>𝘀𝗲𝗻𝗱 𝗮 𝗺𝗲𝘀𝘀𝗮𝗴𝗲 𝘁𝗼 𝗮𝗹𝗹 𝘂𝘀𝗲𝗿𝘀</code>
<code>/ban</code> - <code>𝗯𝗮𝗻 𝗮 𝘂𝘀𝗲𝗿 𝗳𝗿𝗼𝗺 𝘁𝗵𝗲 𝗯𝗼𝘁</code>
<code>/unban</code> - <code>𝘂𝗻𝗯𝗮𝗻 𝗮 𝘂𝘀𝗲𝗿</code>
"""
        
    bot.reply_to(message, commands_list, parse_mode="HTML")

@bot.message_handler(commands=['fake'])
@check_if_banned
@check_maintenance
def fake_us_command(message):
    fake = Faker('en_US')

    full_name = fake.name()
    street = fake.street_address()
    city = fake.city()
    state = fake.state()
    postal = fake.zipcode()
    phone = fake.phone_number()
    
    email_name = full_name.lower().replace(' ', '.')
    email = f"{email_name}@telegmail.com"

    user = message.from_user
    is_subscribed, sub_status = check_subscription(user.id)
    status_tag = "[VIP]" if is_subscribed and user.id != admin_id else "[Owner]" if user.id == admin_id else "[Free]"
    requester_info = f"{user.first_name} {status_tag}"

    reply_text = f"""
🌍 #Generate_Address
━━━━━━━━━━━━━━━━━━━━━━
🏳️ 𝐂𝐨𝐮𝐧𝐭𝐫𝐲: US - United States - [ 🇺🇸 ]
━━━━━━━━━━━━━━━━━━━━━━
👤 𝐅𝐮𝐥𝐥 𝐍𝐚𝐦𝐞: {full_name}
🏠 𝐒𝐭𝐫𝐞𝐞𝐭: {street}
🏙 𝐂𝐢𝐭𝐲: {city}
🌎 𝐒𝐭𝐚𝐭𝐞: {state}
📮 𝐏𝐨𝐬𝐭𝐚𝐥: {postal}
📞 𝐏𝐡𝐨𝐧𝐞: {phone}
🌐 𝐂𝐨𝐮𝐧𝐭𝐫𝐲: United States
📧 𝐄𝐦𝐚𝐢𝐥: {email}
━━━━━━━━━━━━━━━━━━━━━━
👤 𝐑𝐞𝐪 𝐁𝐲: {requester_info}
💻 𝐃𝐞𝐯 𝐛𝐲: Venom - 🍀 (https://t.me/dev_gax)
"""
    bot.reply_to(message, reply_text)


# ——————————— GROUP SUBSCRIPTION SYSTEM ——————————— #

# File to store group subscriptions
GROUP_DATA_FILE = 'group_data.json'
initialize_json(GROUP_DATA_FILE, {}) # Ensure the file is created

@bot.message_handler(commands=['grant1'])
def grant_group_command(message):
    """Admin command to grant a subscription to a group."""
    if message.from_user.id != admin_id:
        bot.reply_to(message, "❌ This command is for the admin only.")
        return

    try:
        parts = message.text.split()
        if len(parts) != 3:
            bot.reply_to(message, "<b>Usage:</b> <code>/grant1 [group_id] [hours]</code>\n\n<b>Example:</b> <code>/grantgroup -100123456789 720</code> (for 30 days)")
            return
            
        target_group_id = int(parts[1])
        hours = float(parts[2])

        with open(GROUP_DATA_FILE, 'r+') as file:
            data = json.load(file)

            expiry_time = datetime.now() + timedelta(hours=hours)
            expiry_time_str = expiry_time.strftime('%Y-%m-%d %H:%M')

            # Add or update the group's subscription
            data[str(target_group_id)] = {'timer': expiry_time_str, 'plan': 'group_vip'}

            file.seek(0)
            json.dump(data, file, indent=4)
            file.truncate()

        # 1. Confirm to the admin
        bot.reply_to(message, f"✅ Subscription granted successfully to group <code>{target_group_id}</code> for {hours} hours.")
        
        # 2. Notify the group
        try:
            bot.send_message(target_group_id, f"🎉 <b>Subscription Activated!</b>\nThis group now has premium access until {expiry_time_str}.")
        except Exception as e:
            bot.reply_to(message, f"⚠️ Could not notify the group. Please make sure the bot is an admin in that group. Error: {e}")

    except (IndexError, ValueError):
        bot.reply_to(message, "<b>Invalid format.</b> Use: <code>/grantgroup [group_id] [hours]</code>")
    except Exception as e:
        bot.reply_to(message, f"An error occurred: {e}")


def check_group_subscription(func):
    """
    Decorator to check if a command is used in a subscribed group.
    """
    @functools.wraps(func)
    def wrapper(message, *args, **kwargs):
        # Allow the command in private chats with the admin
        if message.chat.type == 'private' and message.from_user.id == admin_id:
            return func(message, *args, **kwargs)

        # Block command in non-subscribed groups
        if message.chat.type in ['group', 'supergroup']:
            group_id = str(message.chat.id)
            try:
                with open(GROUP_DATA_FILE, 'r') as file:
                    data = json.load(file)
                
                if group_id in data:
                    expiry_time = datetime.strptime(data[group_id]['timer'], '%Y-%m-%d %H:%M')
                    if datetime.now() < expiry_time:
                        return func(message, *args, **kwargs) # Subscription is active, proceed
            except (FileNotFoundError, json.JSONDecodeError):
                pass
        
        bot.reply_to(message, "❌ This command is only available in subscribed groups. Contact the admin for a subscription.")
        return
    return wrapper



@bot.message_handler(commands=['remove1'])
def revoke_group_command(message):
    """Admin command to revoke a subscription from a group."""
    if message.from_user.id != admin_id:
        bot.reply_to(message, "❌ This command is for the admin only.")
        return

    try:
        parts = message.text.split()
        if len(parts) != 2:
            bot.reply_to(message, "<b>Usage:</b> <code>/revokegroup [group_id]</code>")
            return
            
        target_group_id = str(parts[1])

        with open(GROUP_DATA_FILE, 'r+') as file:
            data = json.load(file)

            if target_group_id in data:
                # Remove the group's subscription
                del data[target_group_id]

                file.seek(0)
                json.dump(data, file, indent=4)
                file.truncate()

                # 1. Confirm to the admin
                bot.reply_to(message, f"✅ Subscription revoked successfully from group <code>{target_group_id}</code>.")
                
                # 2. Notify the group
                try:
                    bot.send_message(int(target_group_id), "⚠️ <b>Subscription Revoked!</b>\nThis group no longer has premium access.")
                except Exception as e:
                    bot.reply_to(message, f"⚠️ Could not notify the group. The bot might have been removed. Error: {e}")
            else:
                bot.reply_to(message, f"⚠️ No active subscription found for group <code>{target_group_id}</code>.")

    except (IndexError, ValueError):
        bot.reply_to(message, "<b>Invalid format.</b> Use: <code>/revokegroup [group_id]</code>")
    except Exception as e:
        bot.reply_to(message, f"An error occurred: {e}")


@bot.message_handler(commands=['role'])
@check_if_banned
@check_maintenance
def role_command(message):
    """Displays the user's current role in the bot."""
    user_id = message.from_user.id
    role = "👤 𝗙𝗿𝗲𝗲 𝗨𝘀𝗲𝗿" # Default role

    if user_id == admin_id:
        role = "👑 𝗢𝘄𝗻𝗲𝗿"
    else:
        is_subscribed, _ = check_subscription(user_id)
        if is_subscribed:
            role = "⭐ 𝗩𝗜𝗣 𝗠𝗲𝗺𝗯𝗲𝗿"

    bot.reply_to(message, f"<b>Yᴏᴜʀ Cᴜʀʀᴇɴᴛ Rᴏʟᴇ:</b>\n{role}")

    

@bot.message_handler(commands=['profile'])
def profile_handler(message):
    user_id = str(message.from_user.id)

    # Load subscription data
    try:
        with open("data.json", "r") as f:
            data = json.load(f)
        if user_id in data:
            plan = data[user_id].get("plan", "Free")
            expires = data[user_id].get("timer", "N/A")
        else:
            plan = "Free"
            expires = "N/A"
    except FileNotFoundError:
        plan = "Free"
        expires = "N/A"

    # Load credits & referrals
    try:
        with open("credits.json", "r") as f:
            credits_data = json.load(f)
        credits = credits_data.get(user_id, {}).get("credits", 0)
        referrals = credits_data.get(user_id, {}).get("referrals", 0)
    except FileNotFoundError:
        credits = 0
        referrals = 0

    profile_text = f"""
👤 𝗣𝗿𝗼𝗳𝗶𝗹𝗲
Plan: {plan}
Expires: {expires}
Credits: {credits}
Referrals: {referrals}
"""
    bot.send_message(message.chat.id, profile_text)



@bot.message_handler(commands=['search'])
@check_if_banned
@check_maintenance
def search_command(message):
    chat_id = message.chat.id
    initial_message = bot.reply_to(message, "𝘀𝗲𝗮𝗿𝗰𝗵 𝘀𝘁𝗮𝗿𝘁𝗲𝗱...⏳")
    args = message.text.split()[1:]
    if len(args) != 3:
        bot.edit_message_text(chat_id=chat_id, message_id=initial_message.message_id, text="𝗽𝗹𝗲𝗮𝘀𝗲 𝗽𝗿𝗼𝘃𝗶𝗱𝗲 𝘁𝗵𝗿𝗲𝗲 𝗮𝗿𝗴𝘂𝗺𝗲𝗻𝘁𝘀 𝗶𝗻 𝘁𝗵𝗲 𝗳𝗼𝗿𝗺𝗮𝘁: \n/search [payment] [name] [domain]")
        return
    
    v1, v2, v3 = args
    result = perform_search(v1, v2, v3)
    bot.edit_message_text(chat_id=chat_id, message_id=initial_message.message_id, text=result,disable_web_page_preview=True)

@bot.message_handler(commands=['bin'])
@check_if_banned
@check_maintenance
def bin_lookup_command(message):
    chat_id = message.chat.id
    initial_message = bot.reply_to(message, "𝗹𝗼𝗼𝗸𝘂𝗽 𝘀𝘁𝗮𝗿𝘁𝗲𝗱...⏳")
    try:
        biN = message.text.split(' ', 1)[1]
        bin_inf = bin_info(biN)
        bot.edit_message_text(chat_id=chat_id, message_id=initial_message.message_id, text=bin_inf)
    except IndexError:
        bot.edit_message_text(chat_id=chat_id, message_id=initial_message.message_id, text="⚠️ Correct usage: `/bin [BIN]`", parse_mode="Markdown")
    except Exception as ex:
        bot.edit_message_text(chat_id=chat_id, message_id=initial_message.message_id, text=f"𝗮𝗻 𝗲𝗿𝗿𝗼𝗿 𝗼𝗰𝗰𝘂𝗿𝗿𝗲𝗱: {str(ex)}")

@bot.message_handler(commands=['cb'])
@check_if_banned
@check_maintenance
def handle_bins_command(message):
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

@bot.message_handler(commands=['len'])
@check_if_banned
@check_maintenance
def handle_len_command(message):
    chat_id = message.chat.id
    initial_message = bot.reply_to(message, "𝗰𝗼𝘂𝗻𝘁 𝘀𝘁𝗮𝗿𝘁𝗲𝗱...⏳")
    response = count_lines(message,bot)
    bot.edit_message_text(chat_id=chat_id, message_id=initial_message.message_id, text=response)

@bot.message_handler(commands=['mix'])
@check_if_banned
@check_maintenance
def handle_mix_command(message):
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
@check_if_banned
@check_maintenance
def handle_filter(message):
    chat_id = message.chat.id
    initial_message = bot.reply_to(message, "𝗳𝗶𝗹𝘁𝗲𝗿 𝘀𝘁𝗮𝗿𝘁𝗲𝗱...⏳")
    try:
        value = message.text.split(' ', 1)[1]
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
            bot.edit_message_text(chat_id=chat_id, message_id=initial_message.message_id, text="𝗻𝗼 𝗹𝗶𝗻𝗲𝘀 𝗳𝗼𝘂𝗻𝗱 𝘄𝗶𝘁𝗵 𝘁𝗵𝗮𝘁 𝗯𝗶𝗻 𝗶𝗻 𝘁𝗵𝗲 𝗳𝗶𝗹𝗲, 𝗼𝗿 𝘆𝗼𝘂 𝗱𝗶𝗱𝗻't 𝗿𝗲𝗽𝗹𝘆 𝘁𝗼 𝗮 𝗳𝗶𝗹𝗲.")
    except IndexError:
        bot.edit_message_text(chat_id=chat_id, message_id=initial_message.message_id, text="⚠️ Correct usage: `/filter [BIN]`", parse_mode="Markdown")

@bot.message_handler(commands=['genf'])
@check_if_banned
@check_maintenance
def generate_cards_file(message):
    chat_id = message.chat.id
    initial_message = bot.reply_to(message, "𝗴𝗲𝗻𝗲𝗿𝗮𝘁𝗶𝗻𝗴 𝘀𝘁𝗮𝗿𝘁𝗲𝗱...⏳")
    try:
        command_args = message.text.split()[1:]
        if not command_args:
            raise IndexError
        
        start_time = datetime.now()
        a = command_args[0]
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
    except IndexError:
        bot.edit_message_text(chat_id=chat_id, message_id=initial_message.message_id, text="⚠️ Correct usage: `/genf [bin] [amount]`", parse_mode="Markdown")
    except Exception as ex:
        bot.edit_message_text(chat_id=chat_id, message_id=initial_message.message_id, text=f"𝗮𝗻 𝗲𝗿𝗿𝗼𝗿 𝗼𝗰𝗰𝘂𝗿𝗿𝗲𝗱: {str(ex)}")

@bot.message_handler(commands=['gen'])
@check_if_banned
@check_maintenance
def generate_card(message):
    chat_id = message.chat.id
    initial_message = bot.reply_to(message, "𝗴𝗲𝗻𝗲𝗿𝗮𝘁𝗶𝗻𝗴 𝘀𝘁𝗮𝗿𝘁𝗲𝗱...⏳")
    try:
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
    except IndexError:
         bot.edit_message_text(chat_id=chat_id, message_id=initial_message.message_id, text="⚠️ Correct usage: `/gen [bin|mm|yy|cvc]`", parse_mode="Markdown")
    except Exception as e:
        bot.edit_message_text(chat_id=chat_id, message_id=initial_message.message_id, text=f"𝗮𝗻 𝗲𝗿𝗿𝗼𝗿 𝗼𝗰𝗰𝘂𝗿𝗿𝗲𝗱: {e}")

@bot.message_handler(commands=['scr'])
@check_if_banned
@check_maintenance
def send_last_messages(message):
    chat_id = message.chat.id
    initial_message = bot.reply_to(message, "𝘀𝗲𝗿𝗮𝗽𝗶𝗻𝗴 𝘀𝘁𝗮𝗿𝘁𝗲𝗱...⏳")
    command_parts = message.text.split()
    if len(command_parts) == 3 and command_parts[0] == '/scr':
        start_time = datetime.now()
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

@bot.message_handler(commands=['sk'])
@check_if_banned
@check_maintenance
def handle_sk_message(message):
    chat_id = message.chat.id
    initial_message = bot.reply_to(message, "𝗰𝗵𝗲𝗰𝗸𝗶𝗻𝗴 𝘀𝘁𝗮𝗿𝘁𝗲𝗱...⏳")
    try:
        sk = message.text.split(' ', 1)[1]
        result = check_key(sk)
        bot.edit_message_text(chat_id=chat_id, message_id=initial_message.message_id, text=result)
    except IndexError:
        bot.edit_message_text(chat_id=chat_id, message_id=initial_message.message_id, text="⚠️ Correct usage: `/sk [SK_KEY]`", parse_mode="Markdown")

@bot.message_handler(commands=['str'])
@check_if_banned
@check_maintenance
@check_cooldown
def stripe_chk_command(message):
    if not gate_status['str']:
        bot.reply_to(message, "❗️ 𝘁𝗵𝗶𝘀 𝗴𝗮𝘁𝗲𝘄𝗮𝘆 𝗶𝘀 𝗰𝘂𝗿𝗿𝗲𝗻𝘁𝗹𝘆 𝗱𝗶𝘀𝗮𝗯𝗹𝗲𝗱.")
        return
    chat_id = message.chat.id
    try:
        card_details = message.text.split(' ', 1)[1]
        initial_message = bot.reply_to(message, "𝗰𝗵𝗲𝗰𝗸𝗶𝗻𝗴 𝘀𝘁𝗮𝗿𝘁𝗲𝗱, 𝗽𝗹𝗲𝗮𝘀𝗲 𝘄𝗮𝗶𝘁 ⌛")
        edited_message = process_card(card_details)[4]
        bot.edit_message_text(chat_id=chat_id, message_id=initial_message.message_id, text=edited_message)
    except IndexError:
        bot.reply_to(message, "⚠️ Correct usage: `/str [card]`", parse_mode="Markdown")
    except Exception as e:
        bot.send_message(chat_id=chat_id, text="𝗮𝗻 𝗲𝗿𝗿𝗼𝗿 𝗼𝗰𝗰𝘂𝗿𝗿𝗲𝗱: " + str(e))


@bot.message_handler(commands=['filep'])
@check_if_banned
@check_maintenance
def payal_file_command(message):
    is_subscribed, _ = check_subscription(message.from_user.id)
    if not is_subscribed:
        bot.reply_to(message, "𝘆𝗼𝘂 𝗺𝘂𝘀𝘁 𝗵𝗮𝘃𝗲 𝗮𝗻 𝗮𝗰𝘁𝗶𝘃𝗲 𝘀𝘂𝗯𝘀𝗰𝗿𝗶𝗽𝘁𝗶𝗼𝗻 𝘁𝗼 𝘂𝘀𝗲 𝘁𝗵𝗶𝘀 𝗰𝗼𝗺𝗺𝗮𝗻𝗱.", reply_markup=create_buy_keyboard())
        return

    if not gate_status['filep']:
        bot.reply_to(message, "❗️ 𝘁𝗵𝗶𝘀 𝗴𝗮𝘁𝗲𝘄𝗮𝘆 𝗶𝘀 𝗰𝘂𝗿𝗿𝗲𝗻𝘁𝗹𝘆 𝗱𝗶𝘀𝗮𝗯𝗹𝗲𝗱.")
        return
    bot.reply_to(message, "𝗦𝗲𝗻𝗱 𝗺𝗲 𝘆𝗼𝘂𝗿 𝗰𝗼𝗺𝗯𝗼 𝗳𝗶𝗹𝗲.")
    bot.register_next_step_handler(message, handle_paypal_file)
        
# ==================== SHOPIFY 10$ CHECK ====================
waiting_for_file = {}
active_tasks = {}

# ====== BLACK KNOWLEDGE SHOPIFY PANEL ======
def create_shopify_progress_keyboard(stats):
    from telebot import types
    markup = types.InlineKeyboardMarkup(row_width=2)

    markup.row(types.InlineKeyboardButton(text=f"💳 {stats.get('CURRENT_CARD', 'N/A')}", callback_data="ignore"))
    markup.row(types.InlineKeyboardButton(text=f"⚡ 𝗦𝗛𝗢𝗣𝗜𝗙𝗬 𝟭𝟬$ | 𝗩𝗘𝗡𝗢𝗠 𝗖𝗛𝗘𝗖𝗞 ⚡", callback_data="ignore"))
    markup.row(types.InlineKeyboardButton(text=f"🧠 {stats.get('LAST_RESPONSE', 'Starting...')}", callback_data="ignore"))
    markup.row(
        types.InlineKeyboardButton(text=f"✅ 𝗔𝗽𝗽𝗿𝗼𝘃𝗲𝗱: {stats.get('APPROVED', 0)}", callback_data="ignore"),
        types.InlineKeyboardButton(text=f"❌ 𝗗𝗲𝗰𝗹𝗶𝗻𝗲𝗱: {stats.get('DECLINED', 0)}", callback_data="ignore")
    )
    markup.row(
        types.InlineKeyboardButton(text=f"📊 𝗖𝗵𝗲𝗰𝗸𝗲𝗱: {stats.get('CHECKED', 0)}/{stats.get('TOTAL', 0)}", callback_data="ignore"),
        types.InlineKeyboardButton(text="〄 𝗦𝘁𝗼𝗽 𝗖𝗵𝗲𝗰𝗸 〄", callback_data="stop_check")
    )
    markup.row(types.InlineKeyboardButton(text="〄 𝗣𝗼𝘄𝗲𝗿𝗲𝗱 𝗯𝘆 𝗩𝗘𝗡𝗢𝗠 ⚡", callback_data="ignore"))
    return markup


@bot.callback_query_handler(func=lambda call: call.data == "stop_check")
def stop_checking_callback(call):
    user_id = call.from_user.id
    if user_id in active_tasks:
        active_tasks[user_id]['should_stop'] = True
        bot.answer_callback_query(call.id, "🛑 𝗦𝘁𝗼𝗽𝗽𝗶𝗻𝗴 𝗩𝗘𝗡𝗢𝗠 𝗖𝗵𝗲𝗰𝗸...")
    else:
        bot.answer_callback_query(call.id, "❗ No active task running.")


@bot.callback_query_handler(func=lambda call: call.data == "ignore")
def ignore_callback(call):
    bot.answer_callback_query(call.id)


# ====== فحص بطاقة واحدة ======
@bot.message_handler(commands=['sh'])
@check_if_banned
@check_maintenance
@check_cooldown
def shopify_single(message):
    if not gate_status.get('sh', True):
        bot.reply_to(message, "❗ 𝗧𝗵𝗶𝘀 𝗴𝗮𝘁𝗲𝘄𝗮𝘆 𝗶𝘀 𝗰𝘂𝗿𝗿𝗲𝗻𝘁𝗹𝘆 𝗱𝗶𝘀𝗮𝗯𝗹𝗲𝗱.")
        return

    try:
        card = message.text.split(' ', 1)[1]
    except IndexError:
        bot.reply_to(message, "⚠️ 𝗨𝘀𝗮𝗴𝗲: `/sh card|mm|yy|cvv`", parse_mode="Markdown")
        return

    chat_id = message.chat.id
    msg = bot.reply_to(message, "⏳ 𝗖𝗵𝗲𝗰𝗸𝗶𝗻𝗴 𝗰𝗮𝗿𝗱...")

    cc, result, ok = process_card_s(card, token=bot.token, ID=chat_id)

    if ok:
        text = f"✅ 𝗔𝗽𝗽𝗿𝗼𝘃𝗲𝗱 (𝗦𝗛𝗢𝗣𝗜𝗙𝗬 𝟭𝟬$)\n━━━━━━━━━━━━━━━\n<code>{cc}</code>\n🧠 {result}"
    else:
        text = f"❌ 𝗗𝗲𝗰𝗹𝗶𝗻𝗲𝗱 (𝗦𝗛𝗢𝗣𝗜𝗙𝗬 𝟭𝟬$)\n━━━━━━━━━━━━━━━\n<code>{cc}</code>\n🧠 {result}"

    bot.edit_message_text(chat_id=chat_id, message_id=msg.message_id, text=text, parse_mode="HTML")


# ====== استقبال ملف الكومبو ======
@bot.message_handler(commands=['shf'])
@check_if_banned
@check_maintenance
def ask_for_combo(message):
    is_subscribed, _ = check_subscription(message.from_user.id)
    if not is_subscribed:
        bot.reply_to(message, "❗ 𝗬𝗼𝘂 𝗺𝘂𝘀𝘁 𝗵𝗮𝘃𝗲 𝗮𝗻 𝗮𝗰𝘁𝗶𝘃𝗲 𝘀𝘂𝗯𝘀𝗰𝗿𝗶𝗽𝘁𝗶𝗼𝗻.", reply_markup=create_buy_keyboard())
        return
    if not gate_status.get('shf', True):
        bot.reply_to(message, "❗ 𝗧𝗵𝗶𝘀 𝗴𝗮𝘁𝗲𝘄𝗮𝘆 𝗶𝘀 𝗰𝘂𝗿𝗿𝗲𝗻𝘁𝗹𝘆 𝗱𝗶𝘀𝗮𝗯𝗹𝗲𝗱.")
        return

    waiting_for_file[message.chat.id] = True
    bot.reply_to(message, "📂 𝗦𝗲𝗻𝗱 𝘆𝗼𝘂𝗿 𝗰𝗼𝗺𝗯𝗼 𝗳𝗶𝗹𝗲 (.txt) 𝗳𝗼𝗿 𝗩𝗘𝗡𝗢𝗠 𝗦𝗛𝗢𝗣𝗜𝗙𝗬 𝗰𝗵𝗲𝗰𝗸.")


# ====== استقبال المستند ======
@bot.message_handler(content_types=['document'])
@check_if_banned
def handle_document(message):
    if message.chat.id in waiting_for_file:
        del waiting_for_file[message.chat.id]
        handle_shopify_file(message)


# ====== فحص الملف بالكامل ======
def handle_shopify_file(message):
    chat_id = message.chat.id

    file_info = bot.get_file(message.document.file_id)
    downloaded = bot.download_file(file_info.file_path)
    cards = [line.strip() for line in downloaded.decode('utf-8', errors='ignore').splitlines() if line.strip()]

    total = len(cards)
    stats = {"APPROVED": 0, "DECLINED": 0, "CHECKED": 0, "TOTAL": total, "CURRENT_CARD": "N/A", "LAST_RESPONSE": "𝗦𝘁𝗮𝗿𝘁𝗶𝗻𝗴..."}
    active_tasks[chat_id] = {"should_stop": False}

    status_msg = bot.send_message(chat_id, "⚡ 𝗦𝘁𝗮𝗿𝘁𝗶𝗻𝗴 𝗩𝗘𝗡𝗢𝗠 𝗦𝗛𝗢𝗣𝗜𝗙𝗬 𝗰𝗵𝗲𝗰𝗸...", reply_markup=create_shopify_progress_keyboard(stats))

    for card in cards:
        if active_tasks.get(chat_id, {}).get("should_stop"):
            break

        stats["CHECKED"] += 1
        stats["CURRENT_CARD"] = card

        try:
            cc, result, ok = process_card_s(card, token=bot.token, ID=chat_id)
            stats["LAST_RESPONSE"] = result
            if ok:
                stats["APPROVED"] += 1
                bot.send_message(chat_id, f"✅ 𝗔𝗽𝗽𝗿𝗼𝘃𝗲𝗱 (𝗦𝗛𝗢𝗣𝗜𝗙𝗬 𝟭𝟬$)\n━━━━━━━━━━━━━━━\n<code>{cc}</code>\n🧠 {result}", parse_mode="HTML")
            else:
                stats["DECLINED"] += 1
        except Exception as e:
            stats["DECLINED"] += 1
            stats["LAST_RESPONSE"] = str(e)

        # تحديث العدادات على الرسالة الرئيسية
        try:
            bot.edit_message_reply_markup(chat_id, status_msg.message_id, reply_markup=create_shopify_progress_keyboard(stats))
        except Exception:
            pass

        time.sleep(2)

    # بعد الانتهاء
    try:
        bot.edit_message_text(
            f"✅ 𝗩𝗘𝗡𝗢𝗠 𝗦𝗛𝗢𝗣𝗜𝗙𝗬 𝗖𝗵𝗲𝗰𝗸 𝗙𝗶𝗻𝗶𝘀𝗵𝗲𝗱 ⚡\n"
            f"━━━━━━━━━━━━━━━━━━━━━\n"
            f"📊 𝗖𝗵𝗲𝗰𝗸𝗲𝗱: {stats['CHECKED']}/{stats['TOTAL']}\n"
            f"✅ 𝗔𝗽𝗽𝗿𝗼𝘃𝗲𝗱: {stats['APPROVED']}\n"
            f"❌ 𝗗𝗲𝗰𝗹𝗶𝗻𝗲𝗱: {stats['DECLINED']}\n"
            f"〄 𝗣𝗼𝘄𝗲𝗿𝗲𝗱 𝗯𝘆 𝗩𝗘𝗡𝗢𝗠 ⚡",
            chat_id=chat_id,
            message_id=status_msg.message_id,
            parse_mode="HTML"
        )
    except Exception:
        pass

    active_tasks.pop(chat_id, None)

# ==================== END SHOPIFY 10$ CHECK ====================



# --- Proxy Initialization (يجب أن تضاف في قسم تهيئة الملفات) ---
def initialize_json(filename, default_data):
    if not os.path.exists(filename):
        with open(filename, 'w') as f:
            json.dump(default_data, f, indent=4)

# 🔴 التعديل هنا: يجب إضافة السطر التالي عند تهيئة ملفات JSON 🔴
# initialize_json('user_proxies.json', {})


# ——————————— User Proxy Retrieval Function ——————————— #
# ——————————— User Proxy Retrieval Function ——————————— #
# ——————————— User Proxy Retrieval Function ——————————— #


# proxy_checker_extended.py
# Requirements: pip install pyTelegramBotAPI requests pysocks
# If integrating into existing bot.py, ensure there's a 'bot' TeleBot instance available.




import os
import re
import json
import time
import socket
import tempfile
import requests
from concurrent.futures import ThreadPoolExecutor, as_completed

# If running standalone, uncomment and set your token:
# from telebot import TeleBot
# TOKEN = "YOUR_TELEGRAM_BOT_TOKEN"
# bot = TeleBot(TOKEN, parse_mode="HTML")

# ---------- Configuration ----------
MAX_WORKERS = 60         # عدلها حسب موارد السيرفر (CPU, Network)
TCP_TIMEOUT = 3.0        # ثواني لقياس TCP connect
HTTP_TIMEOUT = 5.0       # مهلة لكل طلب HTTP عبر البروكسي
RESULTS_DIR = "."        # مجلد لحفظ التقارير المؤقتة

# قائمة مواقع موثوقة للفحص (افضل مزيج APIs + مواقع)
CHECK_SITES = [
    "https://api.ipify.org?format=json",
    "https://ifconfig.me/ip",
    "https://httpbin.org/ip",
    "https://checkip.amazonaws.com",
    "https://icanhazip.com",
    "https://www.google.com",
]
# ---------- Helpers ----------
def parse_proxy_raw(line):
    """
    يقبل صيغ مختلفة:
      - socks5://user:pass@IP:PORT
      - socks5://IP:PORT
      - http://user:pass@IP:PORT
      - http://IP:PORT
      - user:pass@IP:PORT
      - IP:PORT
    Returns dict or None:
        {"raw": original_line, "scheme": "HTTP"/"SOCKS5"/"UNKNOWN", "host": host, "port": port, "has_auth": True/False}
    """
    l = line.strip()
    if not l:
        return None
    scheme = "UNKNOWN"
    work = l

    if l.startswith("socks5://"):
        scheme = "SOCKS5"
        work = l[len("socks5://"):]
    elif l.startswith("http://"):
        scheme = "HTTP"
        work = l[len("http://"):]

    # separate auth if present
    auth = None
    if "@" in work:
        auth, hostport = work.rsplit("@", 1)
    else:
        hostport = work

    if ":" not in hostport:
        return None

    host, port = hostport.rsplit(":", 1)
    try:
        port = int(port)
    except:
        return None

    return {
        "raw": l,
        "scheme": scheme,
        "host": host,
        "port": port,
        "auth": bool(auth)
    }

def tcp_ping_host(host, port, timeout=TCP_TIMEOUT):
    """فتح اتصال TCP سريع لقياس البنج الحقيقي (ms)"""
    try:
        start = time.time()
        sock = socket.create_connection((host, int(port)), timeout=timeout)
        sock.close()
        end = time.time()
        return f"{int((end - start) * 1000)}ms", True
    except Exception:
        return "Timeout", False

def build_requests_proxies(proxy_raw, scheme_test):
    """
    proxy_raw: original line (may include auth or prefix)
    scheme_test: "HTTP" or "SOCKS5" - how to format proxies for requests
    Returns proxies dict for requests.get(...)
    """
    # If raw already contains scheme prefix (e.g., socks5:// or http://) keep it, else prefix
    p = proxy_raw.strip()
    if p.startswith("socks5://") or p.startswith("http://"):
        # use as-is but ensure requests recognizes socks scheme (requires pysocks)
        if scheme_test == "SOCKS5":
            if p.startswith("socks5://"):
                proxy_url = p
            else:
                # raw has http:// (contradiction) -> build socks variant without auth
                # attempt to convert host:port to socks5://host:port
                no_scheme = p.split("://", 1)[1]
                proxy_url = f"socks5://{no_scheme}"
        else:
            if p.startswith("http://"):
                proxy_url = p
            else:
                no_scheme = p.split("://", 1)[1]
                proxy_url = f"http://{no_scheme}"
    else:
        # raw has no scheme -> attach desired scheme
        proxy_url = f"{'socks5' if scheme_test=='SOCKS5' else 'http'}://{p}"

    return {"http": proxy_url, "https": proxy_url}

def test_proxy_sites(proxy_raw, scheme_test, timeout=HTTP_TIMEOUT):
    """
    يحاول فتح قائمة CHECK_SITES عبر البروكسي بنمط scheme_test (HTTP أو SOCKS5).
    Returns tuple: (success_count, details_dict)
    details_dict maps site -> status string ("200","ERROR", "EXC", etc.)
    """
    proxies = build_requests_proxies(proxy_raw, scheme_test)
    details = {}
    successes = 0
    for site in CHECK_SITES:
        try:
            r = requests.get(site, proxies=proxies, timeout=timeout)
            if r.status_code == 200:
                details[site] = "200"
                successes += 1
            else:
                details[site] = f"HTTP_{r.status_code}"
        except Exception as e:
            details[site] = "ERR"
    return successes, details

# ---------- Core single-proxy check ----------
def check_one_proxy_try_both(proxy_line):
    """
    Strategy:
      1) parse host:port and do a TCP connect to measure ping
      2) try HTTP mode: test sites count
      3) try SOCKS5 mode: test sites count
      4) decide: if either mode has >0 successes, that mode is chosen (prefer mode with greater successes),
         return detailed result including ping, tcp_ok, http_successes, socks_successes, chosen_type.
    """
    parsed = parse_proxy_raw(proxy_line)
    if not parsed:
        return {
            "proxy": proxy_line,
            "chosen": "INVALID",
            "tcp_ping": "N/A",
            "tcp_ok": False,
            "http_success": 0,
            "socks_success": 0,
            "sites_http": {},
            "sites_socks": {},
            "status": "INVALID"
        }

    host = parsed["host"]
    port = parsed["port"]

    ping, tcp_ok = tcp_ping_host(host, port)

    # Try HTTP
    http_success, http_details = test_proxy_sites(proxy_line, "HTTP")
    # Try SOCKS5
    socks_success, socks_details = test_proxy_sites(proxy_line, "SOCKS5")

    # choose: prefer protocol with more successes; if tie and >0, pick HTTP first
    chosen = "UNKNOWN"
    if http_success == 0 and socks_success == 0:
        chosen = "DEAD"
        status = "DEAD ❌"
    else:
        if http_success >= socks_success:
            chosen = "HTTP"
            status = f"LIVE ✅ ({http_success}/{len(CHECK_SITES)})"
        else:
            chosen = "SOCKS5"
            status = f"LIVE ✅ ({socks_success}/{len(CHECK_SITES)})"

    return {
        "proxy": proxy_line,
        "chosen": chosen,
        "tcp_ping": ping,
        "tcp_ok": tcp_ok,
        "http_success": http_success,
        "socks_success": socks_success,
        "sites_http": http_details,
        "sites_socks": socks_details,
        "status": status
    }

# ---------- Bulk checks for user's saved proxies ----------
def check_proxies_for_user(user_id, max_workers=MAX_WORKERS):
    try:
        if not os.path.exists("user_proxies.json"):
            return None
        with open("user_proxies.json", "r", encoding="utf-8") as jf:
            data = json.load(jf)
        proxies = data.get(str(user_id), [])
    except Exception:
        proxies = []

    if not proxies:
        return None

    results = []
    with ThreadPoolExecutor(max_workers=min(max_workers, max(4, len(proxies)))) as ex:
        futures = {ex.submit(check_one_proxy_try_both, p): p for p in proxies}
        for fut in as_completed(futures):
            try:
                results.append(fut.result())
            except Exception as e:
                results.append({
                    "proxy": futures[fut],
                    "chosen": "ERR",
                    "tcp_ping": "N/A",
                    "tcp_ok": False,
                    "http_success": 0,
                    "socks_success": 0,
                    "sites_http": {},
                    "sites_socks": {},
                    "status": f"ERROR: {str(e)}"
                })
    return results

# ---------- File-based checking (from uploaded .txt) ----------
def check_proxies_from_file_parallel(file_path, max_workers=MAX_WORKERS):
    if not os.path.exists(file_path):
        return None
    with open(file_path, "r", encoding="utf-8") as f:
        lines = [ln.strip() for ln in f if ln.strip()]

    if not lines:
        return None

    results = []
    with ThreadPoolExecutor(max_workers=min(max_workers, max(4, len(lines)))) as ex:
        futures = {ex.submit(check_one_proxy_try_both, ln): ln for ln in lines}
        for fut in as_completed(futures):
            try:
                results.append(fut.result())
            except Exception as e:
                results.append({
                    "proxy": futures[fut],
                    "chosen": "ERR",
                    "tcp_ping": "N/A",
                    "tcp_ok": False,
                    "http_success": 0,
                    "socks_success": 0,
                    "sites_http": {},
                    "sites_socks": {},
                    "status": f"ERROR: {str(e)}"
                })

    # save single result file
    ts = int(time.time())
    out_path = os.path.join(RESULTS_DIR, f"proxy_results_{ts}.txt")
    with open(out_path, "w", encoding="utf-8") as outf:
        header = "proxy | chosen | tcp_ping | tcp_ok | http_success | socks_success | status\n"
        outf.write(header)
        outf.write("=" * 100 + "\n")
        for r in results:
            outf.write(f"{r['proxy']} | {r['chosen']} | {r['tcp_ping']} | {r['tcp_ok']} | {r['http_success']} | {r['socks_success']} | {r['status']}\n")
            # write site details compactly
            outf.write("  HTTP sites:\n")
            for s, v in r.get("sites_http", {}).items():
                outf.write(f"    {s} => {v}\n")
            outf.write("  SOCKS5 sites:\n")
            for s, v in r.get("sites_socks", {}).items():
                outf.write(f"    {s} => {v}\n")
            outf.write("\n")
    return out_path

# ---------- Telegram handlers (to integrate into your bot) ----------
# NOTE: this block assumes you have a 'bot' TeleBot instance already.
# If you run standalone, uncomment TeleBot creation at top.

# waiting state for file upload after /prx
waiting_for_file = {}

# /setproxy - save proxies for the user (one per line). keep prefixes if provided.
def setproxy_handler(message):
    try:
        text = message.text or ""
        parts = text.split(maxsplit=1)
        if len(parts) < 2:
            bot.reply_to(message, "⚠️ Usage: /setproxy <one proxy per line>\nExamples:\n43.134.12.116:19146\nhttp://1.2.3.4:8080\nsocks5://5.6.7.8:1080")
            return
        body = parts[1].strip()
        lines = [ln.strip() for ln in body.splitlines() if ln.strip()]
        if not lines:
            bot.reply_to(message, "⚠️ No proxies found in your message.")
            return

        # simple validation keep as-is
        saved = []
        for ln in lines:
            # allow if contains ip:port pattern or has scheme
            if re.search(r"\d+\.\d+\.\d+\.\d+:\d+", ln) or ln.startswith("socks5://") or ln.startswith("http://"):
                saved.append(ln)
        if not saved:
            bot.reply_to(message, "❌ No valid proxies found. Use IP:PORT or include http:// or socks5:// prefix.")
            return

        uid = str(message.from_user.id)
        if os.path.exists("user_proxies.json"):
            with open("user_proxies.json", "r", encoding="utf-8") as jf:
                data = json.load(jf)
        else:
            data = {}
        data[uid] = saved
        with open("user_proxies.json", "w", encoding="utf-8") as jf:
            json.dump(data, jf, indent=2)
        bot.reply_to(message, f"✅ Saved {len(saved)} proxies.")
    except Exception as e:
        bot.reply_to(message, f"⚠️ Error in /setproxy: {e}")

# /clearproxy - clear saved proxies
def clearproxy_handler(message):
    try:
        uid = str(message.from_user.id)
        if not os.path.exists("user_proxies.json"):
            bot.reply_to(message, "⚠️ No saved proxies.")
            return
        with open("user_proxies.json", "r+", encoding="utf-8") as jf:
            data = json.load(jf)
            if uid in data:
                del data[uid]
                jf.seek(0)
                json.dump(data, jf, indent=2)
                jf.truncate()
                bot.reply_to(message, "✅ Cleared your saved proxies.")
            else:
                bot.reply_to(message, "⚠️ You had no saved proxies.")
    except Exception as e:
        bot.reply_to(message, f"⚠️ Error in /clearproxy: {e}")

# /proxy_check - check saved proxies and send a result file
def proxy_check_handler(message):
    try:
        uid = message.from_user.id
        msg = bot.reply_to(message, "🚦 Checking saved proxies... this may take a while.")
        results = check_proxies_for_user(uid)
        if not results:
            bot.edit_message_text("⚠️ No saved proxies found.", chat_id=message.chat.id, message_id=msg.message_id)
            return
        # save summary file
        ts = int(time.time())
        out_path = os.path.join(RESULTS_DIR, f"proxy_report_user_{uid}_{ts}.txt")
        live = sum(1 for r in results if r.get("status","").startswith("LIVE"))
        total = len(results)
        with open(out_path, "w", encoding="utf-8") as f:
            f.write(f"Proxy Health Report for {uid}\n")
            f.write(f"Live: {live} / {total}\n\n")
            for r in results:
                f.write(f"{r['proxy']} | chosen={r['chosen']} | ping={r['tcp_ping']} | status={r['status']}\n")
                f.write("  HTTP sites:\n")
                for s, v in r.get("sites_http", {}).items():
                    f.write(f"    {s} => {v}\n")
                f.write("  SOCKS5 sites:\n")
                for s, v in r.get("sites_socks", {}).items():
                    f.write(f"    {s} => {v}\n")
                f.write("\n")
        with open(out_path, "rb") as f:
            bot.send_document(message.chat.id, f, caption="📄 Proxy Health Report")
        bot.edit_message_text("✅ Proxy check completed. Report sent.", chat_id=message.chat.id, message_id=msg.message_id)
        try:
            os.remove(out_path)
        except:
            pass
    except Exception as e:
        bot.reply_to(message, f"⚠️ Error in /proxy_check: {e}")

# /prx - ask user to upload file
def prx_command_handler(message):
    waiting_for_file[message.from_user.id] = True
    bot.reply_to(message, "📂 Please send a .txt file containing proxies (one per line). I will check both HTTP and SOCKS5 automatically.")

# document handler - only process when user did /prx (prevents accidental files)
def document_handler(message):
    try:
        uid = message.from_user.id
        if not waiting_for_file.get(uid, False):
            # ignore unrelated document uploads
            return
        waiting_for_file[uid] = False  # reset immediately

        doc = message.document
        if not doc or not doc.file_name.lower().endswith(".txt"):
            bot.reply_to(message, "⚠️ Please send a .txt file.")
            return

        # download file
        file_info = bot.get_file(doc.file_id)
        downloaded = bot.download_file(file_info.file_path)
        tmp_fd, tmp_path = tempfile.mkstemp(prefix=f"prx_{uid}_", suffix=".txt")
        os.close(tmp_fd)
        with open(tmp_path, "wb") as tf:
            tf.write(downloaded)

        status_msg = bot.send_message(message.chat.id, "⏳ File received. Checking proxies (this may take some time)...")

        out_file = check_proxies_from_file_parallel(tmp_path)

        if out_file:
            with open(out_file, "rb") as f:
                bot.send_document(message.chat.id, f, caption="✅ Proxy Check Results (single file)")
            try:
                os.remove(out_file)
            except:
                pass
        else:
            bot.send_message(message.chat.id, "⚠️ No proxies found in the file or error during checking.")

        # cleanup
        try:
            os.remove(tmp_path)
        except:
            pass
        try:
            bot.delete_message(message.chat.id, status_msg.message_id)
        except:
            pass

    except Exception as e:
        bot.reply_to(message, f"⚠️ Error while processing uploaded file: {e}")

# ---------- Register handlers on telebot instance ----------
# If you integrated into existing bot, register with: bot.message_handler(...) decorators.
# Here we assume user wants direct registration if bot instance exists.

try:
    # attach if 'bot' exists in globals
    bot  # reference to existing TeleBot instance
    # register
    bot.message_handler(commands=['setproxy'])(setproxy_handler)
    bot.message_handler(commands=['clearproxy'])(clearproxy_handler)
    bot.message_handler(commands=['proxy_check'])(proxy_check_handler)
    bot.message_handler(commands=['prx'])(prx_command_handler)
    bot.message_handler(content_types=['document'])(document_handler)
except NameError:
    # no bot in scope (standalone usage) -> user must create TeleBot and register handlers themselves
    print("Note: No 'bot' TeleBot instance found in current scope. Create one and register handlers manually.")

# If running as standalone script, uncomment below to start polling:
# if __name__ == "__main__":
#     print("Starting proxy checker bot...")
#     bot.infinity_polling(timeout=60, long_polling_timeout=60)


# ——————————— Speed Test Logic ——————————— #

# بطاقة وهمية لاستخدامها في اختبار السرعة (يجب أن تكون صيغتها صحيحة)
# ——————————— Speed Test Logic (المُصحح والكامل) ——————————— #

# بطاقة وهمية لاستخدامها في اختبار السرعة (يجب أن تكون صيغتها صحيحة)
# ——————————— Speed Test Logic (المُصحح والكامل) ——————————— #

# بطاقة وهمية لاستخدامها في اختبار السرعة (يجب أن تكون صيغتها صحيحة)
# ——————————— Speed Test Logic (المُصحح لخطأ المعاملات) ——————————— #

DUD_CARD = "5522283003645827|09|2025|481" 
TEST_ITERATIONS = 3 

def measure_gate_latency(check_function, card_details, gate_key, user_id):
    """
    يقيس متوسط زمن الاستجابة لدالة فحص معينة.
    """
    if not gate_status.get(gate_key, False):
        return None, "❌ Disabled"
    
    # 🔴 تعطيل Proxies لإجراء الفحص المباشر
    proxy_data = None 
    # قمنا بتعطيل الاستدعاء لـ get_user_proxy_data لضمان الاتصال المباشر أولاً

    total_time = 0
    success_count = 0 

    for _ in range(TEST_ITERATIONS):
        start_time = time.time()
        try:
            # 🔴 الحل الجذري: استدعاء الدالة بدون تمرير proxy_data صراحةً
            # إذا كانت الدالة لا تقبل معامل proxy_data، فإن تمريره يسبب خطأ.
            
            if gate_key == 'pay5':
                # دالة pay5 تُرجع قيمتين.
                _ = check_function(card_details)
            elif gate_key == 'sh':
                # دالة shopify تحتاج لمعاملي token و ID فقط.
                _ = check_function(card_details, token=bot.token, ID=user_id)
            elif gate_key == 'chk3':
                # Braintree Dual Auth يتطلب استدعاء دالتين (ali1, ali2) بدون معاملات إضافية.
                ali1(card_details)
            else:
                # بقية الدوال (Stripe, Braintree, PayPal)
                # نعتمد على استدعائها بالمعاملات الأساسية فقط
                _ = check_function(card_details)
            
            total_time += (time.time() - start_time)
            success_count += 1

        except Exception as e:
            # هذه الكتلة تلتقط الأخطاء الداخلية في الدوال المحلية (مثل خطأ الاتصال، أو خطأ المعاملات)
            # لتشخيص أسرع، يمكنك طباعة الخطأ:
            # print(f"Speed Test Error in {gate_key}: {e}") 
            continue

    if success_count == 0:
        return None, "⚠️ Failed to connect"
    
    avg_latency_ms = (total_time / success_count) * 1000
    return avg_latency_ms, f"✅ {avg_latency_ms:.0f} ms"


@bot.message_handler(commands=['speedtest'])
@check_if_banned
@check_maintenance
def speedtest_command(message):
    is_subscribed, _ = check_subscription(message.from_user.id)
    if not is_subscribed:
        bot.reply_to(message, "𝘆𝗼𝘂 𝗺𝘂𝘀𝘁 𝗵ﺎ𝘃𝗲 𝗮𝗻 𝗮𝗰𝘁𝗶𝘃𝗲 𝘀𝘂𝗯𝘀𝗰𝗿𝗶𝗽𝘁𝗶𝗼𝗻 𝘁𝗼 𝘂𝘀𝗲 𝘁𝗵𝗶𝘀 𝗰𝗼𝗺𝗺𝗮𝗻𝗱.", reply_markup=create_buy_keyboard())
        return

    initial_message = bot.reply_to(message, "⏳ 𝗦𝘁𝗮𝗿𝘁𝗶𝗻𝗴 𝗴𝗮𝘁𝗲𝘄𝗮𝘆 𝘀𝗽𝗲𝗲𝗱 𝘁𝗲𝘀𝘁 𝗮𝗰𝗿𝗼𝘀𝘀 𝟯 𝗶𝘁𝗲𝗿𝗮𝘁𝗶𝗼𝗻𝘀...")
    
    results = {}
    user_id = message.from_user.id

    # قائمة البوابات للفحص: (Name, Function, Gate_Key)
    gates_to_check = [
        ('Stripe', process_card, 'str'),
        ('Braintree', process_card_b, 'chk'),
        ('PayPal', process_card_p, 'pay'),
        ('PayPal 5$', process_card_paypal5, 'pay5'),
        ('Shopify', process_card_s, 'sh'),
        ('Braintree Dual', ali1, 'chk3'), 
    ]

    for name, func, key in gates_to_check:
        latency, status_text = measure_gate_latency(func, DUD_CARD, key, user_id)
        results[name] = status_text
        
        # تحديث الرسالة باستمرار
        report = "🚀 𝗚𝗮𝘁𝗲𝘄𝗮𝘆 𝗦𝗽𝗲𝗲𝗱 𝗧𝗲𝘀𝘁 𝗥𝗲𝘀𝘂𝗹𝘁𝘀 🚀\n"
        report += "━━━━━━━━━━━━━━━━━━━━━\n"
        # طباعة النتائج بالترتيب
        for gate_name, res in results.items():
             report += f" • {gate_name}: {res}\n"
        
        try:
            bot.edit_message_text(report, chat_id=message.chat.id, message_id=initial_message.message_id)
            time.sleep(1) # تأخير بسيط بين الاختبارات
        except telebot.apihelper.ApiTelegramException:
             pass # تجاهل خطأ "الرسالة لم تتغير"

    final_report = "🚀 𝗚𝗮𝘁𝗲𝘄𝗮𝘆 𝗦𝗽𝗲𝗲𝗱 𝗧𝗲𝘀𝘁 𝗥𝗲𝘀𝘂𝗹𝘁𝘀 🚀\n"
    final_report += "━━━━━━━━━━━━━━━━━━━━━\n"
    for gate_name, res in results.items():
         final_report += f" • {gate_name}: {res}\n"

    bot.edit_message_text(final_report + "\n━━━━━━━━━━━━━━━━━━━━━\n✅ 𝗖𝗼𝗺𝗽𝗹𝗲𝘁𝗲𝗱 𝘁𝗲𝘀𝘁 𝗮𝗰𝗿𝗼𝘀𝘀 𝗮𝗹𝗹 𝗮𝗰𝘁𝗶𝘃𝗲 𝗴𝗮𝘁𝗲𝘀!", chat_id=message.chat.id, message_id=initial_message.message_id)


# ——————————— Get User's Real IP Command ——————————— #

@bot.message_handler(commands=['myip'])
@check_if_banned
@check_maintenance
def myip_command(message):
    chat_id = message.chat.id
    initial_message = bot.reply_to(message, "🌍 𝗙𝗲𝘁𝗰𝗵𝗶𝗻𝗴 𝘆𝗼𝘂𝗿 𝗜𝗣 𝗮𝗱𝗱𝗿𝗲𝘀𝘀... ⏳")

    # 1. محاولة الحصول على البروكسي الخاص بالمستخدم
    proxy_data, proxy_str = get_user_proxy_data(chat_id)
    
    ip_lookup_service = 'https://api.ipify.org?format=text' # خدمة للحصول على IP
    
    try:
        # استخدام البروكسي إذا كان موجودًا
        response = requests.get(ip_lookup_service, proxies=proxy_data, timeout=5)
        ip_address = response.text.strip()
        
        if proxy_str:
            ip_source = f"𝗬𝗼𝘂𝗿 𝗖𝘂𝘀𝘁𝗼𝗺 𝗣𝗿𝗼𝘅𝘆: <code>{proxy_str}</code>"
        else:
            ip_source = "𝗕𝗼𝘁 𝗛𝗼𝘀𝘁𝗶𝗻𝗴 𝗦𝗲𝗿𝘃𝗲𝗿"

        report = f"""
🌐 𝗬𝗼𝘂𝗿 𝗖𝘂𝗿𝗿𝗲𝗻𝘁 𝗘𝘅𝗶𝘁 𝗜𝗣 🌐
━━━━━━━━━━━━━━━━━━━━━
🖥️ 𝗜𝗣 𝗔𝗱𝗱𝗿𝗲𝘀𝘀: <code>{ip_address}</code>
🔗 𝗦𝗼𝘂𝗿𝗰𝗲: {ip_source}
"""
        bot.edit_message_text(report, chat_id=chat_id, message_id=initial_message.message_id, parse_mode='html')

    except Exception:
        bot.edit_message_text("❌ 𝗙𝗮𝗶𝗹𝗲𝗱 𝘁𝗼 𝗿𝗲𝘁𝗿𝗶𝗲𝘃𝗲 𝗜𝗣. 𝗣𝗹𝗲𝗮𝘀𝗲 𝘁𝗿𝘆 𝗮𝗴𝗮𝗶𝗻.", chat_id=chat_id, message_id=initial_message.message_id)



@bot.callback_query_handler(func=lambda call: call.data == "credits_menu")
def credits_menu_callback(call):
    user_id = str(call.from_user.id)

    with open("credits.json", "r") as f:
        credits_data = json.load(f)
    credits = credits_data.get(user_id, {}).get("credits", 0)

    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("↔️ 𝗥𝗲𝗱𝗲𝗲𝗺 𝟱𝟬 𝗖𝗿𝗲𝗱𝗶𝘁𝘀 = 𝟭 𝗛𝗼𝘂𝗿", callback_data="redeem_credits"))
    markup.add(types.InlineKeyboardButton("🎁 𝗖𝗹𝗮𝗶𝗺 𝗗𝗮𝗶𝗹𝘆 𝗚𝗶𝗳𝘁 (+𝟱)", callback_data="daily_gift"))
    markup.add(types.InlineKeyboardButton("🔙 𝗕𝗮𝗰𝗸", callback_data="back"))

    bot.edit_message_caption(
        chat_id=call.message.chat.id,
        message_id=call.message.message_id,
        caption=f"🎁 𝗬𝗼𝘂𝗿 𝗖𝗿𝗲𝗱𝗶𝘁𝘀: {credits}\n\n- 𝗥𝗲𝗱𝗲𝗲𝗺 𝟱𝟬 𝗰𝗿𝗲𝗱𝗶𝘁𝘀 𝗳𝗼𝗿 𝟭 𝗵𝗼𝘂𝗿 𝘀𝘂𝗯𝘀𝗰𝗿𝗶𝗽𝘁𝗶𝗼𝗻.\n- 𝗖𝗹𝗮𝗶𝗺 𝘆𝗼𝘂𝗿 𝗳𝗿𝗲𝗲 𝗱𝗮𝗶𝗹𝘆 𝗴𝗶𝗳𝘁 (+𝟱 𝗰𝗿𝗲𝗱𝗶𝘁𝘀).",
        reply_markup=markup
    )





@bot.callback_query_handler(func=lambda call: call.data == "redeem_credits")
def redeem_credits_callback(call):
    user_id = str(call.from_user.id)

    with open("credits.json", "r+") as f:
        credits_data = json.load(f)

    if user_id not in credits_data or credits_data[user_id]["credits"] < 50:
        bot.answer_callback_query(call.id, text="❌ Not enough credits (50 = 1h)", show_alert=True)
        return
    
    # Deduct 50 credits
    credits_data[user_id]["credits"] -= 50
    with open("credits.json", "w") as f:
        json.dump(credits_data, f, indent=4)

    # Extend subscription
    with open("data.json", "r+") as f:
        data = json.load(f)
        expiry_time = datetime.now() + timedelta(hours=1)
        expiry_time_str = expiry_time.strftime('%Y-%m-%d %H:%M')
        data[user_id] = {"plan": "vip", "timer": expiry_time_str}
        f.seek(0)
        json.dump(data, f, indent=4)
        f.truncate()

    bot.send_message(call.message.chat.id, f"✅ 50 credits redeemed.\n📅 Subscription extended until: {expiry_time_str}")

@bot.callback_query_handler(func=lambda call: call.data == "daily_gift")
def daily_gift_callback(call):
    user_id = str(call.from_user.id)

    with open("credits.json", "r+") as f:
        try:
            credits_data = json.load(f)
        except json.JSONDecodeError:
            credits_data = {}

    if user_id not in credits_data:
        credits_data[user_id] = {"credits": 0, "referred_by": None}

    last_claim = credits_data[user_id].get("last_claim")
    now = datetime.now()

    if last_claim:
        last_claim_dt = datetime.strptime(last_claim, "%Y-%m-%d %H:%M")
        if now - last_claim_dt < timedelta(hours=24):
            remaining = timedelta(hours=24) - (now - last_claim_dt)
            bot.answer_callback_query(
                call.id, 
                text=f"⏳ 𝗖𝗼𝗺𝗲 𝗯𝗮𝗰𝗸 𝗶𝗻 {remaining.seconds//3600}𝗵 {remaining.seconds//60%60}𝗺.", 
                show_alert=True
            )
            return

    # Add daily 5 credits
    credits_data[user_id]["credits"] += 5
    credits_data[user_id]["last_claim"] = now.strftime("%Y-%m-%d %H:%M")

    with open("credits.json", "w") as f:
        json.dump(credits_data, f, indent=4)

    bot.send_message(call.message.chat.id, f"🎉 𝗗𝗮𝗶𝗹𝘆 𝗴𝗶𝗳𝘁 𝗰𝗹𝗮𝗶𝗺𝗲𝗱! +𝟱 𝗰𝗿𝗲𝗱𝗶𝘁??.\n💳 𝗡𝗲𝘄 𝗯𝗮𝗹𝗮𝗻𝗰𝗲: {credits_data[user_id]['credits']}")


# ——————————— Premium Commands (Subscription Required) ——————————— #
@bot.message_handler(commands=['chk'])
@check_if_banned
@check_maintenance
@check_cooldown
def brinetree_chk_command(message):
    if not gate_status['chk']:
        bot.reply_to(message, "❗️ 𝘁𝗵𝗶𝘀 𝗴𝗮𝘁𝗲𝘄𝗮𝘆 𝗶𝘀 𝗰𝘂𝗿𝗿𝗲𝗻𝘁𝗹𝘆 𝗱𝗶𝘀𝗮𝗯𝗹𝗲𝗱.")
        return
    chat_id = message.chat.id
    try:
        card_details = message.text.split(' ', 1)[1]
        initial_message = bot.reply_to(message, "𝗰𝗵𝗲𝗰𝗸𝗶𝗻𝗴 𝘀𝘁𝗮𝗿𝘁𝗲𝗱, 𝗽𝗹𝗲𝗮𝘀𝗲 𝘄𝗮𝗶𝘁 ⌛")
        edited_message = process_card_b(card_details)[4]
        bot.edit_message_text(chat_id=chat_id, message_id=initial_message.message_id, text=edited_message)
    except IndexError:
        bot.reply_to(message, "⚠️ Correct usage: `/chk [card]`", parse_mode="Markdown")
    except Exception as e:
        bot.send_message(chat_id=chat_id, text="𝗮𝗻 𝗲𝗿𝗿𝗼𝗿 𝗼𝗰𝗰𝘂𝗿𝗿𝗲𝗱: " + str(e))

@bot.message_handler(commands=['pay'])
@check_if_banned
@check_maintenance
@check_cooldown
def paypal_chk_command(message):
    if not gate_status['pay']:
        bot.reply_to(message, "❗️ 𝘁𝗵𝗶𝘀 𝗴𝗮𝘁𝗲𝘄𝗮𝘆 𝗶𝘀 𝗰𝘂𝗿𝗿𝗲𝗻𝘁𝗹𝘆 𝗱𝗶𝘀𝗮𝗯𝗹𝗲𝗱.")
        return

    if message.reply_to_message and message.reply_to_message.document:
        is_subscribed, _ = check_subscription(message.from_user.id)
        if not is_subscribed:
            bot.reply_to(message, "𝘆𝗼𝘂 𝗺𝘂𝘀𝘁 𝗵𝗮𝘃𝗲 𝗮𝗻 𝗮𝗰𝘁𝗶𝘃𝗲 𝘀𝘂𝗯𝘀𝗰𝗿𝗶𝗽𝘁𝗶𝗼𝗻 𝘁𝗼 𝘂𝘀𝗲 𝘁𝗵𝗶𝘀 𝗰𝗼𝗺𝗺𝗮𝗻𝗱.", reply_markup=create_buy_keyboard())
            return
        
        file_info = bot.get_file(message.reply_to_message.document.file_id)
        downloaded_file = bot.download_file(file_info.file_path)

        lines = downloaded_file.decode('utf-8').splitlines()
        results = []
        passed, declined, checked = 0, 0, 0

        mes = types.InlineKeyboardMarkup(row_width=1)
        cm_pass = types.InlineKeyboardButton(f"𝐏𝐚𝐬𝐬𝐞𝐝 ✅ {passed}", callback_data='x')
        cm_decl = types.InlineKeyboardButton(f"𝐃𝐄𝐂𝐋𝐈𝐍𝐄𝐃 ❌ {declined}", callback_data='x')
        cm_stop = types.InlineKeyboardButton(f"𝐒𝐓𝐎𝐏 ⚠️", callback_data='stop')
        mes.add(cm_pass, cm_decl, cm_stop)
        ko = bot.reply_to(message, f"𝐂𝗛𝗘𝗖𝗞𝗜𝗡𝗚 𝗬𝗢𝗨𝗥 𝗖𝗔𝗥𝗗𝗦...⌛\nTotal: {len(lines)}", reply_markup=mes).message_id

        for line in lines:
            checked += 1
            try:
                result = process_card_p(line)
                num = result[3]

                if result[4] and num == 1:
                    passed += 1
                    edited_message = result[4].replace("bin_info", f"═════『 𝗕𝗜𝗡 𝗜𝗡𝗙𝗢 』═════\n{bin_info(result[0])}")
                    results.append(edited_message)
                    bot.send_message(message.chat.id, edited_message)
                else:
                    declined += 1
            except Exception as e:
                declined += 1

            mes = types.InlineKeyboardMarkup(row_width=1)
            cm_pass = types.InlineKeyboardButton(f"𝐏𝐚𝐬𝐬𝐞𝗱 ✅ {passed}", callback_data='x')
            cm_decl = types.InlineKeyboardButton(f"𝐃𝐄𝐂𝐋𝐈𝐍𝐄𝗗 ❌ {declined}", callback_data='x')
            cm_stop = types.InlineKeyboardButton(f"𝐒𝐓𝐎𝐏 ⚠️", callback_data='stop')
            mes.add(cm_pass, cm_decl, cm_stop)

            bot.edit_message_text(
                chat_id=message.chat.id,
                message_id=ko,
                text=f"𝐂𝗛𝗘𝗖𝗞𝗜𝗡𝗚 𝗬𝗢𝗨𝗥 𝗖𝐀𝗥𝗗𝗦...⌛\nTotal: {len(lines)} | Checked: {checked}",
                reply_markup=mes
            )

        temp_file = "Temps/paypal_passed.txt"
        with open(temp_file, "w", encoding="utf-8") as f:
            f.write("\n\n".join(results) if results else "No Passed Cards Found ❌")

        with open(temp_file, "rb") as f:
            bot.send_document(
                message.chat.id, f,
                caption=f"✅ Finished\nTotal: {len(lines)}\nPassed: {passed}\nDeclined: {declined}"
            )

        os.remove(temp_file)

    else:
        try:
            card_details = message.text.split(' ', 1)[1]
            initial_message = bot.reply_to(message, "𝗰𝗵𝗲𝗰𝗸𝗶𝗻𝗴 𝘀𝘁𝗮𝗿𝘁𝗲𝗱...⌛")
            result = process_card_p(card_details)
            final_message_text = ""
            if result[4]:
                final_message_text = result[4].replace("bin_info", f"═════『 𝗕𝗜𝗡 𝗜𝗡𝗙𝗢 』═════\n{bin_info(result[0])}")
            else:
                decline_reason = result[1]
                final_message_text = f"❌ 𝗗𝗲𝗰𝗹𝗶𝗻𝗲𝗱\n\n<b>Card:</b> <code>{card_details}</code>\n<b>Response:</b> {decline_reason}"
            bot.edit_message_text(chat_id=message.chat.id, message_id=initial_message.message_id, text=final_message_text)
        except IndexError:
            bot.reply_to(message, "⚠️ Correct usage: `/pay [card]`", parse_mode="Markdown")
        except Exception as e:
            print(f"Error in single /pay command: {e}")
            bot.send_message(message.chat.id, f"𝗮𝗻 𝗲𝗿𝗿𝗼𝗿 𝗼𝗰𝗰𝘂𝗿𝗿𝗲𝗱: {e}")

@bot.message_handler(commands=['filestr'])
@check_if_banned
@check_maintenance
def stripe_fill_command(message):
    is_subscribed, _ = check_subscription(message.from_user.id)
    if not is_subscribed:
        bot.reply_to(message, "𝘆𝗼𝘂 𝗺𝘂𝘀𝘁 𝗵𝗮𝘃𝗲 𝗮𝗻 𝗮𝗰𝘁𝗶𝘃𝗲 𝘀𝘂𝗯𝘀𝗰𝗿𝗶𝗽𝘁𝗶𝗼𝗻 𝘁𝗼 𝘂𝘀𝗲 𝘁𝗵𝗶𝘀 𝗰𝗼𝗺𝗺𝗮𝗻𝗱.", reply_markup=create_buy_keyboard())
        return

    if not gate_status['filestr']:
        bot.reply_to(message, "❗️ 𝘁𝗵𝗶𝘀 𝗴𝗮𝘁𝗲𝘄𝗮𝘆 𝗶𝘀 𝗰𝘂𝗿𝗿𝗲𝗻𝘁𝗹𝘆 𝗱𝗶𝘀𝗮𝗯𝗹𝗲𝗱.")
        return
    
    bot.reply_to(message,"𝗦𝗲𝗻𝗱 𝗺𝗲 𝘆𝗼𝘂𝗿 𝗰𝗼𝗺𝗯𝗼 𝗳𝗶𝗹𝗲.")
    bot.register_next_step_handler(message, handle_stripe_file)

@bot.message_handler(commands=['file'])
@check_if_banned
@check_maintenance
def brintree_file_command(message):
    is_subscribed, _ = check_subscription(message.from_user.id)
    if not is_subscribed:
        bot.reply_to(message, "𝘆𝗼𝘂 𝗺𝘂𝘀𝘁 𝗵𝗮𝘃𝗲 𝗮𝗻 𝗮𝗰𝘁𝗶𝘷𝗲 𝘀𝘂𝗯𝘀𝗰𝗿𝗶𝗽𝘁𝗶𝗼𝗻 𝘁𝗼 𝘂𝘀𝗲 𝘁𝗵𝗶𝘀 𝗰𝗼𝗺𝗺𝗮𝗻𝗱.", reply_markup=create_buy_keyboard())
        return
        
    if not gate_status['file']:
        bot.reply_to(message, "❗️ 𝘁𝗵𝗶𝘀 𝗴𝗮𝘁𝗲𝘄𝗮𝘆 𝗶𝘀 𝗰𝘂𝗿𝗿𝗲𝗻𝘁𝗹𝘆 𝗱𝗶𝘀𝗮𝗯𝗹𝗲𝗱.")
        return
    bot.reply_to(message,"𝗦𝗲𝗻𝗱 𝗺𝗲 𝘆𝗼𝘂𝗿 𝗰𝗼𝗺𝗯𝗼 𝗳𝗶𝗹𝗲.")
    bot.register_next_step_handler(message, handle_braintree_file)

# ——————————— File Handlers and Callbacks ——————————— #
def handle_stripe_file(message):
    if not bot_working and message.from_user.id != admin_id:
        bot.reply_to(message, "⚠️ 𝗕𝗼𝘁 𝗶𝘀 𝗰𝘂𝗿𝗿𝗲𝗻𝘁𝗹𝘆 𝘂𝗻𝗱𝗲𝗿 𝗺𝗮𝗶𝗻𝘁𝗲𝗻𝗮𝗻𝗰𝗲.")
        return
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
            
            if result[4] and (num == 1 or num == 2):
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




def create_reply_markup_stripe(current_card, num_not_working, num_live, num_working, num_cards_3D_secure, num_insufficient_founds, num_ccn, message_text, All):
    markup = types.InlineKeyboardMarkup()
    checked_count = num_working + num_live + num_insufficient_founds + num_ccn + num_cards_3D_secure + num_not_working
    
    markup.row(types.InlineKeyboardButton(text=f"💳 {current_card} 💳", callback_data="current_card"))
    markup.row(types.InlineKeyboardButton(text=f"⚡ 𝗚𝗮𝘁𝗲: 𝗦𝘁𝗿𝗶𝗽𝗲 | 🧠 {message_text}", callback_data="message"))
    markup.row(
        types.InlineKeyboardButton(text=f"✅ 𝗖𝗵𝗮𝗿𝗴𝗲𝗱: {num_working}", callback_data="working"),
        types.InlineKeyboardButton(text=f"⚡ 𝗟𝗶𝘃𝗲: {num_live}", callback_data="live")
    )
    markup.row(
        types.InlineKeyboardButton(text=f"💰 𝗜𝗻𝘀𝘂𝗳𝗳 𝗙𝘂𝗻𝗱𝘀: {num_insufficient_founds}", callback_data="funds"),
        types.InlineKeyboardButton(text=f"❌ 𝗖𝗖𝗡: {num_ccn}", callback_data="ccn")
    )
    markup.row(
        types.InlineKeyboardButton(text=f"🚫 𝗗𝗲𝗰𝗹𝗶𝗻𝗲𝗱: {num_not_working}", callback_data="declined")
    )
    markup.row(
        types.InlineKeyboardButton(text=f"📊 𝗖𝗵𝗲𝗰𝗸𝗲𝗱: {checked_count}/{All}", callback_data="checked")
    )

    # 🕷️ زر الوقوف VENOM STYLE
    markup.row(types.InlineKeyboardButton(text="〄 𝙎𝙩𝙤𝙥 𝙑𝙀𝙉𝙊𝙈 〄", callback_data="stop"))

    return markup



def handle_braintree_file(message):
    if not bot_working and message.from_user.id != admin_id:
        bot.reply_to(message, "⚠️ 𝗕𝗼𝘁 𝗶𝘀 𝗰𝘂𝗿𝗿𝗲𝗻𝘁𝗹𝘆 𝘂𝗻𝗱𝗲𝗿 𝗺𝗮𝗶𝗻𝘁𝗲𝗻𝗮𝗻𝗰𝗲.")
        return
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

            if result[4] and (num == 1 or num == 2):
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

def create_reply_markup_braintree(current_card, num_not_working, num_live, num_insufficient_founds, num_ccn, message_text, All, num_risk):
    markup = types.InlineKeyboardMarkup()
    checked_count = num_live + num_risk + num_insufficient_founds + num_ccn + num_not_working

    markup.row(types.InlineKeyboardButton(text=f"💳 {current_card} 💳", callback_data="current_card"))
    markup.row(types.InlineKeyboardButton(text=f"⚡ 𝗚𝗮𝘁𝗲: 𝗕𝗿𝗮𝗶𝗻𝘁𝗿𝗲𝗲 | 🧠 {message_text}", callback_data="message"))
    markup.row(
        types.InlineKeyboardButton(text=f"✅ 𝗟𝗶𝘃𝗲: {num_live}", callback_data="live"),
        types.InlineKeyboardButton(text=f"⚠️ 𝗥𝗶𝘀𝗸: {num_risk}", callback_data="risk")
    )
    markup.row(
        types.InlineKeyboardButton(text=f"💰 𝗜𝗻𝘀𝘂𝗳𝗳 𝗙𝘂𝗻𝗱𝘀: {num_insufficient_founds}", callback_data="funds"),
        types.InlineKeyboardButton(text=f"❌ 𝗖𝗖𝗡: {num_ccn}", callback_data="ccn")
    )
    markup.row(
        types.InlineKeyboardButton(text=f"📊 𝗖𝗵𝗲𝗰𝗸𝗲𝗱: {checked_count}/{All}", callback_data="checked")
    )
    markup.row(
        types.InlineKeyboardButton(text=f"🚫 𝗗𝗲𝗰𝗹𝗶𝗻𝗲𝗱: {num_not_working}", callback_data="declined")
    )

    # 🕷️ زر الإيقاف بنمط VENOM
    markup.row(types.InlineKeyboardButton(text="〄 𝙎𝙩𝙤𝙥 𝙑𝙀𝙉𝙊𝙈 〄", callback_data="stop"))

    return markup

    
def handle_paypal_file(message):
    if not bot_working and message.from_user.id != admin_id:
        bot.reply_to(message, "⚠️ 𝗕𝗼𝘁 𝗶𝘀 𝗰𝘂𝗿𝗿𝗲𝗻𝘁𝗹𝘆 𝘂𝗻𝗱𝗲𝗿 𝗺𝗮𝗶𝗻𝘁𝗲𝗻𝗮𝗻𝗰𝗲.")
        return
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
            
            if result[4] and num == 1:
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


def create_reply_markup_paypal(current_card, num_not_working, num_working, num_insufficient_founds, num_ccn, message_text, All, num_risk):
    markup = types.InlineKeyboardMarkup()
    checked_count = num_working + num_risk + num_insufficient_founds + num_ccn + num_not_working

    markup.row(types.InlineKeyboardButton(text=f"💳 {current_card} 💳", callback_data="current_card"))
    markup.row(types.InlineKeyboardButton(text=f"⚡ 𝗚𝗮𝘁𝗲: 𝗣𝗮𝘆𝗣𝗮𝗹 | 🧠 {message_text}", callback_data="message"))
    markup.row(
        types.InlineKeyboardButton(text=f"✅ 𝗣𝗮𝘀𝘀𝗲𝗱: {num_working}", callback_data="live"),
        types.InlineKeyboardButton(text=f"🔐 𝟯𝗗/𝗢𝗧𝗣: {num_risk}", callback_data="risk")
    )
    markup.row(
        types.InlineKeyboardButton(text=f"💰 𝗜𝗻𝘀𝘂𝗳𝗳 𝗙𝘂𝗻𝗱𝘀: {num_insufficient_founds}", callback_data="funds"),
        types.InlineKeyboardButton(text=f"❌ 𝗖𝗖𝗡: {num_ccn}", callback_data="ccn")
    )
    markup.row(
        types.InlineKeyboardButton(text=f"📊 𝗖𝗵𝗲𝗰𝗸𝗲𝗱: {checked_count}/{All}", callback_data="checked")
    )
    markup.row(
        types.InlineKeyboardButton(text=f"🚫 𝗗𝗲𝗰𝗹𝗶𝗻𝗲𝗱: {num_not_working}", callback_data="declined")
    )

    # 🕷️ زر الإيقاف VENOM STYLE
    markup.row(types.InlineKeyboardButton(text="〄 𝙎𝙩𝙤𝙥 𝙑𝙀𝙉𝙊𝙈 〄", callback_data="stop"))

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

# ——————————— NEW MASS CHECK LOGIC (5 CARDS MAX) ——————————— #

# --- Reusable function for Mass Check (5 Cards) ---
def perform_mass_check(message, gate_key, check_function, gate_name):
    """
    Performs a mass check on up to 5 cards provided in a single message.
    """
    if not gate_status[gate_key]:
        bot.reply_to(message, f"❗️ 𝘁𝗵𝗶𝘀 𝗴𝗮𝘁𝗲𝘄𝗮𝘆 ({gate_name}) 𝗶𝘀 𝗰𝘂𝗿𝗿𝗲𝗻𝘁𝗹𝘆 𝗱𝗶𝘀𝗮𝗯𝗹𝗲𝗱.")
        return

    try:
        # Split the message content, get only the lines after the command
        cards_input = message.text.split(maxsplit=1)[1]
        
        # Split the input by newline, space, or comma
        raw_cards = re.split(r'[\n\s,]+', cards_input)
        
        # Filter and count valid-looking cards
        valid_raw_cards = [c.strip() for c in raw_cards if c.strip() and len(c.split('|')) >= 4]
        
        # --- NEW LIMIT CHECK LOGIC (using the requested decorated font) ---
        if len(valid_raw_cards) > 5:
            # 🔴 The requested decorated error message
            error_msg = f"""
❌ 𝗪𝗿𝗼𝗻𝗴 𝗨𝘀𝗮𝗴𝗲!
━━━━━━━━━━━━━━━━━━━━━
⚠️ 𝗬𝗼𝘂 𝗮𝗿𝗲 𝗼𝗻𝗹𝘆 𝗮𝗹𝗹𝗼𝘄𝗲𝗱 𝘁𝗼 𝗰𝗵𝗲𝗰𝗸 𝟱 𝗰𝗮𝗿𝗱𝘀 𝗮𝘁 𝗮 𝘁𝗶𝗺𝗲 𝗳𝗼𝗿 𝘁𝗵𝗶𝘀 𝗰𝗼𝗺𝗺𝗮𝗻𝗱.
📝 𝗬𝗼𝘂 𝘀𝘂𝗯𝗺𝗶𝘁𝘁𝗲𝗱: {len(valid_raw_cards)} 𝗰𝗮𝗿𝗱𝘀.
"""
            bot.reply_to(message, error_msg)
            return
        # --- END NEW LIMIT CHECK ---

        cards_to_check = valid_raw_cards
        
        if not cards_to_check:
            # The usage hint also uses the bold sans-serif style
            bot.reply_to(message, f"❌ 𝗨𝘀𝗮𝗴𝗲: {message.text.split()[0]} 𝗰𝗮𝗿𝗱𝟭|𝗺𝗺|𝘆𝘆|𝗰𝘃𝘃 𝗰𝗮𝗿𝗱𝟮|𝗺𝗺|𝘆𝘆|𝗰𝘃𝘃 ... (𝘂𝗽 𝘁𝗼 𝟱)")
            return
            
    except IndexError:
        bot.reply_to(message, f"❌ 𝗨𝘀𝗮𝗴𝗲: {message.text.split()[0]} 𝗰𝗮𝗿𝗱𝟭|𝗺𝗺|𝘆𝘆|𝗰𝘃𝘃 𝗰𝗮𝗿𝗱𝟮|𝗺𝗺|𝘆𝘆|𝗰𝘃𝘃 ... (𝘂𝗽 𝘁𝗼 𝟱)")
        return

    initial_message = bot.reply_to(message, f"⏳ 𝗖𝗵𝗲𝗰𝗸𝗶𝗻𝗴 {len(cards_to_check)} 𝗰𝗮𝗿𝗱𝘀 𝗼𝗻 {gate_name} 𝗚𝗮𝘁𝗲...")
    
    final_report = f"✅ <b>{gate_name} 𝗠𝗮𝘀𝘀 𝗖𝗵𝗲𝗰𝗸 𝗥𝗲𝗽𝗼𝗿𝘁</b> ✅\n"
    final_report += "━━━━━━━━━━━━━━━━━━━━━\n"
    
    total_checked = 0
    
    for card in cards_to_check:
        try:
            # Check function execution
            if gate_key == 'mass_pay5':
                # PayPal $5 has a different return signature (success, response)
                _, response = check_function(card)
                is_live = "CHARGE" in response
                # Extract the main response part cleanly
                display_response = response.split('\n')[0].replace('✅ ', '').replace('❌ ', '').strip()
            else:
                # Other gates return (bin, response, token_info, num, final_message)
                bin_num, response, _, num, final_message = check_function(card)
                is_live = (num == 1 or num == 2) # Charged or Live
                display_response = response

            status_emoji = "✅" if is_live else "❌"
            
            # Format output for the single card
            final_report += f"{status_emoji} <code>{card}</code> | <b>{display_response}</b>\n"
            total_checked += 1

        except Exception as e:
            final_report += f"⚠️ <code>{card}</code> | <b>𝗘𝗿𝗿𝗼𝗿: {str(e)}</b>\n"
            
        # Update progress message periodically (optional, can be removed to reduce API calls)
        try:
            if total_checked % 1 == 0:
                bot.edit_message_text(
                    chat_id=message.chat.id, 
                    message_id=initial_message.message_id, 
                    text=f"⏳ 𝗖𝗵𝗲𝗰𝗸𝗶𝗻𝗴... 𝗖𝗵𝗲𝗰𝗸𝗲𝗱: {total_checked}/{len(cards_to_check)}"
                )
                time.sleep(1)
        except:
            pass
            
    # Send the final report
    bot.edit_message_text(
        chat_id=message.chat.id, 
        message_id=initial_message.message_id, 
        text=final_report,
        parse_mode="HTML"
    )

# --- Mass Check Stripe (/mass_str) ---
@bot.message_handler(commands=['mass_str'])
@check_if_banned
@check_maintenance
@check_cooldown
def stripe_mass_command(message):
    perform_mass_check(message, 'mass_str', process_card, 'Stripe')

# --- Mass Check Braintree (/mass_chk) ---
@bot.message_handler(commands=['mass_chk'])
@check_if_banned
@check_maintenance
@check_cooldown
def braintree_mass_command(message):
    perform_mass_check(message, 'mass_chk', process_card_b, 'Braintree')

# --- Mass Check PayPal (/mass_pay) ---
@bot.message_handler(commands=['mass_pay'])
@check_if_banned
@check_maintenance
@check_cooldown
def paypal_mass_command(message):
    perform_mass_check(message, 'mass_pay', process_card_p, 'PayPal')

# --- Mass Check PayPal $5 (/mass_pay5) ---
@bot.message_handler(commands=['mass_pay5'])
@check_if_banned
@check_maintenance
@check_cooldown
def paypal5_mass_command(message):
    perform_mass_check(message, 'mass_pay5', process_card_paypal5, 'PayPal $5')

# --- Mass Check Shopify (/mass_sh) ---
@bot.message_handler(commands=['mass_sh'])
@check_if_banned
@check_maintenance
@check_cooldown
def shopify_mass_command(message):
    perform_mass_check_sh(message, 'mass_sh', 'Shopify')

# Shopify needs a slightly different handler due to its function signature
def perform_mass_check_sh(message, gate_key, gate_name):
    if not gate_status[gate_key]:
        bot.reply_to(message, f"❗️ 𝘁𝗵𝗶𝘀 𝗴𝗮𝘁𝗲𝘄𝗮𝘆 ({gate_name}) 𝗶𝘀 𝗰𝘂𝗿𝗿𝗲𝗻𝘁𝗹𝘆 𝗱𝗶𝘀𝗮𝗯𝗹𝗲𝗱.")
        return

    try:
        cards_input = message.text.split(maxsplit=1)[1]
        raw_cards = re.split(r'[\n\s,]+', cards_input)
        valid_raw_cards = [c.strip() for c in raw_cards if c.strip() and len(c.split('|')) >= 4]
        
        if len(valid_raw_cards) > 5:
            # 🔴 The decorated error message
            error_msg = f"""
❌ 𝗪𝗿𝗼𝗻𝗴 𝗨𝘀𝗮𝗴𝗲!
━━━━━━━━━━━━━━━━━━━━━
⚠️ 𝗬𝗼𝘂 𝗮𝗿𝗲 𝗼𝗻𝗹𝘆 𝗮𝗹𝗹𝗼𝘄𝗲𝗱 𝘁𝗼 𝗰𝗵𝗲𝗰𝗸 𝟱 𝗰𝗮𝗿𝗱𝘀 𝗮𝘁 𝗮 𝘁𝗶𝗺𝗲 𝗳𝗼𝗿 𝘁𝗵𝗶𝘀 𝗰𝗼𝗺𝗺𝗮𝗻𝗱.
📝 𝗬𝗼𝘂 𝘀𝘂𝗯𝗺𝗶𝘁𝘁𝗲𝗱: {len(valid_raw_cards)} 𝗰𝗮𝗿𝗱𝘀.
"""
            bot.reply_to(message, error_msg)
            return

        cards_to_check = valid_raw_cards
        if not cards_to_check:
            bot.reply_to(message, f"❌ 𝗨𝘀𝗮𝗴𝗲: {message.text.split()[0]} 𝗰𝗮𝗿𝗱𝟭|𝗺𝗺|𝘆𝘆|𝗰𝘃𝘃 𝗰𝗮𝗿??𝟮|𝗺𝗺|𝘆𝘆|𝗰𝘃𝘃 ... (𝘂𝗽 𝘁𝗼 𝟱)")
            return
            
    except IndexError:
        bot.reply_to(message, f"❌ 𝗨𝘀𝗮𝗴𝗲: {message.text.split()[0]} 𝗰𝗮𝗿𝗱𝟭|𝗺𝗺|𝘆𝘆|𝗰𝘃𝘃 𝗰𝗮𝗿𝗱𝟮|𝗺𝗺|𝘆𝘆|𝗰𝘃𝘃 ... (𝘂𝗽 𝘁𝗼 𝟱)")
        return

    initial_message = bot.reply_to(message, f"⏳ 𝗖𝗵𝗲𝗰𝗸𝗶𝗻𝗴 {len(cards_to_check)} 𝗰𝗮𝗿𝗱𝘀 𝗼𝗻 {gate_name} 𝗚𝗮𝘁𝗲...")
    final_report = f"✅ <b>{gate_name} 𝗠𝗮𝘀𝘀 𝗖𝗵𝗲𝗰𝗸 𝗥𝗲𝗽𝗼𝗿𝘁</b> ✅\n"
    final_report += "━━━━━━━━━━━━━━━━━━━━━\n"
    total_checked = 0
    
    for card in cards_to_check:
        try:
            # Shopify check
            cc, response, is_live = process_card_s(card, token=bot.token, ID=message.chat.id)
            status_emoji = "✅" if is_live else "❌"
            final_report += f"{status_emoji} <code>{card}</code> | <b>{response}</b>\n"
            total_checked += 1
        except Exception as e:
            final_report += f"⚠️ <code>{card}</code> | <b>𝗘𝗿𝗿𝗼𝗿: {str(e)}</b>\n"
        
        try:
            if total_checked % 1 == 0:
                bot.edit_message_text(
                    chat_id=message.chat.id, 
                    message_id=initial_message.message_id, 
                    text=f"⏳ 𝗖𝗵𝗲𝗰𝗸𝗶𝗻𝗴... 𝗖𝗵𝗲𝗰𝗸𝗲𝗱: {total_checked}/{len(cards_to_check)}"
                )
                time.sleep(1)
        except:
            pass

    bot.edit_message_text(chat_id=message.chat.id, message_id=initial_message.message_id, text=final_report, parse_mode="HTML")

# --- Mass Check Braintree Dual Auth (/mass_chk3) ---
@bot.message_handler(commands=['mass_chk3'])
@check_if_banned
@check_maintenance
@check_cooldown
def braintree_dual_mass_command(message):
    perform_mass_check_dual(message, 'mass_chk3', 'Braintree Dual Auth')


def perform_mass_check_dual(message, gate_key, gate_name):
    if not gate_status[gate_key]:
        bot.reply_to(message, f"❗️ 𝘁𝗵𝗶𝘀 𝗴𝗮𝘁𝗲𝘄𝗮𝘆 ({gate_name}) 𝗶𝘀 𝗰𝘂𝗿𝗿𝗲𝗻𝘁𝗹𝘆 𝗱𝗶𝘀𝗮𝗯𝗹𝗲𝗱.")
        return

    try:
        cards_input = message.text.split(maxsplit=1)[1]
        raw_cards = re.split(r'[\n\s,]+', cards_input)
        valid_raw_cards = [c.strip() for c in raw_cards if c.strip() and len(c.split('|')) >= 4]
        
        if len(valid_raw_cards) > 5:
            error_msg = f"""
❌ 𝗪𝗿𝗼𝗻𝗴 𝗨𝘀𝗮𝗴𝗲!
━━━━━━━━━━━━━━━━━━━━━
⚠️ 𝗬𝗼𝘂 𝗮𝗿𝗲 𝗼𝗻𝗹𝘆 𝗮𝗹𝗹𝗼𝘄𝗲𝗱 𝘁𝗼 𝗰𝗵𝗲𝗰𝗸 𝟱 𝗰𝗮𝗿𝗱𝘀 𝗮𝘁 𝗮 𝘁𝗶𝗺𝗲 𝗳𝗼𝗿 𝘁𝗵𝗶𝘀 𝗰𝗼𝗺𝗺𝗮𝗻𝗱.
📝 𝗬𝗼𝘂 𝘀𝘂𝗯𝗺𝗶𝘁𝘁𝗲𝗱: {len(valid_raw_cards)} 𝗰𝗮𝗿𝗱𝘀.
"""
            bot.reply_to(message, error_msg)
            return

        cards_to_check = valid_raw_cards
        if not cards_to_check:
            bot.reply_to(message, f"❌ 𝗨𝘀𝗮𝗴𝗲: {message.text.split()[0]} 𝗰𝗮𝗿𝗱𝟭|𝗺𝗺|𝘆𝘆|𝗰𝘃𝘃 𝗰𝗮𝗿𝗱𝟮|𝗺𝗺|𝘆𝘆|𝗰𝘃𝘃 ... (𝘂𝗽 𝘁𝗼 𝟱)")
            return
            
    except IndexError:
        bot.reply_to(message, f"❌ 𝗨𝘀𝗮𝗴𝗲: {message.text.split()[0]} 𝗰𝗮𝗿𝗱𝟭|𝗺𝗺|𝘆𝘆|𝗰𝘃𝘃 𝗰𝗮𝗿𝗱𝟮|𝗺𝗺|𝘆𝘆|𝗰𝘃𝘃 ... (𝘂𝗽 𝘁𝗼 𝟱)")
        return

    initial_message = bot.reply_to(message, f"⏳ 𝗖𝗵𝗲𝗰𝗸𝗶𝗻𝗴 {len(cards_to_check)} 𝗰𝗮𝗿𝗱𝘀 𝗼𝗻 {gate_name} 𝗚𝗮𝘁𝗲...")
    final_report = f"✅ <b>{gate_name} 𝗠𝗮𝘀𝘀 𝗖𝗵𝗲𝗰𝗸 𝗥𝗲𝗽𝗼𝗿𝘁</b> ✅\n"
    final_report += "━━━━━━━━━━━━━━━━━━━━━\n"
    total_checked = 0
    
    for card in cards_to_check:
        try:
            # ali1 فقط
            is_live, response, _ = ali1(card)
            
            status_emoji = "✅" if is_live else "❌"
            final_report += f"{status_emoji} <code>{card}</code> | <b>{response}</b>\n"
            total_checked += 1
        except Exception as e:
            final_report += f"⚠️ <code>{card}</code> | <b>𝗘𝗿𝗿𝗼𝗿: {str(e)}</b>\n"
        
        try:
            if total_checked % 1 == 0:
                bot.edit_message_text(
                    chat_id=message.chat.id, 
                    message_id=initial_message.message_id, 
                    text=f"⏳ 𝗖𝗵𝗲𝗰𝗸𝗶𝗻𝗴... 𝗖𝗵𝗲𝗰𝗸𝗲𝗱: {total_checked}/{len(cards_to_check)}"
                )
                time.sleep(1)
        except:
            pass

    bot.edit_message_text(chat_id=message.chat.id, message_id=initial_message.message_id, text=final_report, parse_mode="HTML")



#—————–————–———————––———#
# Main polling loop with error handling
#—————–————–———————––———#
if __name__ == '__main__':
    # Notify admin immediately that the script has started
    try:
        bot.send_message(admin_id, "✅ 𝗕𝗼𝘁 𝘀𝗰𝗿𝗶𝗽𝘁 𝘀𝘁𝗮𝗿𝘁𝗲𝗱 𝘀𝘂𝗰𝗰𝗲𝘀𝘀𝗳𝘂𝗹ly.")
    except Exception as e:
        print(f"⚠️ 𝗖𝗼𝘂𝗹𝗱 𝗻𝗼𝘁 𝘀𝗲𝗻𝗱 𝘀𝘁𝗮𝗿𝘁𝘂𝗽 𝗺𝗲𝘀𝘀𝗮𝗴𝗲 𝘁𝗼 𝗮𝗱𝗺𝗶𝗻: {e}")

    # --- Announce to all users that the bot is online ---
    
    # --- Start the bot polling loop ---
    while True:
        try:
            print("▶️ 𝗕𝗼𝘁 𝗶𝘀 𝗿𝘂𝗻𝗻𝗶𝗻𝗴 𝗮𝗻𝗱 𝗹𝗶𝘀𝘁𝗲𝗻𝗶𝗻𝗴 𝗳𝗼𝗿 𝗺𝗲𝘀𝘀𝗮𝗴𝗲𝘀...")
            bot.polling(none_stop=True)
        except Exception as e:
            error_message = f"❗️ 𝗕𝗼𝘁 𝗰𝗿𝗮𝘀𝗵𝗲𝗱 𝘄𝗶𝘁𝗵 𝗲𝗿𝗿𝗼𝗿: {e}\n\n🕒 𝗧𝗶𝗺𝗲: {datetime.now()}"
            print(error_message)
            
            with open("error.txt", "a", encoding='utf-8') as error_file:
                error_file.write(f"{error_message}\n" + "="*50 + "\n")
            
            try:
                bot.send_message(admin_id, error_message)
            except Exception as admin_notify_error:
                print(f"⚠️ 𝗖𝗼𝘂𝗹𝗱 𝗻𝗼𝘁 𝗻𝗼𝘁𝗶𝗳𝘆 𝗮𝗱𝗺𝗶𝗻: {admin_notify_error}")
            time.sleep(5)
