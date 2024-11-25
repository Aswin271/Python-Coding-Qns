def maxSubArray(nums):
    cur_sum = 0
    max_sum = float('-inf')
    n = len(nums)
    
    for i in range(n):
        cur_sum += nums[i]
        max_sum = max(max_sum , cur_sum)
        if cur_sum < 0:
            cur_sum = 0
    
    return max_sum

nums = [1,2,3,4,5,6,7,8,9]
print(maxSubArray(nums))        