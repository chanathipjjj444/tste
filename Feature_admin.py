class Person:
    def __init__(self, prefix, name, surname, email, phone_number):
        self.__prefix = prefix
        self.__name = name
        self.__surname = surname
        self.__email = email
        self.__phone_number = phone_number
    def insert_person_info(self):
        pass

class Admin(Person):
    def __init__(self, prefix, name, surname, email, phone_number, update_hotel):
        Person.__init__(self, prefix, name, surname, email, phone_number) 
        self.__update_hotel = update_hotel

class Report:
    def __init__(self, phone, user, complaint_details):
        self.__phone = phone
        self.__user = user
        self.__complaint_details = complaint_details
    def insert_report_details(self):
        pass
    def respond_report(self):
        pass    

class Hotel():
    def __init__(self):
        self.__name_hotel = []
        self.__rating = []
        self.__number_room = []
        self.__hotel_picture = []
    def get_hotel_details(self):
        pass
        
class HotelCatalog():
    def __init__(self):
        self.__hotel_list = []
    def select_hotel(self):
        pass