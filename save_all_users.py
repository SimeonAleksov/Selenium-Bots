def save_users():
    new_user = open('users.txt', 'r').read()

    with open('all_users.txt', 'a') as file:
        file.write(new_user + '\n')
        file.close()
    print("Saving user . . .")
