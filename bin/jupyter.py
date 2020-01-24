#!/usr/bin/env python
# coding: utf-8

# In[3]:


#jupyter notebook test
import matplotlib.pyplot as plt
import random
print("hello jupyter and git hub")


# In[10]:


x=[]
for i in range(1000):
    x.append(random.normalvariate(0,1) )

plt.hist(x,bins=50)
plt.show()











