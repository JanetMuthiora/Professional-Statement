import socket

# specify the IP address to scan
target_ip = "203.101.224.119"  # fruitmaps.com.au

# define the range of ports to scan
min_port = 1
max_port = 1024

# loop over the range of ports and check for open ports
for port in range(min_port, max_port + 1):
    # create a new socket object
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(0.1) # set a timeout value for the socket connection
    
    # try to connect to the target IP and port
    result = s.connect_ex((target_ip, port))
    
    # check if the port is open
    if result == 0:
        print(f"Port {port} is open.")
    
    # close the socket connection
    s.close()
