
def erfen(array,target):
    left, right = 0, len(array) - 1
    while left <= right:
        mid = (left + right)/2
        if array[mid] == target:
            # find target!
            return result
        elif array[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
