class Solution():
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        power=0
        if n%2==0 or n==1:
            while 2**power<=n:
                #print(2**power)
                if 2**power==n:
                    return True
                power+=1
        return False