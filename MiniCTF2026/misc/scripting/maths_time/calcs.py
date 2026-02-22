import socket as sk
import random as rd 
import threading as thd
from time import time 

HOST = "0.0.0.0"
PORT = 5000
FLAG = b"SIGINT{0x5F3759DF_15_my_f4v3_h3x}"

class Eq:
    def __init__(self, a, func, func_str, b):
        self.a = a
        self.func = func
        self.func_str = func_str
        self.b = b

    def __str__(self):
        return (str(self.a) if isinstance(self.a, int) else f"({str(self.a)})") + " " + self.func_str + " " + (str(self.b) if isinstance(self.b, int) else f"({str(self.b)})")
    
    def __int__(self):
        return self.func(int(self.a), int(self.b))

METHODS = ( 
    (lambda a, b: a + b, "+"),
    (lambda a, b: a - b, "-"),
    (lambda a, b: a * b, "*"),
)

def generate_equation(depth: int = 10) -> Eq:
    """
    Generates a random equation with a given depth.
    """
    a = generate_equation(depth - 1) if depth > 1 else rd.randint(1, 10)
    b = generate_equation(depth - 1) if depth > 1 else rd.randint(1, 10)
    func, func_str = rd.choice(METHODS)
    
    return Eq(a, func, func_str, b)

def handle_connection(conn, addr):
    start_time = time()
    conn.settimeout(3)
    try:
        for _ in range(20):
            eq = generate_equation()
            conn.sendall(f"{eq}\n".encode())

            
            data = conn.recv(1024)
            if not data: 
                conn.sendall(b"No data received, closing connection.")
                conn.close()
                return

            if time() - start_time > 3:
                conn.sendall(b"Timeout!\n")
                conn.close()
                return
            
            try:
                data = int(data.decode().strip())
            except ValueError:
                conn.sendall(b"Invalid input!\n")
                conn.close()    
                return 
                
            if int(data) != int(eq):
                conn.sendall(b"Wrong!\n")
                
                conn.close()
                return
        
        conn.sendall(b"Correct!\n")
        conn.sendall(FLAG)
        conn.sendall(b"\n")
        
        conn.close()
    except Exception as e: ...
    finally: 
        conn.close()

def accept_connections():
    with sk.socket(sk.AF_INET, sk.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        print(f"Listening on {HOST}:{PORT}")
        while True:
            conn, addr = s.accept()
            print(f"Accepted connection from {addr[0]}:{addr[1]}")
            thd.Thread(target=handle_connection, args=(conn, addr)).start()

if __name__ == "__main__":
    try:
        accept_connections()
    except KeyboardInterrupt:
        print("Server stopped.")
    except Exception as e:
        print(f"Error: {e}")

