class Solution():
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        for i in range(len(s)):
            sub=s[i:]
            #print(sub)
            for k in range(2,len(s)//len(sub)+1):
                #print(k*sub)
                if k*sub==s:
                    return True
                
        
        
        return False