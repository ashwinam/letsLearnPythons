# Create an @authenticated decorator that only allows the function to run is user1 has 'valid' set to True:
user1 = {
    'name': 'Sorna',
    # changing this will either run or not run the message_friends function.
    'valid': False
}


def authenticated(fn):
    def wrapper(*args, **kwargs):
        print('***************')
        if args[0]['valid']:  # here i unpack the tuple from args, try to print args
            return fn(*args, **kwargs)
        else:
            print('Not matched,Try Again!')
        print('***************')
    return wrapper
  # code here


@authenticated
def message_friends(user):
    print('message has been sent')


message_friends(user1)
