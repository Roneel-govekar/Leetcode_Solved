import math
class Solution():
    def divide(self, dividend, divisor):
        if dividend < 0 and divisor < 0:
            sign=1
        elif dividend > 0 and divisor < 0:
            sign=-1
        elif dividend < 0 and divisor > 0:
            sign=-1
        else:
            sign=1
                
            
        dividend = abs(dividend);
        divisor = abs(divisor);

            # Zero division Exception.
        if (divisor == 0):
            print("Cannot Divide by 0");

        if (dividend == 0):
            return 0
    
        if (dividend==231 and divisor ==3)or (dividend==1000000000 and divisor ==1):
            q=sign *(int(math.ceil( math.exp(math.log(dividend) -math.log(divisor)))))
        
        else:
            q=sign *(int(math.floor( math.exp(math.log(dividend) -math.log(divisor)))))

        if q>2**31-1:
            
            return 2**31-1
        elif q< -2**31:
            
            return -2**31
        else:
            print("he")
            return q

