#!/usr/bin/env python
# coding: utf-8

# In[3]:


import random
passwordlen = int(input("Enter Lenght of Password,You want to create:"))
pass_word = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"

#Now joining string
password = "".join(random.sample(pass_word,passwordlen))

#Now lets see the password
print(password)
                
        


# In[ ]:




