# Import libraries numpy, pandas, date
import numpy as np
import pandas as pd
from datetime import date

# creating empty lists to initialize no value at beginning
GOODS_OR_SERVICES = []
PRICES = []
DATES = []
EXPENSE_TYPES = []

# create a function to add expenses to empty list and arrange the data
def add_expense(good_or_service, price, date, expense_type):
    GOODS_OR_SERVICES.append(good_or_service)
    PRICES.append(price)
    DATES.append(date)
    EXPENSE_TYPES.append(expense_type)
    
# Main program

option = -1 # this will option for users to give input
while(option != 0):
    #create the option menu
    print('Welcome to the simple expense tracker: ')
    print('1. Add Food Expense')
    print('2. Add Household Expense')
    print('3. Add Transportation Expense')
    print('4. Show and Save the Expense Report')
    print('0. Exit')
    
    option = int(input("Choose an option: "))
    
    #print a new line
    print()
    
    #check for the users choice or option or input
    if option == 0:
        print('Exiting the program')
        break
    elif option == 1:
        print('Adding Food')
        expense_types = 'FOOD'
    elif option == 2:
        print('Adding Household')
        expense_types = 'HOUSEHOLD'
    elif option == 3:
        print('Adding Transportation')
        expense_types = 'TRANSPORTATION'
    elif option == 4:
        #create a data frame and add the expenses
        expense_report = pd.DataFrame()
        expense_report['GOODS_OR_SERVICES'] = GOODS_OR_SERVICES
        expense_report['PRICES'] = PRICES
        expense_report['DATES'] = DATES
        expense_report['EXPENSE_TYPES'] = EXPENSE_TYPES
        #save expense report
        expense_report.to_csv('expenses.csv')
        #show the expense report
        print(expense_report)
    else:
        print('Invalid option, Please choose 0, 1, 2, 3 or 4')
        
    # allow user to enter the good or service and the price
    if option == 1 or option == 2 or option == 3:
        good_or_service = input('Enter the good or service for the expense type '+ expense_types+'\n')
        price =  float(input('Enter the price of the good or service:\n'))
        today = date.today()
        add_expense(good_or_service, price, today, expense_types)
    # print a new line
    print()
