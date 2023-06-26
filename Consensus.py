import hashlib
import time

class Block:
    def __init__(self, index, timestamp, transactions, previous_hash):
        self.index = index
        self.timestamp = timestamp
        self.transactions = transactions
        self.previous_hash = previous_hash
        self.nonce = 0
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        data = str(self.index) + str(self.timestamp) + str(self.transactions) + str(self.previous_hash) + str(self.nonce)
        return hashlib.sha256(data.encode()).hexdigest()

class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]
        self.difficulty = 2  

    def create_genesis_block(self):
        return Block(0, time.time(), [], "0")

    def get_latest_block(self):
        return self.chain[-1]

    def add_block(self, new_block):
        new_block.previous_hash = self.get_latest_block().hash
        new_block.hash = new_block.calculate_hash()
        self.chain.append(new_block)

    def is_chain_valid(self):
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i - 1]

            if current_block.hash != current_block.calculate_hash():
                return False

            if current_block.previous_hash != previous_block.hash:
                return False

        return True

    def mine_block(self, transactions):
        new_block = Block(len(self.chain), time.time(), transactions, self.get_latest_block().hash)

        # Proof-of-Work
        while not new_block.hash.startswith("0" * self.difficulty):
            new_block.nonce += 1
            new_block.hash = new_block.calculate_hash()

        self.chain.append(new_block)
        return new_block


class ProofOfWork:
    def __init__(self, blockchain):
        self.blockchain = blockchain
        self.difficulty = 2  # Difficulty level for mining

    def mine_block(self, transactions):
        new_block = Block(len(self.blockchain.chain), time.time(), transactions, self.blockchain.get_latest_block().hash)

        # Proof-of-Work
        while not self.is_valid_proof(new_block):
            new_block.nonce += 1
            new_block.hash = new_block.calculate_hash()

        self.blockchain.add_block(new_block)
        return new_block

    def is_valid_proof(self, block):
        return block.hash.startswith("0" * self.difficulty) and block.hash == block.calculate_hash() and self.blockchain.is_chain_valid()

# Usage example:
blockchain = Blockchain()
pow = ProofOfWork(blockchain)

# Create some transactions
transactions = [
    Transaction("Hari", "Balu", 10),
    Transaction("Chandru", "Ashwin", 5),
    Transaction("Jai", "Shankar", 3)
]

# Mine a new block
new_block = pow.mine_block(transactions)
print(f"Block mined: {new_block.hash}")
