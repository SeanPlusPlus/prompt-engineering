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


# In[11]:


text = f"""
Static electricity is a type of electric charge that is produced when two objects rub against each other and electrons transfer from one object to the other. These objects can be anything from your hair and a balloon to your clothes and the carpet. When this happens, one object becomes positively charged because it lost some electrons, and the other object becomes negatively charged because it gained some electrons. The resulting charge imbalance creates a build-up of potential energy, which can discharge as a spark or shock when the charged object comes into contact with a conductor, like a doorknob or another person. This is why you may sometimes feel a shock when you touch a metal object after walking across a carpeted floor. Overall, static electricity is a natural phenomenon that occurs when certain materials interact with each other and can be observed in many everyday situations.
"""
prompt = f"""
Summarize the text delimited by triple backticks into a single sentence. ```{text}```
"""
response = get_completion(prompt)
print(response)

