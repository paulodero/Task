'''
Created on 5 Sep 2014

@author: podero

This renders the initial page of the service.

Shows the images available in twitpic and gives an option to scrap them 
and dunp into the service
'''
import os
import ops
import webapp2
from google.appengine.ext.webapp import template
from settings import TEMPLATES_PATH

DIRECTORY = os.path.dirname(__file__)
_DEBUG = True
values = {}

from google.appengine.api import urlfetch
urlfetch.set_default_fetch_deadline(2000)


class LandingPage(webapp2.RequestHandler):
    def get(self):
        response = self.request.get('response',None)
        values = ops.defaultValues()
        values['images'] = ops.scrapImages()
        if response:
            values['response'] = 'Images have been scrapped from twitpic. You can now view them from '
            values['link'] = 'http://ibmtask.appspot.com/'
        else:
            values['response'] = 'The following images are displayed from twitpic.'
            values['link'] = ''
            
        wireframe = 'response'
        app_path = os.path.join(DIRECTORY, os.path.join('templates', '%s.html' % wireframe))
        values['app'] = template.render(app_path, values, debug=_DEBUG)
        path = os.path.join(TEMPLATES_PATH,'index.html')
        self.response.out.write(template.render(path, values, debug=_DEBUG))

app = webapp2.WSGIApplication([('/',LandingPage)],debug=True)