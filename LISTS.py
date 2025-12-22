import math

list1=[1,2,3]
list2=list1 # deep copy it means that the variable "list2" will point to same address or to list1,
# there is no new variable created instead we have new name to list1.
# print(list1,id(list1))
# print(list2,id(list2))

list3=[5,6,7]
list4=list3.copy() # this is shallow copy it creates a copy of list3, and we have list4 as copy of list3.
# print(list3,id(list3))
# print(list4,id(list4))

# THERE IS DIFFERENCE BETWEEN 'SUBARRAY' -> continuous part of an array like subset whole array can be a subarray.
# 'SUBSEQUENCE' -> non-continuous part.

#1480 Running sum of 1d array (prefix sum)
# nums = [1,2,3,4]
# ot= [nums[0]]
# for i in range(1,len(nums)):
#     x = ot[i-1] + nums[i]
#     ot.append(x)
# print(ot)

#26 Removing duplicates in sorted array
# nums=[3,3,5,7,7,7,7,9,9,9,12,12]
# start=0
# for i in range(1, len(nums)):
#     if nums[i] != nums[start]:
#         start+=1
#         nums[start] = nums[i]
# nums=nums[:start+1]
#
# print(start+1)

def gcd(a, b):
    while b:
        a=b # a,b = b, a%b
        b=a%b
    return a











