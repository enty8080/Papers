import os
from web3 import Web3

# Set up a connection to the Ethereum network
w3 = Web3(Web3.HTTPProvider(os.environ.get('WEB3_PROVIDER_URI')))

# Set the Ethereum address to receive funds
RECEIVING_ADDRESS = "0xAb8483F64d9C6d1EcF9b849Ae677dD3315835cb2"

# Check if a transaction has been received for the specified address and amount
def check_transaction_received(address, amount):
    latest_block = w3.eth.getBlock('latest')
    for i in range(1, min(latest_block.number, 1000) + 1):
        block = w3.eth.getBlock(latest_block.number - i)
        for tx in block.transactions:
            if tx.to == address and w3.fromWei(tx.value, 'ether') == amount:
                return True
    return False

# Generate a new Ethereum address for this transaction
new_address = w3.eth.account.create().address
print("Send Ethereum to this address:", new_address)

# Wait for the transaction to be received and verified
while True:
    if check_transaction_received(new_address, <amount_in_eth>):
        print("Transaction received and verified.")
        break
