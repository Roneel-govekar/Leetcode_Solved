class Solution():
    def countBits(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        ans=[]
        for i in range(n+1):
        
            count=0
            #print(str(bin(i))[2:])
            i=str(bin(i))[2:]
            #print(i)
            for j in i:
                if j=="1":
                    count+=1
            ans.append(count)
            
        return ans