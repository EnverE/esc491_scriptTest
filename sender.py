import socket
import os
import glob

server_ip = '192.168.137.1'  #laptop’s IP
port = 5001

s = socket.socket()
s.connect((server_ip, port))

# Get all .jpg files from a folder
files = glob.glob('/home/powerpuffgirls/Desktop/demo_v1/*.jpg')

for file_path in files:
    filename = os.path.basename(file_path)
    file_size = os.path.getsize(file_path)

    # Send filename length and name
    s.send(len(filename).to_bytes(4, 'big'))
    s.send(filename.encode())

    # Send file size
    s.send(file_size.to_bytes(8, 'big'))

    # Send file content
 with open(file_path, 'rb') as f:
        while True:
            data = f.read(1024)
            if not data:
                break
            s.send(data)

    print(f"Sent {filename}")

# Send stop signal
s.send(len('END').to_bytes(4, 'big'))
s.send(b'END')

s.close()
print("All files sent successfully.")
