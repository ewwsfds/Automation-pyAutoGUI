from pynput import keyboard
import pyautogui

# =========================
# Mouse Position Recorder
# =========================
#
# K   = Save mouse position and print Click:x,y
# J   = Clear grid list (start new recording)
# L   = Add current mouse position to Grid list
# P   = Print Grid:(x1,y1:x2,y2:...) 
# ESC = Exit program
# =========================

pos_list = []

def on_press(key):
    global pos_list

    try:
        if key.char.lower() == 'k':
            x, y = pyautogui.position()
            print(f"Click:{x},{y}")

        elif key.char.lower() == 'j':
            pos_list.clear()
            print("Grid list cleared.")

        elif key.char.lower() == 'l':
            x, y = pyautogui.position()
            pos_list.append((x, y))
            print(f"Added to Grid: {x},{y}")

        elif key.char.lower() == 'p':
            if pos_list:
                grid_string = ":".join(f"{x},{y}" for x, y in pos_list)
                print(f"Grid:({grid_string})")
            else:
                print("Grid list is empty.")

    except AttributeError:
        # Special keys
        if key == keyboard.Key.esc:
            print("Exiting program...")
            return False  # stops listener

# Start keyboard listener
with keyboard.Listener(on_press=on_press) as listener:
    listener.join()
