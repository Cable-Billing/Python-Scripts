import argparse

parser = argparse.ArgumentParser()
parser.add_argument('Month', type=str, help='Birth month')
parser.add_argument('Day', type=int, help='Birth day')
parser.add_argument('Year', type=int, help='Birth year')
args = parser.parse_args()

# Old months and how many days each one has
oldMonths = {
    'Janurary': 31,
    'February': 28,
    'March': 31,
    'April': 30,
    'May': 31,
    'June': 30,
    'July': 31,
    'August': 31,
    'September': 30,
    'October': 31,
    'November': 30,
    'December': 31
}

# Check if the month exists
if args.Month not in oldMonths:
    print('ERROR: That month doesn\'t exist')
    print('    You might have typed the month in incorrectly')
    quit()

# Gather infomation frm command line arguments
birthMonth = list(oldMonths.keys()).index(args.Month)
birthDay = args.Day
birthYear = args.Year
leapYear = False

print('Your current birthdate is ' + args.Month + ' the ' +str(birthDay) + ', ' + str(birthYear))

# If evenly devisable by 4, check by 100
if (birthYear % 4) == 0:
    # If evenly devisable by 100, check by 400
    if (birthYear % 100) == 0:
        # If evenly divisable by 400 it is a leap year
        if (birthYear % 400) == 0:
            leapYear = True
        # If not even;y devisable by 400 it is not a leap year
        else:
            leapYear = False
    # If not evenly divisable by 100 it is a leap year
    else:
        leapYear = True
# If not evenly devisable by 4 not a leap year
else:
    leapYear = False

i = 0
dayOfTheYear = 0
# Iterate until birth month is reached
while i < (birthMonth):
    # get the number of days the month has from the dictonary
    numberOfDays = list(oldMonths.values())[i]
    # If it is a leap year add one day to February
    if numberOfDays == 28 and leapYear == True:
        numberOfDays += 1
    # Add days to the total
    dayOfTheYear += numberOfDays
    i += 1
# After adding previous month days add date onto the total
dayOfTheYear += birthDay

print('Your birth day is day \'' + str(dayOfTheYear) + '\' in the year')
print('Is your birth year a leap year: ' + str(leapYear))

# The new order and months of the Caleborian Calander
newMonths = ['March', 'April', 'May', 'June', 'Quintilis', 'Sextilis', 'September', 'October', 'November', 'December', 'Janurary', 'February', 'Calebuary']

# Calculate how many months before your new birth month
howManyMonths = int(dayOfTheYear / 28)
# Need to check otherwise wrong month is assigned
if (dayOfTheYear % 28) == 0:
    howManyMonths -= 1
# Calculate the date of the new month
dayInTheMonth = dayOfTheYear - (28 * howManyMonths)
if dayInTheMonth == 0:
    dayInTheMonth = 28
# Assign a new birth month
# To avoid overflow into 'Intermission'
if howManyMonths == 13:
    newMonth = 'Calebuary'
    dayInTheMonth = 28
else:
    newMonth = newMonths[howManyMonths]

print('Your new birthdate is ' + str(newMonth) + ' the ' + str(dayInTheMonth) + ', ' + str(birthYear))
