class Solution():
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        s=set(nums)
        ans=[]
        length=len(nums)
        l=len(s)
        for i in range(1,len(nums)+1):
            if i not in s:
                ans.append(i)
                l+=1
                
        if l==length:
            return ans
            
        return ans