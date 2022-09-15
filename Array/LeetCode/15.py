class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()
        print(nums)

        for i in range(len(nums) - 2):
            # 중복 값(이전에 확인했음) 건너뛰기
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            left = i + 1
            right = len(nums) - 1
            while left < right:
                sumNum = nums[i] + nums[left] + nums[right]
                print(i, left, right, sumNum)
                if sumNum < 0:
                    left += 1
                elif sumNum > 0:
                    right -= 1
                else:  # 0인 경우 정답
                    result.append([nums[i], nums[left], nums[right]])
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1

                if left == len(nums) - 1:
                    break

        return result

