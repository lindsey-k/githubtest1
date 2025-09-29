#!/usr/bin/env python
# coding: utf-8

# In[4]:


def while_inner_plus(input_list):
    stack = [input_list]
    depth_stack = [0]
    innermost = []
    deepest = -1

    while len(stack) > 0:
        cur = stack.pop()
        d = depth_stack.pop()

        has_sub = False
        for x in cur:
            if isinstance(x, list):
                has_sub = True
                stack.append(x)
                depth_stack.append(d + 1)

        if not has_sub and d >= deepest:
            innermost = cur
            deepest = d

    result = []
    for n in innermost:
        result.append(n + 1)
    return result


if __name__ == "__main__":
    example = [1,2,3,4,[5,6,7,[8,9]]]
    print(while_inner_plus(example)) 


# In[ ]:




