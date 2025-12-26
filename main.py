import keyboard
import time

INTERVAL = 60  # секунд
last_time = 0

def on_key(event):
    global last_time
    now = time.time()

    if now - last_time >= INTERVAL:
        last_time = now
        print(f"Принята клавиша: {event.name}")
        return
    else:
        print("Клавиша заблокирована")
        return False

keyboard.hook(on_key, suppress=True)
keyboard.wait()
