import os

def read_transactions(file_paths):
    transactions = []
    for file_path in file_paths:
        if not os.path.exists(file_path):
            continue
        with open(file_path, 'rb') as f:
            transactions.append(f.read().hex())
    return transactions
