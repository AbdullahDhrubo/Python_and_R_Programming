# Ex-5 Maximum of Two Values 

#Defining the function my_max.

def my_max(x,y):
    return x if x>y else y
    
# Evaluating greater integer value using a while true loop.
# Requesting users to input valid input using the error handling method.

while True:
    try:
        x = int(input("Enter the first integer value: "))
        break
    except:
        print('Invalid Input')
while True:
    try:
        y = int(input("Enter the second integer value: "))
        break
    except:
        print('Invalid Input')
        
        
# Printing a display message to the user which value is greater.

print("The greater value is: ",my_max(x,y))
