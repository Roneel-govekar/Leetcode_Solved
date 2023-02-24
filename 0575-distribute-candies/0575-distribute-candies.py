class Solution():
    def distributeCandies(self, candyType):
        """
        :type candyType: List[int]
        :rtype: int
        """
        
        n=len(candyType)//2
        var=set(candyType)
        
        if n>len(var):
            return len(var)
        else:
            return n