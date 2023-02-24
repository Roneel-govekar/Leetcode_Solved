class Solution():
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans=[]
        for i in nums:
            if i not in ans:
                ans.append(i)
        ans.sort()
        if len(ans)==2:
            return ans[-1]
        elif len(ans)==1:
            return ans[-1]
        return ans[-3]