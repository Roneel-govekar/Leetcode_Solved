class Solution():
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count=0
        max1=0
        for i in range(len(nums)):
            if nums[i]==1:
                count+=1
            if count>max1:
                max1=count
            if nums[i]==0:
                count=0
                
        return max1