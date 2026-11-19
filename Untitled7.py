#!/usr/bin/env python
# coding: utf-8

# In[1]:


def binary_search(arr, target, low, high):
    if low > high:
        return -1
    mid = (low + high) // 2
    print("low =", low, "high =", high, "mid =", mid, "A[mid] =", arr[mid])
    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search(arr, target, mid + 1, high)
    else:
        return binary_search(arr, target, low, mid - 1)

arr = [2, 6, 10, 14, 18, 22, 30, 36, 40, 50, 55, 60]
target = 30
result = binary_search(arr, target, 0, len(arr) - 1)
print("Target found at index:", result)


# In[ ]:




