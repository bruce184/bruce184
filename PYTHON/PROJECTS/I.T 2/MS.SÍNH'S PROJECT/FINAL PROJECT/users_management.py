from data_management import load, save

users_file = 'users.csv'

# ADD FUNCTION 
def add_user(user_info):
    users = load(users_file)
    try:
        user_info['Phone'] = int(user_info['Phone'])
    except ValueError:
        print('Invalid input. Please enter a number for Phone.')
        return

    users.append(user_info)
    fieldnames = ['Name', 'Email', 'Phone']
    save(users_file, users, fieldnames)


# DISPLAY FUNCTION 
def display_user():
    users = load(users_file)
    if not users:
        print('No users found.')
        return

    print('All users: ')
    for user in users:
        print(f"Name: {user['Name']} | Email: {user['Email']} | Phone: {user['Phone']}")


# SEARCH FUNCTION 
def search_user(ele):
    users = load(users_file)
    res = [user for user in users if ele.lower() in user['Name'].lower() or ele.lower() in user['Email'].lower()]
    return res


# UPDATE FUNCTION 
def update_user(email, new_info):
    users = load(users_file)
    for user in users:
        if user['Email'] == email:
            for key, value in new_info.items():
                if key == 'Phone':
                    try:
                        value = int(value)
                    except ValueError:
                        print('Invalid input. Please enter a number for Phone.')
                        return
                user[key] = value
            break
    fieldnames = ['Name', 'Email', 'Phone']
    save(users_file, users, fieldnames)


# DELETE FUNCTION 
def delete_user(email):
    users = load(users_file)
    users = [user for user in users if user['Email'] != email]
    fieldnames = ['Name', 'Email', 'Phone']
    save(users_file, users, fieldnames)
