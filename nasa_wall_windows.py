
# coding: utf-8



#downloading image from the nasa api
import time
import urllib
import json
while True:
	
	url = urllib.urlopen("https://api.nasa.gov/planetary/apod?api_key=ScYKcOs02qj066LcwbxMfb5U5m5B64l0scazFTC9")
	urlj = json.load(url)
	if urlj['media_type'] == 'image':
		urllib.urlretrieve(urlj['hdurl'],'C:/Users/dell/Desktop/image.jpg')
		#where "/home/raghuttam/apod_img" the image path.. that might change for each system
	else:
		print("The image is unavailable today as the server has uploaded a "+urlj['media_type'])




#setting the picture to be the wallpaper
	import ctypes
	import os
	SPI_SETDESKWALLPAPER = 20 
	ctypes.windll.user32.SystemParametersInfoA(SPI_SETDESKWALLPAPER, 0, 'C:/Users/dell/Desktop/image.jpg', 3) 
	time.sleep(3600)
#'C:\\Users\\Public\\Pictures\\abc.jpg'

