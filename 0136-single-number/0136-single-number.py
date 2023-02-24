class Solution():
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        in_list=[]
        for i in range(len(nums)):
            if nums[i] in nums[i+1:]:
                in_list.append(nums[i])
                
        for i in nums:
            if i not in in_list:
                ans=i
        return ans