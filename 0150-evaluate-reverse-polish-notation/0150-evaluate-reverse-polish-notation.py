class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        res = 0
        if len(tokens) == 1:
            return int(tokens[0])

        operation =  ["+", "-", "*", "/"]
       
        for token in tokens:
            if token in operation:
                first = stack.pop()
                second = stack.pop()
                res = int(eval(str(second) + token + str(first)))
                stack.append(res)
            else:    
                stack.append(int(token))
        res = stack.pop()
        return res 
