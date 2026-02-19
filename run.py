import time
import requests

DEX_URL = "https://api.dexscreener.com/latest/dex/pairs/solana"

def fetch_pairs():
    try:
        r = requests.get(DEX_URL, timeout=10)
        data = r.json()
        pairs = data.get("pairs", [])
        print(f"📊 Found {len(pairs)} pairs")
    except Exception as e:
        print(f"❌ Dex fetch error: {e}")

def run_forever():
    print("🚀 Money-Maker scanner started")

    while True:
        try:
            print("🔎 Running scan cycle...")
            fetch_pairs()
            print("✅ Scan cycle complete")
        except Exception as e:
            print(f"❌ Error in loop: {e}")

        time.sleep(20)


if __name__ == "__main__":
    run_forever()