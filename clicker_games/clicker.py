from pynput.mouse import Button, Controller
import time
from pynput.mouse import Listener
import sys
from threading import Thread
from pynput import keyboard



mouse = Controller()
print ("Current position: " + str(mouse.position))
auto_clicker_enabled = False

def auto_cicker():
    global auto_clicker_enabled
    print("clicker enabled")
    cur_pos = mouse.position
    while True:
        if cur_pos != mouse.position:
            break
        mouse.click(Button.left, 1)
        time.sleep(0.002)
    print("clicker disabled")




def on_press(key):
    pass

def on_release(key):
    global auto_clicker_enabled

    if key == keyboard.Key.num_lock:
        auto_clicker_enabled = not auto_clicker_enabled
        t = Thread(target=auto_cicker, args=[])
        t.run()
    elif key == keyboard.Key.esc:
        sys.exit(0)

# Collect events until released
with keyboard.Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()

# ...or, in a non-blocking fashion:
keyboard_listener = keyboard.Listener(
    on_press=on_press,
    on_release=on_release)
keyboard_listener.start()

