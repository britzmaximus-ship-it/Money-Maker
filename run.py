import time

def run_forever():
    print("✅ Booted: run_forever() started")
    while True:
        print("✅ Still alive...")
        time.sleep(10)

if __name__ == "__main__":
    run_forever()