from __init__ import session, shelve
from datetime import datetime


class PointDetails:

    def __init__(self, user_id, transaction_id='', transaction_date='', transaction_type='', category='', points=''):
        self.__user_id = user_id
        self.__transaction_id = transaction_id
        self.__transaction_date = transaction_date
        self.__transaction_type = transaction_type
        self.__category = category
        self.__points = points

    def get_transaction_id(self):
        return self.__transaction_id

    def get_transaction_date(self):
        return self.__transaction_date

    def get_transaction_type(self):
        return self.__transaction_type

    def get_category(self):
        return self.__category

    def get_user_id(self):
        return self.__user_id

    def get_points(self):
        return self.__points

    def set_transaction_id(self, transaction_id):
        self.__transaction_id = transaction_id

    def set_transaction_date(self, transaction_date):
        self.__transaction_date = transaction_date

    def set_type(self, transaction_type):
        self.__transaction_type = transaction_type

    def set_category(self, category):
        self.__category = category

    def set_user_id(self, user_id):
        self.__user_id = user_id

    def set_points(self, points):
        self.__points = points

    def add_rewards(self):
        transaction_dict = {}
        reward_dict = {}
        db = shelve.open('reward.db', 'c')
        try:
            transaction_dict = db['Transaction']
        except:
            print("Error in retrieving Transaction from reward.db.")

        count = len(transaction_dict) + 1
        transaction_id = count
        transaction = PointDetails(self.__user_id, str(transaction_id), datetime.now().strftime("%Y-%m-%d"),
                                   self.__transaction_type, self.__category, self.__points)
        transaction_dict[transaction_id] = transaction
        db['Transaction'] = transaction_dict

        try:
            reward_dict = db['Reward']
        except:
            print("Error in retrieving Reward from reward.db.")

        reward_points = reward_dict.get(self.__user_id)
        if reward_points is not None:
            reward_points = reward_points + self.__points
        else:
            reward_points =  self.__points

        reward_dict[self.__user_id] = reward_points
        db['Reward'] = reward_dict
        db.close()

    def redeem(self):
        transaction_dict = {}
        reward_dict = {}
        db = shelve.open('reward.db', 'c')
        try:
            transaction_dict = db['Transaction']
        except:
            print("Error in retrieving Transaction from reward.db.")

        count = len(transaction_dict) + 1
        transaction_id = count
        transaction = PointDetails(self.__user_id, str(transaction_id), datetime.now().strftime("%Y-%m-%d"),
                                   self.__transaction_type, self.__category, self.__points)
        transaction_dict[transaction_id] = transaction
        db['Transaction'] = transaction_dict


        try:
            reward_dict = db['Reward']
        except:
            print("Error in retrieving Reward from reward.db.")

        reward_points = reward_dict.get(self.__user_id)
        if reward_points is not None:
            reward_points = reward_points - self.__points
        else:
            reward_dict[self.__user_id] = self.__points

        db['Reward'] = reward_dict
        db.close()

    def get_reward_points(self):
        db = shelve.open('reward.db', 'c')
        reward_points = 0
        try:
            reward_dict = db['Reward']
            reward_points = reward_dict.get(self.__user_id)
        except:
            print("Error in retrieving reward from reward.db.")

        db.close()

        return reward_points
