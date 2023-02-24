class Solution():
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        i=0
        if x==1:
            return 1
        while i*i<=x:
            i=i+1    
        
        return i-1   
            
            