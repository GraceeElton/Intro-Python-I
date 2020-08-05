"""
Dictionaries are Python's implementation of associative arrays.
There's not much different with Python's version compared to what
you'll find in other languages (though you can also initialize and
populate dictionaries using comprehensions just like you can with
lists!).

The docs can be found here:
https://docs.python.org/3/tutorial/datastructures.html#dictionaries

For this exercise, you have a list of dictionaries. Each dictionary
has the following keys:
 - lat: a signed integer representing a latitude value
 - lon: a signed integer representing a longitude value
 - name: a name string for this location
"""

waypoints = [
    {
        "lat": 43,
        "lon": -121,
        "name": "a place"
    },
    {
        "lat": 41,
        "lon": -123,
        "name": "another place"
    },
    {
        "lat": 43,
        "lon": -122,
        "name": "a third place"
    }
]

# Add a new waypoint to the list
waypoints.append({"happy": "no"})
print(waypoints)
# YOUR CODE HERE

# Modify the dictionary with name "a place" such that its longitude
# value is -130 and change its name to "not a real place"
# Note: It's okay to access the dictionary using bracket notation on the
# waypoints list.

# YOUR CODE HERE

waypoints[0]["lon"] = -130
waypoints[0]["name"] = "not a real place"


# Write a loop that prints out all the field values for all the waypoints
# idk how to just get the values when the dict is in a list.
"""When looping through a sequence, the position index and corresponding 
value can be retrieved at the same time using the enumerate() function.
but how does this work when the dic is in a list????"""


for key, val in enumerate(waypoints):
    print(f"Key is {key} and value is {val}")

# YOUR CODE HERE