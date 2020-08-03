# For the exercise, look up the methods and functions that are available for use
# with Python lists.

x = [1, 2, 3]
y = [8, 9, 10]

# For the following, DO NOT USE AN ASSIGNMENT (=).

# Change x so that it is [1, 2, 3, 4]
# YOUR CODE HERE

# append adds the object to the end of the list! 
# WOKRING
x.append(4)
print(x)

# Using y, change x so that it is [1, 2, 3, 4, 8, 9, 10]
# YOUR CODE HERE

#The EXTEND method adds the contents of one list to the end of another list.
x.extend(y)
print(x)

# Change x so that it is [1, 2, 3, 4, 9, 10]
# YOUR CODE HERE
#DEL() method deletes an element from the list at the index we pass in.
del x[4]
print(x)

# Change x so that it is [1, 2, 3, 4, 9, 99, 10]
# YOUR CODE HERE
#This method inserts an element at a specified position.

x.insert(5, 99)
print(x)

# Print the length of list x
# YOUR CODE HERE
# This method calculates the total length of a list that we pass in as an argument.
print(len(x))


"working on later" 
# Print all the values in x multiplied by 1000
# YOUR CODE HERE