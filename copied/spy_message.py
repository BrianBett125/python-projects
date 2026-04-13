import time
import os
import sys

def clear_screen():
    # Cross-platform screen clear
    os.system("cls" if os.name == "nt" else "clear")

def self_destruct_message(message, seconds):
    print(f"Secret Message (will self-destruct in {seconds} seconds):\n")
    print(f">>> {message} <<<")
    time.sleep(seconds)
    clear_screen()
    print("The message has self-destructed. 💥\n")

if __name__ == "__main__":
    msg = input("Enter your secret message: ")
    try:
        delay = int(input("Display for how many seconds? "))
    except ValueError:
        print("Invalid input. Using default of 5 seconds.")
        delay = 5

    self_destruct_message(msg, delay)

