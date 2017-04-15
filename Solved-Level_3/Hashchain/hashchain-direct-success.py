#!/usr/bin/env python

import md5 #Must be run in python 2.7.x
import sys
import socket
import re

#seed = sys.argv[1] #"3501672ebc68a5524629080e3ef60aef"
#match = sys.argv[2] # "e26d7e19b69192b94af14c4b208c8c9a"

def getHash(seed):
    out = md5.new(seed).hexdigest()
    # print seed, '->', out
    return out

def getPrevHash(seed, match):
    hashc = seed
    prevc = ""
    for _ in xrange(100):
        prevc = hashc
        hashc = getHash(hashc)
        if hashc in match:
            break;
    return prevc


s = socket.socket()
s.connect(('shell2017.picoctf.com', 55973))
id = ""
while True:
    data = str(s.recv(4096))
    if data != "":
        print("RECV>" + data)

        if 'r/f?' in data:
            s.send("f\n")
        elif 'Please authenticate as user' in data:
            regex = re.search(r"Please authenticate as user (.+)", data.strip())
            # seed is md5 of the user id, hence start seed from the ID itself!
            id = regex.group(1)
            #print id
            match = data.split("\n")[2] #3rd line is the hash they give
            if match is not '':
                to_send = getPrevHash(id, match)
                s.send( to_send + "\n" )
        elif 'Next token' in data:
            match = data.split("\n")[0] #1st line is the hash they give
            #print 'match =', match
            to_send = getPrevHash(id, match)
            #print 'sending =', to_send
            s.send( to_send + "\n" )
