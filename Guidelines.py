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


def get_completion(prompt, model="gpt-3.5-turbo"):
    messages = [{"role": "user", "content": prompt}]
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=0,
    )
    return response.choices[0].message["content"]


# In[7]:


f = open("./static-electricity.txt", "r")


# In[8]:


lines = f.readlines()


# In[9]:


print(lines)


# In[11]:


text = lines[0]


# In[12]:


prompt = f"""Summarize the text delimited by triple backticks into a single sentence. ```{text}```"""


# In[14]:


openai.api_key = OPENAI_API_KEY


# In[15]:


response = get_completion(prompt)


# In[16]:


print(response)


# In[17]:


prompt = f"""Generate a list of 3 made-up book titles \
along with their authors and genres. Provide them in \
JSON format with the following keys: \
book_id, title, author, genre.
"""


# In[18]:


print(prompt)


# In[19]:


response = get_completion(prompt)


# In[20]:


print(response)

