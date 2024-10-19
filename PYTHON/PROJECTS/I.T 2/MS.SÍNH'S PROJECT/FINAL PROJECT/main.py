from books_management import add_book, display_book, search_book, update_book, delete_book
from users_management import add_user, display_user, search_user, update_user, delete_user

def book_menu(): 
    while True: 
        # Options 
        print('Books Management Menu:')
        print('1. Add a new book')
        print('2. Display all the books')
        print('3. Search for a book')
        print("4. Update book's information")
        print('5. Delete a book')
        print('6. Back to the main menu')

        # Choice
        ask1 = input('Please enter your choice: ')

        # Add a book 
        if ask1 == '1':
            print('Please enter the book detail(s): ')
            try: 
                book_info = {
                    'ID': input('Book ID: '),
                    'Name':  input('Book name: '),
                    'Author':  input('The Author: '),
                    'Year': input('Published year: '),
                    'Quantity': int(input('Quantity: '))
                }
                add_book(book_info)
                print('Book added successfully!')
            except ValueError:
                print('Invalid input. Please enter a number for Quantity.')
            print('--------------------------------------')

        # Display the books
        elif ask1 == '2':
            display_book()
            print('--------------------------------------')

        # Search by ID or Author 
        elif ask1 == '3':
            element1 = input('Enter Book ID, or the Author to search: ')
            searching1 = search_book(element1)
            if searching1:
                print('Search results: ')
                for res in searching1:
                    print(f"ID: {res['ID']} | Name: {res['Name']} | Author: {res['Author']} | Published Year: {res['Year']} | Quantity: {res['Quantity']}")
            else: 
                print('No book found fitting your description!')
            print('--------------------------------------')

        # Update a book's info 
        elif ask1 == '4':
            book_id = input('Enter the book ID to update: ')
            new_info = {}
            while True:
                field = input("Enter the field to update (ID, Name, Author, Year, Quantity) or 'done' to finish: ")
                if field.lower() == 'done':
                    break
                value = input(f"Enter the new value for {field}: ")
                new_info[field] = value
            update_book(book_id, new_info)
            print('Update successfully!')
            print('--------------------------------------')

        # Delete a book 
        elif ask1 == '5':
            book_ID = input('Enter the book ID to delete: ')
            delete_book(book_ID)
            print('Book deleted successfully!')
            print('--------------------------------------')

        # Back to the main menu 
        elif ask1 == '6':
            print('--------------------------------------')
            break

        # Invalid input 
        else: 
            print('Invalid choice. Choose again.')
            print('--------------------------------------')

def user_menu():
    while True:
        # Options
        print('Users Management Menu:')
        print('1. Add a user')
        print('2. Display all the users')
        print('3. Search for a user')
        print("4. Update user's information")
        print('5. Delete a user')
        print('6. Back to the main menu')

        # Choice 
        ask2 = input('Please enter your choice: ')

        # Add a user 
        if ask2 == '1':
            print("Enter user's information: ")
            try:
                user_info = {
                    'Name': input('Name: '),
                    'Email': input('Email: '),
                    'Phone': int(input('Phone: '))
                }
                add_user(user_info)
                print("User's information added successfully!")
            except ValueError:
                print('Invalid input. Please enter a number for Phone.')
            print('--------------------------------------')

        # Display all the users 
        elif ask2 == '2':
            display_user()
            print('--------------------------------------')

        # Search a user 
        elif ask2 == '3':
            element2 = input("Enter user's name or email to search: ")
            searching2 = search_user(element2)
            if searching2: 
                print('Search results:')
                for res in searching2: 
                    print(f"Name: {res['Name']} | Email: {res['Email']} | Phone: {res['Phone']}")
            else: 
                print('No users found fitting your description!')
            print('--------------------------------------')

        # Update user's info
        elif ask2 == '4':
            email = input('Enter the email of the user to update: ')
            new_info = []
            while True:
                field = input("Enter the field to update (Name, Email, Phone) or 'done' to finish: ")
                if field.lower() == 'done':
                    break
                value = input(f"Enter the new value for {field}: ")
                new_info[field] = value
            update_user(email, new_info)
            print('Update successfully!')
            print('--------------------------------------')
        
        # Delete a user
        elif ask2 == '5':
            email = input("Enter the email of the user to delete: ")
            delete_user(email)
            print('User deleted successfully!')
            print('--------------------------------------')

        # Back to the main menu 
        elif ask2 == '6': 
            print('--------------------------------------')
            break

        # Invalid input 
        else: 
            print('Invalid choice. Choose again.')
            print('--------------------------------------')

def main_menu():
    while True: 
        try: 
            print("Welcome to Hoang's Library Management System!")
            print("1. Manage Books")
            print("2. Manage Users")
            print("3. Exit")
            choice = input("Please enter your choice: ")
            print('--------------------------------------')

            if choice == '1':
                book_menu()
                print('--------------------------------------')
            elif choice == '2':
                user_menu()
                print('--------------------------------------')
            elif choice == '3':
                print("Thank you for using the library management system. Goodbye!")
                break
            else:
                print("Invalid choice. Please enter a valid option.")
                print('--------------------------------------')
        except Exception as e:
            print(f"An error occurred: {e}")
            print('--------------------------------------')

if __name__ == "__main__":
    main_menu()
