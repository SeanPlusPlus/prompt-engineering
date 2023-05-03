#!/usr/bin/env python
# coding: utf-8

# In[1]:


import openai


# In[2]:


import os


# In[ ]:


openai.api_key = ""


# In[7]:


print('hello')


# In[8]:


openai.api_key = os.getenv('OPENAI_API_KEY')


# In[10]:


def get_completion(prompt, model="gpt-3.5-turbo"):
    messages = [{"role": "user", "content": prompt}]
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=0,
    )
    return response.choices[0].message["content"]

