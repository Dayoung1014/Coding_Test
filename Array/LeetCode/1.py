from typing import List

#브루트 포스 O(n^2)
'''
def twoSum(self, nums: List[int], target: int) -> List[int]:
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]
'''

# in 사용 O(n)
def twoSum(self, nums: List[int], target: int) -> List[int]:
    for i in range(len(nums)):
        complement = target - nums[i]
        if complement in nums[i + 1:]:
            return [i, nums[i + 1:].index(complement) + (i + 1)]



# 딕셔너리 사용 (전체 : O(n), 딕셔너리 시간 복잡도 O(1)
'''
def twoSum(self, nums: List[int], target: int) -> List[int]:
    nums_map = {}
    for i, num in enumerate(nums):
        nums_map[num] = i

    for i, num in enumerate(nums):
        if target - num in nums_map and i != nums_map[target - num]:
            return [i, nums_map[target - num]]
'''