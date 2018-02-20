
# coding: utf-8

# In[1]:


import urllib
import json
url = urllib.urlopen("https://api.nasa.gov/planetary/apod?api_key=ScYKcOs02qj066LcwbxMfb5U5m5B64l0scazFTC9")
urlj = json.load(url)
urllib.urlretrieve(urlj['hdurl'],"C:/Users/dell/Desktop/image.jpg")


# In[2]:


import ctypes
import os
SPI_SETDESKWALLPAPER = 20 
ctypes.windll.user32.SystemParametersInfoA(SPI_SETDESKWALLPAPER, 0, 'C:/Users/dell/Desktop/image.jpg', 3) 
#'C:\\Users\\Public\\Pictures\\abc.jpg'

