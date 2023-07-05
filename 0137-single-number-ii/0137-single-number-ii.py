class Solution():
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        for i in range(len(nums)):
            if i == 0 and nums[i] not in nums[i+1:]:
                return nums[i]
            elif i == len(nums)-1 and nums[i] not in nums[:i-1]:
                return nums[i]
            elif nums[i] not in nums[:i-1] and nums[i] not in nums[i+1:]:
                return nums[i]