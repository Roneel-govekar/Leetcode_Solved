class Solution():
    def calPoints(self, operations):
        """
        :type operations: List[str]
        :rtype: int
        """
        ans=[]
        for i in operations:
            
            if i=="+":
                ans.append(ans[len(ans)-1]+ans[len(ans)-2])
                #print(ans)
            elif i=="D":
                #print(ans[len(ans)-1])
                ans.append(2*int(ans[len(ans)-1]))
            elif i=="C":
                ans.pop()
            else:
                ans.append(int(i))
            
        return sum(ans)