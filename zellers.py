print 'welcome, follow the instructions'

firstname = raw_input('\nEnter your first name: ')
lastname  = raw_input('\nEnter your last name:  ')


def input_value(input_name, prompt, min_num, max_num):   # user function definition
    while True:
        data = raw_input(prompt)
        if data:
            try:                           # checking input data format
                input_name = int(data)
            except ValueError:
                print 'Invalid input...'
            else:
                if input_name >= min_num and input_name <= max_num:
                    return input_name
                    break
                input_name = 'Please try again: '
        else:
            print 'Goodbye!'
            break

#variable declaration

month = 0
day = 0
year = 0
century = 0

month = input_value(month, "enter your month of birth(from 1-12, numbering from march as 1 to February i 12): ", 1, 12)
day = input_value(day, "Please enter the day (from 1-31): ", 1, 31)
year = input_value(year, "Please enter the year (from 0 - 99, eg. 88 in 1988): ", 0, 99)
century = input_value(century, "Please enter the century (from 0 - 99, eg. 19 in 1988): ", 0, 99)

A = month
B = day
C = year
D = century

W = (13*A - 1) / 5
X = C / 4
Y = D / 4
Z = W + X + Y + B + C - 2*D
R = Z % 7

birthday = firstname + '  ' + lastname + ' was born on ' + " " + str(B) + "/" + str(A+2) + "/" + str(D) + str(C) + " which was a "

if R == 0:
    print birthday + 'Sunday'
elif R == 1:
    print birthday + 'Monday'
elif R == 2:
    print birthday + 'Tuesday'
elif R == 3:
    print birthday + 'Wednesday'
elif R == 4:
    print birthday + 'Thursday'
elif R == 5:
    print birthday + 'Friday'
elif R == 6:
    print birthday + 'Saturday'
