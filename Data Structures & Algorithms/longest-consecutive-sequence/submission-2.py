class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
            
        nums.sort()  # C 语言底层极速排序
        longest = 1
        current_length = 1
        
        for i in range(1, len(nums)):
            # 如果和上一个数相等，直接跳过（去重）
            if nums[i] == nums[i-1]:
                continue
            # 如果刚好大 1，连续长度 +1
            elif nums[i] == nums[i-1] + 1:
                current_length += 1
            # 如果断层了（比如从 5 直接跳到 10），重新开始数
            else:
                longest = max(longest, current_length)
                current_length = 1  # 重置
                
        return max(longest, current_length)