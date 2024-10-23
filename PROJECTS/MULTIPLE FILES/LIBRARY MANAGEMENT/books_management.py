from data_management import load, save

books_files = 'books.csv'

# ADD FUNCTION 
def add_book(book_info):
    books = load(books_files)
    try:
        book_info['Quantity'] = int(book_info['Quantity'])
    except ValueError:
        print('Invalid input. Please enter a number for Quantity.')
        return 
    
    books.append(book_info)
    fieldnames = ['ID', 'Name', 'Author', 'Year', 'Quantity']
    save(books_files, books, fieldnames)


# DISPLAY FUNCTION 
def display_book():
    books = load(books_files)
    if not books: 
        print('No books found.')
        return

    print('All books: ')
    for book in books: 
        print(f"ID: {book['ID']} | Name: {book['Name']} | Author: {book['Author']} | Published Year: {book['Year']} | Quantity: {book['Quantity']}")


# SEARCH FUNCTION 
def search_book(ele):
    books = load(books_files)
    res = [book for book in books if ele.lower() in book['ID'].lower() or ele.lower() in book['Author'].lower()]
    return res


# UPDATE FUNCTION 
def update_book(book_id, new_info):
    books = load(books_files)
    for book in books:
        if book['ID'] == book_id:
            for key, value in new_info.items():
                if key == 'Quantity':
                    try:
                        value = int(value)
                    except ValueError:
                        print('Invalid input. Please enter a number for Quantity.')
                        return
                book[key] = value
            break
    fieldnames = ['ID', 'Name', 'Author', 'Year', 'Quantity']
    save(books_files, books, fieldnames)


# DELETE FUNCTION 
def delete_book(book_id):
    books = load(books_files)
    books = [book for book in books if book['ID'] != book_id]
    fieldnames = ['ID', 'Name', 'Author', 'Year', 'Quantity']
    save(books_files, books, fieldnames)
