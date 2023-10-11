class DecodeString:
    
    def encode(self, s: str) -> str:
        # method implementation here
        output = ""
        for i in range(len(s)):
            q = ord(s[i]) + i
            q = q + 3
            output = output + chr(q)
        return output

    
    def decode(self, s: str) -> str:
        # method implementation here
        output = ""
        
        for i in range(len(s)):
            q = ord(s[i]) - i
            q = q - 3
            output = output + chr(q)
        
        return output



c = DecodeString()

a = c.encode("abc") # "abc"
print(a)
print(c.decode(a)) # "abc"




# print(c.encode("aaabcbc")) # "3[a]2[bc]"
# print(c.decode("3[a]2[bc]")) # "aaabcbc"
