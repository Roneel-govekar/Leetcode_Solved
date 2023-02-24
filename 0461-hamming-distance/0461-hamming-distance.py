class Solution():
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        x=bin(x)
        y=bin(y)
        x=x[2:]
        y=y[2:]
        
        
        length=max(len(x),len(y))
        
        if len(x)<len(y):
            
            x="0"*(length-len(x))+str(x)
        elif len(x)>len(y):
            
            y="0"*(length-len(y))+str(y)
        print(x)
        print(y)
        count=0    
        for i in range(length):
            if x[i]!=y[i]:
                count+=1
        
        return count