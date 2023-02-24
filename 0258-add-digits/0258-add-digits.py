class Solution():
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        num=str(num)
        while len(num)>1:
            #print(num[0])
            sum=0
            for i in num:
                sum=sum+int(i)
            num=sum
            num=str(num)
            
        #print(num)
        return int(num)