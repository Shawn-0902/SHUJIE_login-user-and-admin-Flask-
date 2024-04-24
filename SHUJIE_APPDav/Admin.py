# User class
class Admin:
    def __init__(self, admin_id, first_name, last_name, authority, email, password, description):

        self.__admin_id = admin_id
        self.__first_name = first_name
        self.__last_name = last_name
        self.__email = email
        self.__description = description
        self.__password = password
        self.__authority = authority

    def get_admin_id(self):
        return self.__admin_id

    def get_first_name(self):
        return self.__first_name

    def get_last_name(self):
        return self.__last_name

    def get_description(self):
        return self.__description

    def get_password(self):
        return self.__password

    def get_email(self):
        return self.__email

    def get_authority(self):
        return self.__authority

    def set_authority(self, authority):
        self.__authority = authority

    def set_admin_id(self, admin_id):
        self.__admin_id = admin_id

    def set_first_name(self, first_name):
        self.__first_name = first_name

    def set_last_name(self, last_name):
        self.__last_name = last_name

    def set_email(self, email):
        self.__email = email

    def set_description(self,description):
        self.__description=description

    def set_password(self, password):
        self.__password = password

    def set_admin_id(self, admin_id):
        # Make it read-only
        pass

    def get_full_name(self):
        return f"{self.__first_name} {self.__last_name}"