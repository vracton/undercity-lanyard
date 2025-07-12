echo "welcome to undercity broken lanyard upload script"

# Ask for name of the user
read -p "Please enter your name: " name
echo "Hello, $name!"
# Ask for slack handle
read -p "Please enter your slack handle: @" slack_handle
echo "Thank you, $slack_handle! Let's proceed with the upload."
# Change the img to add the text

# Enter a custom font path or use a default one
FONT_PATH="./font.ttf"
if [ ! -f "$FONT_PATH" ]; then
    echo "Font file not found at $FONT_PATH. Please provide a valid font file."
    exit 1
fi

magick badge.bmp \
  -font ./font.ttf -pointsize 25 -fill black \
  -annotate +20+30 "$name" \
  -annotate +20+60 "@$slack_handle" \
  newbadge.bmp

# Convert it to a format suitable for the device

~/anaconda3/bin/python bmp_to_array.py newbadge.bmp f.h gImage_img

arduino-cli compile --fqbn rp2040:rp2040:generic_rp2350 --output-dir ./build
if [ $? -ne 0 ]; then
    echo "Compilation failed. Please check the code."
    exit 1
fi
echo "Please press the boot button on the device and press enter when plugged in"
# Wait for the user to press enter
read -p "Press enter to continue..."
# Upload the compiled binary to the device
cp build/GDEY029T94_Arduino.ino.uf2 /Volumes/RP2350/
if [ $? -ne 0 ]; then
    echo "Upload failed. Please check the device connection."
    exit 1
fi
echo "Upload successful! The device should now be running the new code."
