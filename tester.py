# Run from command line while the flask-api-wrapper-for-gdk API is running:
# python tester.py

import json
import requests

GET_TOKEN = '9becbfcf-7eca-4d58-baa1-855c3034dbfe'
POST_TOKEN = 'f056f7dd-6bab-4808-399e-cac4477148f9'

GET_HEADERS = {'content-type': 'application/json', 'Authorization': f'{GET_TOKEN}'}
POST_HEADERS = {'content-type': 'application/json', 'Authorization': f'{POST_TOKEN}'}

API_URL = 'http://127.0.0.1:5000/api/v1'


# Example API call using no authorization header
################################################
url = f'{API_URL}/example_no_auth'
response = requests.get(url)
resp = json.loads(response.text)
#print(json.dumps(resp, indent=4))


# Example API call using authorization header
#############################################
url = f'{API_URL}/example_auth'
response = requests.get(url, headers=GET_HEADERS)
resp = json.loads(response.text)
#print(json.dumps(resp, indent=4))


# Create a wallet with a pin
############################
"""
url = f'{API_URL}/wallet/create'
response = requests.get(url, headers=GET_HEADERS)
resp = json.loads(response.text)
print(json.dumps(resp, indent=4))
mnemonic = resp['mnemonic']
gaid = resp['gaid']
"""

# Some test data from a wallet already set up:
"""
{
    "gaid": "GA2UthatATaM2RgHwaYWm1xwmMSYcN",
    "mnemonic": "emerge wall unique else brother confirm forget capital course antenna gadget distance resemble before reveal scene slide dove theory sponsor century jazz swap assault"
}
"""

# Test wallet data from already set up wallet:
mnemonic = 'emerge wall unique else brother confirm forget capital course antenna gadget distance resemble before reveal scene slide dove theory sponsor century jazz swap assault'


# Get the wallet's balance
##########################
url = f'{API_URL}/wallet/balance'
payload = {
    'mnemonic': mnemonic,
}
response = requests.post(url, data=json.dumps(payload), headers=POST_HEADERS)
resp = json.loads(response.text)
# Test network L-BTC:
# https://blockstream.info/liquidtestnet/asset/144c654344aa716d6f3abcc1ca90e5641e4e2a7f633bc09fe3baf64585819a49
# Live network L-BTC:
# https://blockstream.info/liquid/asset/6f0279e9ed041c3d710a9f57d0c02928416460c4b722ae3457a11eec381c526d
print('Wallet balance:')
print(json.dumps(resp, indent=4))


# Get a new address for the wallet
##################################
# Refer to the comment in the linked example below as you need to provide the
# address to the user to deposit to but you need to store the unblinded_address
# and pointer so you can check against the transaction data from GDK which uses
# unblinded_address and pointer:
# https://github.com/Blockstream/gdk/blob/master/src/swig_python/contrib/gdk_example_liquid_amp.py#L109
url = f'{API_URL}/wallet/new-address'
payload = {
    'mnemonic': mnemonic,
}
response = requests.post(url, data=json.dumps(payload), headers=POST_HEADERS)
resp = json.loads(response.text)
print('New address data:')
print(json.dumps(resp, indent=4))
print('\nAddress data to persist:')
print(f'Deposit to address:                                      {resp["address"]}')
print(f'Unblinded address to track deposit transactions against: {resp["unblinded_address"]}')
print(f'Address pointer to track deposit transactions against:   {resp["pointer"]}')
