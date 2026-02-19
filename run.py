import time

def run_forever():
    print("🚀 Money-Maker scanner started")

    while True:
        try:
            print("🔎 Running scan cycle...")
            
            # placeholder for future scanner logic
            
            print("✅ Scan cycle complete")
        except Exception as e:
            print(f"❌ Error in loop: {e}")

        time.sleep(15)


if __name__ == "__main__":
    run_forever()