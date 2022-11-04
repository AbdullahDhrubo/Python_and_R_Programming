# Ex-2 BMI

# Declaring variables while being in a float. 

weight = float(input("Enter your weight (in kg): "))
height = float(input("Enter your height (in meter): "))

# Calculating BMI values.

BMI = weight/height**2

# Formating BMI to two decimal places.

BMI= "{:.2f}".format(BMI)

# Changing str to float.

BMI= float(BMI)

# if and elif conditions with error handling.

if (weight <= 0 or
    height <= 0):
    print("Please enter a valid number greater than zero, in both weight and height!")
elif BMI < 18.5:
    print("Your BMI is:", BMI, "you are in range of underweight!")
elif 18.5 <= BMI <=24.99:
    print("Your BMI is:", BMI, "you are in range of normal weight!")
elif 25 <= BMI <= 29.99:
    print("Your BMI is:", BMI, "you are in range of overweight!")
elif BMI >= 30:
    print("Your BMI is:", BMI, "you are in range of obese!")
