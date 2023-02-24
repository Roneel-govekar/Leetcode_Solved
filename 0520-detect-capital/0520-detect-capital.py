class Solution():
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        
        letters="qwertyuiopasdfghhjklzxcvbnm"
        upper_count=0
        lower_count=0
        for i in word:
            if i in letters:
                lower_count+=1
            else:
                upper_count+=1
                
        if upper_count==len(word)or lower_count==len(word)or (word[0] in letters.upper() and lower_count==len(word)-1):
            return True
        else:
            return False