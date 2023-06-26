import hashlib

class Transaction:
    def __init__(self, sender, recipient, amount):
        self.sender = sender
        self.recipient = recipient
        self.amount = amount
        self.transaction_id = self.calculate_hash()

    def calculate_hash(self):
        data = str(self.sender) + str(self.recipient) + str(self.amount)
        return hashlib.sha256(data.encode()).hexdigest()

    def is_valid(self):
        if self.sender == self.recipient:
            return False

        if self.amount <= 0:
            return False

        return True


class Blockchain:
    def __init__(self):
        self.chain = []
        self.pending_transactions = []

    def create_transaction(self, sender, recipient, amount):
        transaction = Transaction(sender, recipient, amount)
        if transaction.is_valid():
            self.pending_transactions.append(transaction)
            return transaction.transaction_id
        else:
            return None

    def mine_block(self, miner_address):
        # Include pending transactions in the new block
        block_data = [transaction.__dict__ for transaction in self.pending_transactions]
        new_block = Block(len(self.chain), time.time(), block_data, self.get_latest_block().hash)
        # ... (rest of the mining process)

        # Clear pending transactions after mining
        self.pending_transactions = []

        # Add the new block to the blockchain
        self.chain.append(new_block)

    def get_latest_block(self):
        if len(self.chain) > 0:
            return self.chain[-1]
        else:
            return None
