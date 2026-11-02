import os
import random
import time

# Enable terminal colours on Windows.
os.system("")

GREEN = "\033[92m"
RED = "\033[91m"
DIM = "\033[2m"
RESET = "\033[0m"


def type_line(text, delay=0.012):
    for char in text:
        print(char, end="", flush=True)
        time.sleep(delay)
    print()


def log(message, level="OK"):
    stamp = time.strftime("%H:%M:%S")
    colour = RED if level == "WARN" else GREEN
    type_line(f"{DIM}{stamp}{RESET} {colour}[{level}]{RESET} {message}")
    time.sleep(random.uniform(0.2, 0.6))


def progress(label):
    for percent in range(0, 101, 4):
        filled = percent // 5
        bar = "#" * filled + "-" * (20 - filled)
        print(
            f"\r{GREEN}{label} [{bar}] {percent:3d}%{RESET}",
            end="",
            flush=True,
        )
        time.sleep(random.uniform(0.025, 0.08))
    print()


def crack():
    characters = "0123456789ABCDEF"
    for _ in range(24):
        noise = "".join(random.choices(characters, k=32))
        print(f"\r{GREEN}Testing hash: {noise}{RESET}", end="", flush=True)
        time.sleep(0.055)
    print()
    log("Password recovered: password123", "WARN")
    log("Even the password gave up trying.")


def run_scan(name):
    # These addresses are reserved for documentation.
    # No network requests are made.
    address = f"192.0.2.{random.randint(1, 254)}"

    print(f"\n{GREEN}{'=' * 58}")
    print("  GHOST//SCAN — FICTIONAL TARGET ANALYSIS")
    print(f"{'=' * 58}{RESET}\n")

    log(f"Target alias: {name}")
    log(f"Assigned simulation address: {address}")
    log("Initializing simulated reconnaissance")

    for port, service in [(22, "SSH"), (80, "HTTP"), (443, "HTTPS")]:
        log(f"{address}:{port:<5} OPEN  {service}")

    log("Weak authentication detected", "WARN")
    crack()
    progress("Analyzing digital footprint")

    log("Attention span: shorter than this loading bar", "WARN")
    log("Unfinished projects: storage limit exceeded", "WARN")
    log("Original thoughts: no matching records", "WARN")

    progress("Compiling final assessment")

    roasts = [
        f"{name}, you have the confidence of an expert "
        "and the results of a tutorial skipped halfway.",

        f"{name}, your potential has been a coming-soon page "
        "for so long the domain expired.",

        f"{name}, you aren't mysterious. "
        "People just stopped asking follow-up questions.",

        f"{name}, your entire personality could be replaced "
        "by three recommended videos.",

        f"{name}, you bring the energy of a software update "
        "nobody asked for and everyone postpones.",

        f"{name}, your plans have more abandoned branches "
        "than a dead GitHub account.",

        f"{name}, you talk like the final boss "
        "and perform like the optional tutorial.",

        f"{name}, even your imaginary haters "
        "have moved on to more interesting people.",
    ]

    print(f"\n{RED}{'=' * 58}")
    print("  CLASSIFIED FINDING")
    print(f"{'=' * 58}{RESET}")
    type_line(random.choice(roasts), delay=0.035)
    print(f"\n{GREEN}> Simulation complete. Ego recovery pending.{RESET}\n")


print(f"{GREEN}TRUST ME, I'M HACKING{RESET}")
print("Offline simulation. No real scanning or data access.\n")

try:
    while True:
        name = input("Target name (or 'quit'): ").strip()

        if name.lower() == "quit":
            break
        if not name:
            continue

        # Remove control characters from terminal input.
        name = "".join(char for char in name if char.isprintable())[:40]
        if name:
            run_scan(name)

except (KeyboardInterrupt, EOFError):
    print(f"\n{RESET}Session closed.")
