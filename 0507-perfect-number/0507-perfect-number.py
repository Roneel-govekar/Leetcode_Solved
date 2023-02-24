class Solution():
    def checkPerfectNumber(self, num):
        """
        :type num: int
        :rtype: bool
        """
        ans=0
        for i in range(2,int(num**0.5)+1):
            if num%i==0:
                ans=(ans+i)+(num//i)
                #print(i)
        if num!=1:
            ans=ans+1
        #print(ans)
        if ans==num:
            return True
        else:
            return False