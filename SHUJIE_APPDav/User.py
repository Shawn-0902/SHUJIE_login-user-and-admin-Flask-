# Carbon class
class Carbon:
    count_id = 0

    # initializer method
    def __init__(self, user_id,service, temp, load, time, remarks):
        try:
            self.__time = float(time)
        except ValueError:
            # Handle the case where time cannot be converted to float
            print(f"Invalid time value: {time}")
            self.__time = 0  # Set to a default value or handle appropriately

        self.__user_id = user_id
        self.__service = service
        self.__temp = temp
        self.__load = load
        self.__time = time
        self.__remarks = remarks

    # accessor methods
    def get_user_id(self):
        return self.__user_id

    def get_service(self):
        return self.__service

    def get_temp(self):
        return self.__temp

    def get_load(self):
        return self.__load

    def get_time(self):
        return self.__time

    def get_remarks(self):
        return self.__remarks

    # mutator methods
    def set_user_id(self, user_id):
        self.__user_id = user_id

    def set_service(self, service):
        self.__service = service

    def set_temp(self, temp):
        self.__temp = temp

    def set_load(self, load):
        self.__load = load

    def set_time(self, time):
        self.__time = time

    def set_remarks(self, remarks):
        self.__remarks = remarks

    def get_calculate_carbon_footprint(self):
        service_factor = {'Dryer': 1.0, 'Washer': 0.5}
        temp_factor = {'Hot': 0.98, 'Warm': 0.66, 'Cold': 0.33}
        load_factor = {'Large': 2.0, 'Medium': 1.5, 'Small': 1.0}

        service_value = service_factor.get(self.__service)
        temp_value = temp_factor.get(self.__temp)
        load_value = load_factor.get(self.__load)

        if service_value is None:
            print(f"Invalid service input: {self.__service}")
        if temp_value is None:
            print(f"Invalid temp input: {self.__temp}")
        if load_value is None:
            print(f"Invalid load input: {self.__load}")
        if not isinstance(self.__time, (float, int)):
            print(f"Invalid time input: {self.__time}, Type: {type(self.__time)}")

        if service_value is None or temp_value is None or load_value is None or not isinstance(self.__time,
                                                                                               (float, int)):
            print("Invalid input for calculating carbon footprint.")
            return 0

        carbon_footprint = float((service_value + temp_value + load_value) * self.__time / 60)
        return round(carbon_footprint, 2)

def set_time(self, time):
    try:
        self.__time = float(time)
    except ValueError:
        print(f"Invalid time value: {time}")
        self.__time = 0  # Set to a default value or handle appropriately