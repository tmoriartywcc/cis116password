PASSWORD = 'Waubonsee'
INPUT_PROMPT = 'Please enter password: '
SUCCESS_PROMPT = 'Correct!'
FAIL_PROMPT = 'Incorrect!'

def is_password(user_pass):
    if user_pass == PASSWORD:
        return True
    else:
        return False

def main():
    user_pass = input(INPUT_PROMPT)

    while not is_password(user_pass):
        print(FAIL_PROMPT)
        user_pass = input(INPUT_PROMPT)

    print(SUCCESS_PROMPT)

main()

