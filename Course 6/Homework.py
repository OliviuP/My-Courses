# 3.
# a) Print out a table with header row containing name, age and salary where each is accordingly extended to 15, 5 and 12 characters.
# b)	Print out a line to separate header from data columns that has precisely the table’s length.
# c)	Print out 3 data rows in that table where all columns are even with header columns and salary has two digits after comma.
# | Name            | Age   | Salary       |
# ------------------------------------------
# | John Doe        |    27 |    123456.00 |
# | John Wick       |    40 |     50000.00 |
# | Jeff Bezos      |    45 | 999999999.95 |

header_1 = "Name"
header_2 = "Age"
header_3 = "Salary"

name_1 = "John Doe"
name_2 = "John Wick"
name_3 = "Jeff Bezos"

age_1 = 27
age_2 = 40
age_3 = 45

salary_1 = 123456.00
salary_2 = 50000.00
salary_3 = 999999999.954

print(f"| {header_1:15} | {header_2:5} | {header_3:12} |")
print("-" * 42)
print(f"| {name_1:15} | {age_1:5} | {salary_1:12.2f} |")
print(f"| {name_3:15} | {age_2:5} | {salary_2:12.2f} |")
print(f"| {name_3:15} | {age_3:5} | {salary_3:12.2f} |")

# 4. Write a program that operates on a provided string (read from the keyboard), that always has length of at least 10 characters.
# a. If the string length is even, retrieve a substring that is exactly 4 characters long and is exactly in the middle of the original string.
# b. If the string length is odd, retrieve a substring that is exactly 5 characters long and is exactly in the middle of the original string.
# Tips: Make use of the len() and int() as well as the % and [] operators. Example of the int()
# function.
# A = int(3/2) # rounds down 1.5 to 1 and assigns it to a

# string = str(input("The string is: "))
# string_lenght = len(string)
#
# if string_lenght < 10:
#     print("The string has to be at least 10 characters")
# elif string_lenght % 2 == 0:
#     print(string[string_lenght // 2 - 2:string_lenght // 2 + 2])
# elif string_lenght % 2 != 0:
#     print(string[string_lenght // 2 - 2:string_lenght // 2 + 3])

# A=int(string_lenght)
# print(string_lenght)
# if (A%2) == 0:
#     print(string[4:7])
# else:
#     print(string[4:9])


# 5. Write an application that prints a dictionary containing 3 country - capital pairs:
# a.	 Use input function to query user for a country and its capital three times for each pair (6 inputs total).
# b.	 Print out the resulting dictionary.

# Varianta 1

# country_capital = {}
#
# country = input("Enter country:")
# capital = input("Enter capital:")
# country1 = input("Enter country:")
# capital1 = input("Enter capital:")
# country2 = input("Enter country:")
# capital2 = input("Enter capital:")
#
# country_capital[country] = capital
# country_capital[country1] = capital1
# country_capital[country2] = capital2
# print(country_capital)


# Varianta 2

# n=3
# dict = {}
#
# for i in range(n):
#     country = input("Country pls:")
#     capital = input("Capital Pls:")
#     dict[country] = capital
#
# print(dict)


# 6.	Write the same application from previous point, this time using input() only 3 times.
# a.	User should input country and its capital in one input, separated by a comma
# “Japan,Tokyo”.
# b.	Use string split(", ") function to split the string into a list of 2 substrings - the country
# and the city. The split(", ") function splits a string by a programmer defined delimiter
# into a list of substrings, for example: 'Japan, Tockyo' -> ['Japan', 'Tockyo']
# c.	Print out the resulting dictionary.

# dict1 = {}
#
# country_capital = input("Enter a country and its capital: ").split(",")
#
# country_capital1 = input("Enter a country and its capital:").split(",")
#
# country_capital2 = input("Enter a country and its capital:").split(",")
#
# # dict1 = [country_capital, country_capital1, country_capital2]
#
# dict1[country_capital[0]] = country_capital[1]
# dict1[country_capital1[0]] = country_capital1[1]
# dict1[country_capital2[0]] = country_capital2[1]
#
# print(dict1)

dict1 = {}

country, capital = input("Enter a country and its capital: ").split(",")

country1, capital1 = input("Enter a country and its capital:").split(",")

country2, capital2 = input("Enter a country and its capital:").split(",")

dict1[country] = capital
dict1[country1] = capital1
dict1[country2] = capital2

print(dict1)

# dict2 = {}
# n = 3
#
# for i in range(n):
#     country, capital = input("Enter a country and its capital:") .split()
#     dict2[country] = capital
#
# print(dict2)


# 7.	Write an application that:
# a.	Asks user for a number from 1 to 7.
# b.	If the number provided by user is smaller than 1, prints out “There are no negative number days!”.
# c.	For input number 1, prints out “You chose Monday”.
# d.	If the number provided by user is greater than 7, prints out “There are only 7 days in a week!”.

# number = int(input("Give me a number from 1 to 7: "))
#
# if number < 1:
#     print("There are no negative number days!")
# elif number == 1:
#     print("You chose Monday")
# elif number > 7:
#     print("There are only 7 days in a week")


# varianta 2

n = int(input("Give ma a number from 1 to 7:"))

week = {1: 'Monday',
        2: 'Tuesday',
        3: 'Wednesday',
        4: 'Thursday',
        5: 'Friday',
        6: 'Saturday',
        7: 'Sunday'
        }

if n < 1:
    print("There are no negative number days!")
elif n > 7:
    print("There are only 7 days in a week")
else:
    print(f' You chose {week[n]}')