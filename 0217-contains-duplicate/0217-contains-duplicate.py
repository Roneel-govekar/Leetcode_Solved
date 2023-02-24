class Solution():
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        s1={}
        
        
        for i in nums:
            s1[i]=0
            
        for i in nums:
            s1[i]=s1[i]+1
        #print(s1)   
        for i in nums:
            #print(i)
            if s1[i]>=2:
                return True
        return False