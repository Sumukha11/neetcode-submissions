class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # longest Substring Without Repeating Characters
        seen = set()
        left = 0
        max_length = 0

        for right in range(len(s)):
            char = s[right]  

            while char in seen:
                seen.discard(s[left])
                left += 1
            seen.add(char)
            current_window = right - left +1
            max_length = max(max_length, current_window)

        return(max_length)