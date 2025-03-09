class Solution:
    def isValid(self, s: str) -> bool:
        # 1 <= s.length <= 10^4
        # s consists of parentheses only '(){}[]'
        stack = []
        if not s or len(s) == 1:
            return False
        for ch in s:
            if ch == '(' or ch == '{' or ch == '[':
                stack.append(ch)
            if len(stack) > 0:
                if stack[-1] == '(' and ch == ')':
                    stack.pop()
                elif stack[-1] == '{' and ch == '}':
                    stack.pop()
                elif stack[-1] == '[' and ch == ']':
                    stack.pop() 
                elif stack[-1] == '[' and (ch == '}' or ch == ")"):
                    return False
                elif stack[-1] == '{' and (ch == ')' or ch == "]"):
                    return False
                elif stack[-1] == '(' and (ch == '}' or ch == ']'):
                    return False
            elif not stack:
                if ch == ')' or ch == '}' or ch == ']':
                    return False
        if not stack:
            return True
        return False