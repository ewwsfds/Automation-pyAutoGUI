import os

print("This code will Rename videos sorted Desc")
answer=input("y/n to procced ?")
if answer.lower() in ["n", "no"]:
    quit()


root = os.path.dirname(os.path.abspath(__file__))

# Get videos sorted by index
videos = [
    f for f in os.listdir(root)
    if f.startswith("video") and f.endswith(".mp4")
]

videos.sort(key=lambda x: int(x.replace("video", "").replace(".mp4", "")))

# Step 1: rename to temporary names
temp_names = []

for i, video in enumerate(videos):
    old_path = os.path.join(root, video)

    temp_name = f"temp_video_{i}.mp4"
    temp_path = os.path.join(root, temp_name)

    os.rename(old_path, temp_path)
    temp_names.append(temp_name)

# Step 2: rename to reversed order
total = len(temp_names)

for i, temp_name in enumerate(temp_names):
    temp_path = os.path.join(root, temp_name)

    new_name = f"video{total - 1 - i}.mp4"
    new_path = os.path.join(root, new_name)

    os.rename(temp_path, new_path)