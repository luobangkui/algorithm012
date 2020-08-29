

def partition(array, begin, end):
    counter, pivot = begin, end
    for i in range(begin, end):
        if array[i] < array[pivot]:
            array[i], array[counter] = array[counter], array[i]
            counter += 1
    array[counter], array[pivot] = array[pivot], array[counter]
    return counter

def quicksort(array, begin, end):
    if end <= begin:
        return
    pivot = partition(array, begin, end)
    quicksort(array, begin, pivot - 1)
    quicksort(array, pivot + 1, end)


s = [1,2,6,3,8,0,7]
quicksort(s,0,len(s)-1)
print(s)

