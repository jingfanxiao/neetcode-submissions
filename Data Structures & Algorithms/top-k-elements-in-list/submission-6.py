from collections import defaultdict
from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # 1. 必须是 int，代表初始计数为 0
        count = defaultdict(int) 
        
        for num in nums:
            count[num] += 1
            
        # 2. 排序（你这一句写得非常标准，很棒）
        sorted_items = sorted(count.items(), key=lambda x: x[1], reverse=True)
        
        # 3. 提取前 k 个
        result = []
        for i in range(k):
            result.append(sorted_items[i][0]) 
            
        return result