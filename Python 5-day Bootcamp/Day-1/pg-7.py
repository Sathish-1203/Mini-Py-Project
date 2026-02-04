# Leap year
# A year is a leap year if it is divisible by 4.
# However, if it is divisible by 100, it is not a leap year, unless..
# It is also divisible by 400.

year = int(input("Year:"))
if (year % 4 ==0 and year % 100 != 0) or (year % 400 == 0):
    print(year, "It is Leap year")
else:
    print(year, "It is not a Leap year")
