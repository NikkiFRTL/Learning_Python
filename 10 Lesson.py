import json


def get_stored_user():
    """
    Gets a stored user's name whether exists
    """
    filename = 'username.json'
    try:
        with open(filename) as f:
            user = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return user


def get_new_user():
    """
    Requests a user's name
    """
    user = input('What is your name??\n')
    filename = 'username.json'
    with open(filename, 'w') as f:
        json.dump(user, f)
    return user


def greet_user():
    """
    Greets a user
    """
    user = get_stored_user()
    if user:
        print(f'Welcome back, {user}!')
    else:
        user = get_new_user()
        print(f"We'll remember you when you come back, {user}")


greet_user()
