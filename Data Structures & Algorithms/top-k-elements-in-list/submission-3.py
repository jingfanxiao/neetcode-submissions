from collections import defaultdict
from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)
        for num in nums:
            count[num]+=1
        sorted_items = sorted(count.items(), key=lambda x: x[1], reverse=True)
        result = []
        for i in range(k):
            result.append(sorted_items[i][0]) 
            
        return result
