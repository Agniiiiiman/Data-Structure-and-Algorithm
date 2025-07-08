#The Quicksort algorithm takes an array of values, chooses one of the values as the 'pivot' element, and moves the other values so that lower values are on the left of the pivot element, and higher values are on the right of it.
"""
How it works:

Choose a value in the array to be the pivot element.
Order the rest of the array so that lower values than the pivot element are on the left, and higher values are on the right.
Swap the pivot element with the first element of the higher values so that the pivot element lands in between the lower and higher values.
Do the same operations (recursively) for the sub-arrays on the left and right side of the pivot element.
"""
def quicksort(array):
    # If the list has 0 or 1 item, it's already sorted
    if len(array) <= 1:
        return array

    pivot = array[-1]  # Pick the last number as the pivot
    smaller = []  # Numbers smaller than pivot
    bigger = []   # Numbers bigger than pivot

    # Go through every number except the pivot
    for number in array[:-1]:
        if number <= pivot:
            smaller.append(number)
        else:
            bigger.append(number)

    # Sort smaller and bigger parts, then join everything
    return quicksort(smaller) + [pivot] + quicksort(bigger)

# Try it out
my_array = [64, 34, 25, 12, 22, 11, 90, 5]
sorted_array = quicksort(my_array)
print("Sorted array:", sorted_array)

