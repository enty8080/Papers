from bit.network import NetworkAPI

address = 'your_bitcoin_address_here'
amount = 0.001

transactions = NetworkAPI.get_transactions(address)

for tx in transactions:
    total_output = 0
    for output in tx['outputs']:
        if output['address'] == address:
            total_output += output['value']
    if total_output == amount:
        print('Transaction with ID {} is confirmed and includes an output of {} BTC to this address.'.format(tx['txid'], amount))
        break
