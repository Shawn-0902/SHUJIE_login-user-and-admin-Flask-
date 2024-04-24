class Service:

    def __init__(self,name,description):
        self.__name = name
        self.__description = description

    def set_name(self,name):
        self.__name = name

    def set_description(self, description):
        self.__description = description

    def get_name(self):
        return self.__name

    def get_description(self):
        return self.__description
