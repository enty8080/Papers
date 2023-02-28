from monero.wallet import Wallet
from monero.backends.jsonrpc import JSONRPCWallet

# Connect to a Monero node (replace 'https://example.com' with the URL of your node)
daemon_address = 'https://example.com'
w = Wallet(JSONRPCWallet(daemon_address))

address = 'your_monero_address_here'
amount = 1.0  # the amount you are expecting to receive, in XMR

transactions = w.get_txs(address)

for tx in transactions:
    total_output = 0
    for output in tx['outputs']:
        if output['address'] == address:
            total_output += output['amount']
    if total_output == amount:
        print('Transaction with hash {} is confirmed and includes an output of {} XMR to this address.'.format(tx['hash'], amount))
        break
