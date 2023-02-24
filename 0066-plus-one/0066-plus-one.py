class Solution():
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        digits=[str(x) for x in digits]
        digits=''.join(digits)
        digits=int(digits)+1
        digits=str(digits)
        digits=[int(x) for x in digits]
        #digits=digits.split()
        
        
        return digits