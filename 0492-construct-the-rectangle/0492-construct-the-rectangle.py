class Solution():
    def constructRectangle(self, area):
        """
        :type area: int
        :rtype: List[int]
        """
        min1=10**7
        for i in range(1,area+1):
            j=area//i
            if area%i==0 and i >=j and i-j <min1 :
                min1=i-j
                posi=i
                posj=j
                return [posi,posj]
            
        