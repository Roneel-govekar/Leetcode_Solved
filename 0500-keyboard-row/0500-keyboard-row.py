class Solution():
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        
        s1="qwertyuiop"
        s2="asdfghjkl"
        s3="zxcvbnm"
        
        
        ans=[]
        count=0
        for i in words:
            count=0
            for j in i.lower():
                if j in s1:
                    count+=1
                if count==len(i):
                    ans.append(i)
                    
                    
                    
        for i in words:
            count=0
            for j in i.lower():
                if j in s2:
                    count+=1
                if count==len(i):
                    ans.append(i)
                    
                    
        for i in words:
            count=0
            for j in i.lower():
                if j in s3:
                    count+=1
                if count==len(i):
                    ans.append(i)
                    
                    
                
        
        
        return ans