class Solution():
    def isPowerOfFour(self, n):
        """
        :type n: int
        :rtype: bool
        """
        power=0
        while 4**power<=n:
            #print(2**power)
            if 4**power==n:
                return True
            power+=1
        return False