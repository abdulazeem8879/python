# 6)Write a Python script to reverse a given string.




def reverse(k):
    stri=""
    for x in k:
        stri=x+stri
    return stri

val=reverse("pathan")
print(val)


# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# def reverse_string(s):
#     return s[::-1]

# # Get input from the user
# user_input = input("Enter a string to reverse: ")
# reversed_string = reverse_string(user_input)

# print("Reversed string:", reversed_string)