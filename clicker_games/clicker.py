from pynput.mouse import Button, Controller
import time
from threading import Event, Thread
from pynput import keyboard



mouse = Controller()
print("Current position: " + str(mouse.position))
print("Press Num Lock to start or stop clicking.")
print("Move the mouse to stop clicking, or press Esc to quit.")

auto_clicker_enabled = False
stop_clicking = Event()
exit_program = Event()
click_thread = None
listener = None

def auto_clicker():
    global auto_clicker_enabled

    print("clicker enabled")
    cur_pos = mouse.position
    while not stop_clicking.is_set() and not exit_program.is_set():
        if cur_pos != mouse.position:
            break
        mouse.click(Button.left, 1)
        time.sleep(0.002)

    auto_clicker_enabled = False
    stop_clicking.set()
    print("clicker disabled")


def start_clicker():
    global auto_clicker_enabled, click_thread

    if click_thread is not None and click_thread.is_alive():
        return

    auto_clicker_enabled = True
    stop_clicking.clear()
    click_thread = Thread(target=auto_clicker, daemon=True)
    click_thread.start()


def stop_clicker():
    global auto_clicker_enabled

    auto_clicker_enabled = False
    stop_clicking.set()


def on_press(key: keyboard.Key | keyboard.KeyCode | None) -> None:
    pass


def on_release(key: keyboard.Key | keyboard.KeyCode | None) -> None:
    if key == keyboard.Key.num_lock:
        if auto_clicker_enabled:
            stop_clicker()
        else:
            start_clicker()
    elif key == keyboard.Key.esc:
        print("Exiting program...")
        exit_program.set()
        stop_clicker()
        if listener is not None:
            listener.stop()

# Collect events until released
with keyboard.Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()

