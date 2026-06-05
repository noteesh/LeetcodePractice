class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        encoded_string = ""
        for n in strs:
            encoded_string += n
            encoded_string += "π"
        
        print(encoded_string)
        return encoded_string

        

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """
        ret = []
        cur = ""
        for ch in s:
            if ch == "π":
                ret.append(cur)
                cur = ""
            else:
                cur += ch
        return ret

        


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))