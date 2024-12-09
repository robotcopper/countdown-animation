import numpy as np
from PIL import Image, ImageDraw, ImageFont
import os
import subprocess
import shutil

# Function to generate an image with partially colored text
def create_text_image(text, font, static_color, dynamic_color, dynamic_part, margin=0):
    # Calculate the total size of the text
    img = Image.new('RGBA', (1, 1), (0, 0, 0, 0))  # Temporary background to measure size
    draw = ImageDraw.Draw(img)
    bbox = draw.textbbox((0, 0), text, font=font)
    text_width, text_height = bbox[2] + bbox[0], bbox[3] + bbox[1]
    
    # Add margin
    text_height += margin
    
    # Create a new image with the calculated size
    img = Image.new('RGBA', (text_width, text_height), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    
    # Split the text into static and dynamic parts
    before_dynamic, after_dynamic = text.split(dynamic_part, 1)
    
    # Draw the static part before the numbers
    before_width = draw.textbbox((0, 0), before_dynamic, font=font)[2]
    draw.text((0, 0), before_dynamic, font=font, fill=static_color)
    
    # Draw the dynamic part (numbers)
    draw.text((before_width, 0), dynamic_part, font=font, fill=dynamic_color)
    
    # Draw the static part after the numbers
    after_width = before_width + draw.textbbox((0, 0), dynamic_part, font=font)[2]
    draw.text((after_width, 0), after_dynamic, font=font, fill=static_color)
    
    return img, (text_width, text_height)

# Countdown parameters
font_size = 500
font_path = "/usr/share/fonts/truetype/digital-7/digital-7.ttf"  # Change path if necessary
countdown_start = 100  # Countdown starting at three digits

# Create the directory to save images
os.makedirs("images", exist_ok=True)

# Generate images for the countdown
for i in range(countdown_start, -1, -1):  # Countdown from 100 to 0
    dynamic_part = str(i).zfill(3)  # Format numbers to three digits
    text = f"Match Time : {dynamic_part} sec"
    font = ImageFont.truetype(font_path, font_size)
    
    # Calculate the color of the numbers (transition from green to red)
    progress = (countdown_start - i) / countdown_start  # Progression from 0 to 1
    green_intensity = int(255 * (1 - progress))  # Green decreases
    red_intensity = int(255 * progress)  # Red increases
    dynamic_color = (red_intensity, green_intensity, 0)  # Transition from green to red
    static_color = (255, 255, 255)  # White for the rest of the text
    
    # Create an image with separate colors
    img, text_size = create_text_image(text, font, static_color, dynamic_color, dynamic_part, margin=20)
    
    # Save the image
    img.save(f"images/frame_{countdown_start - i:03d}.png")  # Name files in reverse order

print("Images saved.")

# Calculate maximum dimensions
max_width, max_height = 0, 0
for i in range(countdown_start, 0, -1):
    dynamic_part = str(i).zfill(3)
    text = f"Match Time : {dynamic_part} sec"
    font = ImageFont.truetype(font_path, font_size)
    bbox = ImageDraw.Draw(Image.new('RGBA', (1, 1), (0, 0, 0, 0))).textbbox((0, 0), text, font=font)
    text_width, text_height = bbox[2] - bbox[0], bbox[3] - bbox[1]
    max_width = max(max_width, text_width)
    max_height = max(max_height, text_height)

# Create the video with FFmpeg
command = [
    "ffmpeg",
    "-framerate", "1",  # 1 frame per second
    "-i", "images/frame_%03d.png",  # Use the generated images
    "-c:v", "vp8",  # VP8 codec for WebM output
    "-auto-alt-ref", "0",  # Disable alternate reference frames
    "-an",  # No audio
    "-y",  # Overwrite the output if it exists
    "countdown.webm"  # Name of the output video
]

try:
    subprocess.run(command, check=True)
    print("Video created successfully.")
    
    # Remove the images directory after generation
    shutil.rmtree("images")
    print("Images folder deleted.")
    
except subprocess.CalledProcessError as e:
    print(f"Error while running FFmpeg: {e}")
