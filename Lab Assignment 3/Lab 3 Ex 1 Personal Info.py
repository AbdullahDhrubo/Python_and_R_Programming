#Creating the class to hold personal info data
class PersonalInformation:
#Using constructor to define objects of the class PersonalInformation
    def __init__(self, name, address, age, phone):
        self.__name = name
        self.__address = address
        self.__age = age
        self.__phone = phone

#Using the mutator method to set or update the personal informations.
    def set_name(self, name):
        self.__name = name

    def set_address(self, address):
        self.__address = address

    def set_age(self, age):
        self.__age = age

    def set_phone(self, phone):
        self.__phone = phone

#Using the accessor method to get or fetch the personal informations.
    def get_name(self):
        return self.__name

    def get_address(self):
        return self.__address

    def get_age(self):
        return self.__age

    def get_phone(self):
        return self.__phone

#Method to fetch entire information of the person
    def __str__(self):
        return 'Name: '+ self.__name + '\n' + 'Address: ' + self.__address + '\n' + 'Age: '\
               + str(self.__age) + '\n' + 'Phone: ' + str(self.__phone) + '\n'

#Creating the list for personal info objects for adding values to attributes of objects.
def main():
    Myself = PersonalInformation('Jhonny','Borlange', 28, 949834934)
    Friend = PersonalInformation('David', 'Gavle', 27, 9823793827)
    Family = PersonalInformation('Adams', 'Stockholm', 65, 2358299732)

# Creating a list of range.
    persons = [Myself, Friend, Family]

# Printing output using the for loop.
    for i in persons:
        print(i)

# Calling for our function
main()