import pyautogui
import time
import glob
import re
from collections import namedtuple
import os
# click:x,y
# Print: hello world
# Hotkey: ctrl+tab+enter
# Grid:8(x,y:x,y:x,y)
# Delay:46
# scroll:x
# url
# click-condition:3(500,300)
# click-condition:3-6(500,300)
# grid-repeat:1(100,100:200,100:300,100:)


urlLinks = [
    "https://www.tiktok.com/@fortniteclassic847/video/7513942181837589791",
    "https://www.tiktok.com/@fortniteclassic847/video/7513956777130528030",
]


run_amount = 30

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
                pos = pyautogui.locateOnScreen(image_name, grayscale=False)
            except pyautogui.ImageNotFoundException:
                pos = None  # Treat as "not found"a

            if pos:
                print(f"Found {image_name}")
                print(f"Run Index: {run_index+1} / {run_amount}")
                center = pyautogui.center(pos)
                pyautogui.click(center)
                time.sleep(command_pause)
                break
            else:
                print(f"{image_name} not found, retrying in 2s...")
                print(f"Run Index: {run_index} / {run_amount}")
                time.sleep(image_pause)

        path = f"button{img_run_index+1}.txt"
        if not os.path.exists(path):
            continue

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
                time.sleep(command_pause*2)


            elif line.startswith("click-condition:"):
                data = line.split(":", 1)[1]

                # format: number(x,y) OR start-end(x,y)
                number_part, coords_part = data.split("(")

                coords = coords_part.strip(")")
                x, y = coords.split(",")
                x, y = int(x), int(y)

                if "-" in number_part:
                    start, end = map(int, number_part.split("-"))

                    # convert to 0-based like your old logic
                    start_idx = start - 1
                    end_idx = end - 1

                    if start_idx <= run_index <= end_idx:
                        pyautogui.click(x, y)
                        print(f"[COND] Clicked at {x},{y} ({start}-{end}) runIndex={run_index}")
                        time.sleep(command_pause)
                    else:
                        print(f"[COND] Skipped {x},{y} (runIndex={run_index} not in {start}-{end})")

                else:
                    number = int(number_part)

                    if run_index >= number - 1:
                        pyautogui.click(x, y)
                        print(f"[COND] Clicked at {x},{y} (runIndex={run_index} >= {number-1})")
                        time.sleep(command_pause)
                    else:
                        print(f"[COND] Skipped click at {x},{y} (runIndex={run_index} < {number-1})")

            elif line.startswith("hotkey:"):
                keys = [k.strip().lower() for k in line.split(":", 1)[1].split("+")]

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

                numberValue = int(re.search(r'grid:(\d+)', line).group(1))
                coords = re.findall(r'(\d+),(\d+)', line)
                posList = [Position(int(x), int(y)) for x, y in coords]

                pyautogui.click(
                    posList[numberValue + run_index-1].x,
                    posList[numberValue + run_index-1].y
                )
                time.sleep(command_pause)


            elif line.startswith("grid-repeat:"):
                Position = namedtuple("Position", ["x", "y"])

                numberValue = int(re.search(r'grid-repeat:(\d+)', line).group(1))
                coords = re.findall(r'(\d+),(\d+)', line)
                posList = [Position(int(x), int(y)) for x, y in coords]

                index = numberValue + run_index - 1

                # wrap index
                wrapped_index = index % len(posList)

                # how many times we looped over the list
                cycle = index // len(posList)

                # apply offset per cycle (you can tweak multiplier logic here)
                offset_x = cycle * posList[0].x
                offset_y = cycle * posList[0].y

                final_x = posList[wrapped_index].x + offset_x
                final_y = posList[wrapped_index].y + offset_y

                pyautogui.click(final_x, final_y)
                print(f"[GRID-REPEAT] Clicked at {final_x},{final_y} (cycle={cycle})")
                time.sleep(command_pause)



            elif line.startswith("delay:"):
                seconds = float(line.split(":", 1)[1])
                print(f"Delaying for {seconds} seconds...")
                time.sleep(seconds)

            elif line.startswith("url"):
                pyautogui.write(urlLinks[run_index])
                print(f"Pasted Link: {urlLinks[run_index]}")
                time.sleep(command_pause)

            else:
                print("Unknown command:", line)
