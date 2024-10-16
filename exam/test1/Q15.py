# 15) Write a Python function sum_of_digits(n) that calculates the sum of digits of an integer. Test it with the number 123.

def sum_of_digits(*n):
    
    total=0
    for sum in n:
        total+=sum
    return total

values=sum_of_digits(1,2,3,4)
print(values)
