from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []

        # 왼쪽값 곱셈
        left = 1
        for i in range(0, len(nums)):
            res.append(left)
            left = left * nums[i]

        # res에 오른쪽값 곱셈
        right = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] = res[i] * right
            right = right * nums[i]

        return res