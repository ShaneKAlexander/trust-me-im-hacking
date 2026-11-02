import random
import time

def type_line(text):
    for character in text:
        print(character, end="", flush=True)
        time.sleep(0.025)
    print()

print("\n=== TRUST ME, I'M HACKING ===")
print("Just a joke. No actual hacking.\n")

while True:
    name = input("Target's name (or 'quit'): ").strip()

    if name.lower() == "quit":
        break
    if not name:
        continue

    steps = [
        f"\nLocating {name}...",
        "Connecting to the mainframe...",
        "Asking the firewall nicely...",
        "Access granted. That was concerning.",
        "Downloading remaining brain cells...",
        "Download complete: 0 bytes.",
        "Compiling classified findings...",
    ]

    for step in steps:
        type_line(f"> {step}")
        time.sleep(random.uniform(0.4, 1.0))

    results = [
        f"{name}'s last two brain cells are fighting for third place.",
        f"{name} would lose a staring contest to a loading screen.",
        f"{name}'s biggest weakness is clicking 'free Robux'.",
        f"{name} has been running on 2% battery since 2019.",
        f"{name}'s search history is just 'how to look busy'.",
    ]

    print("\n" + "=" * 50)
    type_line(random.choice(results))
    print("=" * 50 + "\n")
