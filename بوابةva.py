import requests

cookies = {
    'fornax_anonymousId': 'b412d695-041a-4e8f-a128-48bd210cd6e3',
    'SHOP_SESSION_TOKEN': 'aa5e3332-2358-4c49-834c-3ee6a991cd65',
    'poptin_old_user': 'true',
    'poptin_user_id': '0.yy9q0bwo8q8',
    '_privy_ACC4BAB260C967EC17DF0711': '%7B%22uuid%22%3A%227b300534-d5da-4980-9770-9705921be178%22%7D',
    'STORE_VISITOR': '1',
    'poptin_user_country_code': 'false',
    'poptin_user_ip': '197.32.61.255',
    'poptin_c_visitor': 'true',
    'poptin_session_account_89e2702db1c96': 'true',
    'poptin_last_visit': '2025-09-24',
    'bigcommerce_recently_viewed': '153',
    'SHOP_SESSION_ROTATION_TOKEN': 'c6278d83480c751c5a15159b6b31d1db6c821e7385ecd143e5a71f903336d8ca',
    'SF-CSRF-TOKEN': '1b1a2935-401b-4134-9dec-d5862cf5cda7',
    'XSRF-TOKEN': '1135afab7fdcf293311fc781552333a522a0fce40ea5832b7cb81f87420c0d63',
    '__cf_bm': 'MvZYsPmaIe4Inb7yCc71DOD5Va.gHfrmggLLaax6m7Q-1758756470-1.0.1.1-zgAtTAgui34ws.QWFieeQ2l0_H.gA9n3y1MLElTSrnlvOZ.TMHdydZwvt0tvCHaUJFu53uuwZRttcZ_6iidYsPNIOG0vCruzDP8ra11_mQA',
    'athena_short_visit_id': 'a7f1776c-5eab-420b-8df3-3540ddd83dd3:1758756470',
    'poptin_session': 'true',
    'poptin_referrer_protocol': 'secure',
    'poptin_referrer': 'greatlakespetfood.com/login.php',
    'Shopper-Pref': '721AD7308941DD9B42C137F4EF529AE1582EBA85-1759361339304-x%7B%22cur%22%3A%22USD%22%2C%22funcConsent%22%3Atrue%7D',
}

headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9',
    'cache-control': 'max-age=0',
    'content-type': 'application/x-www-form-urlencoded',
    'origin': 'https://greatlakespetfood.com',
    'priority': 'u=0, i',
    'referer': 'https://greatlakespetfood.com/login.php?action=create_account',
    'sec-ch-ua': '"Chromium";v="140", "Not=A?Brand";v="24", "Google Chrome";v="140"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36',
}

params = {
    'action': 'save_new_account',
}

data = {
    'FormField[1][1]': 'sasa0100m@gmail.com',
    'FormField[1][2]': 'copra0100',
    'FormField[1][3]': 'copra0100',
    'FormField[2][4]': '\u202aMohammed',
    'FormField[2][5]': 'Saeed\u202c\u200f',
    'FormField[2][6]': '',
    'FormField[2][7]': '3342379842',
    'FormField[2][8]': '78 Old Woods Passage',
    'FormField[2][9]': '',
    'FormField[2][10]': 'Missouri City',
    'FormField[2][11]': 'United States',
    'FormField[2][12]': 'New York',
    'FormField[2][13]': '10080',
    'g-recaptcha-response': '0cAFcWeA6OovbPqQzA8CFSkfrVP0t9diZ9XB8uDZXbjPsZmQJDCDNymmvSKtrYyEmB9WWeYukMdUvxRHhy5UGm5X08tvijhrc_jhmzOYu0wbaNmvCeeJGOe1kTakaNkZUlQlzxdGN71fsJhG93Y2s_lSvcoiim-lcqCqZWg-bDwPY0TBknPozUkOTHUayu2GQ3oJTc1igjZcCAICjMyTySV0HWdHyhXaCXaJRkjzJ6ZIAOBntlp65fIhB_rbfEH2AhLTUwruFMXLmZ7vBq9rTUY_6lX7G5xwCPE_eAk_pXOc7rn95jXYfvWI045AgIalJOkxFrIOm1GXUE0ekGPf2DKX_lVRJNY66eqBfDKbC9SfEdaYzJmzUAegrS_HzMCeRWYwCyArJsQCcIbjF9gSdND9Id9vXxiMJBvH2Q3VDaQ6mgmzMrtVxH_1GiW45nut2waDuHkRcbbB8BTQnG3-KKbYCH2XZ5h1jchMnaw4UUEXXvAQNqbz5ZTxw9v9lmOBrCdiBDysAfuEnvbWetiOiUHMtG7CG-6b3SQLVfthKeJ6PF6yubft0ffB_zZ97FJfsceiZRG9gqtGHuiH4ESVhTkTgvX0IZO_PSgXA-unZqD9Yo70SqnHr-dDuKk2RRe6nfQqycTwd6IbjggF66N2gm1fseG5BpwQqGfksNke-YsnwQFQT2F7KS4Ah1ChZG43f6n18kyMEUV3-4tFSwQOvHVFdHc4nSbD82pJnmH12iXW9v4vJ96iRgIDZoG-0mLpy5n7ViMPb6gbyY1c2DrVDdPgTo9IxNeH-9zqW04i6imp9p1ZIi1iAxkZIOVHHB1RnGU-twcwnmvmajbXh35ZHUfHoaEU40waBAcYtq6YKSLICDKW07TXEPIebpcC4-FQI0Llu-Cagn06h2ClZ0HzAq0JzyucSZIAQv9Q1tv-SnzvjhGtkn8xjyCzWH33Rz7MGRbJC_Wp-ngVJkvxNuFTUE4zuqJvCYh9G84VpidQac0EcgpCgWrP2GD-MqwxJopXDZQPvTKzdXEREuOGEQ-DSMiUsAt4z6VgdFhenQ8jAh1m2wyHqWGebCPckDM0Ewuz4L0TjI3lR4al0yoS5yAaqoK-4vQy9s5ttWXPt4zkRsBH7heQ4sZESe3xNN3urKh8RkJPvG5ZY7Zre-JCvKlrXFEhtuZFjCx_4oxkQMvhVFDnIK7OOP128WOa_1vF0QKUPzejyisCCT0nBHR1fcGCZoHoc_3BUcuC8v16WoUgw9bs0MMH6K2PTkDBuWLM3ZvWRA5OAA6Cer1kkkqxvzORAnImqezOygHZJqeXI7BZUXtAmjcB6QYcDDq1mbQpLRXN7k4q82G7527l6htOUQgXB0Z4ZZ43sG_ziALc8LlTluKrYkafxs288G2hq2MiWJlw1FHOZ7T0kgsSGP_usLiBhgusv6LSJlfXZcsBl8mSkphOkB2pSaELxGy2nPLYTabDwBiWh2EWojoOmmap-s0ugSJZnv9doUZaY_vzBFutGbTWlcP8pjVh11NOPyfjhhELoZpWouq5k_HhrxJClzqhYxcr3ihYLGOBklYyIAQRTsIR3kJWzXtCZlpEg',
    'authenticity_token': '1135afab7fdcf293311fc781552333a522a0fce40ea5832b7cb81f87420c0d63',
    'sf_authenticity_token': '1b1a2935-401b-4134-9dec-d5862cf5cda7',
}

response = requests.post('https://greatlakespetfood.com/login.php', params=params, cookies=cookies, headers=headers, data=data)


import requests

cookies = {
    'fornax_anonymousId': 'b412d695-041a-4e8f-a128-48bd210cd6e3',
    'SHOP_SESSION_TOKEN': 'aa5e3332-2358-4c49-834c-3ee6a991cd65',
    'poptin_old_user': 'true',
    'poptin_user_id': '0.yy9q0bwo8q8',
    '_privy_ACC4BAB260C967EC17DF0711': '%7B%22uuid%22%3A%227b300534-d5da-4980-9770-9705921be178%22%7D',
    'STORE_VISITOR': '1',
    'poptin_user_country_code': 'false',
    'poptin_user_ip': '197.32.61.255',
    'poptin_session_account_89e2702db1c96': 'true',
    'poptin_c_visitor': 'true',
    'poptin_last_visit': '2025-09-24',
    'SF-CSRF-TOKEN': '1b1a2935-401b-4134-9dec-d5862cf5cda7',
    'XSRF-TOKEN': '1135afab7fdcf293311fc781552333a522a0fce40ea5832b7cb81f87420c0d63',
    'athena_short_visit_id': 'a7f1776c-5eab-420b-8df3-3540ddd83dd3:1758756470',
    'poptin_session': 'true',
    'poptin_referrer_protocol': 'secure',
    'SHOP_TOKEN': 'b1eaac4581aa85c5edacc4beba06ea8c2e266b1111651126ba98e1ea660e9789_1759361416',
    'bigcommerce_recently_viewed': '121 153',
    'SHOP_SESSION_ROTATION_TOKEN': '8b270352dea5cbb81774bef7709e999a0cd1cbc3ad7c1520256beebdf6aa907d',
    '__cf_bm': 'V3PyN83UT4VxHHiucSBGu6gZSkzf3Rbm8aTCinlbVTI-1758757669-1.0.1.1-Ykn.C8XaMd4XVbuN4MKYGxAaGXDr1ANqzTX9s0RMj8ZHPBonqnCAKgiwYI9svUQ2cPn5J3TWGVSjni5Gypgjx4G4gZA_fNNxZCezGMYFXdM',
    'poptin_referrer': 'greatlakespetfood.com/',
    'poptin_previous_url': 'greatlakespetfood.com/',
    'poptin_previous_url_protocol': 'secure',
    'Shopper-Pref': 'A58BAE647152C7B436B4BCAE881F596849B8B912-1759362867761-x%7B%22cur%22%3A%22USD%22%2C%22funcConsent%22%3Atrue%7D',
}

headers = {
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9',
    'content-type': 'multipart/form-data; boundary=----WebKitFormBoundaryguWSdeEA5YQFycBR',
    'origin': 'https://greatlakespetfood.com',
    'priority': 'u=1, i',
    'referer': 'https://greatlakespetfood.com/food-scoop/',
    'sec-ch-ua': '"Chromium";v="140", "Not=A?Brand";v="24", "Google Chrome";v="140"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'stencil-config': '{}',
    'stencil-options': '{}',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36',
    'x-requested-with': 'stencil-utils',
    'x-sf-csrf-token': '1b1a2935-401b-4134-9dec-d5862cf5cda7',
    'x-xsrf-token': '1135afab7fdcf293311fc781552333a522a0fce40ea5832b7cb81f87420c0d63',
    # 'cookie': 'fornax_anonymousId=b412d695-041a-4e8f-a128-48bd210cd6e3; SHOP_SESSION_TOKEN=aa5e3332-2358-4c49-834c-3ee6a991cd65; poptin_old_user=true; poptin_user_id=0.yy9q0bwo8q8; _privy_ACC4BAB260C967EC17DF0711=%7B%22uuid%22%3A%227b300534-d5da-4980-9770-9705921be178%22%7D; STORE_VISITOR=1; poptin_user_country_code=false; poptin_user_ip=197.32.61.255; poptin_session_account_89e2702db1c96=true; poptin_c_visitor=true; poptin_last_visit=2025-09-24; SF-CSRF-TOKEN=1b1a2935-401b-4134-9dec-d5862cf5cda7; XSRF-TOKEN=1135afab7fdcf293311fc781552333a522a0fce40ea5832b7cb81f87420c0d63; athena_short_visit_id=a7f1776c-5eab-420b-8df3-3540ddd83dd3:1758756470; poptin_session=true; poptin_referrer_protocol=secure; SHOP_TOKEN=b1eaac4581aa85c5edacc4beba06ea8c2e266b1111651126ba98e1ea660e9789_1759361416; bigcommerce_recently_viewed=121 153; SHOP_SESSION_ROTATION_TOKEN=8b270352dea5cbb81774bef7709e999a0cd1cbc3ad7c1520256beebdf6aa907d; __cf_bm=V3PyN83UT4VxHHiucSBGu6gZSkzf3Rbm8aTCinlbVTI-1758757669-1.0.1.1-Ykn.C8XaMd4XVbuN4MKYGxAaGXDr1ANqzTX9s0RMj8ZHPBonqnCAKgiwYI9svUQ2cPn5J3TWGVSjni5Gypgjx4G4gZA_fNNxZCezGMYFXdM; poptin_referrer=greatlakespetfood.com/; poptin_previous_url=greatlakespetfood.com/; poptin_previous_url_protocol=secure; Shopper-Pref=A58BAE647152C7B436B4BCAE881F596849B8B912-1759362867761-x%7B%22cur%22%3A%22USD%22%2C%22funcConsent%22%3Atrue%7D',
}

files = {
    'action': (None, 'add'),
    'product_id': (None, '121'),
    'qty[]': (None, '1'),
}

response = requests.post('https://greatlakespetfood.com/remote/v1/cart/add', cookies=cookies, headers=headers, files=files)


import requests

cookies = {
    'fornax_anonymousId': 'b412d695-041a-4e8f-a128-48bd210cd6e3',
    'SHOP_SESSION_TOKEN': 'aa5e3332-2358-4c49-834c-3ee6a991cd65',
    'poptin_old_user': 'true',
    'poptin_user_id': '0.yy9q0bwo8q8',
    '_privy_ACC4BAB260C967EC17DF0711': '%7B%22uuid%22%3A%227b300534-d5da-4980-9770-9705921be178%22%7D',
    'STORE_VISITOR': '1',
    'poptin_user_country_code': 'false',
    'poptin_user_ip': '197.32.61.255',
    'poptin_c_visitor': 'true',
    'poptin_session_account_89e2702db1c96': 'true',
    'poptin_last_visit': '2025-09-24',
    'bigcommerce_recently_viewed': '153',
    'SF-CSRF-TOKEN': '1b1a2935-401b-4134-9dec-d5862cf5cda7',
    'XSRF-TOKEN': '1135afab7fdcf293311fc781552333a522a0fce40ea5832b7cb81f87420c0d63',
    '__cf_bm': 'MvZYsPmaIe4Inb7yCc71DOD5Va.gHfrmggLLaax6m7Q-1758756470-1.0.1.1-zgAtTAgui34ws.QWFieeQ2l0_H.gA9n3y1MLElTSrnlvOZ.TMHdydZwvt0tvCHaUJFu53uuwZRttcZ_6iidYsPNIOG0vCruzDP8ra11_mQA',
    'athena_short_visit_id': 'a7f1776c-5eab-420b-8df3-3540ddd83dd3:1758756470',
    'poptin_session': 'true',
    'poptin_referrer_protocol': 'secure',
    'poptin_referrer': 'greatlakespetfood.com/login.php',
    'Shopper-Pref': 'F4A5651152FE6E543C11BF113F103906CBDD1521-1759361416161-x%7B%22cur%22%3A%22USD%22%2C%22funcConsent%22%3Atrue%7D',
    'SHOP_SESSION_ROTATION_TOKEN': '30e24db574b6c89089aab91c300fc5c4a6cede26ac1c93bfca16e298ead90ea1',
    'SHOP_TOKEN': 'b1eaac4581aa85c5edacc4beba06ea8c2e266b1111651126ba98e1ea660e9789_1759361416',
}

headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9',
    'cache-control': 'max-age=0',
    'priority': 'u=0, i',
    'referer': 'https://greatlakespetfood.com/login.php?action=create_account',
    'sec-ch-ua': '"Chromium";v="140", "Not=A?Brand";v="24", "Google Chrome";v="140"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36',
    # 'cookie': 'fornax_anonymousId=b412d695-041a-4e8f-a128-48bd210cd6e3; SHOP_SESSION_TOKEN=aa5e3332-2358-4c49-834c-3ee6a991cd65; poptin_old_user=true; poptin_user_id=0.yy9q0bwo8q8; _privy_ACC4BAB260C967EC17DF0711=%7B%22uuid%22%3A%227b300534-d5da-4980-9770-9705921be178%22%7D; STORE_VISITOR=1; poptin_user_country_code=false; poptin_user_ip=197.32.61.255; poptin_c_visitor=true; poptin_session_account_89e2702db1c96=true; poptin_last_visit=2025-09-24; bigcommerce_recently_viewed=153; SF-CSRF-TOKEN=1b1a2935-401b-4134-9dec-d5862cf5cda7; XSRF-TOKEN=1135afab7fdcf293311fc781552333a522a0fce40ea5832b7cb81f87420c0d63; __cf_bm=MvZYsPmaIe4Inb7yCc71DOD5Va.gHfrmggLLaax6m7Q-1758756470-1.0.1.1-zgAtTAgui34ws.QWFieeQ2l0_H.gA9n3y1MLElTSrnlvOZ.TMHdydZwvt0tvCHaUJFu53uuwZRttcZ_6iidYsPNIOG0vCruzDP8ra11_mQA; athena_short_visit_id=a7f1776c-5eab-420b-8df3-3540ddd83dd3:1758756470; poptin_session=true; poptin_referrer_protocol=secure; poptin_referrer=greatlakespetfood.com/login.php; Shopper-Pref=F4A5651152FE6E543C11BF113F103906CBDD1521-1759361416161-x%7B%22cur%22%3A%22USD%22%2C%22funcConsent%22%3Atrue%7D; SHOP_SESSION_ROTATION_TOKEN=30e24db574b6c89089aab91c300fc5c4a6cede26ac1c93bfca16e298ead90ea1; SHOP_TOKEN=b1eaac4581aa85c5edacc4beba06ea8c2e266b1111651126ba98e1ea660e9789_1759361416',
}

params = {
    'action': 'account_created',
}

response = requests.get('https://greatlakespetfood.com/login.php', params=params, cookies=cookies, headers=headers)


import requests

cookies = {
    'fornax_anonymousId': 'b412d695-041a-4e8f-a128-48bd210cd6e3',
    'SHOP_SESSION_TOKEN': 'aa5e3332-2358-4c49-834c-3ee6a991cd65',
    'poptin_old_user': 'true',
    'poptin_user_id': '0.yy9q0bwo8q8',
    '_privy_ACC4BAB260C967EC17DF0711': '%7B%22uuid%22%3A%227b300534-d5da-4980-9770-9705921be178%22%7D',
    'STORE_VISITOR': '1',
    'poptin_user_country_code': 'false',
    'poptin_user_ip': '197.32.61.255',
    'poptin_session_account_89e2702db1c96': 'true',
    'poptin_c_visitor': 'true',
    'poptin_last_visit': '2025-09-24',
    'SF-CSRF-TOKEN': '1b1a2935-401b-4134-9dec-d5862cf5cda7',
    'XSRF-TOKEN': '1135afab7fdcf293311fc781552333a522a0fce40ea5832b7cb81f87420c0d63',
    '__cf_bm': 'MvZYsPmaIe4Inb7yCc71DOD5Va.gHfrmggLLaax6m7Q-1758756470-1.0.1.1-zgAtTAgui34ws.QWFieeQ2l0_H.gA9n3y1MLElTSrnlvOZ.TMHdydZwvt0tvCHaUJFu53uuwZRttcZ_6iidYsPNIOG0vCruzDP8ra11_mQA',
    'athena_short_visit_id': 'a7f1776c-5eab-420b-8df3-3540ddd83dd3:1758756470',
    'poptin_session': 'true',
    'poptin_referrer_protocol': 'secure',
    'SHOP_TOKEN': 'b1eaac4581aa85c5edacc4beba06ea8c2e266b1111651126ba98e1ea660e9789_1759361416',
    'poptin_previous_url_protocol': 'secure',
    'bigcommerce_recently_viewed': '121 153',
    'poptin_referrer': 'greatlakespetfood.com/',
    'poptin_previous_url': 'greatlakespetfood.com/',
    'SHOP_SESSION_ROTATION_TOKEN': '8b270352dea5cbb81774bef7709e999a0cd1cbc3ad7c1520256beebdf6aa907d',
    'Shopper-Pref': 'A512B7C6ADC4F45BA722EFD457DCD6FD949A5CDB-1759361519790-x%7B%22cur%22%3A%22USD%22%2C%22funcConsent%22%3Atrue%7D',
}

headers = {
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9',
    'priority': 'u=1, i',
    'referer': 'https://greatlakespetfood.com/checkout',
    'sec-ch-ua': '"Chromium";v="140", "Not=A?Brand";v="24", "Google Chrome";v="140"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36',
    'x-sf-csrf-token': '1b1a2935-401b-4134-9dec-d5862cf5cda7',
    'x-xsrf-token': '1135afab7fdcf293311fc781552333a522a0fce40ea5832b7cb81f87420c0d63',
}

response = requests.get('https://greatlakespetfood.com/api/storefront/cart', cookies=cookies, headers=headers)

import requests

cookies = {
    'fornax_anonymousId': 'b412d695-041a-4e8f-a128-48bd210cd6e3',
    'SHOP_SESSION_TOKEN': 'aa5e3332-2358-4c49-834c-3ee6a991cd65',
    'poptin_old_user': 'true',
    'poptin_user_id': '0.yy9q0bwo8q8',
    '_privy_ACC4BAB260C967EC17DF0711': '%7B%22uuid%22%3A%227b300534-d5da-4980-9770-9705921be178%22%7D',
    'STORE_VISITOR': '1',
    'poptin_user_country_code': 'false',
    'poptin_user_ip': '197.32.61.255',
    'poptin_c_visitor': 'true',
    'poptin_session_account_89e2702db1c96': 'true',
    'poptin_last_visit': '2025-09-24',
    'SF-CSRF-TOKEN': '1b1a2935-401b-4134-9dec-d5862cf5cda7',
    'XSRF-TOKEN': '1135afab7fdcf293311fc781552333a522a0fce40ea5832b7cb81f87420c0d63',
    '__cf_bm': 'MvZYsPmaIe4Inb7yCc71DOD5Va.gHfrmggLLaax6m7Q-1758756470-1.0.1.1-zgAtTAgui34ws.QWFieeQ2l0_H.gA9n3y1MLElTSrnlvOZ.TMHdydZwvt0tvCHaUJFu53uuwZRttcZ_6iidYsPNIOG0vCruzDP8ra11_mQA',
    'athena_short_visit_id': 'a7f1776c-5eab-420b-8df3-3540ddd83dd3:1758756470',
    'poptin_session': 'true',
    'poptin_referrer_protocol': 'secure',
    'SHOP_TOKEN': 'b1eaac4581aa85c5edacc4beba06ea8c2e266b1111651126ba98e1ea660e9789_1759361416',
    'bigcommerce_recently_viewed': '121 153',
    'SHOP_SESSION_ROTATION_TOKEN': '8b270352dea5cbb81774bef7709e999a0cd1cbc3ad7c1520256beebdf6aa907d',
    'poptin_referrer': 'greatlakespetfood.com/food-scoop/',
    'Shopper-Pref': '2221F972FD333CB4AA361B42601DD9F3A8F32179-1759361840053-x%7B%22cur%22%3A%22USD%22%2C%22funcConsent%22%3Atrue%7D',
}

headers = {
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'en-US,en;q=0.9',
    'content-type': 'application/json',
    'origin': 'https://greatlakespetfood.com',
    'priority': 'u=1, i',
    'referer': 'https://greatlakespetfood.com/checkout',
    'sec-ch-ua': '"Chromium";v="140", "Not=A?Brand";v="24", "Google Chrome";v="140"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36',
    'x-checkout-sdk-version': '1.798.0',
    'x-checkout-variant': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwczovL2dyZWF0bGFrZXNwZXRmb29kLmNvbSIsImlhdCI6MTc1ODc1NjcxNywiZG9tYWluIjp7ImNhcnRJZCI6ImI3ZWU5MDgwLTExOTctNGZlZC1iNTUzLTcwNmM5Y2RlZWQwZCIsImNoZWNrb3V0VmFyaWFudCI6Im9wdGltaXplZF9vbmVfcGFnZV9jaGVja291dCJ9fQ.pNMxCqKAg2YpPEkDpehnXY7BIELt8qqlR_MEOHOFpjs',
    'x-sf-csrf-token': '1b1a2935-401b-4134-9dec-d5862cf5cda7',
    'x-xsrf-token': '1135afab7fdcf293311fc781552333a522a0fce40ea5832b7cb81f87420c0d63',
    # 'cookie': 'fornax_anonymousId=b412d695-041a-4e8f-a128-48bd210cd6e3; SHOP_SESSION_TOKEN=aa5e3332-2358-4c49-834c-3ee6a991cd65; poptin_old_user=true; poptin_user_id=0.yy9q0bwo8q8; _privy_ACC4BAB260C967EC17DF0711=%7B%22uuid%22%3A%227b300534-d5da-4980-9770-9705921be178%22%7D; STORE_VISITOR=1; poptin_user_country_code=false; poptin_user_ip=197.32.61.255; poptin_c_visitor=true; poptin_session_account_89e2702db1c96=true; poptin_last_visit=2025-09-24; SF-CSRF-TOKEN=1b1a2935-401b-4134-9dec-d5862cf5cda7; XSRF-TOKEN=1135afab7fdcf293311fc781552333a522a0fce40ea5832b7cb81f87420c0d63; __cf_bm=MvZYsPmaIe4Inb7yCc71DOD5Va.gHfrmggLLaax6m7Q-1758756470-1.0.1.1-zgAtTAgui34ws.QWFieeQ2l0_H.gA9n3y1MLElTSrnlvOZ.TMHdydZwvt0tvCHaUJFu53uuwZRttcZ_6iidYsPNIOG0vCruzDP8ra11_mQA; athena_short_visit_id=a7f1776c-5eab-420b-8df3-3540ddd83dd3:1758756470; poptin_session=true; poptin_referrer_protocol=secure; SHOP_TOKEN=b1eaac4581aa85c5edacc4beba06ea8c2e266b1111651126ba98e1ea660e9789_1759361416; bigcommerce_recently_viewed=121 153; SHOP_SESSION_ROTATION_TOKEN=8b270352dea5cbb81774bef7709e999a0cd1cbc3ad7c1520256beebdf6aa907d; poptin_referrer=greatlakespetfood.com/food-scoop/; Shopper-Pref=2221F972FD333CB4AA361B42601DD9F3A8F32179-1759361840053-x%7B%22cur%22%3A%22USD%22%2C%22funcConsent%22%3Atrue%7D',
}

json_data = {
    'cartId': 'b7ee9080-1197-4fed-b553-706c9cdeed0d',
    'customerMessage': '',
}

response = requests.post(
    'https://greatlakespetfood.com/internalapi/v1/checkout/order',
    cookies=cookies,
    headers=headers,
    json=json_data,
)




headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9',
    'priority': 'u=0, i',
    'referer': 'https://greatlakespetfood.com/food-scoop/',
    'sec-ch-ua': '"Chromium";v="140", "Not=A?Brand";v="24", "Google Chrome";v="140"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36',
}

response = requests.get('https://greatlakespetfood.com/checkout', headers=headers)


import requests

headers = {
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9',
    'authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJFUzI1NiIsImtpZCI6IjIwMTgwNDI2MTYtcHJvZHVjdGlvbiIsImlzcyI6Imh0dHBzOi8vYXBpLmJyYWludHJlZWdhdGV3YXkuY29tIn0.eyJleHAiOjE3NTg4NDMxMDYsImp0aSI6IjBkZjUxYTA0LTFhZjktNDhhZS04Y2ZmLTFhNzg3YTcyYjM1NCIsInN1YiI6ImRwc2ttOHNndHZtOXNmcWYiLCJpc3MiOiJodHRwczovL2FwaS5icmFpbnRyZWVnYXRld2F5LmNvbSIsIm1lcmNoYW50Ijp7InB1YmxpY19pZCI6ImRwc2ttOHNndHZtOXNmcWYiLCJ2ZXJpZnlfY2FyZF9ieV9kZWZhdWx0IjpmYWxzZSwidmVyaWZ5X3dhbGxldF9ieV9kZWZhdWx0IjpmYWxzZX0sInJpZ2h0cyI6WyJtYW5hZ2VfdmF1bHQiXSwiYXVkIjpbImdyZWF0bGFrZXNwZXRmb29kLmNvbSJdLCJzY29wZSI6WyJCcmFpbnRyZWU6VmF1bHQiLCJCcmFpbnRyZWU6Q2xpZW50U0RLIiwiQnJhaW50cmVlOkFYTyJdLCJvcHRpb25zIjp7Im1lcmNoYW50X2FjY291bnRfaWQiOiJHcmVhdExha2VzUGV0Rm9vZF9pbnN0YW50IiwicGF5cGFsX2FjY291bnRfbnVtYmVyIjoiMjIxNDQzMjU4OTUyMjg5NTg3NiIsInBheXBhbF9jbGllbnRfaWQiOiJBUW5mMUxPSWthUllDSWd2bGs4Y0NJVFBSQXJjVnNGeXVlOEJ5amloWlVVaTlrbFFlUFg4SWNvQmJ2aDJ4elRoWUFMRmVaSXN3RlFycm81YiJ9fQ.9CVMdjStUKYVufEXY2mU7-tXBKk8iyJ24EEFa6wjCAuHfoBknHwFlXXSBzw0zrzEkvT3I_GbWRdX-5lLFXZPOw',
    'braintree-version': '2018-05-10',
    'content-type': 'application/json',
    'origin': 'https://assets.braintreegateway.com',
    'priority': 'u=1, i',
    'referer': 'https://assets.braintreegateway.com/',
    'sec-ch-ua': '"Chromium";v="140", "Not=A?Brand";v="24", "Google Chrome";v="140"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'cross-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36',
}

json_data = {
    'clientSdkMetadata': {
        'source': 'client',
        'integration': 'custom',
        'sessionId': '5c3818d6-4639-4ce2-b829-654ded793661',
    },
    'query': 'mutation TokenizeCreditCard($input: TokenizeCreditCardInput!) {   tokenizeCreditCard(input: $input) {     token     creditCard {       bin       brandCode       last4       cardholderName       expirationMonth      expirationYear      binData {         prepaid         healthcare         debit         durbinRegulated         commercial         payroll         issuingBank         countryOfIssuance         productId         business         consumer         purchase         corporate       }     }   } }',
    'variables': {
        'input': {
            'creditCard': {
                'number': '4748440380457124',
                'expirationMonth': '02',
                'expirationYear': '2027',
                'cvv': '597',
                'cardholderName': 'venom',
                'billingAddress': {
                    'countryName': 'United States',
                    'postalCode': '10080',
                    'streetAddress': '78 Old Woods Passage',
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



import requests

headers = {
    'Accept': 'application/json',
    'Accept-Language': 'en-US,en;q=0.9',
    'Authorization': 'JWT eyJhbGciOiJIUzI1NiJ9.eyJleHAiOjE3NTg3NjEyNzAsIm5iZiI6MTc1ODc1NzY3MCwiaXNzIjoicGF5bWVudHMuYmlnY29tbWVyY2UuY29tIiwic3ViIjoxMDAyMzU1NTY4LCJqdGkiOiI5NjEwMzA4OC0zOGZmLTQ3YWUtOTEwYi1lNzU2ZWFjZjNjNTgiLCJpYXQiOjE3NTg3NTc2NzAsImRhdGEiOnsic3RvcmVfaWQiOiIxMDAyMzU1NTY4Iiwib3JkZXJfaWQiOiIxMDA0MTg3MSIsImFtb3VudCI6NzAwLCJjdXJyZW5jeSI6IlVTRCIsInN0b3JlX3VybCI6Imh0dHBzOi8vZ3JlYXRsYWtlc3BldGZvb2QuY29tIiwiZm9ybV9pZCI6InVua25vd24iLCJwYXltZW50X2NvbnRleHQiOiJjaGVja291dCIsInBheW1lbnRfdHlwZSI6ImVjb21tZXJjZSJ9fQ.T1NOMJBXoxzPvs6Zvw28Cl16RD6f6MHiTClfbdNu2Ik',
    'Connection': 'keep-alive',
    'Content-Type': 'application/json',
    'Origin': 'https://greatlakespetfood.com',
    'Referer': 'https://greatlakespetfood.com/',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'cross-site',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36',
    'sec-ch-ua': '"Chromium";v="140", "Not=A?Brand";v="24", "Google Chrome";v="140"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}

json_data = {
    'customer': {
        'geo_ip_country_code': 'EG',
        'id': '32237',
        'session_token': 'fa1540aa6e6e32c0ff046e3106d78526defe03ec',
    },
    'notify_url': 'https://internalapi-1002355568.mybigcommerce.com/internalapi/v1/checkout/order/10041871/payment',
    'order': {
        'billing_address': {
            'city': 'Missouri City',
            'country_code': 'US',
            'country': 'United States',
            'first_name': '\u202aMohammed',
            'last_name': 'Saeed\u202c\u200f',
            'phone': '3342379842',
            'state_code': 'NY',
            'state': 'New York',
            'street_1': '78 Old Woods Passage',
            'zip': '10080',
            'email': 'sasa0100m@gmail.com',
        },
        'coupons': [],
        'currency': 'USD',
        'id': '10041871',
        'items': [
            {
                'code': 'ec2aa163-586e-4f24-b9cf-10cdcde18ab7',
                'variant_id': 100,
                'name': 'Food Scoop',
                'price': 200,
                'unit_price': 200,
                'quantity': 1,
                'sku': 'SC1BLUE',
            },
        ],
        'shipping': [
            {
                'method': 'Ground Shipping',
            },
        ],
        'shipping_address': {
            'city': 'Missouri City',
            'country_code': 'US',
            'country': 'United States',
            'first_name': '\u202aMohammed',
            'last_name': 'Saeed\u202c\u200f',
            'phone': '3342379842',
            'state_code': 'NY',
            'state': 'New York',
            'street_1': '78 Old Woods Passage',
            'zip': '10080',
        },
        'token': '2c70306035ff7b47df43e730af06e706',
        'totals': {
            'grand_total': 700,
            'handling': 0,
            'shipping': 500,
            'subtotal': 200,
            'tax': 0,
        },
    },
    'payment': {
        'device_info': '{"correlation_id":"5c3818d6-4639-4ce2-b829-654ded79"}',
        'gateway': 'braintree',
        'notify_url': 'https://internalapi-1002355568.mybigcommerce.com/internalapi/v1/checkout/order/10041871/payment',
        'vault_payment_instrument': False,
        'method': 'credit-card',
        'credit_card_token': {
            'token': 'tokencc_bh_wgkr34_7rtgpk_k8gk25_c64byr_gq6',
        },
    },
    'store': {
        'hash': 'x2izn21rze',
        'id': '1002355568',
        'name': 'Great Lakes Pet Food',
    },
}

response = requests.post('https://payments.bigcommerce.com/api/public/v1/orders/payments', headers=headers, json=json_data)

print(response.json()['errors'][0]['message'])
