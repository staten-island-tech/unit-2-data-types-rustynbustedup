""" def login (password):
    #if statement is true, we go to the next line
    if password == "secret":
        print("logged in")
    else:
        print("incorrect")
x= input("what da password")
login(x) """

""" def grade(score):
    if score >=92:
        print("A")
    elif score >= 82:
        print("b")
    elif score >=72:
        print("c")
    else: 
        print ("f")
x = int(input("what da score"))
grade(x) """

""" def gamble(age,id):
    if age >=21:
        if id: 
            print("Gamble away")
        else:
            print("You need Id verification")
    else:
        print("Youre too young") """

def gamble(age, id):
    if age >=21 and id == True:
        print("have fun")
    elif age >=21 and id == False:
        print ("you need ID verification")
    else:
        print("youre too young")



