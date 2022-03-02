class Person: #super class
    def __init__(self, name, address, phone):
        self.__name = name
        self.__address = address
        self.__phone = phone

    def print_person(self):
        print("Name:", self.__name )
        print("Address:", self.__address)
        print("Phone:", self.__phone)

#sub class
class Customer(Person):
    def __init__(self, name, address, phone, customer_no, mailing_list):
        Person.__init__(self, name, address, phone)

        self.__customer_no = customer_no
        self.__mailing_list = mailing_list

    def print_person(self):
        print("Customer Number:", self.__customer_no)
        print("Mailing List Preference:", self.__mailing_list)
        


        