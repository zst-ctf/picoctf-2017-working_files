#!/usr/bin/env python3
#! /usr/bin/env python
import socket
import re

s = socket.socket()
s.connect(('shell2017.picoctf.com', 51091))

#Please give me the 'm' character '640' times, followed by a single '6'.

while True:
    data = s.recv(4096)
    if data != "":
        print("RECV>" + data)
        if 'Please give me the ' in data:
            regex = re.search(r"give me the '(.)' character '(.+)' times.+?'(.)'", data)
            ch = regex.group(1)
            numb = int(regex.group(2))
            returnString = ch*numb + regex.group(3);
            print returnString;
            s.send(returnString + "\n")
