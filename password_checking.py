"""
checking password
"""

def main ():
    password = "ShenXiaoting99"
    if password == getpassword(password):
        print("Access Granted")
    else :
        print("Access Denied")

def getpassword(password):
    password = input("Enter your password : ")
main()