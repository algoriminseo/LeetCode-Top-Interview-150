class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_map = {}
        result = []
        for num in nums:
            freq_map[num] = freq_map.get(num, 1) + 1
        
        while k != 0:
            max_val = max(freq_map.values())
            max_key = max(freq_map, key= freq_map.get)
           
            result.append(max_key)
            freq_map.pop(max_key)
            k -= 1
        return result

        