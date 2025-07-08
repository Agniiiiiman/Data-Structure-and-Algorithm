#The Selection Sort algorithm finds the lowest value in an array and moves it to the front of the array.
""""
How it works:

Go through the array to find the lowest value.
Move the lowest value to the front of the unsorted part of the array.
Go through the array again as many times as there are values in the array.

""" 
# Selection Sort Implementation
"""""
To implement the Selection Sort algorithm in a programming language, we need:

An array with values to sort.
An inner loop that goes through the array, finds the lowest value, and moves it to the front of the array. This loop must loop through one less value each time it runs.
An outer loop that controls how many times the inner loop must run. For an array with n  values, this outer loop must run 
(n-1 )times.
"""""
my_array = [64, 34, 25, 5, 22, 11, 90, 12]

n = len(my_array)
for i in range(n):
    min_index = i
    for j in range(i + 1, n):
        if my_array[j] < my_array[min_index]:
            min_index = j
    # Swap the smallest value with the current position
    my_array[i], my_array[min_index] = my_array[min_index], my_array[i]

print("Sorted array:", my_array)
