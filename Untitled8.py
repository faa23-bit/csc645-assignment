#!/usr/bin/env python
# coding: utf-8

# In[1]:


def binary_search(arr, target):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

arr = [3, 7, 11, 15, 19, 23, 27, 31, 38, 45]
targets = [23, 5, 38]
for target in targets:
    result = binary_search(arr, target)
    if result != -1:
        print(f"{target} found at index {result}")
    else:
        print(f"{target} not found")


# In[ ]:




