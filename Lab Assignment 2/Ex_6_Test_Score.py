# Ex-6 Test Average and Grade

# Defining the function calc_average. 

def calc_average(a,b,c,d,e):
    return (a+b+c+d+e)/5

# Defining the function determine_grade and determining conditions for grade score.

def determine_grade (score):
    if score >= 90:
        print("Your grade is: ", "A")
    elif score >= 80:
        print("Your grade is: ", "B")
    elif score >= 70:
        print("Your grade is: ", "C")
    elif score >= 60:
        print("Your grade is: ", "D")
    else:
        print("Your grade is: ", "F")

# Asking user for input and declaring variables. 

score_a = int(input("enter 1st result: "))
score_b = int(input("enter 2nd result: "))
score_c = int(input("enter 3rd result: "))
score_d = int(input("enter 4th result: "))
score_e = int(input("enter 5th result: "))

# Changing our variables into a range.

score = [score_a,score_b,score_c,score_d,score_e]

# for loop to determine grades.

for i in score:
    determine_grade(i)

# Displaying the average score to the user.

print('Average test score:',calc_average(score_a,score_b,score_c,score_d,score_e))


