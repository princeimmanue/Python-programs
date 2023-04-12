# Login program using python 
# created by Prince immanuel 

#code 
def login():
    print(">>>>>>>>>>>>>>>>>>>>>>>LOGIN>>>>>>>>>>>>>>>>>>>>>>")
    username = input("Username :") # enter the username "user" 
    pwd = input("Password :") # enter the password "1234@"
    
    if username == "user" and pwd =="1234@":
        print("successfully login !")
    else: 
        print("username or password invalid !")
login()