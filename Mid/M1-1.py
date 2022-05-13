from heapq import heapify, heappop, heappush

def findKthSmallest(nums: List[int], k: int) -> int:
    l=[-num for num in nums[:k]]
    
    heapify(l)  # heapify the first k elements
    
    for i in range(k,len(nums)):
        if nums[i] < (-l[0]):
            # replace the biggest element in the heap with the current element
            heappop(l)
            heappush(l,-nums[i])

    return -l[0]
