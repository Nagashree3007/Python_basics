'''
@Author: Nagashree C R
@Date: 2024-07-11
@Last Modified by: Nagashree C R
@Last Modified: 2024-07-11
@Title : find the given year is leap year or not.
'''

def is_leap_year(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

year =input()
if len(year)==4:
  year=int(year)
  is_leap_year(year)
  if is_leap_year(year):
    print(f"{year} is a leap year.")
  else:
    print(f"{year} is not a leap year.")
else:
  print("invalid input....enter only four digit number")
