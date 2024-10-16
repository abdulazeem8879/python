# 10)Create a Python function multiply_elements(lst) that multiplies all elements of a list together. Test it with the list [2, 3, 4].

def multiply_elements(lst):
    counter=0
    for x in lst:
        counter=x*x
        print(counter)
    
    
li=[2,3,4]
multiply_elements(li)