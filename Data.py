#hello

""" x=3
y = float(3)
print(x,y) """


""" values = [1,2.23,5,7,2,30,15]
print(values)
for i in values:
    print(values[0])
    print(values[6]) """

""" x = "this is a thing"
y= x.split( )
z = y[0]
print(y)
print(z) """
#word counter
""" def sentence():
    answer = input ("pease emter semtanse: ")
    words = answer.split()
    hello = len(words)
    print(hello)
    for word in words:
        print(word)
sentence() """
#day of the week calculator 
""" day_of_week = input("what day is it? ")
if day_of_week == "Friday":
    print("correct")
else:
    print("incorrect") """

""" values = [1,2.23,5,7,2,30,15]
print(values)
for i in values:
    print(i) """

""" #odd or even numbers
def even(number):
    if number % 2 == 0:
        print("even")
    else:
        print("odd")

number = int(input("Pease emter a numba: "))
even(number) """

""" #Tip calculator
def tip(service):
    if service == "Great":
        tip = "25%"
    elif service == "Good":
        tip = "20%"
    elif service == "Okay":
        tip = "15%"
    elif service == "Bad":
        tip = "0%"
    else:
        tip = "IS IT GREAT GOOD OKAY OR BAD"
    print(f"Suggested tip: {tip}")
service_input = input("How was the service (Great, Okay, Good, Bad)?")
tip(service_input)  """

#Factor calculator 
""" def find_factors(number):
    factors = []
    for i in range(1, number + 1):
        if number % i == 0:
            factors.append(i)
    return factors
factor = int(input("Please enter a number: ")) 
print(f"Factors of {factor}: {find_factors(factor)}") """

#GCF Calculator 
def find_factors(number):       
    factors = [] #defines the lits
    for i in range(1, number + 1):
        if number % i == 0: # finds the number w remainder of 0 in the list 
            factors.append(i)
    return factors
num1 = int(input("pease emter firsp numba:")) # make a input from the person for the first numeber
num2 = int(input("pease empter sepond numba:"))
factor1 = find_factors (num1) #finds the number from the first number 
factor2 = find_factors (num2) 
common_factors = list(set(factor1) and set(factor2)) # puts the lists of factors into a common factor list 
GCF = max (common_factors) #call the function 
print ("da GCF is", GCF) 




