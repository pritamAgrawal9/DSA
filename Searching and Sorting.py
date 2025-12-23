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
# for i in range(n):
#     min_num = nums[i]
#     ind = i
#     for j in range(i+1,n):
#         if nums[j] < min_num:
#             min_num = nums[j]
#             ind = j
#
#     temp = nums[i]
#     nums[i] = nums[ind]
#     nums[ind]=temp

# # Merge Sort
# def merge(nums,l,mid,r):
#         a=nums[l:mid+1]
#         b=nums[mid+1:r+1]
        # i,j,k=0,0,l
        # while k <= r:
        #     if j==len(b):
        #         nums[k] = a[i]
        #         i += 1
        #         k += 1
        #     elif i==len(a):
        #         nums[k] = b[j]
        #         j += 1
        #         k += 1
        #     elif a[i] < b[j]:
#                 nums[k] = a[i]
#                 i+=1
#                 k+=1
#             else:
#                 nums[k]=b[j]
#                 j+=1
#                 k+=1
# def merge_sort(nums,l,r):
#     if l>=r:
#         return
#     mid = (l+r)//2
#     merge_sort(nums,l,mid)
#     merge_sort(nums,mid+1,r)
#     merge(nums,l,mid,r)
# merge_sort(nums,0,len(nums)-1)
# print(nums)

# Quick Sort
def partition()