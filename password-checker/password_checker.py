#This code is a work in progress

password = input("Enter A Password: ")
char = len(password)
#char stores a real number in the variable

def checker():
    if(char >= 12):
        print("You Have A Strong Password 12+ Characters")
    elif(char >= 8 and char <= 12):
        print("You Have A Medium Password 8+ Characters Less Than 12")
    else:
        print("You Have A Weak Password < 8 Characters")

def specialchecker(pw):
    special = ("!@#$%^&*()")
    for password in pw:
        if password in special:
            return True
    return False

print(specialchecker(password))   # True

checker()
