# Selection Sort
def descending_selection_sort(arr):
    for i in range(len(arr)):
        max_index = i
        for j in range(i+1, len(arr)):
            if arr[j] > arr[max_index]:
                max_index = j

        arr[i], arr[max_index] = arr[max_index], arr[i]

    return arr

test_array = [3, 6, 8, 9, 2, 1]

print(test_array)
print(descending_selection_sort(test_array))

# Bubble Sort
def bubble_sort(arr):
    for 
# Insertion Sort

# Merge Sort

