class Solution():
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        a=0
        b=1
        i=0
        if n==0:
            return 0
        elif n==1:
            return 1
        else:
            while i<=n-2:
                i+=1
                a,b=b,a+b
                print("a,b",a,b)

            return b