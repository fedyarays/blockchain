import struct
from sha256 import sha256

class BlockHeader:
    def __init__(self, block_size, prev_block_hash, merkle_root, timestamp, nonce):
        self.block_size = block_size
        self.prev_block_hash = prev_block_hash
        self.merkle_root = merkle_root
        self.timestamp = timestamp
        self.nonce = nonce

    def serialize(self):
        return (struct.pack("<I", self.block_size) +
                bytes.fromhex(self.prev_block_hash) +
                bytes.fromhex(self.merkle_root) +
                struct.pack("<I", self.timestamp) +
                struct.pack("<I", self.nonce))

    def hash(self):
        return sha256(self.serialize())

    def mine(self):
        while True:
            block_hash = self.hash()
            if block_hash.startswith('0000'):
                return self, block_hash
            self.nonce += 1
