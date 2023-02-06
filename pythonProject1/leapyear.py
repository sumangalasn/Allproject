year=int(input("enter the year: "))
if year % 400==0:
    print("its is a leap year")
elif year %4==0:
    print("it is a leap year")
elif year % 100==0:
    print("it is a leap year")
else:
    print("it is not a leap year")
