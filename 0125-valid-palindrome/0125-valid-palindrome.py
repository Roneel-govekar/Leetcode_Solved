class Solution():
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s=s.lower()
        str=[]
        print(s)
        for i in range(len(s)):
            #print(s[i])
            if (s[i]>='a' and  s[i]<='z') or (s[i]>='0' and  s[i]<='9'):
                str.append(s[i])
                #print(s[i])
        
        rev=''.join(str)[::-1]
        if rev==''.join(str):
            return True
        else:
            return False