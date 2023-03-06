class Solution():
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        a=1
        b=1
        i=0
        while i<n:
            temp=b
            b=a+b
            a=temp
            i+=1
        return a