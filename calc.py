import os, math, globals

a = 0
b = 0
c = 0
x = 0
y = 0
D = 0

def closer():
	answer = input("Do you want to use calculator again? (Y/y or N/n)")
	if answer == "Y" or answer == "y":
		calculate()
	else:
		os.system("exit")

def calculate():
	globals.cmd("Calculator")
	print("""
░█████╗░░█████╗░██╗░░░░░░█████╗░██╗░░░██╗██╗░░░░░░█████╗░████████╗░█████╗░██████╗░	
██╔══██╗██╔══██╗██║░░░░░██╔══██╗██║░░░██║██║░░░░░██╔══██╗╚══██╔══╝██╔══██╗██╔══██╗
██║░░╚═╝███████║██║░░░░░██║░░╚═╝██║░░░██║██║░░░░░███████║░░░██║░░░██║░░██║██████╔╝
██║░░██╗██╔══██║██║░░░░░██║░░██╗██║░░░██║██║░░░░░██╔══██║░░░██║░░░██║░░██║██╔══██╗
╚█████╔╝██║░░██║███████╗╚█████╔╝╚██████╔╝███████╗██║░░██║░░░██║░░░╚█████╔╝██║░░██║
░╚════╝░╚═╝░░╚═╝╚══════╝░╚════╝░░╚═════╝░╚══════╝╚═╝░░╚═╝░░░╚═╝░░░░╚════╝░╚═╝░░╚═╝
""")
	print("If you don't know how to use that calculator just give as math symbol the word 'help'")
	method = input(">: ")
	if method == "help":
		print("To start calculating please select one of the options below and give the required input:")
		print("Please select '+' if you want to find the result of an addition in the form of 'x+y'")
		print("Please select '-' if you want to find the result of a subtraction in the form of 'x-y'")
		print("Please select '*' if you want to find the result of a proliferation in the form of 'x*y'")
		print("Please select '/' if you want to find the result of a division in the form of 'x/y'")
		print("Please select '%' if you want to find the division remainder of a division in the form of 'x/y'")
		print("Please select '√' if you want to find the square root of a number in the form of '√x'")
		print("Please select '|' if you want to find the absolute value of a number in form of '|x|'")
		print("Please select '^' if you want to find the result of a number in power of another number in form of 'x^y'")
		print("Please select '+x' if you want to find the result of a first degree equation by addition in form of 'x+a=b'")
		print("Please select '-x' if you want to find the result of a first degree equation by subtraction in form of 'x-a=b'")
		print("Please select '*x' if you want to find the result of a first degree equation with multiplication in form of 'x*a=b'")
		print("Please select '/x' if you want to find the result of a first degree equation by division in form of 'x/a=b'")
		print("Please select 'x^2=' if you want to find the result of a quadric equation in form of 'ax^2+bx+c=0'")
		print("Please select '>/' if you want to find the maximum common divisor of two numbers a and b with a>b")
		print("Please select '<*' if you want to find the minimum common multiple of two numbers a and b")
	elif method == "+":
		x = input("[1]: ")
		y = input("[2]: ")
		output = int(x) + int(y)
		print(">: " + str(output))
	elif method == "-":
		x = input("[1]: ")
		y = input("[2]: ")
		output = int(x) - int(y)
		print(">: " + str(output))
	elif method == "*":
		x = input("[1]: ")
		y = input("[2]: ")
		output = int(x) * int(y)
		print(">: " + str(output))
	elif method == "/":
		x = input("[1]: ")
		y = input("[2]: ")
		output = int(x) / int(y)
		print(">: " + str(output))
	elif method == "%":
		x = input("[1]: ")
		y = input("[2]: ")
		output = int(x) % int(y)
		print(">: " + str(output))
	elif method == "√":
		x = input("[1]: ")
		output = math.sqrt(int(x))
		print(">: " + str(output))
	elif method == "^":
		x = input("[1]: ")
		y = input("[2]: ")
		output = int(x) ** int(y)
		print(">: " + str(output))
	elif method == "x^2=":
		a = int(input("[1]: "))
		b = int(input("[2]: "))
		c = int(input("[3]: "))
		D = b**2 - 4 * a * c
		print("D = " + str(D))
		if D > 0:
			out1 = ((-1 * b) + math.sqrt(D))/2*a
			out2 = ((-1 * b) - math.sqrt(D))/2*a
			print("x1 = " + ">: " + str(out1))
			print("x2 = " + ">: " + str(out2))
		elif D == 0:
			out = (-1 * b)/2*a
			print("x = " + ">: " + str(out))
		else:
			print("Error: No solution in R...")
	elif method == "+x":
		a = int(input("[1]: "))
		b = int(input("[2]: "))
		out = b - a
		print(">: " + str(out))
	elif method == "-x":
		a = int(input("[1]: "))
		b = int(input("[2]: "))
		out = b + a
		print(">: " + str(out))
	elif method == "*x":
		a = int(input("[1]: "))
		b = int(input("[2]: "))
		out = b / a
		print(">: " + str(out))
	elif method == "/x":
		a = int(input("[1]: "))
		b = int(input("[2]: "))
		out = b * a
		print(">: " + str(out))
	elif method == ">/":
		a = int(input("[1]: "))
		b = int(input("[2]: "))
		out = math.gcd(a,b)
		print(">: " + str(out))
	elif method == "<*":
			a = int(input("[1]: "))
			b = int(input("[2]: "))
			out = math.lcm(a,b)
			print(">: " + str(out))
	elif method == "|":
		x = int(input("[1]: "))
		out = abs(x)
		print(">: " + str(out))
	else:
		print("Error: Math solution not available...")
	closer()

calculate()