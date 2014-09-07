'''
Created on 6 Sep 2014

@author: podero

This script helps to scrap off images from twitpic into 
this service
'''
import ops
import os
import webapp2




DIRECTORY = os.path.dirname(__file__)
_DEBUG = True

class ScrapHandler(webapp2.RequestHandler):
    def get(self):       
        uploaded_image = ops.getImages()
        ops.addImages(uploaded_image)                   
        self.redirect('/?response=yes')

app = webapp2.WSGIApplication([ ('/scrap', ScrapHandler)],
                              debug=True)