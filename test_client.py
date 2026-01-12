import socket
import time
import sys

# Configuration
HOST = '10.10.206.7'
PORT = 9000

if len(sys.argv) > 1:
    HOST = sys.argv[1]

def send_data():
    print(f"Attempting to connect to {HOST}:{PORT}...")
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((HOST, PORT))
            print(f"Connected to {HOST}:{PORT}")
            
            # Send dummy SMDR data
            # Format usually: date, time, duration, caller, callee, directional, ...
            # We'll simulate a few records
            records = [
                b"2025/01/12,12:00:00,00:01:30,101,200,I,1234567890\r\n",
                b"2025/01/12,12:05:00,00:05:00,200,102,O,0987654321\r\n",
                b"2025/01/12,12:15:00,00:00:45,103,101,I,1122334455\r\n"
            ]
            
            for i, record in enumerate(records):
                print(f"Sending record {i+1}...")
                s.sendall(record)
                time.sleep(1)
                
            print("Data sent successfully.")
    except ConnectionRefusedError:
        print(f"Connection refused. Is the server running on {HOST}:{PORT}?")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == '__main__':
    send_data()
