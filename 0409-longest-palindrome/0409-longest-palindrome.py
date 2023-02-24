class Solution():
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        s=list(s)
        keys=[]
        count=0
        for i in s:
            if i not in keys:
                keys.append(i)
        dict_letter = { i : 0 for i in keys }
        
        for i in s:     
            dict_letter[i]=dict_letter[i]+1
        
        sorted_dict_letter = sorted(dict_letter.items(), key=lambda x:x[1], reverse=True)
        total=0
        print(sorted_dict_letter)
        max_value=sorted_dict_letter[0][1]
        #print(max_value)
        for i in range(1,len(sorted_dict_letter)):
            #print(sorted_dict_letter[i][1])
            if max_value%2==0:
                
                if sorted_dict_letter[i][1]%2!=0: 
                    if count==0:
                        count=1
                        total=total+sorted_dict_letter[i][1]
                    else:
                        total=total+sorted_dict_letter[i][1]-1
                    
                else:
                    total=total+sorted_dict_letter[i][1]
                    
            else:
                if sorted_dict_letter[i][1]%2==0:
                    total=total+sorted_dict_letter[i][1]
                else:
                    total=total+sorted_dict_letter[i][1]-1
                    
                
            
        total=total+max_value    
        return total