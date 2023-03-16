class Solution():
    def findLHS(self, nums):
        """
        :type nums: List[int]
        :rtype: int"""
       
        n=sorted(nums)
        length=0
        pairs=[]
        for i in range(len(n)-1):
            if abs(n[i]-n[i+1])==1:
                pairs.append([n[i],n[i+1]])
                
        for j in pairs:
            
            ans=[i for i in nums if i in j]
            ans=len(ans)
            if ans>length:
                length=ans
            
        return length