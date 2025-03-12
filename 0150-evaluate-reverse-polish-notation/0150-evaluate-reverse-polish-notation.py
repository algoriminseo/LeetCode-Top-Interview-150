#Time Complexity : O(n), where n is length of tokens
#Space Complexity : O(n), where n is length of tokens.
#We need to store n elements if aritmetic operations is in the near to last element in the stack



class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        if len(tokens) == 1:
            return int(tokens[0])

        operation =  ["+", "-", "*", "/"]
       
        for token in tokens:
            if token == "+":
                stack.append(stack.pop() + stack.pop())
            elif token == "-":
                a, b = stack.pop(), stack.pop()
                stack.append(b - a)
            elif token == "/":
                a, b = stack.pop(), stack.pop()
                stack.append(int(float(b)/a))
            elif token == "*":
                stack.append(stack.pop() * stack.pop())
            else:    
                stack.append(int(token))
      
        return stack.pop() 
