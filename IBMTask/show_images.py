'''
Created on 6 Sep 2014

@author: podero

This script sends a post request to the service API

It receives images inform of strings which have been encoded using base64 as a response

It then sends these encoded images to be rendered in the html page

The 
'''

import urllib
import urllib2
import webapp2
import os
import json

from google.appengine.api import urlfetch
from google.appengine.ext.webapp import template
from settings import TEMPLATES_PATH

urlfetch.set_default_fetch_deadline(2000)

DIRECTORY = os.path.dirname(__file__)
_DEBUG = True

class ShowImagesHandle(webapp2.RequestHandler):
    def get(self):
        url = 'http://ibmtask-service.appspot.com/rpc'
        params = urllib.urlencode({
                "action": "Echo",
                "params": '{"number":"6"}',
                "key": "mySecretKey"
        })
        response = urllib2.urlopen(url, params).read() 
        
        image_data = json.loads(response)
        displayImages = []
        for imageDict in image_data:
            dictionary = {}
            dictionary['image'] = imageDict['image']
            dictionary['file_type'] = imageDict['file_type']
            displayImages.append(dictionary)
        
        values = defaultValues()
        values['displayImages'] = displayImages
        wireframe = 'gallery'
        app_path = os.path.join(DIRECTORY, os.path.join('templates', '%s.html' % wireframe))
        values['app'] = template.render(app_path, values, debug=_DEBUG)
        path = os.path.join(TEMPLATES_PATH,'index.html')
        self.response.out.write(template.render(path, values, debug=_DEBUG))

def defaultValues():
    return  {
              }      
     
app = webapp2.WSGIApplication([ ('/.*', ShowImagesHandle)],
                              debug=True)