class Solution():
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        
        
        stack=[]
        for i in tokens:
            
            
            if i != "+" and i != "*" and i != "/" and i != "-":
                #print(i)
                stack.append(float(i))
            else:
                #print(stack)
                op2=float(stack.pop())
                op1=float(stack.pop())
                if i=="*":
                    ans=op1*op2
                elif i=="+":
                    ans=op1+op2
                elif i=="/":
                    ans=op1/op2
                    if ans>0:
                        ans=math.floor(ans)
                    else:
                        ans=math.ceil(ans)
                else:
                    ans=op1-op2
                stack.append(ans)
                #print(stack)
                
                
            
            
        
        return int(stack[0])