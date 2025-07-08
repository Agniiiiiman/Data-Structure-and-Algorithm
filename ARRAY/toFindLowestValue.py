#Algorithm: Find The Lowest Value in an Array
"""""
How it works:

Go through the values in the array one by one.
Check if the current value is the lowest so far, and if it is, store it.
After looking at all the values, the stored value will be the lowest of all values in the array.

"""


my_array = [7, 12, 9, 4, 11]
minVal = my_array[0]

for i in my_array:
    if i < minVal:
        minVal = i

print('Lowest value:',minVal)
