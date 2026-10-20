class Solution:

    def encode(self, strs: List[str]) -> str:
        resultEncode = ""

        for s in strs:
            resultEncode += str(len(s))
            resultEncode += "#"
            resultEncode += s
        return resultEncode

    def decode(self, s: str) -> List[str]:
        resultDecode = []
        i =0
        start = 0

        while i < len(s):
            if s[i] == "#":
                length=int(s[start:i])
                word = s[i + 1 : i + 1 + length]
                resultDecode.append(word)
                i = i+1+length
                start = i
            i += 1
        return resultDecode

solution = Solution()
strs = ["hello", "world"]
encoded = solution.encode(strs)
decoded = solution.decode(encoded)