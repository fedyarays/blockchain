import argparse
import time
import os
from merkle_root import merkle_root
from block_header import BlockHeader
from utils import read_transactions

def main(transaction_files, prev_block_hash_file):
    # Чтение транзакций
    transactions = read_transactions(transaction_files)

    # Чтение хэша предыдущего блока
    if not os.path.exists(prev_block_hash_file):
        return

    with open(prev_block_hash_file, 'r') as f:
        prev_block_hash = f.read().strip()

    # Вычисление корня Меркла
    merkle_root_hash = merkle_root(transactions)

    # Создание заголовка блока
    block_size = 4 + 32 + 32 + 4 + 4  # Размер заголовка блока
    timestamp = int(time.time())
    nonce = 0
    block_header = BlockHeader(block_size, prev_block_hash, merkle_root_hash, timestamp, nonce)

    # Поиск nonce
    mined_block_header, block_hash = block_header.mine()

    # Сохранение блока в файл
    with open('mined_block.bin', 'wb') as f:
        f.write(mined_block_header.serialize())

    print(f"Block mined!\nHash: {block_hash}\nNonce: {mined_block_header.nonce}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(prog='Blockchain')
    parser.add_argument('--transactions',
                        nargs='+',
                        required=True,
                        help='List of transactions')
    parser.add_argument('--prev-block-hash',
                        required=True,
                        help='Previous block hash')
    args = parser.parse_args()
    main(args.transactions, args.prev_block_hash)