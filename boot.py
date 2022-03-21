import os, globals

globals.cmd("Bootloader")

dataInfo = open("user/info.data")
data = dataInfo.read()

if data == "0":
    os.startfile("register.py")
if data == "1":
    os.startfile("login.py")