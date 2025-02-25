#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip3 install pyttsx3')


# In[ ]:


import pyttsx3
engine = pyttsx3.init()  
engine.say("Hello, how are you?")
engine.runAndWait()


# In[ ]:


text = [
    'This is introduction to NLP',
    'It is likely to be useful to people',
    'Machine learning is the new electricity',
    'There would be less hype around AI and more action going forward',
    'Python is the best tool',
    'R is a good language',
    'I want more books like this'
]


# In[ ]:


engine = pyttsx3.init()
engine.say(text)
engine.runAndWait()


# In[ ]:


import pyttsx3

# Object creation
engine = pyttsx3.init()

# **RATE**
rate = engine.getProperty('rate')  # Getting details of current speaking rate
print("Current speaking rate:", rate)

# Setting up a new voice rate
engine.setProperty('rate', 150)

# **VOLUME**
volume = engine.getProperty('volume')  # Getting current volume level (min=0 and max=1)
print("Current volume level:", volume)

# Setting up volume level between 0 and 1
engine.setProperty('volume', 1.0)

# **VOICE**
voices = engine.getProperty('voices')  # Getting details of current voices

# Changing the voice (0 for male, 1 for female)
engine.setProperty('voice', voices[1].id)  # 1 = Female voice

# Speaking the text
engine.say("Hello World!")
engine.say("My current speaking rate is " + str(rate))
engine.say("My current speaking volume is " + str(volume))

engine.runAndWait()


# In[ ]:


get_ipython().system('pip install goslate')


# In[ ]:


import goslate


# In[ ]:


gs = goslate.Goslate()
translatedText = gs.translate(text,'en')
print(translatedText)


# In[ ]:


get_ipython().system('pip install translate')


# In[ ]:


##translating text to telugu
from translate import Translator
translator= Translator(to_lang="te")
translation = translator.translate("who are you? I AM saketh")
translation


# In[ ]:




