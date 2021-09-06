#
# Simple script which helps test if Lightwave RF energy sensor UPD packets
# are visible on  the computer. 
#
# (c) Angelo Santagata @angelosantagata
#
import socket
data = None
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(('0.0.0.0', 9761))
sock.settimeout(30.0)  # Wait a Max of 30 seconds

print ("*** ******************************")
print ("* Lightwave RF UDP packet tester *")
print ("**********************************")

while True:
    try:
       print("Waiting for up to 30 seconds for data from LWRF Energy Device")
       data, _ = sock.recvfrom(1024)  # buffer size is 1024 bytes
       print("Data received from LWRF Energy!! ")
       print("--------------------------------------------------------")
       print("%s" % data)
       print("--------------------------------------------------------")
       print(" ")
    except socket.timeout as ex:
       print("No data received, check firewall, computer on same network etc  ")

