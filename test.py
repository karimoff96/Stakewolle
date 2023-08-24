import requests
import base64

def get_block_transactions(block_number):
    # Замените URL на актуальный API endpoint https://www.mintscan.io/akash/info линк не актуален
    url = f"https://api.mintscan.io/akash/blocks/{block_number}"
    
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        
        if "data" in data and "txs" in data["data"]:
            txs_base64 = data["data"]["txs"]
            decoded_txs = [base64.b64decode(tx).decode("utf-8") for tx in txs_base64]
            
            return decoded_txs
        else:
            return "В блоке транзакции нет"
    else:
        return "Ощибка при извличение даты"

block_number = 11260637  # Замените на номер блока, который вам интересен
transactions = get_block_transactions(block_number)

for idx, tx in enumerate(transactions, start=1):
    print(f"Транзакция {idx}:\n{tx}\n{'='*50}")