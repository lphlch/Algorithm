class Solution:
    def f(self, nums1, nums2, m, n, k):
        if m >= len(nums1):
            return nums2[n+k-1]
        if n >= len(nums2):
            return nums1[m+k-1]
        if k == 1:
            return min(nums1[m], nums2[n])

        if m+k//2-1 < len(nums1):
            n1 = nums1[m+k//2-1]
        else:
            n1 = 100000
        if n+k//2-1 < len(nums2):
            n2 = nums2[n+k//2-1]
        else:
            n2 = 100000

        if n1 < n2:
            return self.f(nums1,  nums2, m+k//2, n, k-k//2)
        else:
            return self.f(nums1,  nums2, m, n+k//2, k-k//2)

    def findMedianSortedArrays(self, nums1, nums2) -> float:
        k1 = (len(nums1) + len(nums2) + 1) // 2
        k2 = (len(nums1) + len(nums2) + 2) // 2
        mid1 = self.f(nums1, nums2, 0, 0, k1)
        mid2 = self.f(nums1, nums2, 0, 0, k2)
        return (mid1+mid2)/2


s = Solution()
print(s.findMedianSortedArrays(
    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 3, 3, 3, 3, 6, 8, 9, 10, 15]))
