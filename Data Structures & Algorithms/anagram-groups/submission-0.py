class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        alphabet = "abcdefghijklmnopqrstuvwxyz"
        anagram_map = {}

        for word in strs:
            freq_dict = {}
            count = {}
            
            for letter in word:       
                count[letter] = count.get(letter, 0)+1
            for letter in alphabet:
                freq_dict[letter] = count.get(letter, 0)
            freq_tuple = tuple(freq_dict.values())

            if freq_tuple not in anagram_map:
                anagram_map[freq_tuple] = []
            anagram_map[freq_tuple].append(word)
            
        return list(anagram_map.values())
