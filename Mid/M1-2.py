from random import randint

def randomSelect(nums, l, r, k):
    p = randint(l, r)  # random select a number between l and r
    # swap the selected number with the last number
    nums[r], nums[p] = nums[p], nums[r]
    # the following is the same as quick select
    i = j = l
    while j < r:
        if nums[r] >= nums[j]:
            nums[i], nums[j] = nums[j], nums[i]  # swap
            i += 1

        j += 1

    nums[i], nums[r] = nums[r], nums[i]  # swap

    if i < r-k+1:
        return randomSelect(nums, i+1, r, k)
    elif i > r-k+1:
        return randomSelect(nums, l, i-1, k-r+i-1)
    else:
        return nums[i]

def findKthSmallest(nums: List[int], k: int) -> int:
    n=len(nums)
    return randomSelect(nums, 0, n-1, n-k+1)