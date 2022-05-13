def partition(arr, p, r, k):
    i = p+1
    j = r
    x = k

    while True:
        while arr[i] < x and i < r:
            i += 1
        while arr[j] >= x and j > p:
            j -= 1
        if i >= j:
            break
        arr[i], arr[j] = arr[j], arr[i]

    pos = arr.index(x)
    arr[pos] = arr[j]
    arr[j] = x

    return j


def select(arr, p, r, k):
    if(r-p < 75):
        arr[p:r+1] = sorted(arr[p:r+1])
        return arr[p+k-1]

    for i in range(0, int((r-p-4)/5+1)):
        # sort 5 elements, for get the median
        arr[p+5*i:p+5*i+4+1] = sorted(arr[p+5*i:p+5*i+4+1])

        # swap the median to the first position, for better getting the median of medians
        arr[p+i], arr[p+5*i+2] = arr[p+5*i+2], arr[p+i]
        x = select(arr, p, int(p+(r-p-4)/5), int((r-p-4)/10))
        i = partition(arr, p, r, x)    # partition the array
        j = i-p+1

        if(k <= j):
            return select(arr, p, i, k)
        else:
            return select(arr, i+1, r, k-j)


def findKthSmallest(arr, k: int):
    kthNum = select(arr, 0, len(arr)-1, k)
    nums = [num for num in arr if num <= kthNum]
    nums.sort()
    return nums[:k]
