import base64
from colorama import init, Fore, Back, Style
welcomeInput= raw_input(Style.BRIGHT + Fore.BLUE + "Enter 1 to encrypt a string," + Style.BRIGHT + Fore.RED + " 2 to decrypt a string: ") 

if(int(welcomeInput)==1 or int(welcomeInput)==2):
    if int(welcomeInput)==1:
        inputString= raw_input(Style.BRIGHT + Fore.BLUE + "Enter the string you want to encrypt:") 
        base64Value = base64.b64encode(inputString.encode())
        print "Base64 Value = " + base64Value
    elif int(welcomeInput)==2:
        inputString= raw_input(Style.BRIGHT + Fore.RED + "Enter the string you want to decrypt:") 
        stringValue = base64.b64decode(inputString).decode('utf-8')
        print "Base64 Value = " + stringValue
  
