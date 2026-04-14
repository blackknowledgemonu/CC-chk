import requests

cookies = {
    '__stripe_mid': 'daf5700c-2b84-4ef4-8c52-e73c93895a2729e77c',
    '__stripe_sid': 'e3fcecb4-effb-4d58-b9e6-152fc82c6e18a37321',
    'cookieyes-consent': 'consentid:blJRdzl0TFZ3SEFZZ2hwS29HOWtZTVZYRHhiQUpHVUQ,consent:no,action:yes,necessary:yes,functional:no,analytics:no,performance:no,advertisement:no,other:no',
    'fd-form-66a7b27718e5f771eb0ba3b3-dismissed-count': '1',
}

headers = {
    'authority': 'www.caringforgodsacre.org.uk',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
    'cache-control': 'max-age=0',
    'content-type': 'multipart/form-data; boundary=----WebKitFormBoundaryyQoxKucWBRl7gBCA',
    # 'cookie': '__stripe_mid=daf5700c-2b84-4ef4-8c52-e73c93895a2729e77c; __stripe_sid=e3fcecb4-effb-4d58-b9e6-152fc82c6e18a37321; cookieyes-consent=consentid:blJRdzl0TFZ3SEFZZ2hwS29HOWtZTVZYRHhiQUpHVUQ,consent:no,action:yes,necessary:yes,functional:no,analytics:no,performance:no,advertisement:no,other:no; fd-form-66a7b27718e5f771eb0ba3b3-dismissed-count=1',
    'origin': 'https://www.caringforgodsacre.org.uk',
    'referer': 'https://www.caringforgodsacre.org.uk/product/the-burial-ground-botanical-companion/',
    'sec-ch-ua': '"Chromium";v="139", "Not;A=Brand";v="99"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Mobile Safari/537.36',
}

files = {
    'quantity': (None, '1'),
    'add-to-cart': (None, '990'),
}

response = requests.post(
    'https://www.caringforgodsacre.org.uk/product/the-burial-ground-botanical-companion/',
    cookies=cookies,
    headers=headers,
    files=files,
)


cookies = {
    '__stripe_mid': 'daf5700c-2b84-4ef4-8c52-e73c93895a2729e77c',
    '__stripe_sid': 'e3fcecb4-effb-4d58-b9e6-152fc82c6e18a37321',
    'cookieyes-consent': 'consentid:blJRdzl0TFZ3SEFZZ2hwS29HOWtZTVZYRHhiQUpHVUQ,consent:no,action:yes,necessary:yes,functional:no,analytics:no,performance:no,advertisement:no,other:no',
    'fd-form-66a7b27718e5f771eb0ba3b3-dismissed-count': '1',
    'woocommerce_items_in_cart': '1',
    'woocommerce_cart_hash': 'eff1fa865ba122b7128ea6727ed9f143',
    'wordpress_logged_in_c535aa967722b52995bfcebf2955ee6b': 'marsha.rose08%7C1757078889%7CjrWXT0p570ArdyrcPkjridehvHmFTADfgkCDw1LIqBb%7C4dcab4d1b3b315cc6617b71a41d0a7398d6c218b1564aa463fdf3af53b1f43a4',
    'wp_woocommerce_session_c535aa967722b52995bfcebf2955ee6b': '1316%7C1756041570%7C1755955170%7C%24generic%24kainPJoo-a_0jgswkoUik6YVGUFRsZLLxOLrpmJe',
}

headers = {
    'authority': 'www.caringforgodsacre.org.uk',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
    # 'cookie': '__stripe_mid=daf5700c-2b84-4ef4-8c52-e73c93895a2729e77c; __stripe_sid=e3fcecb4-effb-4d58-b9e6-152fc82c6e18a37321; cookieyes-consent=consentid:blJRdzl0TFZ3SEFZZ2hwS29HOWtZTVZYRHhiQUpHVUQ,consent:no,action:yes,necessary:yes,functional:no,analytics:no,performance:no,advertisement:no,other:no; fd-form-66a7b27718e5f771eb0ba3b3-dismissed-count=1; woocommerce_items_in_cart=1; woocommerce_cart_hash=eff1fa865ba122b7128ea6727ed9f143; wordpress_logged_in_c535aa967722b52995bfcebf2955ee6b=marsha.rose08%7C1757078889%7CjrWXT0p570ArdyrcPkjridehvHmFTADfgkCDw1LIqBb%7C4dcab4d1b3b315cc6617b71a41d0a7398d6c218b1564aa463fdf3af53b1f43a4; wp_woocommerce_session_c535aa967722b52995bfcebf2955ee6b=1316%7C1756041570%7C1755955170%7C%24generic%24kainPJoo-a_0jgswkoUik6YVGUFRsZLLxOLrpmJe',
    'referer': 'https://www.caringforgodsacre.org.uk/basket/',
    'sec-ch-ua': '"Chromium";v="139", "Not;A=Brand";v="99"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Mobile Safari/537.36',
}

response = requests.get('https://www.caringforgodsacre.org.uk/checkout/', cookies=cookies, headers=headers)


headers = {
    'authority': 'api.stripe.com',
    'accept': 'application/json',
    'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
    'content-type': 'application/x-www-form-urlencoded',
    'origin': 'https://js.stripe.com',
    'referer': 'https://js.stripe.com/',
    'sec-ch-ua': '"Chromium";v="139", "Not;A=Brand";v="99"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Mobile Safari/537.36',
}

data = 'billing_details[name]=Marsha+Rose&billing_details[email]=ronald.ramire%40telegmail.com&billing_details[phone]=%2B44+7911+123456&billing_details[address][city]=Manchester&billing_details[address][country]=GB&billing_details[address][line1]=14+King+Street&billing_details[address][line2]=&billing_details[address][postal_code]=M2+4WU&billing_details[address][state]=Greater+Manchester&type=card&card[number]=5524+6100+0076+8145&card[cvc]=076&card[exp_year]=31&card[exp_month]=01&allow_redisplay=unspecified&payment_user_agent=stripe.js%2F6671a0211f%3B+stripe-js-v3%2F6671a0211f%3B+payment-element%3B+deferred-intent&referrer=https%3A%2F%2Fwww.caringforgodsacre.org.uk&time_on_page=78295&client_attribution_metadata[client_session_id]=437f8e08-8e54-497c-b6bb-e7504ad9cf17&client_attribution_metadata[merchant_integration_source]=elements&client_attribution_metadata[merchant_integration_subtype]=payment-element&client_attribution_metadata[merchant_integration_version]=2021&client_attribution_metadata[payment_intent_creation_flow]=deferred&client_attribution_metadata[payment_method_selection_flow]=merchant_specified&client_attribution_metadata[elements_session_config_id]=76ac23ee-03cb-49b3-ba2e-17dd05a235d0&guid=3e482fd5-f2dc-45c3-a7e3-f701ca45cebdf7ba0c&muid=daf5700c-2b84-4ef4-8c52-e73c93895a2729e77c&sid=e3fcecb4-effb-4d58-b9e6-152fc82c6e18a37321&key=pk_live_2QnqLoJqhYrHePqQ9TUyjld2&_stripe_version=2024-06-20&radar_options[hcaptcha_token]=P1_eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJwZCI6MCwiZXhwIjoxNzU1ODY5NTExLCJjZGF0YSI6IlNyOHhpK3l6Skp0a0wyb3NaZ3dZaXpsT2VOajlXbEFQc1k1dW9pR2ZZMzBKR3RTRFZTNlQxNS9tYjFlR0NTOUgxbnE0RWhoUnBTWjZoNmY5cXk2eE9XaGp0TjVyN2xBa3V5dGovRytUOVpDQ05LTUpmT2J2MFptcE9JSjBqZThCN2VwNWxrTEpQRmlKWUpHTEw3ZWk3Yk1rc0I3Q1gyRGMyaHRLYitkdEd4VFdUS2o5UkxoSS91dm45WXIvZW1KZ2drVGM2SmRrRXpKZjRrYnQiLCJwYXNza2V5IjoiK0pjZXR3aldGazlzSzFYVFNhYk9PbU96RVNrQUlsZW0vbEtaa2crRFhXTTNhVTUrMWxaTVNlR3V3OXU3dDlpMkhGMDdwR1RjbGJ4SjFtVURTVi9zQzA4cklONWp5Y0Y2b3hlQUtHNWRXSmwvZFpzN2R0ZWxvcUw2cW53QnpBd1VFQ0V3U1BlL201MG5ZNDEzekhIOHUxZmwrOFFkNC92V1dkMDFaZHhRQXZOUWMxWXJEcUwycEI2N3NYS2twZ3g3YXB6QkFaR05yb0F4Z1VPSEp2TUpBaEJwWUhibXlacGJ3OG80U2kyN2ZjaWVzMStnYXdhdGg0MllzZ2NadHJxUjZXQVgvYlU2dnZTdWdOdWh2bitKTzI4a05yTVBsL1VBWlVPcVYya3AxaWZ0ZVZDRTlPYU9GMXZKekRHR2FtUjAwcVR3SllQWUg4LzlwV2Z1dGVybXg0WWhNK21IVzI5T3RZdWpVMUp3RTJ5dnBVNFUxK3NrNWltTnJscWtFSExNVE90bDRRZDBlZ1JhekJFYmZSeG1QNHV2Zi9qNUFpNVFkbUttRUQwdDByb2d0bmdJbkxtZkJYOG52TjZYWXFnR2tXczBmZ3VzS3EyNHZMWXlMQjlmUlNiV3ZJOVovNWJTQ2d1U0x0UFh5WWlzekxJaVUvcWpKZy9pcE90WjFXTDF3ZGsxdW93a0h6U2M1WldESnhLVUxsN0c4U3J5dEFrb3hnTzNhN2ZkRTlEMkI5cGxlWUpKWmpneXZyaTdBdDBWa1g5V1pQRHgzUHB5UTl0UEcxVHloWU9oN0xTL0VzVHk0YkJoZTRBbHpvZjVaYitoM1FEYnE4amNwYmk5ODZPaDYzZzMvazRZNmVZcVIxVlpVQ0wrZnd0MFR0Qll5amN3YktZODBHSEJDMFVoL0I2SXZoZHFWQllhY3plamN2QldiMXlTN0xBZDZoM1VsMThUTEd2SEY0T25YbFZ6bklPL3V3S3hSRmo2bGt4Vk1PdWF5NTllcTFvUVpZNzhKZm1CZFBqbmV3MDdpZStnYWlIUnp1dDhjRDhsSmhCK1ZCbnhsM1ltZXlxL2RhWENKeHRZbGYzY2lLQ3lIVEFzY0FsbzhkRGFRY3dUY244N21GQlUwOEZqNUdaZ0hnenh5Z2RtM0Z3QlRoVk1uNThIT1U3TUFqLzFSMjJlRzRvZU9YRTM4djFPTUQrTXVBbTZMUHpWWG5wSWJjMk9KRUZLWE1kK3BBemY1dGdGdTRRb21JT1JSS1RPK2J6ZUhqaS9jVDYySTdhU1U1NkFDVGFleHJTM0V5c3RqdHpkRTB1K2UxWGxVUWZDK3JXdFZSaTNSSytpenNqS3pYM3ZtRFdTVmJyR2NmTER0SExuQVpldjQ0R0pzV3Z2NEhnT3JUbWRETzlGalBJWU5xZlNFQWhTOU92d1BwT2ZGbGQ3dmxaSmc4ZFgzNERWWmdXT2RvNlQ3RnpWdUxxSFMzS0dScDBIakpJdHF0NlVMZ1lNR3BIUkw2b2tSSnMrNHBDamFTOVgyTlcrdGNWcDlsem12WUhiTk9PVnJsUGt3cTJablBzUnpSV0lYdnhQSml4KzZNRTFQMTVzU1ZFRWl5cS9XblE3TXNmY2FVREF0ekc3b2hQMzhqVEtEZ254eWNNMWg5cHZMb1JkakV2MzBVL1YyZy95STBPTmJLSnpSUU1qZW9JcXVsQlZleW1KUmRVV005VFRYRzF3NVJHbEtLQXhYemFnYkZKM2lmeXhwbEkyTHhWVWRpQ05XVjQrUFoxbUhxaG9pOXdxdnVvWGhHWStLZWY1OXg3VlpUcmV0K2FONkp4Y3VZM2xtMFJEWlVDUXk5MExIOG9xRTVyTG5UbDN1bWx1d1JJRVI5M2c4WGs3WDJwc0lIdVFwNldlTkgvb3NabTZBL2FOV01rWGRLbStIUkYxMWh6N3MxRlJvalkyMTk2MStHeW5BcHhzVUlaM1JQQW5odUF5ZWdqRDdURTBTK3NGME9YbG82M0dnYUI1dUhTdmY4ekhMdUl5dHRNMHhXWnJrbW1uSXJVdWVZc3FQRHdsYnF0Zm5sRjk0V0dBZHhmYkVsTDkraXdFQXRoeTNzaFN2NUNiRzhEL1p6U2ZKVUtEZFZWcXA1Q1VOY2ZlR1Y1MlJaUUJQY2Y3dXhGMTZSYU9uRGpxeE4rMm8zL2lLNFJFeXJDNGVyRE1qM2NxUFRHVllQdkdFcCt1OTZybzBCQk9VditXMXlXdTh2ZUEzaEc4Z2cxTEw5NW15QnlTTmdyMkdkVzZRK2tiTG44bStPV3RJRjVGRjlTL3dVVHNiQT09Iiwia3IiOiI5YTM3NGFhIiwic2hhcmRfaWQiOjUzNTc2NTU5fQ.-EaIXkYn5H2xpx_zC2yesJOyoCBscWogfj7c3WR8W0U'

response = requests.post('https://api.stripe.com/v1/payment_methods', headers=headers, data=data)


cookies = {
    '__stripe_mid': 'daf5700c-2b84-4ef4-8c52-e73c93895a2729e77c',
    '__stripe_sid': 'e3fcecb4-effb-4d58-b9e6-152fc82c6e18a37321',
    'cookieyes-consent': 'consentid:blJRdzl0TFZ3SEFZZ2hwS29HOWtZTVZYRHhiQUpHVUQ,consent:no,action:yes,necessary:yes,functional:no,analytics:no,performance:no,advertisement:no,other:no',
    'fd-form-66a7b27718e5f771eb0ba3b3-dismissed-count': '1',
    'woocommerce_items_in_cart': '1',
    'wordpress_logged_in_c535aa967722b52995bfcebf2955ee6b': 'marsha.rose08%7C1757078889%7CjrWXT0p570ArdyrcPkjridehvHmFTADfgkCDw1LIqBb%7C4dcab4d1b3b315cc6617b71a41d0a7398d6c218b1564aa463fdf3af53b1f43a4',
    'wp_woocommerce_session_c535aa967722b52995bfcebf2955ee6b': '1316%7C1756041570%7C1755955170%7C%24generic%24kainPJoo-a_0jgswkoUik6YVGUFRsZLLxOLrpmJe',
    'woocommerce_cart_hash': '04d2b61a9582da047728bd1a462ec473',
}

headers = {
    'authority': 'www.caringforgodsacre.org.uk',
    'accept': 'application/json, text/javascript, */*; q=0.01',
    'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    # 'cookie': '__stripe_mid=daf5700c-2b84-4ef4-8c52-e73c93895a2729e77c; __stripe_sid=e3fcecb4-effb-4d58-b9e6-152fc82c6e18a37321; cookieyes-consent=consentid:blJRdzl0TFZ3SEFZZ2hwS29HOWtZTVZYRHhiQUpHVUQ,consent:no,action:yes,necessary:yes,functional:no,analytics:no,performance:no,advertisement:no,other:no; fd-form-66a7b27718e5f771eb0ba3b3-dismissed-count=1; woocommerce_items_in_cart=1; wordpress_logged_in_c535aa967722b52995bfcebf2955ee6b=marsha.rose08%7C1757078889%7CjrWXT0p570ArdyrcPkjridehvHmFTADfgkCDw1LIqBb%7C4dcab4d1b3b315cc6617b71a41d0a7398d6c218b1564aa463fdf3af53b1f43a4; wp_woocommerce_session_c535aa967722b52995bfcebf2955ee6b=1316%7C1756041570%7C1755955170%7C%24generic%24kainPJoo-a_0jgswkoUik6YVGUFRsZLLxOLrpmJe; woocommerce_cart_hash=04d2b61a9582da047728bd1a462ec473',
    'origin': 'https://www.caringforgodsacre.org.uk',
    'referer': 'https://www.caringforgodsacre.org.uk/checkout/',
    'sec-ch-ua': '"Chromium";v="139", "Not;A=Brand";v="99"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Mobile Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
}

params = {
    'wc-ajax': 'checkout',
}

data = {
    'wc_order_attribution_source_type': '',
    'wc_order_attribution_referrer': '',
    'wc_order_attribution_utm_campaign': '',
    'wc_order_attribution_utm_source': '',
    'wc_order_attribution_utm_medium': '',
    'wc_order_attribution_utm_content': '',
    'wc_order_attribution_utm_id': '',
    'wc_order_attribution_utm_term': '',
    'wc_order_attribution_utm_source_platform': '',
    'wc_order_attribution_utm_creative_format': '',
    'wc_order_attribution_utm_marketing_tactic': '',
    'wc_order_attribution_session_entry': '',
    'wc_order_attribution_session_start_time': '',
    'wc_order_attribution_session_pages': '',
    'wc_order_attribution_session_count': '',
    'wc_order_attribution_user_agent': '',
    'billing_first_name': 'Marsha',
    'billing_last_name': 'Rose',
    'billing_company': '',
    'billing_country': 'GB',
    'billing_address_1': '14 King Street',
    'billing_address_2': '',
    'billing_city': 'Manchester',
    'billing_state': 'Greater Manchester',
    'billing_postcode': 'M2 4WU',
    'billing_phone': '+44 7911 123456',
    'billing_email': 'ronald.ramire@telegmail.com',
    'shipping_first_name': '',
    'shipping_last_name': '',
    'shipping_company': '',
    'shipping_country': 'GB',
    'shipping_address_1': '',
    'shipping_address_2': '',
    'shipping_city': '',
    'shipping_state': '',
    'shipping_postcode': '',
    'order_comments': '',
    'shipping_method[0]': 'table_rate:4',
    'payment_method': 'stripe',
    'wc-stripe-payment-method-upe': '',
    'wc_stripe_selected_upe_payment_type': '',
    'wc-stripe-is-deferred-intent': '1',
    'terms': 'on',
    'terms-field': '1',
    'woocommerce-process-checkout-nonce': '69cc2c65f9',
    '_wp_http_referer': '/?wc-ajax=update_order_review',
    'wc-stripe-payment-method': 'pm_1Ryv3LLEW73XPfgfBtx23AGE',
}

response = requests.post('https://www.caringforgodsacre.org.uk/', params=params, cookies=cookies, headers=headers, data=data)

print(response.json())