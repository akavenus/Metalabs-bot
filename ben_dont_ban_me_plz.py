import requests
from bs4 import BeautifulSoup
import json
s = requests.Session()
full_name = input('Enter your full name: ')
email = input('Enter your email: ')
domain = input('Enter the domain (dashboard.estocksoftware.com)': )
password = input('Enter the password': )
login_required = 'no'
if login_required == 'no':
    headers1 = {
        'Accept': '*/*',
        'Connection': 'keep-alive',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.91 Safari/537.36',
        'Accept-Language': 'en-US,en;q=0.3',
        'Cache-Control': 'max-age=0',
        'DNT': '1', 
        'Upgrade-Insecure-Requests': '1',
        'Referer': 'https://google.com',
        'Accept-Encoding': '*/*'
    }
    xa = s.get(url, headers=headers1)
    print(xa.status_code)
    xb = s.get(f'https://{domain}/api/user', headers=headers2)
    print(xb.status_code)
    soup1 = BeautifulSoup(xa.text, 'lxml')
    metalabs_data = soup1.find('script', type = 'application/json')
    json_object = json.loads(metalabs_data.contents[0])
    metalabs_account = json_object['props']['pageProps']['account']['id']
    release_id = json_object['props']['pageProps']['release']['id']
    headers2 = {
        'Accept': 'application/json, text/plain, */*',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'en-US,en;q=0.9',
        'Meta-Labs-Account': meta_labs_account,
        'Cache-Control': 'no-cache',
        'Pragma': 'no-cache',
        'Referer': f'https://{domain}/purchase?password={password}',
        'Sec-CH-UA': '"Google Chrome";v="89", "Chromium";v="89", ";Not A Brand";v="99"',
        'Sec-CH-UA-Mobile': '?0',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-orgin',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.91 Safari/537.36',
    }
    options_headers = {
        'Accept': '*/*',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'en-US,en;q=0.9',
        'access-control-request-headers': 'content-type,meta-labs-account,x-amz-cf-id,x-amz-req-id',
        'access-control-request-method': 'POST',
        'Cache-Control': 'no-cache',
        'Orgin': 'https://' + domain,
        'Pragma': 'no-cache',
        'Referer': 'https://' + domain = '/',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'cross-site',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.91 Safari/537.36',
    }
    resp = requests.options('https://portal-api.metalabs.io/v1/checkouts', headers=options_headers)
    print(resp.status_code)
    headers3 = {
        'Accept': 'application/json, text/plain, */*',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'en-US,en;q=0.9',
        'Cache-Control': 'no-cache',
        'meta-labs-account': metalabs_account,
        'Orgin': 'https://' + domain,
        'Pragma': 'no-cache',
        'Referer': 'https://' + domain = '/',
        'Sec-CH-UA': '"Google Chrome";v="89", "Chromium";v="89", ";Not A Brand";v="99"',
        'Sec-CH-UA-Mobile': '?0',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'cross-site',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.91 Safari/537.36',
        'x-amz-cf-id': None,
        'x-amz-req-id': None
    }
    payload = {"release":release_id,"billing_details":{"name":full_name,"email":email,"address":None},"payment_method":None}
    xc = s.post('https://portal-api.metalabs.io/v1/checkouts', json=payload, headers=headers3)
    print(xc.status_code)
    xc.raise_for_status()
