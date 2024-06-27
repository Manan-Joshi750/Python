def max_subarray(nums):
    max_sum = current_sum = nums[0]
    start = end = s = 0

    for i in range(1, len(nums)):
        if nums[i] > current_sum + nums[i]:
            current_sum = nums[i]
            s = i # Update the starting index of the current subarray
        else:
            current_sum += nums[i]
        
        if current_sum > max_sum:
            max_sum = current_sum
            start = s # Update the start of the max subarray
            end = i # Update the end of the max subarray

    return max_sum, nums[start:end+1]

nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
max_sum, subarray = max_subarray(nums)
print(f"Maximum subarray sum: {max_sum}")
print(f"Maximum subarray: {subarray}")