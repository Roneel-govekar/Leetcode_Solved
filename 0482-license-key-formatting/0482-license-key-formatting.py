class Solution():
    def licenseKeyFormatting(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        s=str(s)
        ans=[]
        s=[i for i in s if i!="-"]
        s=''.join(s)
        
        #print(s[:(len(s))%4])
        ans.append(s[:(len(s))%k])
        
        for i in range((len(s))%k,(len(s)),k):
            
            #print(s[pos1:pos2])
            ans.append(s[i:i+k])

        
        ans=[str.upper(i) for i in ans if i!='']
        ans='-'.join(ans)
        
        
        return ans