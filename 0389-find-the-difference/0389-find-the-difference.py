class Solution():
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        t=list(t)    
        for i in s:
            print(i)
            print(t.index(i))
            t.pop(t.index(i))
        return "".join(t)