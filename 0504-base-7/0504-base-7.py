class Solution():
    def convertToBase7(self, num):
        """
        :type num: int
        :rtype: str
        """
        ans=[]
        
        if num>0:
            while num>0:
                rem=num%7
                ans.append(str(rem))
                num=num//7
                
            ans=''.join(ans[::-1])
        elif num<0:
            num=abs(num)
            while num>0:
                rem=num%7
                ans.append(str(rem))
                num=num//7
            ans=''.join(ans[::-1])
            ans="-"+ans
        else: 
            ans='0'

        
        return ans