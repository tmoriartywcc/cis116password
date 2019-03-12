PASSWORD = 'Waubonsee'

def check_password(user_pass):
    if user_pass == PASSWORD:
        print('Correct!')
    else:
        print('Incorrect!')

def main():
    user_pass = input('Please enter password: ')
    check_password(user_pass)

main()