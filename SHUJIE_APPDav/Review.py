class Review:
    # count_id = 0

    # initializer method
    def __init__(self, review_id, first_name, last_name, gender, star_rating, remarks):
        # Review.count_id += 1
        # self.__Review_id = Review.count_id
        self.__review_id = review_id
        self.__first_name = first_name
        self.__last_name = last_name
        self.__gender = gender
        self.__star_rating = star_rating
        self.__remarks = remarks

    # accessor methods
    def get_review_id(self):
        return self.__review_id

    def get_first_name(self):
        return self.__first_name

    def get_last_name(self):
        return self.__last_name

    def get_gender(self):
        return self.__gender

    def get_star_rating(self):
        return self.__star_rating

    def get_remarks(self):
        return self.__remarks

    # mutator methods
    def set_review_id(self, review_id):
        self.__review_id = review_id

    def set_first_name(self, first_name):
        self.__first_name = first_name

    def set_last_name(self, last_name):
        self.__last_name = last_name

    def set_gender(self, gender):
        self.__gender = gender

    def set_star_rating(self, star_rating):
        self.__star_rating = star_rating

    def set_remarks(self, remarks):
        self.__remarks = remarks
