class Solution():
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
    
        total1=0
        total2=0
        
        
        for i in range(len(a)):
            total1=total1+(2**(len(a)-i-1))*int(a[i])
        
        for i in range(len(b)):
            total2=total2+(2**(len(b)-i-1))*int(b[i])
            
        sum=total1+total2    
        
        ans=str(bin(sum))
        
        return ans[2:]