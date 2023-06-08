'''
Actively track user input (once/second to limit performance impact) and simulate keypress after 2 minutes of inactivity.
After simulation the script will pause for one minute waiting for user input before continuing this behavior until input is observed (once/minute).
'''
import time
from pynput import mouse, keyboard
from datetime import datetime, timedelta

keyboard_controller = keyboard.Controller()
user_last_active = datetime.now()
stop_app = False

def reset_time():
    global user_last_active 
    user_last_active = datetime.now()

def on_press(key):
    global stop_app
    reset_time()

    if key == keyboard.Key.end:
        print("Exiting...")
        stop_app = True

def on_release(key):
    reset_time()

def on_move(x,y):
    reset_time()

def on_click(x, y, button, pressed):
    reset_time()

def on_scroll(x, y, dx, dy):
    reset_time()

def main():
    global user_last_active, keyboard_controller

    keyboard.Listener(
        on_press=on_press,
        on_release=on_release
    ).start()

    mouse.Listener(
        on_click=on_click,
        on_move=on_move,
        on_scroll=on_scroll
    ).start()

    while not stop_app:
        offset_time = user_last_active + timedelta(minutes=2)
        now = datetime.now()
        
        if now >= offset_time:
            keyboard_controller.press(keyboard.Key.ctrl)
            keyboard_controller.release(keyboard.Key.ctrl)
            time.sleep(60)
        time.sleep(1)

if __name__ == "__main__":
    main()