#The Insertion Sort algorithm uses one part of the array to hold the sorted values, and the other part of the array to hold values that are not sorted yet.
""""
How it works:

Take the first value from the unsorted part of the array.
Move the value into the correct place in the sorted part of the array.
Go through the unsorted part of the array again as many times as there are values.
"""

my_array = [64, 34, 25, 12, 22, 11, 90, 5]

for i in range(1, len(my_array)):
    key = my_array[i]  # Current value to be placed
    j = i - 1
    while j >= 0 and my_array[j] > key:
        my_array[j + 1] = my_array[j]  # Shift larger elements to the right
        j -= 1
    my_array[j + 1] = key  # Insert the current value at the correct position

print("Sorted array:", my_array)
