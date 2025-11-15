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

