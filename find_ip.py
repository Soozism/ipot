import socket
j =0
z =0
port = input("please input your port for finde local ip: ")
for i in range(256):
   sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
   ip = f'127.{z}.{j}.{i}'
   result = sock.connect_ex((ip,port))
   if i == 255:
       i = 1
       j+=1
   if j==255:
       j = 1
       z+=1
   if result == 0:
      print(ip +" Port is open")
   else:
      print(ip +" Port is not open")
   sock.close()
