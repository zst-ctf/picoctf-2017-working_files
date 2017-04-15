#!/usr/bin/env python3
import socket
import re

s = socket.socket()
s.connect(('shell2017.picoctf.com', 57641))

i = 0;
while i < 3000:
    data = str(s.recv(4096))
    if data != "":
        bytesToSend = str(i) + "\n"
        print("RECV>" + data)
        if 'Congratulations!' in data:
            print("Success", i)
            i = 9999
        elif 'Can you guess it?' in data:
            print("Trying", i)
            s.send(bytesToSend)
            i += 1

