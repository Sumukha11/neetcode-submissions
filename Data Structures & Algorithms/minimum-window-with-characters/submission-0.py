class Solution:
    def minWindow(self, s: str, t: str) -> str:
        result = []
        required = {}

        for char in t:
            required[char]=required.get(char, 0) + 1

        window = {}
        left = 0

        min_length = float("inf")
        min_start = 0
        formed = 0

        for right in range(len(s)):
            char = s[right]
            window[char] = window.get(char, 0) + 1
            
            if char in required and window[char] == required[char]:
                formed += 1

            while formed == len(required):
                current = right - left + 1

                if current < min_length:
                    min_length = current
                    min_start = left

                left_char = s[left]
                window[left_char] -= 1

                if left_char in required and window[left_char] < required[left_char]:
                    formed -= 1
                left += 1

        if min_length == float("inf"):
            return("")
        else:
            return(s[min_start:min_start + min_length])