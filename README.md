# Countdown Timer Project

This project generates a countdown timer with a dynamic color transition from green to red. The timer text is generated as an image with the number portion changing color, and a video is created from these images.

![alt text](assets/countdown.gif)

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
   cd countdown-timer
   ```

2. Run the script:
   ```bash
   python countdown.py
   ```

## License

This project is licensed under the [BSD 3-Clause License](LICENSE).
