class Solution():
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        s=" ".join(s.split())
        word=[]
        ans=[]

        for i in range(len(s)-1,-1,-1):
            if s[i]!=" ":
                word.append(s[i])
                
            else:
                print(("".join(word))[::-1])
                ans.append(("".join(word))[::-1])
                word=[]
        
        ans.append(("".join(word))[::-1])
        print(("".join(word))[::-1])
        return " ".join(ans)