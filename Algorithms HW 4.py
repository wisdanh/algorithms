# 1. Even First

array1 = [7, 3, 5, 6, 4, 10, 3, 2]

def even_first(arr):
    j = 0
    for i in range(len(arr)):
        if arr[j]%2!=0:
            temp = arr[j]
            arr.remove(arr[j])
            arr.append(temp)
        else:
            j+=1
    return arr

print(even_first(array1))

# 2. Increment a Number

array_test = [1, 2, 9]

def increment_integer(arr):
    for i in range(len(arr)):
        if arr[i] == 1: arr[i] = 1
        elif arr[i] == 9: arr[i] = 0
        else: arr[i] += i
    return arr

print(increment_integer(array_test))


# def even_first(arr):
#     index = 1
#     for i in range(1, len(arr)):
#         if (arr[index-1] % 2 !=0) and (arr[i] % 2):
#             arr[index] = arr[i]
#             index +=1
#        # if arr[i] % 2 and arr[i-1] % 2 !=0:
#
#     return index




