class Booking:
    def __init__(self, booking_id, date, time_slot, machine_id, status, model, capacity, price_per_use):
        self.__booking_id = booking_id
        self.__date = date
        self.__time_slot = time_slot
        self.__machine_id = machine_id
        self.__status = status
        self.__model = model
        self.__capacity = capacity
        self.__price_per_use = price_per_use

    # Getters
    def get_booking_id(self):
        return self.__booking_id

    def get_date(self):
        return self.__date

    def get_time_slot(self):
        return self.__time_slot

    def get_machine_id(self):
        return self.__machine_id

    def get_status(self):
        return self.__status

    def get_model(self):
        return self.__model

    def get_capacity(self):
        return self.__capacity

    def get_price_per_use(self):
        return self.__price_per_use

    # Setters
    def set_booking_id(self, booking_id):
        self.__booking_id = booking_id

    def set_date(self, date):
        self.__date = date

    def set_time_slot(self, time_slot):
        self.__time_slot = time_slot

    def set_machine_id(self, machine_id):
        self.__machine_id = machine_id

    def set_status(self, status):
        self.__status = status

    def set_model(self, model):
        self.__model = model

    def set_capacity(self, capacity):
        self.__capacity = capacity

    def set_price_per_use(self, price_per_use):
        self.__price_per_use = price_per_use
