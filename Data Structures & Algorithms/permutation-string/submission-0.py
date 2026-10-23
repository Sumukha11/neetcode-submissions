class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        window_size = len(s1)
        freq_dict = {}
        count = {}
        left = 0

        for j in range(window_size):
            char = s1[j]
            freq_dict[char] = freq_dict.get(char, 0) + 1

        for right in range(len(s2)):
            char = s2[right]
            count[char] = count.get(char, 0) + 1

            if right >= window_size - 1:
                if count == freq_dict:
                    return(True)
                
                outgoing = s2[left]
                count[outgoing] -= 1
                if count[outgoing] == 0:
                    del count[outgoing]
                left += 1
        return(False)