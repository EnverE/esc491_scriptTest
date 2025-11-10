import socket
import os
from ultralytics import YOLO

#  Directory where received images will be saved
save_dir = r"C:\Users\tatli\PycharmProjects\esc491_scriptTest\Image"
os.makedirs(save_dir, exist_ok=True)

# Path to your trained YOLO model
model_path = r"dataPath\train\weights\best.pt"

# Initialize YOLO model once
print("Loading YOLO model...")
model = YOLO(model_path)
print("✅ YOLO model loaded successfully.")

# Create socket server
server_ip = '0.0.0.0'
port = 5001

s = socket.socket()
s.bind((server_ip, port))
s.listen(1)
print(f"📡 Waiting for connection on port {port}...")

conn, addr = s.accept()
print(f"🔗 Connected by {addr}")

while True:
    #  Receive filename length 
    filename_len = conn.recv(4)
    if not filename_len:
        break
    filename_len = int.from_bytes(filename_len, 'big')

    #  Receive filename 
    filename = conn.recv(filename_len).decode()
    if filename == 'END':
        break  # stop signal

    #  Receive file size 
    file_size = int.from_bytes(conn.recv(8), 'big')

    #  Full path to save 
    save_path = os.path.join(save_dir, filename)

    #  Receive file data 
    with open(save_path, 'wb') as f:
        received = 0
        while received < file_size:
            data = conn.recv(1024)
            if not data:
                break
            f.write(data)
            received += len(data)

    print(f"📥 Received: {filename}")

    #  Run YOLO detection on the received image 
    print(f"🔍 Running YOLO on {filename}...")
    results = model.predict(
        source=save_path,
        imgsz=640,
        conf=0.5,
        save=True,
        save_txt=True
    )
    print(f" Processed {filename}")

print("🎉 All files received and processed.")
conn.close()
