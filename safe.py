__author__ = 'Kazon Wilson'

# This is the class file for calculating all information from the employee's safe.


class Safe:

    def __init__(self):
        # Create a constant for the amount of tube slots in the register.
        # Since this value does not change, there is no need to get this value from user input.
        self.__TUBE_SLOTS = 8

        self.__beginning_qty = [0] * self.__TUBE_SLOTS
        self.__ending_qty = [0] * self.__TUBE_SLOTS
        self.__tube_amts = [0] * self.__TUBE_SLOTS
        self.__beginning_prod = [0] * self.__TUBE_SLOTS
        self.__ending_prod = [0] * self.__TUBE_SLOTS
        self.__beginning_total = 0
        self.__ending_total = 0
        self.__beg_tube_qty_finished = True
        self.__end_tube_qty_finished = True
        self.__tube_amt_finished = True
        self.__beg_qty_count = 0
        self.__end_qty_count = 0
        self.__new_beg_qty = 0
        self.__new_end_qty = 0
        self.__tube_count = 0
        self.__new_amt = 0

    def get_qty(self):
        print('Enter the quantity of tubes in each slot for your beginning (Beginning QTY)')
        try:
            for btube in range(self.__TUBE_SLOTS):
                print('Tube #', btube + 1, ': ', sep='', end='')
                self.__beginning_qty[btube] = int(input())
                self.__beg_tube_qty_finished = True
                self.__beg_qty_count += 1
        except ValueError:
            print("ERROR: Drops must be valid numbers")
            self.__beg_tube_qty_finished = False

        # If the user enters an invalid number, the program moves to this while loop.
        while not self.__beg_tube_qty_finished:
            print('Enter the quantity of tubes in each slot for your beginning (Beginning QTY)')
            try:
                # The loop begins at the last index where they entered an invalid number.
                # The index number is determined by the self.__end_qty_count accumulator.
                for btube in range(self.__TUBE_SLOTS - self.__beg_qty_count):
                    print('Tube #', self.__beg_qty_count + 1, ': ', sep='', end='')
                    self.__new_beg_qty = int(input())
                    # The new (and hopefully valid) value entered by the user is inserted into the list at the index
                    # they entered an invalid number at.
                    self.__tube_amts.insert(self.__beg_qty_count, self.__new_beg_qty)
                    # This is set to true so that the while loops safely exits as soon as this nested for-loop finishes
                    # and the user has entered all valid numbers.
                    self.__beg_tube_qty_finished = True
                    self.__beg_qty_count += 1
            except ValueError:
                print("ERROR: Drops must be valid numbers")
                self.__beg_tube_qty_finished = False

        # The same process for beginning is repeated for ending, see beginning for important notes.
        print('Now enter the quantity of tubes in each slot for your ending (Ending QTY)')
        try:
            for etube in range(self.__TUBE_SLOTS):
                print('Tube #', etube + 1, ': ', sep='', end='')
                self.__ending_qty[etube] = int(input())
                self.__end_tube_qty_finished = True
                self.__end_qty_count += 1
        except ValueError:
            print("ERROR: Drops must be valid numbers")
            self.__end_tube_qty_finished = False

        while not self.__end_tube_qty_finished:
            print('Enter the quantity of tubes in each slot for your ending (Ending QTY)')
            try:
                for etube in range(self.__TUBE_SLOTS - self.__end_qty_count):
                    print('Tube #', self.__end_qty_count + 1, ': ', sep='', end='')
                    self.__new_end_qty = int(input())
                    self.__ending_qty.insert(self.__end_qty_count, self.__new_end_qty)
                    self.__end_tube_qty_finished = True
                    self.__end_qty_count += 1
            except ValueError:
                print("ERROR: Drops must be valid numbers")
                self.__end_tube_qty_finished = False

        return self.__beginning_qty, self.__ending_qty

    def get_amt(self):
        print('Enter the total amount of money a tube should be holding per slot ($ amt)')
        try:
            for tube_amt in range(self.__TUBE_SLOTS):
                print('Slot #', tube_amt + 1, ': ', sep='', end='')
                self.__tube_amts[tube_amt] = int(input())
                self.__tube_amt_finished = True
                self.__tube_count += 1
        except ValueError:
            print("ERROR: Drops must be valid numbers")
            self.__tube_amt_finished = False

        while not self.__tube_amt_finished:
            print('Enter the total amount of money a tube should be holding per slot ($ amt)')
            try:
                for tube_amt in range(self.__TUBE_SLOTS - self.__tube_count):
                    print('Slot #', self.__tube_count + 1, ': ', sep='', end='')
                    self.__new_amt = int(input())
                    self.__tube_amts.insert(self.__tube_count, self.__new_amt)
                    self.__tube_amt_finished = True
                    self.__tube_count += 1
            except ValueError:
                print("ERROR: Drops must be valid numbers")
                self.__tube_amt_finished = False

        return self.__tube_amts

    def calc_prods(self):
        self.__beginning_prod = [a*b for a, b in zip(self.__beginning_qty, self.__tube_amts)]
        self.__ending_prod = [a*b for a, b in zip(self.__ending_qty, self.__tube_amts)]
        self.__beginning_total = sum(self.__beginning_prod)
        self.__ending_total = sum(self.__ending_prod)

        return self.__beginning_prod, self.__ending_prod, self.__beginning_total, self.__ending_total