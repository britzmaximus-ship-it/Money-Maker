import time
import requests

DEX_URL = "https://api.dexscreener.com/latest/dex/pairs/solana"

SCAN_INTERVAL = 20  # seconds


def fetch_dex():
    try:
        r = requests.get(DEX_URL, timeout=10)

        if r.status_code != 200:
            print(f"❌ Dex HTTP error: {r.status_code}")
            return []

        try:
            data = r.json()
        except Exception as e:
            print("❌ Dex JSON parse error")
            print("Raw response:", r.text[:200])
            return []

        pairs = data.get("pairs", [])
        return pairs[:5]  # only show first 5 for now

    except Exception as e:
        print(f"❌ Dex fetch error: {e}")
        return []


def run_forever():
    print("🚀 Money-Maker scanner started")

    while True:
        print("🔎 Running scan cycle...")

        pairs = fetch_dex()

        if pairs:
            print(f"✅ Pulled {len(pairs)} pairs")
        else:
            print("⚠️ No pairs returned")

        print("✅ Scan cycle complete\n")
        time.sleep(SCAN_INTERVAL)


if __name__ == "__main__":
    run_forever()