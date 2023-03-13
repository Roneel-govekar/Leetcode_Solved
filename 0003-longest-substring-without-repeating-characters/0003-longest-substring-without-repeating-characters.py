class Solution():
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        sub=[]
        fsub=0
        for i in s:
            if i not in sub:
                sub.append(i)
                #print("sub",sub)
            else:
                while i in sub:
                    sub.pop(0)
                    #print(sub)
                sub.append(i)
            if fsub<len(sub):
                fsub=len(sub)
        return fsub