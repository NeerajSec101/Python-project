## importing socket module
import socket
## getting the hostname by socket.gethostname() method
hostname =input("Enter host nmae:")
## getting the IP address using socket.gethostbyname() method
ip_address = socket.gethostbyname(hostname)
## printing the hostname and ip_address
print(f"Hostname: {hostname}")
print(f"IP Address: {ip_address}")
