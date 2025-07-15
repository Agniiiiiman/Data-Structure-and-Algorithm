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

# Insertion Sort using function

def insertion_sort(arr):
    # Traverse from 1 to len(arr)
    for i in range(1, len(arr)):
        key = arr[i]  # Current element to be inserted
        j = i - 1

        # Move elements that are greater than key one position ahead
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1

        # Place key after the element just smaller than it
        arr[j + 1] = key

# Example array
my_array = [12, 11, 13, 5, 6]

print("Original array:", my_array)

insertion_sort(my_array)

print("Sorted array:", my_array)
