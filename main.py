import os
import random
import shutil
import time

os.system("")  # Enable terminal colours on Windows.

GREEN = "\033[92m"
DIM = "\033[2m"
RED = "\033[91m"
RESET = "\033[0m"
CHARS = "0123456789ABCDEF"


def width():
    return min(shutil.get_terminal_size().columns - 1, 90)


def clear():
    print("\033[2J\033[H", end="", flush=True)


def say(text, delay=0.018):
    for char in text:
        print(char, end="", flush=True)
        time.sleep(delay)
    print()


def log(text):
    stamp = time.strftime("%H:%M:%S")
    say(f"{DIM}{stamp}{RESET}{GREEN}  > {text}", 0.008)
    time.sleep(random.uniform(0.15, 0.45))


def code_storm(seconds=2):
    end = time.monotonic() + seconds
    while time.monotonic() < end:
        row = "".join(
            random.choice(CHARS + "   ") for _ in range(width())
        )
        print(random.choice([GREEN, DIM + GREEN]) + row)
        time.sleep(0.035)
    print(GREEN, end="")


def progress(label):
    print()
    percent = 0
    while percent < 100:
        percent = min(100, percent + random.randint(1, 6))
        filled = percent // 4
        bar = "█" * filled + "░" * (25 - filled)
        print(
            f"\r  {label} [{bar}] {percent:3d}%",
            end="",
            flush=True,
        )
        time.sleep(random.uniform(0.03, 0.12))
    print("\n")


def decrypt():
    secret = "ACCESS GRANTED"
    print()
    for step in range(len(secret) + 1):
        for _ in range(3):
            noise = "".join(
                random.choice(CHARS) for _ in range(len(secret) - step)
            )
            print(
                f"\r  DECRYPTING :: {secret[:step]}{noise}",
                end="",
                flush=True,
            )
            time.sleep(0.055)
    print("\n")


def run(name):
    clear()
    print(GREEN)
    print("═" * width())
    print("   G H O S T   P R O T O C O L")
    print("   CINEMATIC TERMINAL // OFFLINE SIMULATION")
    print("═" * width())
    print()

    log("BOOTING SECURE CONSOLE...")
    log("Loading cryptographic modules")
    code_storm(1.5)

    log(f"TARGET LOCKED :: {name}")
    log("Routing through simulated relay nodes")

    for node in range(1, 5):
        token = "".join(random.choices(CHARS, k=16))
        log(f"RELAY {node:02d} :: {token} :: CONNECTED")

    progress("ESTABLISHING UPLINK")

    log("PERIMETER DETECTED")
    log("Analyzing defensive signatures")
    code_storm(1.2)
    progress("DECODING FIREWALL")

    print(RED)
    say("  [!] COUNTERMEASURE DETECTED", 0.045)
    time.sleep(0.8)
    say("  [!] CONNECTION UNSTABLE", 0.045)
    time.sleep(0.7)
    print(GREEN)

    log("Switching to secondary channel")
    code_storm(1.5)
    decrypt()

    log("SIMULATED ARCHIVE UNLOCKED")
    progress("RECONSTRUCTING TARGET PROFILE")

    findings = [
        "EGO SIZE ............. EXCEEDS AVAILABLE MEMORY",
        "COMMON SENSE ......... FILE NOT FOUND",
        "BRAIN ACTIVITY ....... CONNECTION TIMED OUT",
        "LIFE PLANS ........... STILL IN DRAFTS",
    ]
    for finding in findings:
        log(finding)
        time.sleep(0.35)

    time.sleep(1)
    print("\n" + "═" * width())
    say("  FINAL INTELLIGENCE REPORT", 0.055)
    print("═" * width() + "\n")

    roasts = [
        f"{name}, you talk like the final boss "
        "and perform like the tutorial NPC.",

        f"{name}, your potential has been 'coming soon' "
        "for so long the domain expired.",

        f"{name}, you're living proof that confidence "
        "doesn't require supporting evidence.",

        f"{name}, even your imaginary haters "
        "found someone more interesting.",

        f"{name}, your brain has so many open tabs "
        "and somehow none of them are loading.",
    ]

    say(random.choice(roasts), 0.045)
    print()
    log("SESSION TERMINATED // EGO DAMAGE CONFIRMED")
    print(RESET)


try:
    while True:
        print(GREEN)
        name = input("\nENTER TARGET NAME (or quit): ").strip()
        name = "".join(c for c in name if c.isprintable())[:40]

        if name.lower() == "quit":
            break
        if name:
            run(name)
            input("\nPress Enter to start another session...")

except (KeyboardInterrupt, EOFError):
    pass

finally:
    print(RESET)
