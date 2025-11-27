class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = ['A', 'a', 'E', 'e', 'I', 'i', 'O', 'o', 'U', 'u']

        p1 = 0
        p1Bool = False
        p2 = len(s) - 1
        p2Bool = False
        ret = list(s)

        while p1 < p2:
            if p1Bool and p2Bool:
                ret[p1], ret[p2] = ret[p2], ret[p1]
                p1Bool = False
                p2Bool = False
                p1 += 1
                p2 -= 1
            elif not p1Bool:
                if ret[p1] in vowels:
                    p1Bool = True
                else:
                    p1 += 1
            elif not p2Bool:
                if ret[p2] in vowels:
                    p2Bool = True
                else:
                    p2 -= 1
        return "".join(ret)