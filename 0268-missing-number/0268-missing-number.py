class Solution():
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if 0 not in nums:
            return 0
        max_num=max(nums)
        for i in range(1,max_num):
            if i not in nums:
                return i
            
        return max_num+1