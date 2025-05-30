Simple Python Blockchain

A minimal, locally deployable blockchain implemented in a single Python file, with a basic Proof-of-Work consensus algorithm and a REST API for submitting transactions, mining blocks, and inspecting the chain.

Contents

blockchain.py — All blockchain logic and HTTP endpoints.

Prerequisites

Python 3.8 or higher

Flask web framework

Installation

Clone or download this repository.

Install dependencies:

pip install flask

Running the Node

Launch the Flask server (default port 5000):

python blockchain.py

The server will be available at http://localhost:5000/.

API Endpoints

Endpoint

Method

Description

/transactions/new

POST

Submit a new transaction

/mine

GET

Trigger Proof-of-Work, mine a new block, and receive a reward transaction

/chain

GET

Retrieve the full blockchain

1. Submit a Transaction

curl -X POST http://localhost:5000/transactions/new \
     -H "Content-Type: application/json" \
     -d '{"sender":"alice","recipient":"bob","amount":5}'

Response:

{ "message": "Transaction will be in block 2" }

2. Mine a Block

curl http://localhost:5000/mine

Response:

{
  "message": "New block forged",
  "block": {
     "index": 2,
     "timestamp": 1627889187.123456,
     "transactions": [{ "sender": "0", "recipient": "you", "amount": 1 }],
     "nonce": 52347,
     "previous_hash": "0000ab34..."
  }
}

3. View the Full Chain

curl http://localhost:5000/chain

Response:

{
  "chain": [...],
  "length": 2
}

How It Works

Data Structures

Blocks are simple Python dicts containing index, timestamp, transactions, nonce, and previous_hash.

Transactions are appended to current_transactions until a block is mined.

Proof-of-Work

The proof_of_work method finds a nonce such that sha256(last_nonce + nonce) yields a hash with four leading zeros.

Upon mining, the miner receives a reward transaction from "0" to "you".

REST API

Built with Flask; three endpoints to submit transactions, mine blocks, and fetch the chain.

Next Steps

After confirming this basic node runs correctly, you can iterate:

Add peer-to-peer synchronization

Separate modules with OOP structure

Configurable ports and difficulty

Persistent storage (SQLite, JSON files)

Alternative consensus (Proof-of-Authority)

This project is released under the MIT License.

