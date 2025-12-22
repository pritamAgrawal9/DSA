# Bubble Sort
nums = [3,2,8,1,7,6,4]
n = len(nums)
i=j=0
while i < n:
    is_swap = False
    while j < n-i-1:
        if nums[j] > nums[j+1]:
            t = nums[j]
            nums[j] = nums[j+1]
            nums[j+1] = t
            is_swap=True
        j += 1
    if not is_swap:
        break
    j=0
    i += 1
print(nums)

# Insertion Sort