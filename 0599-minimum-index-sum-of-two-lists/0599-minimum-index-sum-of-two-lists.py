class Solution():
    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
        max_len=10**4
        ans=[]
        for i in list1:
            if i in list2:
                i_val=list1.index(i)
                j_val=list2.index(i)
                if (i_val+j_val)<=max_len:
                    max_len=i_val+j_val
                    
                    ans.append([i,max_len])
        prej=[i[1] for i in ans ]
        prej=min(prej)
        ans1=[i[0] for i in ans if i[1]==prej]
        return ans1