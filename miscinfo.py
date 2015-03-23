__author__ = 'Kazon Wilson'

# This is the class file for storing all information from the employee's shift report.


class MiscInfo:
    def __init__(self, employee_name, shift, store_num, date):
        self.__employee_name = employee_name
        self.__shift_num = shift
        self.__store_num = store_num
        self.__date = date

    def set_employee_name(self, employee_name):
        self.__employee_name = employee_name

    def set_shift_num(self, shift_num):
        self.__shift_num = shift_num

    def set_store_num(self, store_num):
        self.__store_num = store_num

    def set_date(self, date):
        self.__date = date

    def get_employee_name(self):
        return self.__employee_name

    def get_shift_num(self):
        return self.__shift_num

    def get_store_num(self):
        return self.__store_num

    def get_date(self):
        return self.__date

    def __str__(self):
        return "Employee name: " + self.__employee_name + \
            "\nShift: " + str(self.__shift_num) + \
            "\nStore #: " + str(self.__store_num) + \
            "\nDate: " + self.__date