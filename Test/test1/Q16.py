# 16) Write a Python function sum_of_arguments(n) that calculates the sum of arguments. Test it with the number 10,20,30,40

def sum_of_arguments(*n):
    
    total=0
    for sum in n:
        total+=sum
    return total

values=sum_of_arguments(10,20,30,40)
print(values)

    
    