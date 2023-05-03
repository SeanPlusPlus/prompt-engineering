#!/usr/bin/env python
# coding: utf-8

# In[1]:


import openai


# In[2]:


import os


# In[3]:


from dotenv import load_dotenv


# In[4]:


load_dotenv()


# In[5]:


OPENAI_API_KEY=os.getenv('OPENAI_API_KEY')


# In[6]:


openai.api_key = OPENAI_API_KEY


# In[7]:


def get_completion(prompt, model="gpt-3.5-turbo"):
    messages = [{"role": "user", "content": prompt}]
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=0,
    )
    return response.choices[0].message["content"]

