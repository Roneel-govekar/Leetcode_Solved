class Solution():
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a=0
        nums.sort()
        for i in range(0,len(nums),2):
            #print(nums[i],nums[i+1])
            a=a+min(nums[i],nums[i+1])
        return a