# Ex- 3

# Declaring inputted float variable, calculating and printing the output.

def property():
    actual_value = float(input("Enter the actual value of the property: "))
    assesment_value = actual_value*0.6
    print("The assessment value is:",format(assesment_value, '.2f'),
         "The property tax is: ", format(assesment_value*(.72/100),',.2f'))

# Calling function. 

property()
