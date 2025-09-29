#!/usr/bin/env python
# coding: utf-8

# In[1]:


def recursive_inner_plus(input_list):

    def helper(cur, depth):
      
        if all(not isinstance(x, list) for x in cur):
            return cur, depth


        best_list, best_depth = [], -1
        for item in cur:
            if isinstance(item, list):
                cand_list, cand_depth = helper(item, depth + 1)
                if cand_depth > best_depth:
                    best_list, best_depth = cand_list, cand_depth
        return best_list, best_depth

    innermost, _ = helper(input_list, 0)
    return [n + 1 for n in innermost]

print(recursive_inner_plus([1,[2,[3,[4]]]]))




# In[ ]:




