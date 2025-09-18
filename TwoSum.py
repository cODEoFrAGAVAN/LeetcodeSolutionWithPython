from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_map = {}
        for i, num in enumerate(nums):
            diff = target - num
            if diff in num_map:
                return [num_map[diff], i]
            num_map[num] = i


Length: int = int(input("Enter the length of the list\t"))
TargetValue: int = int(input("Enter the target value\t"))
InputList: list[int] = [
    int(input("Enter the values\t")) for _ in range(0, Length)
]
obj1 = Solution()
ReturnValue = obj1.twoSum(nums=InputList, target=TargetValue)
print(ReturnValue)
