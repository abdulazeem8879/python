# 22) find the unicode values of A,Z,l,m,n,@,#


# Characters to find Unicode values for
characters = ['A', 'Z', 'l', 'm', 'n', '@', '#']

# Getting Unicode values
unicode_values = {char: ord(char) for char in characters}

# Printing the results
for char, value in unicode_values.items():
    print(f"Unicode value of '{char}': {value}")
