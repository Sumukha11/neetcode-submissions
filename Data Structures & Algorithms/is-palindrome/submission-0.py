class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.replace(" ", "")
        s = "".join(char.lower() for char in s if char.isalnum())
        left = 0
        right = len(s)-1

        while left < right:
            if s[left] != s[right]:
                return(False)
                break
            left += 1
            right -= 1
        else:
            return(True)