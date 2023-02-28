import requests

# Set the Bitcoin address to receive funds
RECEIVING_ADDRESS = "1BvBMSEYstWetqTFn5Au4m4GFg7xJaNVN2"

# Generate a new address for each transaction for privacy and security reasons
def generate_new_address():
    url = "https://api.blockchain.info/v2/receive"
    params = {"xpub": "<your xpub key>", "callback": "<your callback URL>"}
    response = requests.get(url, params=params)
    if response.status_code == 200:
        data = response.json()
        return data["address"]
    else:
        return None

# Check if a transaction has been received for the specified address and amount
def check_transaction_received(address, amount):
    url = f"https://blockchain.info/rawaddr/{address}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        for transaction in data["txs"]:
            for output in transaction["out"]:
                if output["addr"] == address and output["value"] == amount:
                    return True
        return False
    else:
        return None

# Generate a new Bitcoin address for this transaction
new_address = generate_new_address()
print("Send Bitcoins to this address:", new_address)

# Wait for the transaction to be received and verified
while True:
    if check_transaction_received(new_address, <amount_in_satoshis>):
        print("Transaction received and verified.")
        break
