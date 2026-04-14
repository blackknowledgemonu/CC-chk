# File: second_script.py
import requests

def GetStr(string, start, end):
    string = ' ' + string
    ini = string.find(start)
    if ini == -1:
        return ''
    ini += len(start)
    end_idx = string.find(end, ini)
    if end_idx == -1:
        return ''
    return string[ini:end_idx].strip()

def check_key(sk):
    skval = '100'

    data = {
       "card[number]": "5278540001668044",
       "card[exp_month]": "10",
       "card[exp_year]": "2029",
       "card[cvc]": "252"
    }
    headers = {
        "Content-Type": "application/x-www-form-urlencoded"
    }
    auth = (sk, '')

    response1 = requests.post('https://api.stripe.com/v1/tokens', data=data, headers=headers, auth=auth)
    r1 = response1.text
    msg = GetStr(r1, '"message": "', '"')

    response2 = requests.get('https://api.stripe.com/v1/balance', auth=auth)
    r2 = response2.text

    currn = GetStr(r2, '"currency": "', '"')
    balance = GetStr(r2, '"amount":', ',')
    pending = GetStr(r2, '"pending": [{\n      "amount":', ',')
    if not pending:
        pending = GetStr(r2, '"livemode": true,\n  "pending": [\n    {\n      "amount":', ',')
    
    if pending:
        try:
            pending = float(pending) / float(skval)
        except ValueError:
            pending = 0
    
    if 'usd' in r2:
        currn = '$'
        currf = '🇺🇸'
        currs = 'USD'
    elif 'inr' in r2:
        currn = '₹'
        currf = '🇮🇳'
        currs = 'INR'
    elif 'cad' in r2:
        currn = '$'
        currf = '🇨🇦'
        currs = 'CAD'
    elif 'aud' in r2:
        currn = 'A$'
        currf = '🇦🇺'
        currs = 'AUD'
    elif 'aed' in r2:
        currn = 'د.إ'
        currf = '🇦🇪'
        currs = 'AED'
    elif 'sgd' in r2:
        currn = 'S$'
        currf = '🇸🇬'
        currs = 'SGD'
    elif 'nzd' in r2:
        currn = '$'
        currf = '🇳🇿'
        currs = 'NZD'
    elif 'eur' in r2:
        currn = '€'
        currf = '🇪🇺'
        currs = 'EUR'
    elif 'gbp' in r2:
        currn = '£'
        currf = '🇬🇧'
        currs = 'GBP'
    else:
        currn = 'N/A'
        currf = 'N/A'
        currs = currn

    if "rate_limit" in r1:
        result = f"Result:⚠️ RATE LIMIT\n\nKEY : {sk}\nRESPONSE : Request rate limit exceeded.\nBALANCE : {balance} {currn}\nPENDING AMOUNT : {pending} {currn}\nCURRENCY : {currs} {currf} "
    elif "tok" in r1 or "Your card was declined." in r1:
        result = f"Result:✅ LIVE KEY\n\nKEY : {sk}\nRESPONSE : Your card was declined.\nBALANCE : {balance} {currn}\nPENDING AMOUNT : {pending} {currn}\nCURRENCY : {currs} {currf} "
    elif "Invalid API Key provided" in r1:
        result = f"Result:❌ INVALID KEY\n\nKEY : {sk}\nRESPONSE : Invalid API Key Provided."
    elif "testmode_charges_only" in r1:
        result = f"Result:❌ DEAD KEY\n\nKEY : {sk}\nRESPONSE : Your account cannot currently make live charges.\nBALANCE : {balance} {currn}\nPENDING AMOUNT : {pending} {currn}\nCURRENCY : {currs} {currf} "
    elif "api_key_expired" in r1:
        result = f"Result:❌ EXPIRED KEY\n\nKEY : {sk}\nRESPONSE : Expired API Key Provided."
    else:
        result = f"Result:⚠️ RESPONSE NOT LISTED\n\nKEY : {sk}\nRESPONSE : {msg}\nBALANCE : {balance} {currn}\nPENDING AMOUNT : {pending} {currn}\nCURRENCY : {currs} {currf} "

    return result
