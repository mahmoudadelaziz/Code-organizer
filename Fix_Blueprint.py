"""
This code should serve as a blueprint to do the following for each "batch"*:
---> "Create" the objects corresponding to the datapoints.
---> "Send" the datapoints.

* The number of elements in each batch is still to be determined.
"""

# Placeholder dictionary
myDict = {}

# The ranges to loop through (batch sizes)
ranges = [2, 4, 9]


# The inner loop works 2 times, and then 4 times, and then 9 times
# These ranges could be replaced with a single value or any suitable set of values
for x in ranges:
    for y in range(x):
        # Start filling out the dictionary
        myDict[f"type_{x}_Ex_{y}"] = f"Val_{y+2}" # Arbitrary values, just an example
        # ...

print(myDict.keys())

print(myDict)