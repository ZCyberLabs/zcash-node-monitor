# Zcash Node Monitor

A lightweight CLI tool to inspect a local `zcashd` full node using JSON-RPC.  
Designed for developers, node operators, researchers, and anyone working with the Zcash network.

---

## Features

### Chain and sync status
- Current block height
- Estimated block height
- Verification progress
- Initial block download state

### Node and network information
- Node version
- Protocol version
- Peer count
- Basic networking info

### Value pools
- Transparent pool
- Sprout pool
- Sapling pool
- Orchard pool
- Lockbox (if exposed)

---

## Requirements

- Python 3
- A running `zcashd` node with RPC enabled
- The `requests` Python library

Install the dependency via:

pip install --user requests

---

## Installation

Clone the repository:

git clone https://github.com/ZCyberLabs/zcash-node-monitor


(Optional) create a virtual environment:

python3 -m venv .venv
source .venv/bin/activate
pip install requests


---

## Usage

Run the monitor:


The script automatically reads RPC configuration from:

~/.zcash/zcash.conf

Future versions will support CLI flags like:

--rpcuser
--rpcpassword
--rpchost
--rpcport

---

## Roadmap

- CLI argument support
- JSON output mode
- Prometheus metrics exporter
- Docker image
- Systemd monitoring service
- Alerting integrations
- Improved error handling

---

## License

MIT License  
See the LICENSE file for full details.



