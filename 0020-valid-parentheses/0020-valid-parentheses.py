class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        
        for i in range(len(s)):
            if s[i] == '(' or s[i] == '{' or s[i] == '[':
                stack.append(s[i])
            elif len(stack)==0:
                return False
            elif (s[i] == ')' and stack[-1] == '(') or (s[i] == '}' and stack[-1] == '{') or (s[i] == ']' and stack[-1] == '['):
                stack.pop()
            else:
                return False
        
        return len(stack) == 0