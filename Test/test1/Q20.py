#  4. Write a Python script that takes three numbers as input and prints the largest of the three numbers.

# num =int(input('enter number ...'))

def number_counter(num1,num2,num3):
    
    if num1>num2 and num1>num3:
        print(f" {num1} is greater the num2 and num3")
    elif num2>num1 and num2>num3:
        print(f"{num2} is greater the num1 and num3")
    else:
        print(f"{num3} is greater the num1 and num2")

number_counter(100,20,80)


