class Solution():
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        ransomNote=list(ransomNote)
        magazine=list(magazine)
        count=0
        for i in ransomNote:
            if i in magazine:
                magazine.pop(magazine.index(i))
                count=count+1
        
        if count==len(ransomNote):
            return True
        else:
            return False