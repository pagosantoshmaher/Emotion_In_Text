#!/usr/bin/env python
# coding: utf-8

# In[2]:


#Import the modules
import text2emotion as te


# In[6]:


isears = open("/home/pago/Documents/face-to-face_interview/speech/text/92.txt", "r")


# In[8]:


#Call to the function
te.get_emotion(isears.read())


# In[10]:


import streamlit as st
# To make things easier later, we're also importing numpy and pandas for
# working with sample data.
import numpy as np
import pandas as pd


# In[ ]:




