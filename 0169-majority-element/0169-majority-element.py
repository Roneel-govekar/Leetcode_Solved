class Solution():
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count_dir={}
        
        for i in range(len(nums)):     
            count_dir[nums[i]]=0
            
        for i in range(len(nums)):     
            count_dir[nums[i]]=count_dir[nums[i]]+1 
        maximum=0    
        for i in count_dir:
            
            if count_dir[i]>maximum:
                maximum=count_dir[i]
                pos=i
            
        return pos