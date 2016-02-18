from not_something.txt import DBReader

db_reader = DBReader()
# user_data = []
def password_match():
    pass
while True:
    username_to_search = input("Please enter your USERNAME: ")
    password_to_search = input("What is your password? ")
    try:
        user_data = db_reader.get
    if user_input in username:
        print("Username verified. \nWelcome {}! \nGood to see you  \n".format(user_input))
        unknown_user = False
    else:
        print("Not valid username.  Try again")
username = user_input
while unknown_password:
    user_password_input = input("Please enter your password on file: ")
    if user_password_input in password:
        print("Password verified.\n")
        unknown_password = False
    else:
        print("Not a valid password.  \n Try again")
password = user_password_input

user_data = [line for line in database_list if line[0].lower() == username.lower()]
for items in user_data:
    for item in items:
        if item == username:
            continue
        elif item == password:
            continue
        else:
            print("User specific info: {}".format(item))

while unknown_new_user:
    add_new_user = input("Do you  to add new user? y/n ")
    if add_new_user.lower() == 'y':
        with open("database", "a") as outfile:
            new_user_name = input("Enter new username: ")
            if new_user_name not in username:
                outfile.write("\n" + (new_user_name).lower())
                outfile.write("," + input("Enter password: ").lower())
                outfile.write("," + input("Enter user's name: ").lower())
                outfile.write("," + input("Enter user's favorite color: ").lower())
                outfile.write("," + input("Enter user's favorite animal: ").lower())
                print("Awesome, you added a new user!")
                continue
            else:
                print("Sorry, that user already exists.")
    else:
        unknown_new_user = False

logout = input("Log out? y/n ")
if logout.lower() == 'y':
    print("You logged out!")
else:
    print("Sorry' you're logged out. ")