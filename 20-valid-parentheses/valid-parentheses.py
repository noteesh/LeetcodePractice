class Solution:
    def isValid(self, s: str) -> bool:

        st = []

        for i, n in enumerate(s):
            if n == '(' or n == '{' or n == '[':
                st.append(n)
            
            elif n == ')':
                if not st or st.pop() != '(':
                    return False
            elif n == '}':
                if not st or st.pop() != '{':
                    return False
            elif n == ']':
                if not st or st.pop() != '[':
                    return False
        
        if not st:
            return True
        return False
            
        