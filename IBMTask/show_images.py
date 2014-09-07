'''
Created on 6 Sep 2014

@author: podero
'''

import urllib
import urllib2
import webapp2
import os

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
                "params": '{"number":"5"}',
                "key": "mySecretKey"
        })
        response = urllib2.urlopen(url, params).read() 
        
        image_data = response[1:-1]    
        image_data = image_data.split(',')
        displayImages = []
        for imageString in image_data:
            displayImages.append(imageString)
        
        values = defaultValues()
        values['displayImages'] = displayImages
        values['length'] = len(displayImages)
        wireframe = 'index'
        app_path = os.path.join(DIRECTORY, os.path.join('templates', '%s.html' % wireframe))
        values['app'] = template.render(app_path, values, debug=_DEBUG)
        path = os.path.join(TEMPLATES_PATH,'index.html')
        self.response.out.write(template.render(path, values, debug=_DEBUG))

def defaultValues():
    return  {
              }      
     
app = webapp2.WSGIApplication([ ('/.*', ShowImagesHandle)],
                              debug=True)