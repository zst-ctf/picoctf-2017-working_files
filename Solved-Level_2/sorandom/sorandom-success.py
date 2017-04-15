#!/usr/bin/python -u
import random,string

random.seed("random")
enc = "BNZQ:2m8807395d9os2156v70qu84sy1w2i6e"
#flag = "FLAG:"+open("flag", "r").read()[:-1]

orig = 0;
final = ""
for c in enc:
    randNumb = -1
    if c.islower():
    #rotate number around alphabet a random amount
        randNumb = random.randrange(0,26)
        orig = ord(c) - ord('a') - randNumb
        if orig < 0:
            orig += 26
        orig += ord('a')
    elif c.isupper():
        randNumb = random.randrange(0,26)
        orig = ord(c) - ord('A') - randNumb
        if orig < 0:
            orig += 26
        orig += ord('A')
    elif c.isdigit():
        randNumb = random.randrange(0,10)
        orig = ord(c) - ord('0') - randNumb
        if orig < 0:
            orig += 10
        orig += ord('0')
    else:
        orig = ord(c)
    final += chr(orig)
    print c, chr(orig), randNumb
print final