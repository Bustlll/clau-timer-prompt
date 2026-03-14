#!/usr/bin/env python3
"""
Timer script that counts down from specified hours and minutes,
optionally presses ESC N times, types a message, and presses Enter once.
"""

import time
import sys
from pynput.keyboard import Controller, Key

def countdown_timer(hours, minutes, esc_presses, message):
    total_seconds = (hours * 3600) + (minutes * 60)

    print(f"Starting countdown: {hours}h {minutes}m ({total_seconds} seconds)")
    print("Press Ctrl+C to stop\n")

    while total_seconds > 0:
        h = total_seconds // 3600
        m = (total_seconds % 3600) // 60
        s = total_seconds % 60

        print(f"\rTime remaining: {h:02d}:{m:02d}:{s:02d}", end="", flush=True)
        time.sleep(1)
        total_seconds -= 1

    print("\n\nTIME IS UP\n")

    keyboard = Controller()
    time.sleep(0.5)

    # Press ESC specified number of times if > 0
    for _ in range(esc_presses):
        keyboard.press(Key.esc)
        keyboard.release(Key.esc)
        time.sleep(0.1)

    # Type the message
    keyboard.type(message)
    time.sleep(0.1)

    # Press Enter once
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)

    print(f"ESC pressed {esc_presses} time(s)")
    print(f'Message sent: "{message}"')
    print("Enter pressed once")

def main():
    if len(sys.argv) < 4:
        print("Usage:")
        print('  python3 timerMessage.py [-esc <count>] <hours> <minutes> "<message>"')
        sys.exit(1)

    try:
        # Default values
        esc_presses = 0

        # Check if -esc flag is used
        if sys.argv[1] == "-esc":
            esc_presses = int(sys.argv[2])
            hours = int(sys.argv[3])
            minutes = int(sys.argv[4])
            message = sys.argv[5]
        else:
            hours = int(sys.argv[1])
            minutes = int(sys.argv[2])
            message = sys.argv[3]

        # Validations
        if esc_presses < 0 or hours < 0 or minutes < 0:
            raise ValueError("Values must be non-negative")
        if hours == 0 and minutes == 0:
            raise ValueError("Timer duration must be greater than zero")

        countdown_timer(hours, minutes, esc_presses, message)

    except (ValueError, IndexError) as e:
        print(f"Error: {e}")
        print('Example with ESC: python3 timerMessage.py -esc 1 2 30 "continue"')
        print('Example without ESC: python3 timerMessage.py 0 1 "ls"')
        sys.exit(1)
    except KeyboardInterrupt:
        print("\nTimer stopped by user.")
        sys.exit(0)

if __name__ == "__main__":
    main()
