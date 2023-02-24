class Solution():
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        #s[k-1::-1]+s[k-len(s):]
        ans=[]
        for i in range(0,len(s),2*k):
            #print(i)
            #print(s[i:i+2*k])
            temp=s[i:i+2*k]
            #print(temp[k-1::-1]+temp[k-len(temp):])
            ans.append(temp[k-1::-1]+temp[k-len(temp):])
            
        
        return ''.join(ans)[:len(s)]