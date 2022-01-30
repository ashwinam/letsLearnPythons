# password checker it takes the password but printing out the password in a * format

# username = input('Enter the username: ')
# password = input('Enter the password: ')

# print(f'Hey {username}, your password is { "*" * len(password)} and it {len(password)} character long.')

# lets write in a cleaner way

print('What is your username?')
username = input()
print('What is your password?')
password = input()

password_length = len(password)
print(password_length)
hidden_password = "*" * password_length

print(f'{username}, your password is {hidden_password} and it {password_length} letters long.')

