


def merge(array, left, mid, right):
    temp = []
    i, j = left, mid+1
    while i <= mid and j <= right:
        if array[i] <= array[j]:
            temp.append(array[i])
            i += 1
        else:
            temp.append(array[j])
            j += 1

    while i <= mid:
        temp.append(array[i])
        i += 1

    while j <= right:
        temp.append(array[j])
        j += 1

    array[left:right+1] = temp

def mergesort(array, left, right):
    if right <= left:
        return
    mid = (left + right) >> 1
    mergesort(array, left, mid)
    mergesort(array, mid+1, right)
    merge(array, left, mid, right)


s = [1,3,2,3,1]
mergesort(s, 0, len(s)-1)
print(s)