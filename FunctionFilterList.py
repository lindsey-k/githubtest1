#!/usr/bin/env python
# coding: utf-8

# In[1]:


print("Advanced Function and Logic Assignment")


# In[2]:


def function_filter_list(nums, threshold):
    result = []
    for n in nums:
        if n <= threshold:
            result.append(n)
    return result

test_list = [1,2,3,4,5,6,7,8,9]
print(function_filter_list(test_list, 6))   


# In[ ]:




