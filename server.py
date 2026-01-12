import socket
import os
import datetime
import sys

# Configuration
HOST = '0.0.0.0'
PORT = int(os.environ.get('SMDR_PORT', 9000))
DATA_DIR = '/data'

# Ensure data directory exists
if not os.path.exists(DATA_DIR):
    try:
        os.makedirs(DATA_DIR)
    except OSError as e:
        print(f"Error creating data directory {DATA_DIR}: {e}")
        # Fallback for local testing if running without docker volume
        if not os.path.exists('data'):
            os.makedirs('data')
        DATA_DIR = 'data'

def run_server():
    print(f"Starting SMDR Receiver on {HOST}:{PORT}...")
    print(f"Saving logs to {DATA_DIR}")
    
    while True:
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
                s.bind((HOST, PORT))
                s.listen()
                print("Listening for connections...")
                
                while True:
                    conn, addr = s.accept()
                    print(f"Connected by {addr}")
                    with conn:
                        buffer = b""
                        while True:
                            data = conn.recv(1024)
                            if not data:
                                print(f"Connection closed by {addr}")
                                break
                            
                            # Append to daily log file
                            # Avaya SMDR is typically CR/LF terminated lines. 
                            # We'll just append raw bytes to keep it simple and robust.
                            try:
                                today = datetime.date.today().isoformat()
                                filename = os.path.join(DATA_DIR, f"smdr_{today}.csv")
                                with open(filename, 'ab') as f:
                                    f.write(data)
                                    f.flush() # Ensure data is written immediately
                            except Exception as file_e:
                                print(f"Error writing to file: {file_e}")
                            
        except Exception as e:
            print(f"Server error: {e}")
            print("Retrying in 5 seconds...")
            import time
            time.sleep(5)

if __name__ == '__main__':
    run_server()
