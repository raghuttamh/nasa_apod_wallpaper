#py_file
#Only for Linux
import json
import urllib.request
import os

os.system('export GIO_EXTRA_MODULES=/usr/lib/x86_64-linux-gnu/gio/modules/')

#with urllib.request.urlopen("http://www.python.org") as url:
url = urllib.request.urlopen('https://api.nasa.gov/planetary/apod?api_key=guvojFkM3uqbvnSTlidKDlMhGY1g3QeiNQkXn19G')
urlj = json.load(url)

if urlj['media_type'] == 'image':
	urllib.urlretrieve(urlj['hdurl'],'/home/raghuttam/apod_img.jpg')
	#where "/home/raghuttam/apod_img" the image path.. that might change for each system
	print(urlj['title'])
else:
	print("The image is unavailable today as the server has uploaded a "+urlj['media_type'])

os.system('export GIO_EXTRA_MODULES=/usr/lib/x86_64-linux-gnu/gio/modules/')
os.system('gsettings set org.gnome.desktop.background picture-uri file:///home/raghuttam/apod_img.jpg')
#where "/home/raghuttam/apod_img" the image path.. that might change for each system
