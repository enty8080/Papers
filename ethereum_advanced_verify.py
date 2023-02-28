from web3 import Web3

# Connect to an Ethereum node (replace 'https://example.com' with the URL of your node)
w3 = Web3(Web3.HTTPProvider('https://example.com'))

address = 'your_ethereum_address_here'
amount = 1.0  # the amount you are expecting to receive, in ETH

transactions = w3.eth.get_transactions(address)
for tx in transactions:
    receipt = w3.eth.get_transaction_receipt(tx)
    if receipt:
        transaction = w3.eth.get_transaction(tx)
        if transaction['to'] == address and w3.fromWei(transaction['value'], 'ether') == amount:
            print('Transaction with hash {} is confirmed and includes a transfer of {} ETH to this address.'.format(tx.hex(), amount))
            break
