'''
Created on 6 Sep 2014

@author: podero
'''

from google.appengine.ext import db

'''
This entity type will act as a cache for the urls from twitpic 

in order not to request for them again during image scrapping
'''
class  UrlCache(db.Model):
    image_name = db.StringProperty()
    image_url = db.StringProperty()
    
class ImageModel(db.Model):
    image_name = db.StringProperty()   
    image_url   = db.StringProperty() 
    img  = db.BlobProperty()
