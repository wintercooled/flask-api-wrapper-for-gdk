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
print('\nWallet balance:')
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
print('\nNew address data:')
print(json.dumps(resp, indent=4))
print('\nAddress data to persist:')
print(f'Deposit to address:                                      {resp["address"]}')
print(f'Unblinded address to track deposit transactions against: {resp["unblinded_address"]}')
print(f'Address pointer to track deposit transactions against:   {resp["pointer"]}')

# Some example address data for this account that L-BTC was sent to (test net)
# which you will find transaction data for further down. Note that the send was
# to the vj* address. The unblinded address and pointer are used to match
# incoming transactions against, NOT the confidential vj* address:
"""
Address data to persist:
Deposit to address:                                      vjU8FvL4DsAqFihqAtHraWLGqJFq5YCUbRPPjboPPCVRucTceLUbCDDG2x12Zod6taGkJNMXJcHPQV7f
Unblinded address to track deposit transactions against: 8honKYihiGEkkAT4NjSgCr8nmj8ndWQesm
Address pointer to track deposit transactions against:   53
"""
# We will set this here so we can check against it in incoming transactions:
unblinded_address_already_sent_to = '8honKYihiGEkkAT4NjSgCr8nmj8ndWQesm'
pointer_for_unblinded_address_already_sent_to = 53

# Get some network info (block height)
######################################
url = f'{API_URL}/block-height'
payload = {
    'mnemonic': mnemonic,
}
response = requests.post(url, data=json.dumps(payload), headers=POST_HEADERS)
block_height = json.loads(response.text)
chain_block_height = int(block_height['block_height'])
print(f'\nchain_block_height: {chain_block_height}')


# Get the wallet's transactions
###############################
url = f'{API_URL}/wallet/transactions'
payload = {
    'mnemonic': mnemonic,
}
response = requests.post(url, data=json.dumps(payload), headers=POST_HEADERS)
txs = json.loads(response.text)
#print('Wallet transactions:')
#print(json.dumps(txs, indent=4))

# We can track incoming transactions using the output array and the
# receive_address and pointer fields, as mentioned above.

for tx in txs:
    #print(json.dumps(tx, indent=4))
    tx_id = tx['txhash']
    block_height = tx['block_height']
    tx_type = tx['type']
    confirmation_status = tx['confirmation_status']
    outputs = tx['outputs']
    for output in outputs:
        if output['is_relevant']:
            print('\nOUTPUT:')
            print(f'tx_id:               {tx_id}')
            print(f'confirmation_status: {confirmation_status}')
            print(f'block_height:        {block_height}')
            print(f'tx_type:             {tx_type}')
            print(f'* unblinded_address: {output["unblinded_address"]}')
            print(f'* pointer:           {output["pointer"]}')
            print(f'receive_address:     {output["address"]}')
            print(f'amount_sat:          {output["satoshi"]}')
            print(f'asset_id:            {output["asset_id"]}')
            if (output["unblinded_address"] == unblinded_address_already_sent_to and
                output["pointer"] == pointer_for_unblinded_address_already_sent_to):
                print(' -> THE ABOVE WAS THE ADDRESS DEPOSITED TO IN THE TEST TRANSACTION')


# Send some L-BTC from the wallet
#################################
# We will actually send it to an address from this wallet
url = f'{API_URL}/wallet/send-to-address'
payload = {
    'mnemonic': mnemonic,
    'sat_amount': 1,
    'asset_id': '144c654344aa716d6f3abcc1ca90e5641e4e2a7f633bc09fe3baf64585819a49',
    'destination_address': 'vjTxijBwAms4i6MWgqVwnsZWpGEDkwj8jXLstHE8PAEKCzr2Hmr6AAGj4uxzCQs3yT84AKdm1GZtUnhg'
}
response = requests.post(url, data=json.dumps(payload), headers=POST_HEADERS)
tx_hash = json.loads(response.text)
print('\nSent transaction:')
print(json.dumps(tx_hash, indent=4))
