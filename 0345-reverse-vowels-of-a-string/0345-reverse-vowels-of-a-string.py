class Solution():
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        s=list(s)
        pos=[]
        posval=[]
        j=0
        vowels=["a","e","i","o","u","A","E","I","O","U"]
        for i in range(len(s)):
            if s[i] in vowels:
                pos.append(i)
                posval.append(s[i])
        posval.reverse()        
        for i in pos:
            s[i]=posval[j]
            j+=1
        return ''.join(s)