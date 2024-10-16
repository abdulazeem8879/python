# 19)Write a Python script that checks if a given year is a leap year. Use the following conditions:

# A year is a leap year if it is divisible by 4.

def check_year (a):
    if a%4 == 0:
        print(f"{a} Is a leap Year")
    elif a%100 == 0 and a%400 == 0:
        print(f"{a} Is leap Year")  
    else :
        print(f"{a} Is Not leap Year")       

check_year(2028)