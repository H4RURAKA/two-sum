from typing import List

def twoSum(self, nums: List[int], target: int) -> List[int]:

    visit_nums = {}

    for i, num in enumerate(nums) :
        gap = target - num
        if gap in visit_nums :
            return [visit_nums[gap], i]
        visit_nums[num] = i
    
    return
