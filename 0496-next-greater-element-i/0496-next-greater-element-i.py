class Solution():
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        ans=[]
        for i in range(len(nums1)):
            #print(nums1[i])
            #print("index",nums2.index(nums1[i]))
            #print("array",nums2[nums2.index(nums1[i]):])
            c=0
            for j in nums2[nums2.index(nums1[i]):]:
                
                if j>nums1[i]:
                    #print("ans",j)
                    ans.append(j)
                    break
                else:
                    #print("c",c)
                    c+=1
            if c==len(nums2[nums2.index(nums1[i]):]):
                ans.append(-1)
                
                
            
                
                
            
            
        return ans