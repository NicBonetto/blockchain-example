class Blockchain(object):
    def __init__(self):
        self.chain = []
        self.current_transactions = []
    
    def new_transaction(self, sender, recipient, amount):

        self.current_transactions.append({
            'sender': sender,
            'recipient': recipient,
            'amount': amount
        })

        return self.last_block['index'] + 1