class Solution():
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        total_digits=[" "]
        
        while total_digits:
        
            total_digits.append(n)

            n=str(n)
            n=[int(x) for x in n]
            n=[x*x for x in n]
            total=0
            
            for i in n:
                total=total + i
            n=total
            
            if n==1:
                return True
            else:
                if n in total_digits:
                    return False
                    break
        
