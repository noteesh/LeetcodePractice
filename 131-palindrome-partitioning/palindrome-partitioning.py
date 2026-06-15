class Solution:
    def partition(self, s: str) -> List[List[str]]:
        ret = []

        def paths(start, path):
            if start == len(s):
                ret.append(path[:])
                return
            
            
            for n in range(start + 1, len(s) + 1):
                ss = s[start:n]
                if isPalindrome(ss):
                    path.append(ss)
                    paths(n, path)
                    path.pop()


        def isPalindrome(string):
            l = len(string)
            
            if l <= 1:
                return True

            left = 0
            right = l - 1
            
            while left < right:
                if string[left] != string[right]:
                    return False
                left += 1
                right -= 1
            
            return True

        paths(0, [])
        return ret

