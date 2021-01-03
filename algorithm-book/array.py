def twoSum(nums, target):
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target:
                return print([i,j])


def twoSum(nums, target):
    for i,n in enumerate(nums):
        complement = target - n

        if complement in nums[i + 1 :]:
            return nums.index(n), nums[i+i: ].index(complement) + (i+1)

def twoSum(nums,target):
    nums_map ={}
    for i,num in enumerate(nums):
        nums_map[num] = i

    for i, num in enumerate(nums):
        if target - num in nums_map and i!=nums_map[target-num]:
            return nums.index(num), nums_map[target-num]


def twoSum(nums, target):
    nums_map = {}
    for i,num in enumerate(nums):
        if target -num in nums_map:
            return [nums_map[target - num], i]
        nums_map[num] = i


nums = [2,7,11,15]
target = 9
twoSum(nums, target)