__author__ = 'Kazon Wilson'

# This is the class file for calculating all information from the employee's register.

from math import trunc


class Register:

    def __init__(self):
        self.__REG_SLOTS = 9
        self.__beginning_values = []
        self.__ending_values = []
        self.__reg_slot_values = ['$2', '$10', '$5', '$1', '.50', '.25', '.10', '.05', '.01']
        self.__beginning_subtotal = 0.0
        self.__ending_subtotal = 0.0
        self.__beginning_ledge = 0.0
        self.__ending_ledge = 0.0
        self.__beginning_total = 0.0
        self.__ending_total = 0.0
        self.__beg_reg_finished = True
        self.__end_reg_finished = True
        self.__breg = 0
        self.__ereg = 0
        self.__beginning_reg = {}
        self.__ending_reg = {}
        self.__beg_reg_count = 0
        self.__end_reg_count = 0
        self.__dict_counter1 = 0
        self.__dict_counter2 = 0

    def get_reg(self):
        print('Enter the amount of money in each slot of the register for your beginning')
        try:
            for reg_value in self.__reg_slot_values:
                print(reg_value, ': ', sep='', end='')
                self.__breg = float(input())

                # This is not really the safest way to do this, but if a user inputs too many numbers
                # past the decimal point, this will truncate them. I did this because it's a hassle to create a check
                # that will throw an error if the user enters too many numbers, ie. the self.__breg value is entered
                # as a string, then split by the decimal, then it checks to see if it is valid. Finally, the string
                # is then converted to a float and the program can safely resume. Doing this would be easy if it
                # didn't need to be done within a for loop. :(
                self.__breg = trunc(self.__breg*100)/100
                self.__beginning_values.append(self.__breg)
                self.__beg_reg_count += 1
        except ValueError:
            print("ERROR: Drops must be valid numbers")
            self.__beg_reg_finished = False

        # If the user enters an invalid number, the program moves to this while loop.
        while not self.__beg_reg_finished:
            try:
                # The loop begins at the last index of self.__reg_slot_values where they entered an invalid number.
                # The index number is determined by the self.__beg_reg_count accumulator. As the loop progresses,
                # 1 is added to the overall value.

                for reg_value in self.__reg_slot_values[self.__beg_reg_count:]:
                    print(reg_value, ': ', sep='', end='')
                    self.__breg = float(input())

                    # Once again, not safe.
                    self.__breg = trunc(self.__breg*100)/100

                    # The new (and hopefully valid) value entered by the user is inserted into the list at the index
                    # they entered an invalid number at.
                    self.__beginning_values.insert(self.__beg_reg_count, self.__breg)

                    # This is set to true so that the while loops safely exits as soon as this nested for-loop finishes
                    # and the user has entered all valid numbers.
                    self.__beg_reg_finished = True
                    self.__beg_reg_count += 1
            except ValueError:
                print("ERROR: Drops must be valid numbers")
                self.__beg_reg_finished = False

        # Process is repeated for ending register. See beginning register for important notes.
        print('Now enter the amount of money in each slot of the register for your ending')
        try:
            for reg_value in self.__reg_slot_values:
                print(reg_value, ': ', sep='', end='')
                self.__ereg = float(input())
                self.__ereg = trunc(self.__ereg*100)/100
                self.__ending_values.append(self.__ereg)
                self.__end_reg_count += 1
        except ValueError:
            print("ERROR: Drops must be valid numbers")
            self.__end_reg_finished = False

        while not self.__end_reg_finished:
            try:
                for reg_value in self.__reg_slot_values[self.__end_reg_count:]:
                    print(reg_value, ': ', sep='', end='')
                    self.__ereg = float(input())
                    self.__ereg = trunc(self.__ereg*100)/100
                    self.__ending_values.insert(self.__end_reg_count, self.__ereg)
                    self.__end_reg_finished = True
                    self.__end_reg_count += 1
            except ValueError:
                print("ERROR: You must enter a valid number!")
                self.__end_reg_finished = False

        while True:
            try:
                self.__beginning_ledge = float(input('Enter the amount for your beginning safe ledge (If applicable): '))
                break
            except ValueError:
                print("ERROR: You must enter a valid number!")

        while True:
            try:
                self.__ending_ledge = float(input('Enter the amount for your ending safe ledge (If applicable): '))
                break
            except ValueError:
                print("ERROR: You must enter a valid number!")

        return self.__beginning_values, self.__ending_values, self.__beginning_ledge, self.__ending_ledge,\
            self.__reg_slot_values

    def create_dict(self):
        # This creates a dictionary for easier printing in the main program.
        # It would look like this ex. {'$2':value, '10':value}
        for a in self.__reg_slot_values:
            self.__beginning_reg[a] = self.__beginning_values[self.__dict_counter1]
            self.__dict_counter1 += 1

        for b in self.__reg_slot_values:
            self.__ending_reg[b] = self.__ending_values[self.__dict_counter2]
            self.__dict_counter2 += 1

        return self.__beginning_reg, self.__ending_reg

    def calc_reg(self):
        self.__beginning_subtotal = sum(self.__beginning_values)
        self.__ending_subtotal = sum(self.__ending_values)
        self.__beginning_total = self.__beginning_subtotal + self.__beginning_ledge
        self.__ending_total = self.__ending_subtotal + self.__ending_ledge

        return self.__beginning_total, self.__ending_total, self.__beginning_subtotal, self.__ending_subtotal
