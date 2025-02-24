    

class Solution:


    def hIndex(self, citations: List[int]) -> int:
        citations.sort()
        length = len(citations)

        for i , citation in enumerate(citations):
            if citation >= length - i:
                return length - i 
        
        return 0 