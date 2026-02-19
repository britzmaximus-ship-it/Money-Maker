import time
import requests

DEX_URL = "https://api.dexscreener.com/latest/dex/pairs/solana"

def scan_once():
    print("🔎 Running scan cycle...")

    try:
        response = requests.get(DEX_URL, timeout=10)

        if response.status_code != 200:
            print(f"❌ Dex HTTP error: {response.status_code}")
            return

        data = response.json()

        pairs = data.get("pairs", [])

        if not pairs:
            print("⚠️ No pairs returned")
            return

        print(f"✅ Found {len(pairs)} pairs")

    except Exception as e:
        print(f"❌ Dex fetch error: {e}")

def run_forever():
    print("🚀 Money-Maker scanner started")

    while True:
        scan_once()
        print("✅ Scan cycle complete\n")
        time.sleep(20)