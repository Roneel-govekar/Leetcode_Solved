class Solution():
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        j=-1
        for i in range(len(s)//2):
            temp=s[j]
            s[j]=s[i]
            s[i]=temp
            j-=1
            
        print(s)