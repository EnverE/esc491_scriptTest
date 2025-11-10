# ESC491 Raspberry Pi Image Transfer & YOLO Processing

This project enables a Raspberry Pi to send image files to a laptop via socket connection.  
The laptop receives and saves the images for YOLO model inference.

## Files
- **send_images.py** – runs on Raspberry Pi to send `.jpg` files
- **receive_images.py** – runs on laptop to receive and save them
- **yolo_process.py** – runs YOLO model on received images

## Usage
1. Start `receive_images.py` on laptop.
2. Run `send_images.py` on Raspberry Pi.
3. Process images with `yolo_process.py`.
