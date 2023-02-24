class Solution():
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        i=0
        if num==1:
            return True
        else:
            while i<(num//2)+1:
                if i**2>num:
                    return False
                if i**2==num:
                    return True
                i+=1
        return False