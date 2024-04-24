class LaundryMachine:
    # Fixed image path as a class attribute
    FIXED_IMAGE_PATH = 'static/img/laundry_machine.png'

    def __init__(self, machine_id, status, model, capacity, price_per_use):
        self.__machine_id = machine_id
        self.__status = status
        self.__model = model
        self.__capacity = capacity
        self.__price_per_use = price_per_use
        self.__image = LaundryMachine.FIXED_IMAGE_PATH  # Use the fixed image path

    # Getters
    def get_machine_id(self):
        return self.__machine_id

    def get_status(self):
        return self.__status

    def get_model(self):
        return self.__model

    def get_capacity(self):
        return self.__capacity

    def get_available_times(self):
        return self.__available_times

    def get_price_per_use(self):
        return self.__price_per_use

    def get_image(self):
        return self.__image

    # Setters
    def set_machine_id(self, machine_id):
        self.__machine_id = machine_id

    def set_status(self, status):
        self.__status = status

    def set_model(self, model):
        self.__model = model

    def set_capacity(self, capacity):
        self.__capacity = capacity

    def set_available_times(self, available_times):
        self.__available_times = available_times

    def set_price_per_use(self, price_per_use):
        self.__price_per_use = price_per_use

    def set_image(self, image):
        self.__image = image

    # Additional methods for the time_slot
    def add_time_slot(self, time_slot):
        if time_slot not in self.__available_times:
            self.__available_times.append(time_slot)

    def remove_time_slot(self, time_slot):
        if time_slot in self.__available_times:
            self.__available_times.remove(time_slot)
