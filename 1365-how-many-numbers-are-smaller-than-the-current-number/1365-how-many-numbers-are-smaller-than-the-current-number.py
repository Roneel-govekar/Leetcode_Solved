class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        count=0
        ans=[]
        for i in range(len(nums)):
            for j in range(len(nums)):
                if nums[j]<nums[i]:
                    count+=1
                    
            ans.append(count)
            count=0
        return ans