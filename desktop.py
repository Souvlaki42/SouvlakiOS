import os,time,globals, socket, urllib.request
globals.cmd("Desktop")

loginName = open("user/username.pass").read()
loginPass = open("user/password.pass").read()
loginPc = open("user/pc.pass").read()
version = open("version.pass").read()

print("""
░██████╗░█████╗░██╗░░░██╗██╗░░░██╗██╗░░░░░░█████╗░██╗░░██╗██╗░█████╗░░██████╗
██╔════╝██╔══██╗██║░░░██║██║░░░██║██║░░░░░██╔══██╗██║░██╔╝██║██╔══██╗██╔════╝
╚█████╗░██║░░██║██║░░░██║╚██╗░██╔╝██║░░░░░███████║█████═╝░██║██║░░██║╚█████╗░
░╚═══██╗██║░░██║██║░░░██║░╚████╔╝░██║░░░░░██╔══██║██╔═██╗░██║██║░░██║░╚═══██╗
██████╔╝╚█████╔╝╚██████╔╝░░╚██╔╝░░███████╗██║░░██║██║░╚██╗██║╚█████╔╝██████╔╝
╚═════╝░░╚════╝░░╚═════╝░░░░╚═╝░░░╚══════╝╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░╚════╝░╚═════╝░
""")

globals.help()

while True:
	select = input("[?]: ")
	if select == "0":
		os.startfile("desktop.py")
	if select == "1":
		os.startfile("brows.py")
	if select == "2":
		os.startfile("note.py")
	if select == "3":
		os.startfile("files.py")
	if select == "4":
		b_login = input("Please enter the password for user " + loginName + ": ")
		if b_login == loginPass:
			print("[1] Username: " + loginName)
			print("[2] Password: " + loginPass)
			print("Hostname:", socket.gethostname())
			print("Computer's Name: " + loginPc)
			print("Local Ip: " + socket.gethostbyname(socket.gethostname()))
			print("Public Ipv4: " + urllib.request.urlopen('https://v4.ident.me').read().decode('utf8'))
			print("Public Ipv6: " + urllib.request.urlopen('https://v6.ident.me').read().decode('utf8'))

			edit_b = input("[bios]: ")
			if edit_b == "1":
				edit_n = input("Please enter your new username: ")
				with open("user/username.pass", "w") as f:
					f.writelines(edit_n)
				print("Username changed to " + edit_n)
				os.system("pause")
				os.startfile("desktop.py")
				os.system("exit")
				break
			if edit_b == "2":
				edit_p = input("Please enter your new password: ")
				with open("user/password.pass", "w") as f:
					f.writelines(edit_p)
				print("Password changed to " + edit_p)
				os.system("pause")
				os.startfile("desktop.py")
				os.system("exit")
				break
	if select == "5":
		os.startfile("term.py")
	if select == "6":
		os.startfile("calc.py")
	if select == "7":
		os.startfile("defender.py")
	if select == "8":
		pass
	if select == "9":
		print("The date is: " + time.strftime("%d/%m/%y"))
		print("The time is: " + time.strftime("%H:%M:%S"))
	if select == "10":
		globals.cmd()
		globals.help()
	if select == "11":
		print("SouvlakiOS " + version + " by Souvlaki42")
	if select == "12":
		os.startfile("calendar.py")
	if select == "13":
		os.system("exit")
		break
	if select == "14":
		os.startfile("user.py")
		os.system("exit")
		break
	if select == "15":
		with open("user/info.data", "w") as f:
			f.writelines("0")
		os.system("exit")
		break