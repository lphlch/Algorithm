class Solution:
    def f(self, nums1, nums2, k):
        if(len(nums1) < len(nums2)):
            nums1, nums2 = nums2, nums1
        if(len(nums2) == 0):
            return nums1[k-1]
        if(k == 1):
            return min(nums1[0], nums2[0])
        temp = min(k//2, len(nums2))
        if(nums1[temp-1] >= nums2[temp-1]):
            return self.f(nums1, nums2[temp:], k-temp)
        else:
            return self.f(nums1[temp:], nums2, k-temp)

    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        k1 = (len(nums1) + len(nums2) + 1) // 2
        k2 = (len(nums1) + len(nums2) + 2) // 2

        return (self.f(nums1, nums2, k1) + self.f(nums1, nums2, k2)) / 2
