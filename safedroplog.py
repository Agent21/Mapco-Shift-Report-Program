__author__ = 'Kazon Wilson'

# This is the class file for calculating all information from the employee's safe drops.


class SafeDropLog:

    def __init__(self):
        self.__total_drops = 0
        self.__safe_drop_max = 0
        self.__safe_drop_list = []
        self.__get_drops_finished = True
        self.__get_drops_count = 0
        self.__new_safe_drop_value = 0
        self.__drop_value = 0

    def get_drops(self):
        # The user enters the total amount of drops they made. Next, they enter the values for each drop and these
        # values are appended to a new list called self.__drop_list. Finally, the list is returned for use in the main
        # program.

        while True:
            try:
                self.__safe_drop_max = int(input('Enter the total amount of drops you made: '))
                break
            except ValueError:
                print("ERROR: You must enter a valid number!")

        try:
            for drops in range(self.__safe_drop_max):
                print('Drop #', drops + 1, ': ', sep='', end='')
                self.__drop_value = int(input())
                self.__safe_drop_list.append(self.__drop_value)
                self.__get_drops_count += 1
        except ValueError:
            print("ERROR: Drops must be valid numbers")
            self.__get_drops_finished = False

        while not self.__get_drops_finished:
            try:
                for drops in range(self.__safe_drop_max - self.__get_drops_count):
                    print('Drop #', self.__get_drops_count + 1, ': ', sep='', end='')
                    self.__new_safe_drop_value = int(input())
                    self.__safe_drop_list.insert(self.__get_drops_count, self.__new_safe_drop_value)
                    self.__get_drops_count += 1
            except ValueError:
                print("ERROR: Drops must be valid numbers")
                self.__get_drops_finished = False
            finally:
                break

        return self.__safe_drop_list

    def calc_drops(self):
        self.__total_drops = sum(self.__safe_drop_list)

        return self.__total_drops