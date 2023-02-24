class Solution():
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        i=1
        while n>0:
            n=n-i
            
            if n<=i:
                return i
            i+=1
        