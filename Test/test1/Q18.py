#  18)Write a Python script that takes a grade (0 to 100) as input and prints the corresponding letter grade based on the following scale:

# 90 and above: A
# 80 to 89: B
# 70 to 79: C
# 60 to 69: D
# Below 60: F

def grade():
    
    person=int(input('enter your grade..'))
    
    if person>90 :
        print("grade A")
    elif person>80 and person<90:
        print('grade B')
    elif person>70 and person<80:
        print('grade C')
    elif person>60 and person<70:
        print("grade D")
    else:
        print("grade F")

grade()