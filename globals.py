import os
username = open("user/username.pass").read()

def cmd(title: str):
    os.system("title " + title)
    os.system("color 2")
    os.system("cls")

def help():
    print("Welcome back, " + username + "!!!")
    print("""
    [0] Desktop
    [1] Browser
    [2] Notepad (Not Available Yet!)
    [3] Files (Not Available Yet!)
    [4] NBIOS
    [5] Terminal
    [6] Calculator
    [7] Defender (May doesn't work yet!)
    [8] Update (Doesn't work yet!)
    [9] Date/Time
    [10] Clear
    [11] Version
    [12] Calendar
    [13] Shut Down
    [14] Restart
    [15] Format
    """)