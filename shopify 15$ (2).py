# bot_venom_encryptor.py
# 𝗘𝗻𝗰𝗿𝘆𝗽𝘁𝗲𝗱 𝗯𝘆 𝗩𝗲𝗻𝗼𝗺 ✅
# Telegram Encryption Bot (Simple/Strong) + Expiry by Hours

import io
import os
import base64
import textwrap
from datetime import datetime, timedelta
from telegram import Update, InputFile, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (
    ApplicationBuilder, CommandHandler, CallbackQueryHandler,
    MessageHandler, ContextTypes, filters
)

# === Your Telegram Bot Token ===
BOT_TOKEN = "7040898503:AAGHQ-8s55l3SELZexgVYk2p94utaXdS4ng"

# ---------- Helpers ----------
def chunk_string(s: str, size: int = 2000):
    return [s[i:i+size] for i in range(0, len(s), size)]

def make_expiry_snippet(expiry_dt: datetime) -> bytes:
    """Generate an expiry check snippet to embed in encrypted code."""
    expiry_str = expiry_dt.strftime("%Y-%m-%d %H:%M:%S")
    snippet = textwrap.dedent(f'''
    # --- Auto Expiry Check ---
    import datetime
    now = datetime.datetime.now()
    expiry = datetime.datetime.strptime("{expiry_str}", "%Y-%m-%d %H:%M:%S")
    if now > expiry:
        print("❌ Tool expired. Contact the developer to renew access.")
        raise SystemExit(1)
    # --- End Expiry ---
    ''')
    return snippet.encode("utf-8")

# ---------- Simple HEX Encryption ----------
def build_simple_encryption(original_bytes: bytes, expiry_dt: datetime | None) -> bytes:
    if expiry_dt:
        original_bytes = make_expiry_snippet(expiry_dt) + b"\n" + original_bytes

    hexstr = original_bytes.hex()
    chunks = chunk_string(hexstr, 2000)
    lines = [
        "# -*- coding: utf-8 -*-",
        "# 𝗘𝗻𝗰𝗿𝘆𝗽𝘁𝗲𝗱 𝗯𝘆 𝗩𝗲𝗻𝗼𝗺 ✅",
        "import codecs",
        "hex_chunks = ["
    ]
    for c in chunks:
        lines.append(f'    "{c}",')
    lines += [
        "]",
        'full_hex = "".join(hex_chunks)',
        'decoded = codecs.decode(full_hex, "hex")',
        'try:',
        '    src = decoded.decode("utf-8")',
        'except Exception:',
        '    src = decoded.decode("latin-1")',
        'exec(src, globals(), globals())'
    ]
    return "\n".join(lines).encode("utf-8")

# ---------- Strong AES/Fernet Encryption ----------
def build_strong_encryption(original_bytes: bytes, expiry_dt: datetime | None) -> bytes:
    if expiry_dt:
        original_bytes = make_expiry_snippet(expiry_dt) + b"\n" + original_bytes
    try:
        from cryptography.fernet import Fernet
    except Exception:
        raise RuntimeError("Missing library: run `pip install cryptography`")

    key = Fernet.generate_key()
    f = Fernet(key)
    encrypted = f.encrypt(original_bytes)
    b64_enc = base64.b64encode(encrypted).decode("ascii")
    chunks = chunk_string(b64_enc, 2000)

    wrapper_lines = [
        "# -*- coding: utf-8 -*-",
        "# 𝗘𝗻𝗰𝗿𝘆𝗽𝘁𝗲𝗱 𝗯𝘆 𝗩𝗲𝗻𝗼𝗺 ✅",
        "import base64",
        "from cryptography.fernet import Fernet",
        f"key = {repr(key)}",
        "data_chunks = ["
    ]
    for c in chunks:
        wrapper_lines.append(f'    "{c}",')
    wrapper_lines += [
        "]",
        'data_b64 = "".join(data_chunks)',
        'encrypted = base64.b64decode(data_b64)',
        'src = Fernet(key).decrypt(encrypted)',
        'exec(src, globals(), globals())'
    ]
    return "\n".join(wrapper_lines).encode("utf-8")

# ---------- Telegram Bot Handlers ----------
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("⚙️ Simple Encryption", callback_data="simple")],
        [InlineKeyboardButton("🛡️ Strong Encryption (AES/Fernet)", callback_data="strong")],
        [InlineKeyboardButton("⏱️ Set Expiry (Hours)", callback_data="set_hours")]
    ]
    await update.message.reply_text(
        "Welcome to Venom Encryptor 🕷️\n\n"
        "Choose your encryption mode or set expiry time in hours:",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )

async def choose_mode(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    mode = query.data
    if mode == "set_hours":
        context.user_data["awaiting_hours"] = True
        await query.edit_message_text(
            "⏱️ Send the number of hours the encrypted file should stay active.\n"
            "Example: `3` → the tool expires 3 hours after encryption.\n"
            "Type `cancel` to skip expiry.",
            parse_mode="Markdown"
        )
        return
    context.user_data["mode"] = mode
    if mode == "strong":
        await query.edit_message_text("🛡️ Strong encryption selected. Send a `.py` file to encrypt (requires `cryptography`).")
    else:
        await query.edit_message_text("⚙️ Simple encryption selected. Send a `.py` file to encrypt.")

async def handle_text(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not context.user_data.get("awaiting_hours"):
        return
    text = update.message.text.strip().lower()
    if text == "cancel":
        context.user_data.pop("awaiting_hours", None)
        context.user_data.pop("expiry_hours", None)
        await update.message.reply_text("✅ Expiry setting canceled.")
        return
    try:
        hrs = int(text)
        if hrs <= 0:
            raise ValueError
        context.user_data["expiry_hours"] = hrs
        context.user_data.pop("awaiting_hours", None)
        await update.message.reply_text(f"✅ Expiry set: {hrs} hour(s) from encryption time.\nNow send your `.py` file to encrypt.")
    except Exception:
        await update.message.reply_text("❌ Invalid input. Send a positive number (e.g. `3`) or `cancel`.", parse_mode="Markdown")

async def handle_file(update: Update, context: ContextTypes.DEFAULT_TYPE):
    doc = update.message.document
    if not doc or not doc.file_name.endswith(".py"):
        await update.message.reply_text("❌ Please send a valid `.py` file.")
        return

    mode = context.user_data.get("mode", "simple")
    expiry_hours = context.user_data.get("expiry_hours")
    await update.message.reply_text(f"🔁 Encrypting file ({'Strong' if mode=='strong' else 'Simple'}) ...")

    file = await doc.get_file()
    data = await file.download_as_bytearray()
    original_bytes = bytes(data)

    expiry_dt = None
    if expiry_hours:
        expiry_dt = datetime.now() + timedelta(hours=int(expiry_hours))

    try:
        if mode == "strong":
            wrapped = build_strong_encryption(original_bytes, expiry_dt)
            out_name = os.path.splitext(doc.file_name)[0] + "_enc_strong.py"
        else:
            wrapped = build_simple_encryption(original_bytes, expiry_dt)
            out_name = os.path.splitext(doc.file_name)[0] + "_enc_simple.py"
    except Exception as e:
        await update.message.reply_text(f"❌ Encryption failed:\n{e}")
        return

    bio = io.BytesIO(wrapped)
    bio.name = out_name
    caption = "✅ Encrypted successfully!\n# 𝗘𝗻𝗰𝗿𝘆𝗽𝘁𝗲𝗱 𝗯𝘆 𝗩𝗲𝗻𝗼𝗺 ✅"
    if expiry_dt:
        caption += f"\n⏱️ Active until: {expiry_dt.strftime('%Y-%m-%d %H:%M:%S')}"
    if mode == "strong":
        caption += "\n⚠️ Requires `cryptography` to run."

    await update.message.reply_document(InputFile(bio, filename=out_name), caption=caption)

# ---------- Main ----------
def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(choose_mode))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_text))
    app.add_handler(MessageHandler(filters.Document.ALL, handle_file))
    print("🚀 Venom Encryptor is running — send /start in Telegram.")
    app.run_polling()

if __name__ == "__main__":
    main()
