class Solution():
    def checkRecord(self, s):
        """
        :type s: str
        :rtype: bool
        """
        countA=countP=countL=0
        for i in range(len(s)):
            if s[i-1] =="A":
                countA+=1
                if countA>=2:
                    return False
        for i in range(1,len(s)-1):        
            if s[i] =="L" and s[i+1] =="L" and s[i-1] =="L":
                countL+=3
                return False
            
        return True