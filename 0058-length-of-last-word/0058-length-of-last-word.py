class Solution():
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        #print(s)
        
        
        s=s.split()
        length=len(s[-1])
        return length
    