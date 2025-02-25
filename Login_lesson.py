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



#Lesson 2/25/25
x = True 
y = True

def GCF():
    if x == True and y == True 
    print("true")
#inefficien


def vote(age, id)
    if age <18 or id == False:
        print("cannot vote")
    elif age >18 and id == True:
        print("vote")


def skins(money, age, isAvialable"):
    if money <10 or age <18 or isAvailable ==False:
        return ("cannot buy")
def skins2 (money, cost, isAvialable")
    if isAvailable == True:
        if money >10 or cost ==0:
            print("Go off Queen")
        else:
            print("janet Broke Gurl")


def skins3 (money, age, isAvialable"):
    if isAvailable == False or age <18:
        print("nope")