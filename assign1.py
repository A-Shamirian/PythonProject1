# Annie Shamirian
# 1026A: Assignment 1

# Prompt user to enter first and last name. Print their full name back to them capitalized.
user_first_name = input('What is your first name? ')
user_last_name = input('What is your last name? ')
print('YOUR NAME IS', str.upper(user_first_name), str.upper(user_last_name) + '.')

# Prompt user to enter three integers
user_integer1 = int(input('Enter an integer: '))
user_integer2 = int(input('Enter an integer: '))
user_integer3 = int(input('Enter an integer: '))

# Determine whether the first integer is larger than the second integer which is larger than the third integer.
# Otherwise, determine if the second integer plus the third integer is larger than the first integer
# (second and third integer are not equal to each other).
if user_integer1 > user_integer2 > user_integer3:
    print(f'{user_integer1}', 'is larger than', f'{user_integer2}' + ',', 'which is greater than', f'{user_integer3}'
          + '.')
elif user_integer2 + user_integer3 > user_integer1 and user_integer2 != user_integer3:
    print(f'{user_integer2}', '+', f'{user_integer3}', 'is greater than', f'{user_integer1}' + ',', 'and',
          f'{user_integer2}', 'is not equal to', f'{user_integer3}' + '.')

# Check if any of the integers are even and indicate which ones are (and what number they are divisible by). If no
# integers are even, none of the conditions were true.
if user_integer1 % 2 == 0 or user_integer2 % 2 == 0 or user_integer3 % 2 == 0:
    if user_integer1 % 2 == 0:
        print(f'{user_integer1}', 'is divisible by 2,', f'{int(user_integer1 / 2)}', 'time(s).')
    if user_integer2 % 2 == 0:
        print(f'{user_integer2}', 'is divisible by 2,', f'{int(user_integer2 / 2)}', 'time(s).')
    if user_integer3 % 2 == 0:
        print(f'{user_integer3}', 'is divisible by 2,', f'{int(user_integer3 / 2)}', 'time(s).')
else:
    print('None of the conditions were true.')

