class Solution():
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        s=list(s)
        count=j=0
        temp=len(s)
        if temp!=0:
            for i in t:
                #print(i)
                if i==s[j]:
                    s.pop(0)
                    if len(s)==0:
                        return True
                    count+=1

            if count==temp:
                return True
            else:
                return False
        else:
            return True
        