class Solution():
    def countSegments(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s)>0:
            ans =s.split(" ")
            #print(ans)
            ans=[i for i in ans if i!=""]
            #print(ans)
            return len(ans)
        else:
            return 0
        