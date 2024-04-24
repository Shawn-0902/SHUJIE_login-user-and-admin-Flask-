class Location:
    def __init__(self,location_id, country, postal_code):
        self.__country = country
        self.__postal_code = postal_code
        self.__location_id = location_id

    def set_country(self,country):
        self.__country = country

    def set_postal_code(self,postal_code):
        self.__postal_code = postal_code

    def set_location_id(self,location_id):
        self.__location_id = location_id

    def get_country(self):
        return self.__country

    def get_postal_code(self):
        return self.__postal_code

    def get_location_id(self):
        return self.__location_id

class Laundromat:

    def __init__(self,name,address,opening_time,closing_time,star_rating,image):
        self.__name = name
        self.__address = address
        self.__opening_time = opening_time
        self.__closing_time = closing_time
        self.__star_rating = star_rating
        self.__image = image

    def set_name(self,name):
        self.__name = name

    def set_address(self, address):
        self.__address = address

    def set_opening_time(self,opening_time):
        self.__opening_time = opening_time

    def set_closing_time(self, closing_time):
        self.__closing_time = closing_time

    def set_star_rating(self,star_rating):
        self.__star_rating = star_rating

    def set_image(self, image):
        self.__image = image

    def get_name(self):
        return self.__name

    def get_address(self):
        return self.__address

    def get_opening_time(self):
        return self.__opening_time

    def get_closing_time(self):
        return self.__closing_time

    def get_star_rating(self):
        return self.__star_rating

    def get_image(self):
        return self.__image
