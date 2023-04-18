

from pystyle import *
print(Box.Lines("[+] Learnpython with bilel86 [+]"))
Write.Print("  this programm for login ...", Colors.red, interval=0.1)
Write.Print(" write username & password \n\n", Colors.red_to_white, interval=0.1)
print(Box.DoubleCube("Login "))

while True:
    username= Write.Input('write username: \n', Colors.black, interval=0.1)
    password= Write.Input('write password: \n\n', Colors.black,interval=0.1)
    if username == 'bilel' and password =='bilel1234':
        Write.Print("Succeful ..\n", Colors.green,interval=0.1)
        input('\n press any key to exit ...')
    else:
        Write.Print("Error try again \n\n", Colors.red, interval=0.1)

