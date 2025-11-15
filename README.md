# Zcash Node Monitor

Simple Python script to monitor a local `zcashd` full node via JSON-RPC.

## Features

- Shows basic chain and sync status:
  - Chain name
  - Current blocks vs. estimated height
  - Verification progress
  - Initial block download state
- Displays node and network info:
  - Peers
  - Version and protocol version
- Prints value pools (transparent, sprout, sapling, orchard, lockbox)

## Requirements

- Running `zcashd` node with RPC enabled
- Python 3
- `requests` library

You can install `requests` via:

```bash
pip install --user requests
