class Solution():
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """
        pattern=list(pattern)
        s=s.split(" ")
        if len(s)!=len(pattern):
            return False
        else:
            for i in range(len(s)):
                for j in range(i+1,len(s)):
                    if pattern[i]==pattern[j]:
                        if s[i]!=s[j]:
                            return False
                    elif pattern[i]!=pattern[j]:
                        if s[i]==s[j]:
                            return False
        
        return True