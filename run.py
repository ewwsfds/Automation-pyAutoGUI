import pyautogui
import time
import glob
import re
from collections import namedtuple

# click:x,y
# Print: hello world
# Hotkey: ctrl+tab+enter
# Grid:8(x,y:x,y:x,y)
# Delay:46
# scroll:x

run_amount = 3

command_pause=1

image_pause=2
for run_index in range(run_amount):

    # Find all files that start with "button" and end with ".png"
    img_files = glob.glob("button*.png")

    for img_run_index in range(len(img_files)):

        image_name = f"button{img_run_index+1}.png"

        # 🔁 Keep trying until image is found
        while True:
            try:
                pos = pyautogui.locateOnScreen(image_name, confidence=0.8)
            except pyautogui.ImageNotFoundException:
                pos = None  # Treat as "not found"

            if pos:
                print(f"Found {image_name}")
                center = pyautogui.center(pos)
                pyautogui.click(center)
                time.sleep(command_pause)
                break
            else:
                print(f"{image_name} not found, retrying in 2s...")
                time.sleep(image_pause)


        # Read file and store lines into list
        with open(f"button{img_run_index+1}.txt", "r") as file:
            lines = file.readlines()

        # Remove newline characters
        lines = [line.strip() for line in lines]

        # Loop through each line (foreach)
        for line in lines:
            line = line.strip().lower()


            if line.startswith("click"):
                coords = line.split(":")[1]
                x, y = coords.split(",")
                x, y = int(x), int(y)

                pyautogui.click(x, y)
                print(f"Clicked at {x},{y}")
                time.sleep(command_pause)

            elif line.startswith("print:"):
                text = line.split(":", 1)[1]
                pyautogui.write(text)
                print(f"Typed: {text}")
                time.sleep(command_pause)

            elif line.startswith("hotkey:"):
                keys = line.split(":", 1)[1].split("+")
                pyautogui.hotkey(*keys)
                print(f"Hotkey pressed: {'+'.join(keys)}")
                time.sleep(command_pause)

            elif line.startswith("scroll:"):
                value = int(line.split(":", 1)[1])

                pyautogui.scroll(value)

                print(f"Scrolled: {value}")
                time.sleep(command_pause)


            elif line.startswith("grid:"):
                Position = namedtuple("Position", ["x", "y"])

                numberValue = int(re.search(r'Grid:(\d+)', line).group(1))
                coords = re.findall(r'(\d+),(\d+)', line)
                posList = [Position(int(x), int(y)) for x, y in coords]

                pyautogui.click(
                    posList[numberValue + run_index].x,
                    posList[numberValue + run_index].y
                )
                time.sleep(command_pause)

            elif line.startswith("delay:"):
                seconds = float(line.split(":", 1)[1])
                print(f"Delaying for {seconds} seconds...")
                time.sleep(seconds)

            else:
                print("Unknown command:", line)
