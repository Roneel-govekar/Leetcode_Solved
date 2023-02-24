class Solution():
    def numberToWords(self, num):
        """
        :type num: int
        :rtype: str
        """
        word=""
        
        
        onesplace={" ":"",0:"",1:"One",2:"Two",3:"Three",4:"Four",5:"Five",6:"Six",7:"Seven",8:"Eight",9:"Nine",10:"Ten",11:"Eleven",12:"Twelve",13:"Thirteen",14:"Fourteen",15:"Fifteen",16:"Sixteen",17:"Seventeen",18:"Eighteen",19:"Nineteen"}
        tensplace={" ":"",0:"",2:"Twenty",3:"Thirty",4:"Forty",5:"Fifty",6:"Sixty",7:"Seventy",8:"Eighty",9:"Ninety"}
        others={' ':"",100:"Hundred",1000:"Thousand",1000000:"Million",1000000000:"Billion"}
        zero={0:"Zero"}
        n=str(num)
        length=len(n)
        if length!=12:
            for i in range(12-length):
                n=" "+n
        length=len(n)
        
        word=[]
        if n[2]!= " " : 
            if length==12 and n[0]!=' ':
                word.append(onesplace[int(n[0])]+" "+ others[100])
            if n[1]!=" " and n[1]=="1":
                word.append(onesplace[int(n[1])+10]+" "+others[1000000])
            elif n[1]==" ":
                word.append(onesplace[int(n[2])]+" "+others[1000000000])
            else:
                word.append(tensplace[int(n[1])]+" "+onesplace[int(n[2])]+" "+others[1000000000])
                
        
        if n[5]!= " ":
            if n[3]!=' ' and n[3]!="0":
                word.append(onesplace[int(n[3])]+" "+ others[100])
            if n[4]!=" " and n[4]=="1":
                
                word.append(onesplace[int(n[5])+10]+" "+others[1000000])
            elif n[4]==" ":
                
                word.append(onesplace[int(n[5])]+" "+others[1000000])
            else:
                if n[3]=="0" and n[4]=="0" and n[5]=="0" and n[8]=="0" and n[7]=="0" and n[6]=="0":
                    word.append("")
                else:
                    word.append(tensplace[int(n[4])]+" "+onesplace[int(n[5])]+" "+others[1000000])    
        
            
        if n[8]!= " ":  
            if n[6]!=" " and n[6]!="0":
                word.append(onesplace[int(n[6])]+" "+ others[100])
            if n[7]!=" " and  n[7]=="1":
                word.append(onesplace[int(n[8])+10]+" "+others[1000])
            elif n[7]==" ":
                word.append(onesplace[int(n[8])]+" "+others[1000])
            else: 
                if n[8]=="0" and n[7]=="0" and n[6]=="0":
                    word.append("")
                else:
                    
                    word.append(tensplace[int(n[7])]+" "+onesplace[int(n[8])]+" "+others[1000])
        
            
        if n[11]!=" ": 
            
            if n[9]!="0" and n[9]!=" ":
                word.append(onesplace[int(n[9])]+" "+ others[100])
                if n[10]=="1":                
                    word.append(onesplace[int(n[11])+10])
                elif n[10]!="1": 
                    if int(n[10])!=0:
                        word.append(tensplace[int(n[10])]+" "+onesplace[int(n[11])])
                    else:
                        word.append(onesplace[int(n[11])])
            
            if n[9]=='0' and n[9]!=" ":
                if n[10]=="1":                
                    word.append(onesplace[int(n[11])+10])
                elif n[10]!="1":                
                    word.append(tensplace[int(n[10])]+" "+onesplace[int(n[11])])
                #word.append(tensplace[int(n[10])]+" "+onesplace[int(n[11])])
            
            
            if n[9]==" " and n[10]!=" ":
                if n[10]=="1":                
                    word.append(onesplace[int(n[11])+10])
                elif n[10]!="1":                
                    word.append(tensplace[int(n[10])]+" "+onesplace[int(n[11])])
                    
            if n[10]==" ":
                if n[11]!="0":
                    word.append(onesplace[int(n[11])])
                else:
                    word.append("Zero")
                
            
                
        word=' '.join(word).strip()
        
        return " ".join(word.split())