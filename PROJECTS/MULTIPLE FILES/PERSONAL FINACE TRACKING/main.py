# Import the all needed modules 
import pandas as pd # to access different rows/columns in the file 
import csv # to use this file type to store the data 
from datetime import datetime # to use datetime objects
from data_entry import get_date, get_description, get_amount, get_category # to use the functions
import matplotlib.pyplot as plt # for the graph 

# A CLASS FOR THE DATA FILE AND WHAT IT DOES WHEN THERE'S DATA IN IT 
class CSV: 
    # CREATE A NEW CSV FILE  
    CSV_FILE = 'finance_data.csv'
        # define formnat setting for the file 
    columns = ['Date', 'Amount', 'Category', 'Description']
    format = '%d-%m-%Y'

        # class method decorator: access the class itself, but not the class's instances (~variables created from this class)
    @classmethod 
    # INITIALIZE THE CSV FILE  
    def initialize_csv(cls): 
        try: 
        # Open and read the data file 
            pd.read_csv(cls.CSV_FILE)
        # If the file exists, continue 
        except FileNotFoundError: 
        # Name the Collumns we have 
                # Data Frame: object within pandas that allow us to access different rows/collumns from a csv file
            df = pd.DataFrame(columns = cls.columns)
        # Import the Data Frame to the CSV file 
                # save a local file with the same name above in the same directory as this python file 
            df.to_csv(cls.CSV_FILE, index = False)
    
    # MAKE A DEPOSIT
    @classmethod
    def entry(cls, date, amount, category, description): 
        # Create a new formatted Dictionary 
        new_entry = {
            'Date': date,
            'Amount': amount, 
            'Category': category,
            'Description': description
        }
        # Write to the CSV file 
            # context manager: AUTO CLOSE the file for us, help DEAL with memory leaks 
        with open(cls.CSV_FILE, 'a', newline = '') as csv_file:
                # 'DictWriter': csv writer to insert the dictionary into the csv file
            writer = csv.DictWriter(csv_file, fieldnames = cls.columns) 
            writer.writerow(new_entry)
        print('Entry added successfully!')

    # GET THE DATA TO DISPLAY IN A TABLE
    @classmethod 
    def data(cls):
        df = pd.read_csv(cls.CSV_FILE)
        return df.values.tolist()

    # VIEW THE DATA IN A PERIOD
    @classmethod
    def transactions(cls, start_date, end_date):
        try: 
        # Open and Read the data file 
            df = pd.read_csv(cls.CSV_FILE)
            # To check if it runs 
            # print("Data before conversion:")
            # print(df.head())

        # Convert the 'Date' column into datetime objects 
            # Access all the values in the date column
                # to ensure they're the correct object -> to sort them 
            df['Date'] = pd.to_datetime(df['Date'], format= cls.format)
            start_date = datetime.strptime(start_date, cls.format)
            end_date = datetime.strptime(end_date, cls.format)
        except ValueError as e:
            print(f"Error during date conversion: {e}")
            return # How to know when to 'return' and 'return functions'

        '''mask: something that can be applied to the different rows inside of a dateframe to see if we should select that row or not
                reason why we can compare like below: because all the data is now 'datetime' object not strings 
           '&': bitwise end operator (kinda ~and), only used when we're using pandas dataframe or mask specifically 
                reason why we use this: to be able to apply to every single row inside of df and filter the different elements'''
        mask = (df['Date'] >= start_date) & (df['Date'] <= end_date)
        filtered_df = df.loc[mask] # loc function 

        # If there is nothing to show 
        if filtered_df.empty:
            print('No transactions found in the given date range')
        # If there is 
        else: 
            print('---------------------//------------------------')
            print(f'Transaction from {start_date.strftime(cls.format)} to {end_date.strftime(cls.format)}')
                # NOT 100% CLEAR 
                # 'date' (column name) as the key, and the function we want to apply to every element inside that column
            print(filtered_df.to_string(index = False, formatters = {'Date': lambda x: x.strftime(cls.format)})) # lambda function (1st x is the parameter, the rest is the expression)

            # # Convert DataFrame to list of lists to display 
            # data = filtered_df.values.tolist()
            # headers = cls.columns
            # # Display the table
            # display_table(data, headers)

            # Compile a Summary for easier reading 
            total_income = filtered_df[filtered_df['Category'] == 'Income']['Amount'].sum()
            total_expense = filtered_df[filtered_df['Category'] == 'Expense']['Amount'].sum()
            print('\nSummary')
            print(f'Total Income: ${total_income:.2f}')
            print(f'Total Expense: ${total_expense:.2f}')
            print(f'Net Savings: ${(total_income - total_expense):.2f}')
            print('---------------------//------------------------')
        
        # What does this do???
        return filtered_df 


# A FUNCTION TO MAKE A DEPOSIT
def add():
    CSV.initialize_csv() 
    date = get_date("Enter the date of the transaction (dd-mm-yyyy) or enter for today's date: ", allow_default = True) 
    amount = get_amount() 
    category = get_category()
    description = get_description()
    CSV.entry(date, amount, category, description)
# CSV.transactions('01-01-2024', '30-07-2025')


# A FUNCTION TO DISPLAY THE DATA INTO A TABLE 
def display_table(data, headers):
    col_widths = [max(len(str(item)) for item in col) for col in zip(*data, headers)]
    format_string = " | ".join(f"{{:<{width}}}" for width in col_widths)
    print(format_string.format(*headers))
    print("-" * (sum(col_widths) + 3 * (len(headers) - 1)))
    for row in data:
        print(format_string.format(*row))


# CONVERT FROM A TEXT-BASED DATA DISPLAY TO A GRAPHICAL DATA DISPLAY 
def plot_transactions(df):
    # Ensure the date is in the correct format
    df['Date'] = pd.to_datetime(df['Date'], format = '%d-%m-%Y')
    df.set_index('Date', inplace = True)

    # NOT 100% CLEAR
    # Create 2 seperate dataframes: income and expense
        #'D': daily frequence 
        #'.resample': to create rows for every single day -> fill out the 'missing' day ; aggregate different values on the same day 
    income_df = df[df['Category'] == 'Income'].resample('D').sum().reindex(df.index, fill_value = 0)
    expense_df = df[df['Category'] == 'Expense'].resample('D').sum().reindex(df.index, fill_value = 0)

    # All the needed commands to show the graph 
    plt.figure(figsize = (10, 5))
    plt.plot(income_df.index, income_df['Amount'], label = 'Income', c = 'g')
    plt.plot(expense_df.index, expense_df['Amount'], label = 'Expense', c = 'r')
    plt.title('Income and Expense over Time', fontdict = {'family': 'serif', 'color': 'blue', 'size': 25, 'weight':'bold'})
    plt.xlabel('Date', fontdict = {'family': 'serif', 'color': 'blue', 'size': 15, 'weight':'bold'})
    plt.ylabel('Amount ($)', fontdict = {'family': 'serif', 'color': 'blue', 'size': 15, 'weight':'bold'})
    plt.legend()
    # plt.grid(True) 
    plt.grid(which = 'major', ls = '-', c = 'black', lw = '1.0')
    # plt.minorticks_on()
    # plt.grid(which = 'minor', ls = '-', c = 'grey', lw = '1.0')
    plt.show()


# THE 'MAIN' CODE FOR ALL THE FUNCTIONS 
def main():
    while True: 
        print('Welcome to your personal finance tracker!')
        print('1. Add a new transaction')
        print('2. View existing transactions and summary within a date range')
        print('3. Exit')
        choice = input ('Please enter your choice: ')

        if choice == '1':
            print('---------------------------------')
            add() 
            print('---------------------------------')
        elif choice == '2': 
            print('---------------------------------')
            start_date = get_date('Enter the start date (dd-mm-yyyy): ')
            end_date = get_date('Enter the end date (dd-mm-yyyy): ')
            try: 
                datetime.strptime(start_date, CSV.format)
                datetime.strptime(end_date, CSV.format)
                df = CSV.transactions(start_date, end_date)
                if input('Do you want to view them as a graph?(y/n) ').lower() == 'y':
                    plot_transactions(df)
            except ValueError:
                print('Invalid date format. Please enter again in dd-mm-yyy format.')
            print('---------------------------------')
        elif choice == '3': 
            print('Exciting...')
            print('---------------------------------')
            break 
        else: 
            print('Invalid choice. Choose again.')
            print('---------------------------------')

# To protect this file, it only runs when we execute this file 
if __name__ == '__main__':
    main() 

