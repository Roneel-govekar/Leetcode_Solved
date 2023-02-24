class Solution():
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        s=s.lower()
        s=list(s)
        s.sort()
        
        
        t=t.lower()
        t=list(t)
        t.sort()
        
        s=''.join(s)
        t=''.join(t)
        
        if s==t:
            return True
        else:
            return False
        