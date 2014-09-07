'''
Created on 6 Sep 2014

@author: podero

This script helps to scrap off images from twitpic into 
this service
'''

import urllib
import webapp2
import ops
import models
import base64
import os

from google.appengine.ext import db
from google.appengine.api import images

DIRECTORY = os.path.dirname(__file__)
_DEBUG = True

class ImageModel(db.Model):
    image_name = db.StringProperty()
    image_url = db.StringProperty(multiline=True)
    img = db.BlobProperty()


def image_key(image_name=None):
    return db.Key.from_path('Image', image_name or 'default_image')

class ScrapHandler(webapp2.RequestHandler):
    def get(self):       
        uploaded_image = ops.getImages()       
        for imag in uploaded_image:
            key = imag.image_name
            image = models.ImageModel(key_name = key)
            image.image_name = imag.image_name
            image.image_url = imag.image_url
            img = images.resize(urllib.urlopen(imag.image_url).read(), 32, 32)
            image.img = db.Blob(img)
            decodeimage = urllib.urlopen(imag.image_url)
            image.imageText = base64.b64encode(decodeimage.read())
            image.put()
            
            self.redirect('/?response=yes')

app = webapp2.WSGIApplication([ ('/scrap', ScrapHandler)],
                              debug=True)