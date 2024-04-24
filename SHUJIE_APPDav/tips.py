class Tips:
    # count_id = 0

    def __init__(self, tip_id, title, desc):
        # Products.count_id += 1
        self.__tip_id = tip_id
        self.__title = title
        self.__desc = desc

    def get_tip_id(self):
        return self.__tip_id

    def get_title(self):
        return self.__title

    def get_desc(self):
        return self.__desc

    def set_tip_id(self, tip_id):
        self.__tip_id = tip_id

    def set_title(self, title):
        self.__title = title

    def set_desc(self, desc):
        self.__desc = desc