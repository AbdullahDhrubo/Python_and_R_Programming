# Ex-1 DVD Club Points

# User input

number = int(input("Enter the number of videos purchased this month: "))

# If-elif statement to test conditions and printing output.  

if number <0:
    print("Enter a valid positive integer!!")
elif number == 0:
    print("You’ve earned: 0 point")
elif number == 1:
    print("You’ve earned: 5 points")
elif number == 2:
    print("You’ve earned: 15 points")
elif number == 3:
    print("You’ve earned: 30 points")
elif number >= 4:
    print("You’ve earned: 60 points")
