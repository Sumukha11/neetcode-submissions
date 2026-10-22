class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq_dict = {}
        max_len = 0
        max_freq = 0
        left = 0

        for right in range(len(s)):
            char = s[right]
            freq_dict[char] = freq_dict.get(char , 0) + 1
            max_key = max(freq_dict, key=freq_dict.get)
            max_freq = freq_dict[max_key]
            window_lenght = right - left + 1

            if window_lenght - max_freq > k:
                freq_dict[s[left]] -= 1
                left += 1
            else:
                max_len = max(max_len, right - left + 1)

        return(max_len)