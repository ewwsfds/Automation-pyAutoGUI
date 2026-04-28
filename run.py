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


run_amount = 28

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

            if line.strip().startswith("click-condition:"):
                data = line.split(":", 1)[1]

                number_part = data.split("(", 1)[0]

                coords = data.split("(", 1)[1].strip(")")
                x, y = coords.split(",")
                x, y = int(x), int(y)

                

                if "-" in number_part:
                    start, end = number_part.split("-")
                    start = int(start)
                    end = int(end)
                    if run_index+1>=start & run_index+1<end:
                        pyautogui.click(x, y)
                        print(f"[COND] Clicked at {x},{y} ({start}-{end}) runIndex={run_index}")
                        time.sleep(command_pause)
                
                else:
                    number_part=int(number_part)
                    if run_index+1>=number_part :
                        pyautogui.click(x, y)
                        print(f"[COND] Clicked at {x},{y} ({number_part}) runIndex={run_index}")
                        time.sleep(command_pause)  

                continue   
        

            elif line.strip().startswith("click"):
                coords = line.split(":")[1]
                x, y = coords.split(",")
                x, y = int(x), int(y)

                pyautogui.click(x, y)
                print(f"Clicked at {x},{y}")
                time.sleep(command_pause)

            elif line.strip().startswith("print:"):
                text = line.split(":", 1)[1]
                pyautogui.write(text)
                print(f"Typed: {text}")
                time.sleep(command_pause*2)



                   
                

            elif line.strip().startswith("hotkey:"):
                keys = [k.strip().lower() for k in line.split(":", 1)[1].split("+")]

                pyautogui.hotkey(*keys)

                print(f"Hotkey pressed: {'+'.join(keys)}")
                time.sleep(command_pause)

            elif line.strip().startswith("scroll:"):
                value = int(line.split(":", 1)[1])

                pyautogui.scroll(value)

                print(f"Scrolled: {value}")
                time.sleep(command_pause)

            elif line.strip().startswith("grid-repeat:"):
                # 1. remove everything up to first ":"
                data = line.split(":", 1)[1]

                # 2. index = until first "("
                index = data.split("(", 1)[0]
                index = int(index)
                # 3. coordArrayBlob = inside (...)
                coordArrayBlob = data.split("(", 1)[1].split(")", 1)[0]

                # 4. coorArray = split by ":"
                coorArray = coordArrayBlob.split(":")

                readIndex=(run_index) % (len(coorArray))+index-1


                x,y= coorArray[readIndex].split(",")
                pyautogui.click(int(x), int(y))
                print(f"[GRID-REPEAT] Clicked at {x},{y} (cycle={readIndex})")
                time.sleep(command_pause)
                continue


            elif line.strip().startswith("grid:"):
                Position = namedtuple("Position", ["x", "y"])

                numberValue = int(re.search(r'grid:(\d+)', line).group(1))
                coords = re.findall(r'(\d+),(\d+)', line)
                posList = [Position(int(x), int(y)) for x, y in coords]

                pyautogui.click(
                    posList[numberValue + run_index-1].x,
                    posList[numberValue + run_index-1].y
                )
                time.sleep(command_pause)




            elif line.strip().startswith("delay:"):
                seconds = float(line.split(":", 1)[1])
                print(f"Delaying for {seconds} seconds...")
                time.sleep(seconds)

            elif line.strip().startswith("url"):
                pyautogui.write(urlLinks[run_index])
                print(f"Pasted Link: {urlLinks[run_index]}")
                time.sleep(command_pause)

            else:
                print("Unknown command:", line)
