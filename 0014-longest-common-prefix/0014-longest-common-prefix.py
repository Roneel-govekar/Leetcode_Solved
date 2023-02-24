class Solution():
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        str=[]
        strs.sort(key=len)
        
        smallest_len=len(strs[0])+1
        #print(smallest_len)
        if len(strs)==1:
            return strs[0]
            
        else:
            for i in range(smallest_len):
                start_str=strs[0][:i]
                #print("start string",start_str)
                count=0
                #print(i)
                for j in strs:
                    #print(j[:i])
                    if j[:i]==start_str:
                        #print("asdas")
                        count=count+1
                if count==len(strs):
                    str.append(start_str)
                    count=0

            return str[-1]