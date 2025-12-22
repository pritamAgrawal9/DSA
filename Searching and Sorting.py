# Bubble Sort
nums = [3,2,8,1,7,6,4]
n = len(nums)
# i=j=0
# while i < n:
#     is_swap = False
#     while j < n-i-1:
#         if nums[j] > nums[j+1]:
#             t = nums[j]
#             nums[j] = nums[j+1]
#             nums[j+1] = t
#             is_swap=True
#         j += 1
#     if not is_swap:
#         break
#     j=0
#     i += 1
# print(nums)

# Insertion Sort
# for i in range(1,n):
#     key=nums[i]
#     j = i-1
#     while j>=0 and nums[j]>key: # 3 2 8 1 7 6 4
#         nums[j+1]=nums[j]
#         j-=1
#         nums[j+1]=key
# print(nums)

# Selection Sort
for i in range(n):
    min_num = nums[i]
    ind = i
    for j in range(i+1,n):
        if nums[j] < min_num:
            min_num = nums[j]
            ind = j

    temp = nums[i]
    nums[i] = nums[ind]
    nums[ind]=temp
