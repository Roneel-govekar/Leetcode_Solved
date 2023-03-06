class Solution():
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        : nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        
        for i in range(len(nums1)):
            if i>=m:
                nums1.insert(i,nums2[i-m])
                
                nums1.pop()
        nums1.sort()
        return nums1