# Bubble Sort
nums = [3,2,8,1,7,6,4]
n = len(nums)
i=j=0
while i < n:
    while j < n-i-1:
        if nums[j] > nums[j+1]:
            t = nums[j]
            nums[j] = nums[j+1]
            nums[j+1] = t
        j += 1
    j=0
    i += 1
print(nums)