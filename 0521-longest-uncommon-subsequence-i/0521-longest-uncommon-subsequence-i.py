class Solution():
    def findLUSlength(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: int
        """
        if len(a)<len(b):
            small=a
            big=b
        else:
            small=b
            big=a
        max_un=0
        ans=-1
        for i in range(len(big)):
            for j in range(i,len(big)+1):
                sub=big[i:j]
                
                if sub not in small and len(sub)>max_un:
                    ans=len(sub)
                    max_un=len(sub)
                    
        return ans