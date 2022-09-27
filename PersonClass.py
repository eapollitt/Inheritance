class Person: 

    def __init__(self, name, address, phone_number):
        self.__name = name
        self.__address = address
        self.__phone_number = phone_number

    def get_name(self): 
        return self.__name

    def get_address(self):
        return self.__address

    def get_phone_number(self):
        return self.__phone_number

    def print_person(self): 
        print(self.__name, self.__address, self.__phone)

class Customer(Person):

    def __init__(name, number, mailing):
        Person.__init__(name, number, mailing)
        mailing 