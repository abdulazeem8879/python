# 8)Create a Python function count_vowels(s) that counts the number of vowels in a given string. Test it with the string "Hello World".


def count_vowels(s):
    counter=0
    for x in s:
        if x=="a" or x=="e" or  x=="i" or x=="o" or x=="u" :
            counter=counter+1
    return counter

vowels=count_vowels("hello world eeeieieieiieieiie")
print(vowels)