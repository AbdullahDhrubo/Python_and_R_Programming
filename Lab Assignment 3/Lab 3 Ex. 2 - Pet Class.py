# Creating a class Pet.
class Pet:

# Arguments are given default values '' to create empty class instances
    def __init__(self, name = '', animal_type = '', age= ''):
        self.__name = name
        self.__animal_type = animal_type
        self.__age = age

# Method to get or fetch pet details
    def get_name(self):
        return self.__name

    def get_animal_type(self):
        return self.__animal_type

    def get_age(self):
        return self.__age

# Method to set or update pet details
    def set_name(self,name):
        self.__name = name

    def set_animal_type(self,animal_type):
        self.__animal_type = animal_type

    def set_age(self, age):
        self.__age = age

# Method to fetch entire information of the pet.
    def __str__(self):
        pet_info = (self.__name + ' is a ' + self.__animal_type + ' which is ' + str(self.__age) + ' years old.')
        return pet_info

# Asking user input for number of pets and creating the list for pet objects,
# using set method to add values to attributes of the object
def main():
    no_of_pets = int(input('Enter Number of pets you have:'))
    pets_list =[]
    for num in range(1,no_of_pets+1):
        name = input("Your pet name: ")
        animal_type = input("What type of pet is it: ")
        age = input("How old is your pet: ")
# Updating the values of our attributes, using user inputs.
        pets = Pet()
        pets.set_name(name)
        pets.set_animal_type(animal_type)
        pets.set_age(age)
        pets_list.append(pets)
# Giving an option to the user which type of listing to be printed.
    listing = []
    user_choice = int(input('Please select option 1 or 2.\n 1.Show all pets \n 2.Chosen Pet \n'))
    if user_choice == 1:
        listing = pets_list
    else:
        pet_type = input('Enter animal Type you want to show:')
        for pet in pets_list:
            if pet.get_animal_type() == pet_type:
                listing.append(pet)
# Printing the output using the for loop.
    for pet in listing:
        print(pet)
# Calling our function.
main()