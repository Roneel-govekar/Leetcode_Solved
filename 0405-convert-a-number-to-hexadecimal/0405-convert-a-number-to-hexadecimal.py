class Solution():
    def toHex(self, num):
        """
        :type num: int
        :rtype: str
        """
        ans=0
        if num<0:
            num=bin(num)
            num=num[3:]
            num=str(num)
            num="0"*(32-len(num))+str(num)
            num=["0" if i=="1" else "1" for i in num ]
            num=''.join(num)
            for i in range(len(num)):    
                ans=ans+ 2**(31-i)*int(num[i])
            ans=ans+1
            num=hex(ans)
            num=num[2:]
        else:
            num=hex(num)
            num=num[2:]
            
        return num