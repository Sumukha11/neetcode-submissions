class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        result = []
        
        for num in nums:    
            count[num] = count.get(num, 0) + 1
        sort = sorted(count.items(), key=lambda item: item[1], reverse=True)

        for i in range(k):
            current_tuple = sort[k-1-i]
            result.append(current_tuple[0])
        return result