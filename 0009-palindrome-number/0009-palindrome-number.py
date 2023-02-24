class Solution():
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        n=x
        #length=len(x)
        palin=0
        i=0
        while x>0:
            d=x%10
            palin=palin*10+d
            x=x//10
        if palin==n:
            return True
        else:
            return False