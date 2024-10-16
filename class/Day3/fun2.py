a=10 #global scope veriables
b=20

# def display():
    # a=10 local scope veriables
    # its not access out of the functions
    # print(a)
    # print(b)
    
# display()
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# def add(a=2,b=3): #default value assigning
    # print(a+b)

# add(3)
# >>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<<<<<
# def mul(*a):
#     result=1
#     for x in a:
#         result=result*x
    # print(f'the result is {result}')

# mul(2,3)
# mul(1,2,3,4,5)

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# for dictionaty pass
# def person(**b): # pass dictonary as a paramater
    # print(b)

# person(name='khan',age=21,address='nanded')

# person1={"name":"khan",
#          "age":21,
#          "address":"nanded"
#          }
# person(person1)

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

def fizz_buss(x):
    if x % 3:
        print('fizz')
    elif x % 5:
        print("buzz")
    elif x % 3 and x % 5:
        print("fizz_buzz")
    else:
        print(x)
    
fizz_buss(3)

 

