year = int(input('Enter the year'))
if (year % 400 == 0) and (year % 100 == 0):
    print(f"{year} is a leap year")

# not divided by 100 means not a century year
# year divided by 4 is a leap year
elif (year % 4 ==0) and (year % 100 != 0):
    print(f"{year} is a leap year")

else:
    print(f"{year} is not a leap year")
