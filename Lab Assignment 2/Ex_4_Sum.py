# Ex-4 Sum of Numbers

# Declaring variable. 

number = 0
num_total = 0

# Using the while loop asking the series of positive numbers and to end the loop a negative number. 

while True:
    print()
    add_num = float(input("Enter the series of positive numbers. "
          "To end, enter a negative number "))
    if add_num < 0:
        break
    num_total += add_num

# Printing result

print("Sum of the positive numbers is: ", num_total)
