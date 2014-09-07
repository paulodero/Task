'''
Created on 6 Sep 2014

@author: podero

This file contains some important functions used 
'''
import json
import urllib2
import urllib
import base64
import HTMLParser
import models


def scrapImages():

    h = HTMLParser.HTMLParser()
    max_length = 20
    pictures = []
    
    twitpic_api = "http://api.twitpic.com/2/users/show.json?username=rootpablo&page=1"

    twitpic_data = json.load(urllib2.urlopen(twitpic_api))

    twitpic_images = twitpic_data["images"]
    
    resetUrls()
    
    for item in twitpic_images:
        twitpic_id = item['short_id']
        twitpic_title = item["message"]
        twitpic_title = twitpic_title.replace('/', u'\u2044')
        twitpic_title = twitpic_title[:max_length]
        twitpic_file_type = item["type"]
        twitpic_file_url = "http://twitpic.com/show/full/"+twitpic_id
        twitpic_file_name= h.unescape(twitpic_title.replace(" ", "")) + "." + twitpic_file_type
        twitpic_file_name = twitpic_file_name
        pictures.append(twitpic_file_url)
        addUrl(twitpic_file_name, twitpic_file_url,twitpic_file_type)
    return pictures

def resetUrls():
    q = models.UrlCache().all()
    for row in q:
        row.image_active = False
        row.put()
    
def addUrl(image_name,image_url,twitpic_file_type):
    key = image_name
    row = models.UrlCache(key_name = key)
    row.image_name = image_name
    row.image_url = image_url
    row.image_active = True
    row.file_type = twitpic_file_type
    row.put()

def getImages():
    q = models.UrlCache().all().filter('image_active =', True)
    row = q.fetch(6)
    return row

def getImage(count):
    q = models.ImageModel().all()
    row = q.fetch(int(count))
    return row

def defaultValues():
    return  {
              }   
def addImages(uploaded_image):
    for imag in uploaded_image:
        key = imag.image_name
        image = models.ImageModel(key_name = key)
        image.image_name = imag.image_name
        image.file_type = imag.file_type
        decodeimage = urllib.urlopen(imag.image_url)
        image.imageText = base64.b64encode(decodeimage.read())
        image.put()