class Solution():
    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count=1
        finalCount=1
        for i in range(len(nums)-1):
            if nums[i]<nums[i+1]:
                
                count+=1
                if count>finalCount:
                    finalCount=count   
            else:
                if count>finalCount:
                    finalCount=count
                count=1
        
        return finalCount