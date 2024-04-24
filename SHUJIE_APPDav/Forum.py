class Forum:
    def __init__(self, forum_id, name, gender, content, postedOn):
        self.__forum_id = forum_id
        self.__name = name
        self.__gender = gender
        self.__content = content
        self.__postedOn = postedOn

    def get_forum_id(self):
        return self.__forum_id

    def get_name(self):
        return self.__name

    def get_gender(self):
        return self.__gender

    def get_content(self):
        return self.__content

    def get_postedOn(self):
        return self.__postedOn

    def set_forum_id(self, forum_id):
        self.__forum_id = forum_id

    def set_name(self, name):
        self.__name = name

    def set_gender(self, gender):
        self.__gender = gender

    def set_content(self, content):
        self.__content = content

    def set_postedOn(self, postedOn):
        self.__postedOn = postedOn