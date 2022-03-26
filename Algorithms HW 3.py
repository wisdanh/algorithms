#Below the Arithmetical Mean

list1 = [1,3,5,6,4,10,2,3]

def mean_find(list):
    sum = 0
    for i in list:
        sum += i
        mean = sum / len(list)
    return mean

#print(mean_find(list1))

def list_return(list):
    list2 = []
    for i in list:
        if (i < mean_find(list)): #and (i not in list2):
            list2.append(i)
    return list2

#rint(list_return(list1))

# Two Lowest Elements

list3 = [198,3,4,9,10,9,2]

def find_min(list):
    min1 = min(list)
    list.remove(min1)
    min2 = min(list)

    return min1, min2

print(find_min(list3))



