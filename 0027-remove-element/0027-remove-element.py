class Solution():
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        count=0
        for i in range(len(nums)):            
            if val==nums[i]:
                count=count+1
                nums[i]=101
                
            
        
        nums.sort()
        count=len(nums)-count
        nums=[x for x in nums if x!=101]
        
        
        
        
        return count