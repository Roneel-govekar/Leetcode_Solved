class Solution():
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        index=" "
        if target>nums[-1]:
            index=len(nums)
        elif target<nums[0]:
            index=0
        else:
            for i in range(len(nums)):
                if nums[i]==target:
                    index=i
                    break
                else:
                    if nums[i]<target and nums[i+1]>target:
                        index=i+1

        return index