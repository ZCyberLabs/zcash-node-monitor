#!/usr/bin/env python3
import json
import requests
from base64 import b64encode

RPC_USER = "zcashuser"
RPC_PASSWORD = "megaLangesSicheresPasswort123!"
RPC_URL = "http://127.0.0.1:8232/"

def call_rpc(method, params=None):
    if params is None:
        params = []
    payload = {
        "jsonrpc": "1.0",
        "id": "zcash-monitor",
        "method": method,
        "params": params,
    }

    auth_str = f"{RPC_USER}:{RPC_PASSWORD}".encode("utf-8")
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Basic " + b64encode(auth_str).decode("utf-8"),
    }

    resp = requests.post(RPC_URL, headers=headers, data=json.dumps(payload))
    resp.raise_for_status()
    data = resp.json()
    if data.get("error"):
        raise RuntimeError(data["error"])
    return data["result"]

def main():
    try:
        bci = call_rpc("getblockchaininfo")
        net = call_rpc("getnetworkinfo")
    except Exception as e:
        print(f"[!] RPC error: {e}")
        return

    print("=== Zcash Node Monitor ===")
    print(f"Chain:             {bci.get('chain')}")
    print(f"Blocks:            {bci.get('blocks')}/{bci.get('estimatedheight')}")
    print(f"Verification prog: {bci.get('verificationprogress'):.6f}")
    print(f"IBD complete:      {bci.get('initial_block_download_complete')}")
    print(f"Size on disk:      {bci.get('size_on_disk')} bytes")
    print()
    print(f"Peers:             {net.get('connections')}")
    print(f"Version:           {net.get('version')} {net.get('subversion')}")
    print(f"Protocol version:  {net.get('protocolversion')}")
    print()
    print("Value pools:")
    for pool in bci.get("valuePools", []):
        print(f"  - {pool['id']}: {pool['chainValue']} ZEC (monitored={pool['monitored']})")

if __name__ == "__main__":
    main()
