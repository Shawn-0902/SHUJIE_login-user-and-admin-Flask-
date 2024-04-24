class Event:

    def __init__(self,name,description,date,image):
        self.__name = name
        self.__description = description
        self.__date = date
        self.__image = image

    def set_name(self,name):
        self.__name = name

    def set_description(self, description):
        self.__description = description

    def set_date(self,date):
        self.__date = date

    def set_image(self, image):
        self.__image = image

    def get_name(self):
        return self.__name

    def get_description(self):
        return self.__description

    def get_date(self):
        return self.__date

    def get_image(self):
        return self.__image
