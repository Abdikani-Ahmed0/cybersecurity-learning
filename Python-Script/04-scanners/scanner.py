import socket

target = input("Enter target IP: ")

for port in range(1, 1025):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket.setdefaulttimeout(0.5)

    result = s.connect_ex((target, port))

    if result == 0:
        print(f"Port {port} is OPEN")

    s.close()

