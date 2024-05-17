# if statement
number = 10

# check if number is greater than 0
if number > 0:
    print('Number is positive')

print('This statement always executes')

# if else statement

number = -10

if number > 0:
    print('Positive number')

else:
    print('Negative number')

print('This statement always executes')

# if elif else
number = 0

if number > 0:
    print('Positive number')

elif number < 0:
    print('Negative number')

else:
    print('Zero')

print('This statement is always executed')

# nested if statement

number = 5

# outer if statement
if number >= 0:
    # inner if statement
    if number == 0:
        print('Number is 0')

    # inner else statement
    else:
        print('Number is positive')

# outer else statement
else:
    print('Number is negative')

print('This statement is always executed')
