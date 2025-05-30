# Simple Python Blockchain

A minimal, locally deployable blockchain implemented in a single Python file, featuring:

* **Proof-of-Work consensus** (four leading zeros)
* **REST API** for transactions, mining, and chain inspection
* **Single-node** setup, ideal for local testing and learning

---

## 🚀 Getting Started

These instructions will help you run the blockchain on your local machine.

### Prerequisites

* **Python 3.8+**
* **pip** (should come with Python)
* (Optional) **virtualenv** or **venv** for isolated environment

### Installation

1. **Clone the repository**

   ```bash
   git clone https://github.com/your-repo/local_blockchain.git
   cd local_blockchain
   ```
2. **Install dependencies**

   ```bash
   pip install flask
   ```

---

## 🏃‍♂️ Running the Node

Start the Flask server (default port `5000`):

```bash
python blockchain.py
```

Once running, the API will be available at `http://localhost:5000/`.

---

## 📒 API Reference

| Endpoint            | Method | Description                                           |
| ------------------- | ------ | ----------------------------------------------------- |
| `/transactions/new` | POST   | Submit a new transaction                              |
| `/mine`             | GET    | Perform mining, add a new block, and receive a reward |
| `/chain`            | GET    | Retrieve the full blockchain                          |

### 1. Submit a Transaction

```bash
curl -X POST http://localhost:5000/transactions/new \
     -H "Content-Type: application/json" \
     -d '{"sender":"alice","recipient":"bob","amount":5}'
```

**Response**

```json
{ "message": "Transaction will be in block 2" }
```

### 2. Mine a Block

```bash
curl http://localhost:5000/mine
```

**Response**

```json
{
  "message": "New block forged",
  "block": {
    "index": 2,
    "timestamp": 1627889187.123456,
    "transactions": [
      { "sender": "0", "recipient": "you", "amount": 1 }
    ],
    "nonce": 52347,
    "previous_hash": "0000ab34..."
  }
}
```

### 3. View the Full Chain

```bash
curl http://localhost:5000/chain
```

**Response**

```json
{
  "chain": [ ... ],
  "length": 2
}
```

---

## 🧠 How It Works

1. **Data Structures**

   * **Blocks**: Python dicts containing `index`, `timestamp`, `transactions`, `nonce`, `previous_hash`.
   * **Transactions**: Queued in `current_transactions` until mined.

2. **Proof-of-Work**

   * Find a `nonce` such that `SHA256(last_nonce + nonce)` starts with **four zeros**.
   * Miner receives a reward transaction from `"0"` to the node owner.

3. **REST API**

   * Built with Flask; exposes three endpoints for interaction.

---

## 🔄 Next Steps / Iterations

After verifying the basic node works, you can extend:

* ✅ **Peer-to-Peer Sync** (network layer)
* ✅ **Module Refactoring** (OOP structure)
* ✅ **Configurable Ports & Difficulty**
* ✅ **Persistent Storage** (SQLite, JSON files)
* ✅ **Alternate Consensus** (Proof-of-Authority)

---

## 📄 License

This project is released under the **MIT License**. See `LICENSE` for de
