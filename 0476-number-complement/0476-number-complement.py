class Solution():
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        ans=0
        num=bin(num)
        num=num[2:]
        num=str(num)
        
        num=["0" if i=="1" else "1" for i in num ]
        
        num=''.join(num)
        for i in range(len(num)):    
                ans=ans+2**(len(num)-1-i)*int(num[i])
        
        return ans