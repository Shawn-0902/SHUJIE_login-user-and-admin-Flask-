# User class
class User1:

    def __init__(self, user_id, first_name, last_name, email, gender, birthdate, city, postal_code, address, password,
                 security_question1=None, security_answer1=None, security_question2=None, security_answer2=None,
                 security_question3=None, security_answer3=None):
        self.__user_id = user_id
        self.__first_name = first_name
        self.__last_name = last_name
        self.__email = email
        self.__gender = gender
        self.__birthdate = birthdate
        self.__city = city
        self.__postal_code = postal_code
        self.__address = address
        self.__password = password
        self.__security_question1 = security_question1
        self.__security_answer1 = security_answer1
        self.__security_question2 = security_question2
        self.__security_answer2 = security_answer2
        self.__security_question3 = security_question3
        self.__security_answer3 = security_answer3

    def get_security_question1(self):
        return self.__security_question1

    def get_security_answer1(self):
        return self.__security_answer1

    def get_security_question2(self):
        return self.__security_question2

    def get_security_answer2(self):
        return self.__security_answer2

    def get_security_question3(self):
        return self.__security_question3

    def get_security_answer3(self):
        return self.__security_answer3

    def set_security_question1(self, question):
        self.__security_question1 = question

    def set_security_answer1(self, answer):
        self.__security_answer1 = answer

    def set_security_question2(self, question):
        self.__security_question2 = question

    def set_security_answer2(self, answer):
        self.__security_answer2 = answer

    def set_security_question3(self, question):
        self.__security_question3 = question

    def set_security_answer3(self, answer):
        self.__security_answer3 = answer

    def get_user_id(self):
        return self.__user_id

    def get_first_name(self):
        return self.__first_name

    def get_last_name(self):
        return self.__last_name

    def get_gender(self):
        return self.__gender

    def get_birthdate(self):
        return self.__birthdate

    def get_city(self):
        return self.__city

    def get_postal_code(self):
        return self.__postal_code

    def get_address(self):
        return self.__address

    def get_password(self):
        return self.__password

    def get_email(self):
        return self.__email

    def set_first_name(self, first_name):
        self.__first_name = first_name

    def set_last_name(self, last_name):
        self.__last_name = last_name

    def set_email(self, email):
        self.__email = email

    def set_gender(self, gender):
        self.__gender = gender

    def set_birthdate(self, birthdate):
        self.__birthdate = birthdate

    def set_city(self, city):
        self.__city = city

    def set_postal_code(self, postal_code):
        self.__postal_code = postal_code

    def set_address(self, address):
        self.__address = address

    def set_password(self, password):
        self.__password = password

    def set_user_id(self, user_id):
        # Make it read-only
        pass

    def get_full_name(self):
        return f"{self.__first_name} {self.__last_name}"
