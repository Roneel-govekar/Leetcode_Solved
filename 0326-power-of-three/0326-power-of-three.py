class Solution():
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        
        power=0
        while 3**power<=n:
            #print(2**power)
            if 3**power==n:
                return True
            power+=1
        return False