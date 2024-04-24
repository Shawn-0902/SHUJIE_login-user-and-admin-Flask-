class Products:
    # count_id = 0

    def __init__(self, product_id, name, type, rating, img):
        # Products.count_id += 1
        self.__product_id = product_id
        self.__name = name
        self.__type = type
        self.__rating = rating
        self.__img = img

    def get_product_id(self):
        return self.__product_id

    def get_name(self):
        return self.__name

    def get_type(self):
        return self.__type

    def get_rating(self):
        return self.__rating

    def get_img(self):
        return self.__img

    def set_product_id(self, product_id):
        self.__product_id = product_id

    def set_name(self, name):
        self.__name = name

    def set_type(self, type):
        self.__type = type

    def set_rating(self, rating):
        self.__rating = rating

    def set_img(self, img):
        self.__img = img
