class Solution():
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        
        for i in range(len(s)):
            fs=s[i]
            ft=t[i]
            #print(fs,ft)
            
            #print(s[i+1:].find(fs))
            pos=s[i+1:].find(fs)
            #print(s[i+1+pos])
            #print("-----")
            if t[i+1+pos]!=ft:
                return False
            
        for i in range(len(t)):
            fs=s[i]
            ft=t[i]
            #print(fs,ft)
            
            #print(t[i+1:].find(ft))
            pos=t[i+1:].find(ft)
            #print(t[i+1+pos])
            #print("-----")
            if s[i+1+pos]!=fs:
                return False
        return True