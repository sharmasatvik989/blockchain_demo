import hashlib
import json
import time
from flask import Flask, request, jsonify

class Blockchain:
    #Defining the Chain and transaction
    def __init__(self):
        self.chain = []
        self.current_transactions = []
        # create genesis block
        self.new_block(nonce=100, previous_hash='1')

    #Adding a new block with identifiers
    def new_block(self, nonce, previous_hash=None):
        block = {
            'index': len(self.chain) + 1,
            'timestamp': time.time(),
            'transactions': self.current_transactions,
            'nonce': nonce,
            'previous_hash': previous_hash or self.hash(self.chain[-1])
        }
        self.current_transactions = []
        self.chain.append(block)
        return block

    #Adding a new transaction with transactional identifiers
    def new_transaction(self, sender, recipient, amount):
        self.current_transactions.append({
            'sender': sender,
            'recipient': recipient,
            'amount': amount
        })
        return self.last_block['index'] + 1

    #Will not take self as first argument when class is instantiated 
    @staticmethod
    def hash(block):
        block_string = json.dumps(block, sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()

    #Read- only attributes
    @property
    def last_block(self):
        return self.chain[-1]

    #Mining a new block
    def proof_of_work(self, last_nonce):
        nonce = 0
        while True:
            guess = f'{last_nonce}{nonce}'.encode()
            guess_hash = hashlib.sha256(guess).hexdigest()
            if guess_hash[:4] == '0000':  # difficulty: 4 leading zeros
                return nonce
            nonce += 1

# Instantiate
app = Flask(__name__)
blockchain = Blockchain()

@app.route('/mine', methods=['GET'])
def mine():
    last_nonce = blockchain.last_block['nonce']
    nonce = blockchain.proof_of_work(last_nonce)

    # reward
    blockchain.new_transaction(sender="0", recipient="you", amount=1)

    block = blockchain.new_block(nonce)
    return jsonify({
        'message': 'New block forged',
        'block': block
    }), 200

@app.route('/transactions/new', methods=['POST'])
def new_tx():
    data = request.get_json()
    for k in ('sender','recipient','amount'):
        if k not in data:
            return f'Missing {k}', 400
    idx = blockchain.new_transaction(data['sender'], data['recipient'], data['amount'])
    return jsonify({'message': f'Transaction will be in block {idx}'}), 201

@app.route('/chain', methods=['GET'])
def full_chain():
    return jsonify({
        'chain': blockchain.chain,
        'length': len(blockchain.chain)
    }), 200

if __name__ == '__main__':
    app.run(port=5000)