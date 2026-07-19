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
    "https://www.tiktok.com/@t1een.cybersec.sh/video/7639866959667973409?is_from_webapp=1&sender_device=pc&web_id=7664238020274472470",
    "https://www.tiktok.com/@t1een.cybersec.sh/video/7619766964977814816?is_from_webapp=1&sender_device=pc&web_id=7664238020274472470",
    "https://www.tiktok.com/@t1een.cybersec.sh/video/7609477651111218454?is_from_webapp=1&sender_device=pc&web_id=7664238020274472470",
    "https://www.tiktok.com/@t1een.cybersec.sh/video/7649866379025222944?is_from_webapp=1&sender_device=pc&web_id=7664238020274472470",
    "https://www.tiktok.com/@t1een.cybersec.sh/video/7510307522985594134?is_from_webapp=1&sender_device=pc&web_id=7664238020274472470",
    "https://www.tiktok.com/@t1een.cybersec.sh/video/7655900336938405153?is_from_webapp=1&sender_device=pc&web_id=7664238020274472470",
    "https://www.tiktok.com/@t1een.cybersec.sh/video/7503413965221793046?is_from_webapp=1&sender_device=pc&web_id=7664238020274472470",
    "https://www.tiktok.com/@t1een.cybersec.sh/video/7624929967935147297?is_from_webapp=1&sender_device=pc&web_id=7664238020274472470",
    "https://www.tiktok.com/@t1een.cybersec.sh/video/7615627101336587542?is_from_webapp=1&sender_device=pc&web_id=7664238020274472470",
    "https://www.tiktok.com/@t1een.cybersec.sh/video/7616077748225854752?is_from_webapp=1&sender_device=pc&web_id=7664238020274472470",
    "https://www.tiktok.com/@t1een.cybersec.sh/video/7617837767040519456?is_from_webapp=1&sender_device=pc&web_id=7664238020274472470",
    "https://www.tiktok.com/@t1een.cybersec.sh/video/7539943298203520278?is_from_webapp=1&sender_device=pc&web_id=7664238020274472470",
    "https://www.tiktok.com/@t1een.cybersec.sh/video/7512197201079160086?is_from_webapp=1&sender_device=pc&web_id=7664238020274472470",
    "https://www.tiktok.com/@t1een.cybersec.sh/video/7646501458245963041?is_from_webapp=1&sender_device=pc&web_id=7664238020274472470",
    "https://www.tiktok.com/@t1een.cybersec.sh/video/7654209363799821600?is_from_webapp=1&sender_device=pc&web_id=7664238020274472470",
    "https://www.tiktok.com/@t1een.cybersec.sh/video/7645701298590895393?is_from_webapp=1&sender_device=pc&web_id=7664238020274472470",
    "https://www.tiktok.com/@t1een.cybersec.sh/video/7504361253951819030?is_from_webapp=1&sender_device=pc&web_id=7664238020274472470",
    "https://www.tiktok.com/@t1een.cybersec.sh/video/7630905445623860512?is_from_webapp=1&sender_device=pc&web_id=7664238020274472470",
    "https://www.tiktok.com/@t1een.cybersec.sh/video/7633413789106359585?is_from_webapp=1&sender_device=pc&web_id=7664238020274472470",
    "https://www.tiktok.com/@t1een.cybersec.sh/video/7539326472020856086?is_from_webapp=1&sender_device=pc&web_id=7664238020274472470",
    "https://www.tiktok.com/@t1een.cybersec.sh/video/7621656277688601889?is_from_webapp=1&sender_device=pc&web_id=7664238020274472470",
    "https://www.tiktok.com/@t1een.cybersec.sh/video/7499377518739229974?is_from_webapp=1&sender_device=pc&web_id=7664238020274472470",
    "https://www.tiktok.com/@t1een.cybersec.sh/video/7656659076658564384?is_from_webapp=1&sender_device=pc&web_id=7664238020274472470",
    "https://www.tiktok.com/@t1een.cybersec.sh/video/7616764177922673952?is_from_webapp=1&sender_device=pc&web_id=7664238020274472470",
    "https://www.tiktok.com/@t1een.cybersec.sh/video/7615294848324668694?is_from_webapp=1&sender_device=pc&web_id=7664238020274472470",
    "https://www.tiktok.com/@t1een.cybersec.sh/video/7496207315503222038?is_from_webapp=1&sender_device=pc&web_id=7664238020274472470",
    "https://www.tiktok.com/@t1een.cybersec.sh/video/7503412090225429782?is_from_webapp=1&sender_device=pc&web_id=7664238020274472470",
    "https://www.tiktok.com/@t1een.cybersec.sh/video/7511443893607517462?is_from_webapp=1&sender_device=pc&web_id=7664238020274472470",
    "https://www.tiktok.com/@t1een.cybersec.sh/video/7648071835585760545?is_from_webapp=1&sender_device=pc&web_id=7664238020274472470",
    "https://www.tiktok.com/@t1een.cybersec.sh/video/7496221422440779030?is_from_webapp=1&sender_device=pc&web_id=7664238020274472470",
    "https://www.tiktok.com/@t1een.cybersec.sh/video/7645703190855355680?is_from_webapp=1&sender_device=pc&web_id=7664238020274472470",
    "https://www.tiktok.com/@t1een.cybersec.sh/video/7630901945892408608?is_from_webapp=1&sender_device=pc&web_id=7664238020274472470",
    "https://www.tiktok.com/@t1een.cybersec.sh/video/7508454835323227414?is_from_webapp=1&sender_device=pc&web_id=7664238020274472470",
    "https://www.tiktok.com/@t1een.cybersec.sh/video/7616851663202127137?is_from_webapp=1&sender_device=pc&web_id=7664238020274472470",
    "https://www.tiktok.com/@t1een.cybersec.sh/video/7615241552562064662?is_from_webapp=1&sender_device=pc&web_id=7664238020274472470",
    "https://www.tiktok.com/@t1een.cybersec.sh/video/7561912116890897686?is_from_webapp=1&sender_device=pc&web_id=7664238020274472470",
    "https://www.tiktok.com/@t1een.cybersec.sh/photo/7652228065292061985?is_from_webapp=1&sender_device=pc&web_id=7664238020274472470",
    "https://www.tiktok.com/@t1een.cybersec.sh/video/7621207870566042913?is_from_webapp=1&sender_device=pc&web_id=7664238020274472470",
    "https://www.tiktok.com/@t1een.cybersec.sh/video/7642889619603721504?is_from_webapp=1&sender_device=pc&web_id=7664238020274472470",
    "https://www.tiktok.com/@t1een.cybersec.sh/video/7582345461898464534?is_from_webapp=1&sender_device=pc&web_id=7664238020274472470",
    "https://www.tiktok.com/@t1een.cybersec.sh/video/7615633427731057942?is_from_webapp=1&sender_device=pc&web_id=7664238020274472470",
    "https://www.tiktok.com/@t1een.cybersec.sh/video/7656174434465680673?is_from_webapp=1&sender_device=pc&web_id=7664238020274472470",
    "https://www.tiktok.com/@t1een.cybersec.sh/video/7627226680284695840?is_from_webapp=1&sender_device=pc&web_id=7664238020274472470",
    "https://www.tiktok.com/@t1een.cybersec.sh/video/7562219145438366999?is_from_webapp=1&sender_device=pc&web_id=7664238020274472470",
    "https://www.tiktok.com/@t1een.cybersec.sh/video/7650728502953594145?is_from_webapp=1&sender_device=pc&web_id=7664238020274472470",
    "https://www.tiktok.com/@t1een.cybersec.sh/video/7642896866157399329?is_from_webapp=1&sender_device=pc&web_id=7664238020274472470",
    "https://www.tiktok.com/@t1een.cybersec.sh/video/7629322429277441312?is_from_webapp=1&sender_device=pc&web_id=7664238020274472470",
    "https://www.tiktok.com/@t1een.cybersec.sh/video/7502600953472781590?is_from_webapp=1&sender_device=pc&web_id=7664238020274472470",
    "https://www.tiktok.com/@t1een.cybersec.sh/video/7561842092645879062?is_from_webapp=1&sender_device=pc&web_id=7664238020274472470",
    "https://www.tiktok.com/@t1een.cybersec.sh/video/7653636090653429025?is_from_webapp=1&sender_device=pc&web_id=7664238020274472470",
    "https://www.tiktok.com/@t1een.cybersec.sh/video/7562597100697947414?is_from_webapp=1&sender_device=pc&web_id=7664238020274472470",
    "https://www.tiktok.com/@t1een.cybersec.sh/video/7660901450863709472?is_from_webapp=1&sender_device=pc&web_id=7664238020274472470",
    "https://www.tiktok.com/@t1een.cybersec.sh/video/7661019407719714081?is_from_webapp=1&sender_device=pc&web_id=7664238020274472470",
    "https://www.tiktok.com/@t1een.cybersec.sh/video/7633904994588036384?is_from_webapp=1&sender_device=pc&web_id=7664238020274472470",
    "https://www.tiktok.com/@t1een.cybersec.sh/video/7562949169405496598?is_from_webapp=1&sender_device=pc&web_id=7664238020274472470",
    "https://www.tiktok.com/@t1een.cybersec.sh/video/7662504567187295520?is_from_webapp=1&sender_device=pc&web_id=7664238020274472470",
    "https://www.tiktok.com/@hassan_grz5/video/7662161999568194838?is_from_webapp=1&sender_device=pc&web_id=7664238020274472470",
    "https://www.tiktok.com/@843v7/video/7661701923711569159?is_from_webapp=1&sender_device=pc&web_id=7664238020274472470"
]

run_amount = 60


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
                    if start <= run_index + 1 <= end:
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

                readIndex = (run_index + index - 1) % len(coorArray)


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
