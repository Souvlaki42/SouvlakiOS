import os,globals, time

globals.cmd("Login")

loginName = open("user/username.pass").read()
loginPass = open("user/password.pass").read()

print("""
░██████╗░█████╗░██╗░░░██╗██╗░░░██╗██╗░░░░░░█████╗░██╗░░██╗██╗░█████╗░░██████╗
██╔════╝██╔══██╗██║░░░██║██║░░░██║██║░░░░░██╔══██╗██║░██╔╝██║██╔══██╗██╔════╝
╚█████╗░██║░░██║██║░░░██║╚██╗░██╔╝██║░░░░░███████║█████═╝░██║██║░░██║╚█████╗░
░╚═══██╗██║░░██║██║░░░██║░╚████╔╝░██║░░░░░██╔══██║██╔═██╗░██║██║░░██║░╚═══██╗
██████╔╝╚█████╔╝╚██████╔╝░░╚██╔╝░░███████╗██║░░██║██║░╚██╗██║╚█████╔╝██████╔╝
╚═════╝░░╚════╝░░╚═════╝░░░░╚═╝░░░╚══════╝╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░╚════╝░╚═════╝░

██╗░░░░░░█████╗░░██████╗░██╗███╗░░██╗
██║░░░░░██╔══██╗██╔════╝░██║████╗░██║
██║░░░░░██║░░██║██║░░██╗░██║██╔██╗██║
██║░░░░░██║░░██║██║░░╚██╗██║██║╚████║
███████╗╚█████╔╝╚██████╔╝██║██║░╚███║
╚══════╝░╚════╝░░╚═════╝░╚═╝╚═╝░░╚══╝
""")

while True:
	logN = input("Please enter your last username: ")
	logP = input("Please enter your last password: ")

	if logN == loginName and logP == loginPass:
		time.sleep(0.5)
		os.startfile("desktop.py")
		break
	else:
		print("Error: wrong username or password")