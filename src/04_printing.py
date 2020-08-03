"""
Python provides a number of ways to perform printing. Research
how to print using the printf operator, the `format` string 
method, and by using f-strings.
"""
x = 10
y = 2.24552
z = "I like turtles!"

# Using the printf operator (%), print the following feeding in the values of x,
# y, and z:
# x is 10, y is 2.25, z is "I like turtles!"

## 1.2 the 2 means how many deicmal point you want 
# put the varible at the end in order how you want this to read.
print('x is %d, y is %1.2f, z is "%s"' % (x, y, z))

# Use the 'format' string method to print the same thing
#helpful link https://www.youtube.com/watch?v=F3sxzkr715c
print(f"x is {x}, y is {y}, z is '{z}'".format(x=x, y=round(y, 2),z=z))


# Finally, print the same thing using an f-string
#example -     print(f"Hello {name}")
# how to i round? ANSWER = https://www.knowledgehut.com/blog/programming/python-rounding-numbers#:~:text=The%20function%20round()%20accepts,off%20a%20number%2C%20say%204.5.
# round(number, number of digits)
print(f"x is {x}, y is {round(y , 2)}, z is '{z}'")
