# Undercity eink lanyard
fixed for windows

## How to flash it

### Windows

1. Install a venv ``python -m venv .venv``
2. Run  ``.venv\Scripts\activate``
3. Run ``pip install -r req.txt``
4. Run ``python run.py`` and follow the text

### macOS

1. Clone the repo
    ```bash
    git clone
    ```
2. You need anaconda installed & arduino-cli. Install anaconda using this [link](https://www.anaconda.com/docs/getting-started/anaconda/install#macos-linux-installation)
    ```bash
    # arduino cli
    brew install arduino-cli

    arduino-cli config add board_manager.additional_urls https://github.com/earlephilhower/arduino-pico/releases/download/global/package_rp2040_index.json

    arduino-cli lib install "Adafruit NeoPixel"
    ```
3. Just run the script
    ```bash
    chmod +x upload.sh
    ./upload.sh
    ```
4. Follow the instructions and yay!
