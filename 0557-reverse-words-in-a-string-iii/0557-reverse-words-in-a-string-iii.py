class Solution():
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        ans=s.split(" ")
        rev=[]
        for i in ans:
            #print(i[::-1])
            rev.append(i[::-1])
        
        return ' '.join(rev)