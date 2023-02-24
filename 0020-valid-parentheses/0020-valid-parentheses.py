class Solution():
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        count=1
        open_brackets=['{','(','[']
        
        pair={'}':'{',']':'[',')':'('}
        brakets=[' ']
        for i in s:
                
            if i in open_brackets:
                brakets.append(i)
                
            elif pair[i] == brakets[-1]:
                brakets.pop()
            else:
                brakets.append(i)
                
                
                
        if len(brakets)==1 :
            return True
        else:
            return False
        
    