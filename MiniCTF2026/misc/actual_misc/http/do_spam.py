import socket
import random
import time

def spam_tcp_traffic(target_ip='127.0.0.1', target_port=1583, interval=.1):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        sock.connect((target_ip, target_port))
        print(f"Connected to {target_ip}:{target_port}")
        while True:
            # Generate random bytes
            data = random.randbytes(random.randint(10, 100))
            sock.sendall(data)
            print(f"Sent {len(data)} bytes")
            time.sleep(interval)
    except Exception as e:
        print(f"Error: {e}")
    finally:
        sock.close()

while True:
    spam_tcp_traffic()
    time.sleep(.1)

if __name__ == "__main__":
    spam_tcp_traffic()

