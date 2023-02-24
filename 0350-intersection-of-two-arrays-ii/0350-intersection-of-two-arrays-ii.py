class Solution():
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        
        if len(nums1)<len(nums2):
            temp=nums1
            nums1=nums2
            nums2=temp
        ans=[]    
        for i in nums2:
            if i in nums1:
                ans.append(i)
                nums1.pop(nums1.index(i))
            
        return ans