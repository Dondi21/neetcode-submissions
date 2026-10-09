class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set() # Unordered, unindexed and unchangable data type
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False