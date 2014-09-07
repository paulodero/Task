'''
Created on 6 Sep 2014

@author: podero
'''

from google.appengine.ext import db


#This entity type will act as a cache for the urls from twitpic 
#in order not to request for them again during image scrapping
class  UrlCache(db.Model):
    image_name = db.StringProperty()
    image_url = db.StringProperty()
    image_active = db.BooleanProperty()
    file_type = db.StringProperty()
    
#Will contain the images scrapped off from the service    
class ImageModel(db.Model):
    image_name = db.StringProperty()   
    file_type = db.StringProperty() 
    imageText = db.TextProperty()
