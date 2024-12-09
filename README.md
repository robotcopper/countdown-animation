# Countdown Timer Project

This project generates a countdown timer with a dynamic color transition from green to red. The timer text is generated as an image with the number portion changing color, and a video is created from these images.

<p align="center">
    <img src="assets/countdown.gif">
</p>

# Table of Contents

1. [Features](#features)
2. [Requirements](#requirements)
3. [Usage](#usage)
4. [Example Countdown (100 seconds)](#example-countdown-100-seconds)
5. [License](#license)

## Features:
- Customizable countdown range.
- Numbers transition smoothly from green to red.
- Outputs a WebM video format to keep the background transparent.

## Requirements

- Python 3.x
- FFmpeg (for video creation)
    - Install FFmpeg (if not already installed):
        - On Ubuntu/Debian:
            ```bash
            sudo apt update
            sudo apt install ffmpeg
            ```
## Python Dependencies:
- **Pillow**: For image creation and manipulation.
    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. Clone the repository:
   ```bash
   git clone https://github.com/robotcopper/countdown-animation.git
   cd countdown-animation
   ```

2. Run the script:
   ```bash
   python countdown.py
   ```

## Example Countdown (100 seconds): 
A pre-configured countdown of 100 seconds (from 100 to 000) is already available. Simply run the default script.
The resulting video is pre-generated and available in the `assets` folder.

## License

This project is licensed under the [BSD 3-Clause License](LICENSE).
