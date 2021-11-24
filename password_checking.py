"""
checking password
"""


def main():
    password = input("Enter your password : ")
    if getpassword(password):
        print("Access Granted")
    else:
        print("Access Denied")


def getpassword(password):
    return password=="ShenXiaoting99"


main()
