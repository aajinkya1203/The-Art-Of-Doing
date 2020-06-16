import re
print("Welcome to the Database Admin Program!")

# a dictionary to keep track of all accounts including the admin account!
accounts = {
    "admin00": "admin1234",
    "aajinkya1203": "helloWorld",
    "david": "seatGeek",
    "jeff": "myNameJeff@123",
    "thomas": "fookingUp0909"
}

# taking username and password input from the user
user_name = input("Enter your Username: ").lower()

# accepting password if username is right
if user_name in accounts.keys():
    pass_word = input("Enter your password: ")
    # passoword auth
    if pass_word != accounts[user_name]:
        print("Incorrect Password!")
    else:
        # checking admin conditions and showing all accounts if user is admin logged in
        if user_name == 'admin00':
            for key, value in accounts.items():
                print("Username:",key,"\t\tPassword:",value)
        else:
            choice = input("Would you like to change the password (yes/no): ")
            if choice.startswith('n'):
                pass
            else:
                print("\nYour new password must be of alteast 8 digits!")
                new_pass = input("Enter your New Password: ")
                pattern = "[a-zA-Z0-9_@]{8}"
                passed = re.match(pattern, new_pass)
                if passed:
                    accounts[user_name] = new_pass
                    print("Password Changed!")
                else:
                    print("Passwod doesn't match the requirement!\nIt should have atleast 8 digits!")
else:
    print("\nOopsie!\nUsername not in database, goodbye.")