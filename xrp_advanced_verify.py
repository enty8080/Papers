from xrpl.clients import JsonRpcClient
from xrpl.transaction import get_transaction_from_hash

# Connect to an XRP node (replace 'https://s.altnet.rippletest.net:51234' with the URL of your node)
client = JsonRpcClient('https://s.altnet.rippletest.net:51234')

address = 'your_xrp_address_here'
amount = 1.0  # the amount you are expecting to receive, in XRP

response = client.request('account_tx', account=address)
transactions = response['result']['transactions']

for tx in transactions:
    transaction = get_transaction_from_hash(tx['hash'], client)
    if transaction and transaction['TransactionType'] == 'Payment' and transaction['Destination'] == address and float(transaction['Amount']) == amount:
        print('Transaction with hash {} is confirmed and includes a transfer of {} XRP to this address.'.format(tx['hash'], amount))
        break
