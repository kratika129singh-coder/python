def isLeapYear(year):
    if( year % 400 == 0 or ( year % 4 == 0 and year % 100 != 0)):
        return True
    else:
        return False

year=[1900,2000,2024,2030,2025,2005]
for y in year:
    if isLeapYear(y):
        print(f"{y} : Leap Year")
    else:
        print(f"{y} : Not Leap Year")