class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        st = []

        for n in tokens:
            num1 = 0
            num2 = 0
            if n != '+' and n != '-' and n != '*' and n != '/':
                st.append(n)
            elif n == '+':
                num1 = st.pop()
                num2 = st.pop()
                st.append(int(num1) + int(num2))

            elif n == '-':
                num1 = st.pop()
                num2 = st.pop()
                st.append(int(num2) - int(num1))
            
            elif n == '*':
                num1 = st.pop()
                num2 = st.pop()
                st.append(int(num1) * int(num2))
            
            elif n == '/':
                num1 = st.pop()
                num2 = st.pop()
                st.append(int(num2) / int(num1))
    
        return int(st.pop())



        