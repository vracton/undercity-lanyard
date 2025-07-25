import os
import shutil
import requests
from PIL import Image, ImageFont, ImageDraw
from bmp_to_array import image_to_c_array
import subprocess

if os.name != 'nt':
    subprocess.run("brew install arduino-cli", shell=True)

subprocess.run("arduino-cli config add board_manager.additional_urls https://github.com/earlephilhower/arduino-pico/releases/download/global/package_rp2040_index.json", shell=True)

subprocess.run("arduino-cli core install rp2040:rp2040", shell=True)
subprocess.run("arduino-cli lib install \"Adafruit NeoPixel\"", shell=True)

print("Welcome to undercity hopefully fixed lanyard upload script")

try:
    for f in os.listdir("./build"):
        os.remove(os.path.join("./build", f))
except FileNotFoundError:
    pass

try:
    os.remove("img.png")
except FileNotFoundError:
    pass
try:
    os.remove("img_resized.png")

except FileNotFoundError:
    pass

try:
    os.remove("newbadge.bmp")
except FileNotFoundError:
    pass

try:
    os.remove("f.h")
except FileNotFoundError:
    pass

name = input("Enter the name of the badge: ")
if not name:
    print("Name is required.")
    exit(1)
print (f"Hola: {name}")
slack_handle = input("Enter the Slack handle: ")
if not slack_handle:
    print("Slack handle is required.")
    exit(1)

print(f"Hey: {slack_handle}! Nice to meet you!")

pro = input("Enter any text you want to add: ")

if not pro:
    print("No additional text provided.")

# img = input("Enter the url to the image: ")
img = None

if img:
    response = requests.get(img)
    if response.status_code == 200:
        with open("img.png", "wb") as f:
            f.write(response.content)
    else:
        print("Failed to download image.")
    try:
        img = Image.open("img.png")
        img = img.resize((300, 300), Image.LANCZOS)
        img.save("img_resized.png")
    except Exception as e:
        print(f"Error processing image: {e}")
        exit(1)

else:
    img = None
    # print("No image URL provided.")





try:
    font = ImageFont.truetype("./font.ttf", 25)
    
    temp_img = Image.new('RGB', (1000, 100), color='white')
    draw = ImageDraw.Draw(temp_img)
    
    bbox = draw.textbbox((0, 0), name, font=font)
    name_width = bbox[2] - bbox[0]
    
    # print(f"Name width: {name_width} pixels")
    
except Exception as e:
    print(f"Error calculating text width: {e}")
    exit(1)

pronoun_x = name_width + 40

try:
    badge = Image.open("badge.bmp")
    draw = ImageDraw.Draw(badge)
    
    main_font = ImageFont.truetype("./font.ttf", 25)
    bank_font = ImageFont.truetype("./bankfont.ttf", 15)
    
    draw.text((20, 10), name, font=main_font, fill="black")
    
    draw.text((20, 40), f"@{slack_handle}", font=main_font, fill="black")
    
    draw.text((pronoun_x, 30), pro, font=bank_font, fill="black")
    
    badge.save("newbadge.bmp")
    print("Badge created successfully!")
    
except Exception as e:
    print(f"Error creating badge: {e}")
    exit(1)


if img:
    try:
        img = Image.open("img_resized.png")
        badge.paste(img, (20, 60))
        badge.save("newbadge.bmp")
        print("Badge with image created successfully!")
    except Exception as e:
        print(f"Error adding image to badge: {e}")
        exit(1)


image_to_c_array("newbadge.bmp", "f.h", "gImage_img")
subprocess.run("arduino-cli compile --fqbn rp2040:rp2040:generic_rp2350 --output-dir ./build", shell=True)

input("Press Enter to AFTER you pressed the boot button on the board")

if os.name == 'nt':
    shutil.copy("build/undercity-lanyard.ino.uf2", "D:/")
else:
    shutil.copy("build/undercity-lanyard.ino.uf2", "/Volumes/RP2350/")



try:
    os.remove("img.png")
except FileNotFoundError:
    pass
try:
    os.remove("img_resized.png")

except FileNotFoundError:
    pass

try:
    os.remove("newbadge.bmp")
except FileNotFoundError:
    pass

try:
    os.remove("f.h")
except FileNotFoundError:
    pass

for f in os.listdir("./build"):
    os.remove(os.path.join("./build", f))