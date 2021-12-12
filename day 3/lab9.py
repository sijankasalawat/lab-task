#Take username and password from user and check it again for the three times whether
# the user has entered the rightusername and password.
# If yes then print a message "Logged in Successfully", if not then print invalid credentials
#for consecutive 3 times and if the limit exceeds than print "Attempt finished".

user_name = str(input("enter the username"))
pass_word = str(input("enter the password"))

for i in range(0, 3):
    x = str(input("enter your username"))
    y = str(input("enter your password"))
    if x == user_name and y == pass_word:
        print("login successful")
        break
    elif i < 3:
        if x != user_name and y != pass_word and i < 3:
            print("invalid credentials")
else:
    print("exceeded 3 attempts")