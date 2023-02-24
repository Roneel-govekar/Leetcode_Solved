class Solution():
    def isUgly(self, n):
        """
        :type n: int
        :rtype: bool
        """
        a=[1,2,3,5]
        fact=[]
        i = 2
        if n>1:
            while(n > 1):
                
                if(n % i == 0):
                    fact.append(i)
                    print(i)
                    n = n / i
                else:
                    i+= 1
                    if i>5:
                        return False

            for i in fact:
                if i not in a:
                    return False
            return True
        elif n==1:
            return True
        else:
            return False