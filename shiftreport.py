__author__ = 'Kazon Wilson'

# This program was designed to allow cashiers to process information from their shift report at a faster pace than
# it would take them if they calculated everything by hand.

#import csv  # Might use this later.
import re
import time
import miscinfo
import safe
import register
import safedroplog


def main():
    # User begins their shift report by entering misc info, (ie. their name, shift, and store #, date will
    # automatically be acquired.

    # User is prompted to enter their name.
    employee_name = input('Please enter your name: ')

    # If the user enters anything other than letters for their name, an error will be thrown.
    while not re.match("^[A-Za-z ]*$", employee_name):
        print("ERROR: Please only enter letters!")
        employee_name = input('Please enter your name: ')

    # Make sure the user doesn't input an empty string.
    while employee_name == '':
        print("ERROR: Please enter something!")
        employee_name = input('Please enter your name: ')

    # User is prompted to enter their shift number
    # If the user enters anything other than numbers or they enter a value greater than 3,
    # an error will be thrown.
    while True:
        try:
            shift = int(input('Please enter the shift (1-3): '))
            while shift > 3:
                print("ERROR: There are only 3 shifts in a day!")
                shift = int(input('Please enter the shift (1-3): '))
            break

        except ValueError:
            print("ERROR: You must enter a valid number!")

    # User is prompted to enter their store number
    # If the user enters anything other than numbers or an error will be thrown.
    store_num = input('Please enter your store number: ')

    while not re.match("^[0-9]*$", store_num):
        print("ERROR: Store number can only be numbers!!")
        store_num = input('Please enter your store number: ')

    # A string for the current date is stored is created.
    date = (time.strftime("%m-%d-%Y"))

    # Create an object from the miscinfo class that stores information for the parameters.
    misc_info = miscinfo.MiscInfo(employee_name, shift, store_num, date)    # Useless object.

    # Create an object from the safe class.
    first_shift_safe = safe.Safe()

    # Create an object from the register class.
    first_shift_reg = register.Register()

    # Create an object from the safedroplog class.
    first_shift_safedroplog = safedroplog.SafeDropLog()

    # Program will acquire information for the safe section of the shift report.
    tube_amts = first_shift_safe.get_amt()  # May use this for writing to a csv file later on.

    beginning_qty, ending_qty = first_shift_safe.get_qty()

    beginning_prod, ending_prod, beginning_safe_total, ending_safe_total = first_shift_safe.calc_prods()

    tube_req = input('Would you like to see your beginning and ending total for each slot? (Enter yes or no): ')

    # If the user enters anything other than letters, an error will be thrown.
    while not re.match("^[A-Za-z]*$", tube_req):
        print("ERROR: Please only enter letters!")
        tube_req = input('Would you like to see your beginning and ending total for each slot? (Enter yes or no): ')

    if tube_req.lower() == "yes" and "y" and "ye":
        print("Here's a list of your beginning products")
        print('\n'.join('Slot #{0}: {1}'.format(*k) for k in enumerate(beginning_prod, 1)))
        print()
        print("Here's a list of your ending products")
        print('\n'.join('Slot #{0}: {1}'.format(*k) for k in enumerate(ending_prod, 1)))
        print()

    print()
    print("The beginning total for your safe is $", format(beginning_safe_total, ',d'))
    print()
    print("The ending total for your safe is $", format(ending_safe_total, ',d'))
    print()

    # Program will acquire information for the register section of the shift report.
    beginning_value, ending_value, beginning_ledge, ending_ledge, reg_slot_values = first_shift_reg.get_reg()

    beginning_reg_total, ending_reg_total, b_reg_subtotal, e_reg_subtotal = first_shift_reg.calc_reg()

    print("The beginning total for your register is $", format(beginning_reg_total, ',.2f'))
    print()
    print("The ending total for your register is $", format(ending_reg_total, ',.2f'))
    print()

    # Create a dictionary storing the values for beginning and end register for later use.
    beginning_reg, ending_reg = first_shift_reg.create_dict()

    # Program will acquire information from the user's safe drop log and stores the list in a variable.
    safe_drop_list = first_shift_safedroplog.get_drops()

    # Drops are calculated here and stored in a variable.
    total_drops = first_shift_safedroplog.calc_drops()

    print("The total of your drops are $", format(total_drops, ',.2f'))
    print()

    # Calculate/print beginning/ending count.
    beginning_count = beginning_safe_total + beginning_reg_total

    ending_count = ending_safe_total + ending_reg_total

    print("Your beginning count is $", format(beginning_count, ',.2f'))
    print()
    print("Your ending count is $", format(ending_count, ',.2f'))
    print()

    # Total cash is calculated/printed from the value of total drops, beginning count, and ending count.
    total_cash = (total_drops - beginning_count) + ending_count

    print("Your total cash is $", format(total_cash, ',.2f'))
    print()

    # Calls the get_reg_receipt_inf function and pass the total_cash variable as an argument.
    subtotal, total_reg_sales, credit_cards, ebt, coupons, lottery_paid_outs = get_reg_receipt_inf(total_cash)

    print("Your total money is $", format(subtotal, ',.2f'))
    print()

    # The program determines whether the user is over, short or had a perfect day.
    cash_over_short = subtotal - total_reg_sales

    if cash_over_short > 0:
        print("You are over $", format(cash_over_short, '+,.2f'))
    elif cash_over_short == 0:
        print("Nice! Your register is perfect!")
    else:
        print("You are short $", format(cash_over_short, ',.2f'))

    file_write_req = input('Would you like to store this information in a file? (Enter yes or no): ')

    # User must enter only letters, or else an error will be thrown and they will be prompted to try again.
    while not re.match("^[A-Za-z ]*$", file_write_req):
        print("ERROR: Please only enter letters!")
        file_write_req = input('Would you like to store this information in a file? (Enter yes or no): ')

    try:
        if file_write_req.lower() == "yes" and "y" and "ye":

            # Create filename constant.
            FILENAME = ("Shift Reports\\Mapco_Shift_Report_" + str(shift) + "_" + date + str(store_num) + '.txt')

            # Open a file using the filename constant.
            outfile = open(FILENAME, 'w')

            # Begin writing shift information to the file.
            outfile.write(str(misc_info))
            outfile.write('\n\n')
            outfile.write('----SAFE----')
            outfile.write('\n\n')
            outfile.write("Beginning tube QTY")
            outfile.write('\n')
            outfile.write('\n'.join('Slot #{0}: ${1}'.format(*k) for k in enumerate(beginning_qty, 1)))
            outfile.write('\n')
            outfile.write('Beginning safe total: $' + str(beginning_safe_total))
            outfile.write('\n\n')
            outfile.write("Ending tube QTY")
            outfile.write('\n')
            outfile.write('\n'.join('Slot #{0}: ${1}'.format(*k) for k in enumerate(ending_qty, 1)))
            outfile.write('\n')
            outfile.write('Ending safe total: $' + str(format(ending_safe_total, ',.2f)')))
            outfile.write('\n\n')
            outfile.write("Beginning tube totals")
            outfile.write('\n')
            outfile.write('\n'.join('Slot #{0}: ${1}'.format(*k) for k in enumerate(beginning_prod, 1)))
            outfile.write('\n\n')
            outfile.write("Ending tube totals")
            outfile.write('\n')
            outfile.write('\n'.join('Slot #{0}: ${1}'.format(*k) for k in enumerate(ending_prod, 1)))
            outfile.write('\n\n')
            outfile.write('----REGISTER----')
            outfile.write('\n\n')
            outfile.write("Beginning register")
            outfile.write('\n')
            for reg_slot_values in beginning_reg:
                outfile.write(reg_slot_values + ': $' + str(beginning_reg[reg_slot_values]))
                outfile.write('\n')
            outfile.write('\n')
            outfile.write('Beginning register subtotal: $' + str(format(b_reg_subtotal, ',.2f')))
            outfile.write('\n')
            outfile.write('Beginning safe ledge: $' + str(format(beginning_ledge, ',.2f')))
            outfile.write('\n')
            outfile.write('Beginning register total: $' + str(format(beginning_reg_total, ',.2f')))
            outfile.write('\n\n')
            outfile.write("Ending register")
            outfile.write('\n')
            for reg_slot_values in ending_reg:
                outfile.write(reg_slot_values + ': $' + str(ending_reg[reg_slot_values]))
                outfile.write('\n')
            outfile.write('\n\n')
            outfile.write('Ending register subtotal: $' + str(format(e_reg_subtotal, ',.2f')))
            outfile.write('\n')
            outfile.write('Ending safe ledge: $' + str(format(ending_ledge, ',.2f')))
            outfile.write('\n')
            outfile.write('Ending register total: $' + str(format(ending_reg_total, ',.2f')))
            outfile.write('\n\n')
            outfile.write('----SAFE DROPS----')
            outfile.write('\n\n')
            outfile.write('\n'.join('Drop #{0}: {1}'.format(*k) for k in enumerate(safe_drop_list, 1)))
            outfile.write('\n')
            outfile.write('Total drops: $' + str(format(total_drops, ',.2f')))
            outfile.write('\n')
            outfile.write('Beginning count: $' + str(format(beginning_count, ',.2f')))
            outfile.write('\n')
            outfile.write('Ending count: $' + str(format(ending_count, ',.2f')))
            outfile.write('\n\n')
            outfile.write('Total cash: $' + str(format(total_cash, ',.2f')))
            outfile.write('\n')
            outfile.write('EBT: $' + str(format(ebt, ',.2f')))
            outfile.write('\n')
            outfile.write('Credit cards: $' + str(format(credit_cards, ',.2f')))
            outfile.write('\n')
            outfile.write('Total coupons: $' + str(format(coupons, ',.2f')))
            outfile.write('\n')
            outfile.write('Total lottery paid outs: $' + str(format(lottery_paid_outs, ',.2f')))
            outfile.write('\n')
            outfile.write('Total money: $' + str(format(subtotal, ',.2f')))
            outfile.write('\n')
            outfile.write('Total sales: $' + str(format(total_reg_sales, ',.2f')))
            outfile.write('\n')
            outfile.write('Cash over/short: $' + str(format(cash_over_short, ',.2f')))

            # Close the file.
            outfile.close()
            print('Data successfully written.')

    except Exception as err:
        print(err)


def get_reg_receipt_inf(total_cash):

    # Program prompts the user for all information from the receipt provided by their register.
    while True:
        try:
            man_cards = float(input("Please enter an amount for manual cards: "))
            break
        except ValueError:
            print("ERROR: You must enter a valid number!")

    while True:
        try:
            ebt = float(input("Please enter an amount for EBT: "))
            break
        except ValueError:
            print("ERROR: You must enter a valid number!")

    while True:
        try:
            credit_cards = float(input("Please enter an amount for credit cards: "))
            break
        except ValueError:
            print("ERROR: You must enter a valid number!")

    while True:
        try:
            total_coupons = float(input("Please enter an amount for total coupons: "))
            break
        except ValueError:
            print("ERROR: You must enter a valid number!")

    while True:
        try:
            lottery_paid_outs = float(input("Please enter an amount for lottery paid outs: "))
            break
        except ValueError:
            print("ERROR: You must enter a valid number!")

    # User must input the total amount of money handled during their shift given from their cash register.
    while True:
        try:
            total_reg_sales = float(input("Please enter an amount for total register sales (from receipt): "))
            break
        except ValueError:
            print("ERROR: You must enter a valid number!")

    # The value for manual cards is added to the credit card total.
    credit_cards += man_cards

    # The subtotal is calculated.
    subtotal = total_cash + ebt + credit_cards + total_coupons + lottery_paid_outs

    return subtotal, total_reg_sales, credit_cards, ebt, total_coupons, lottery_paid_outs


# Invoke the main function
main()