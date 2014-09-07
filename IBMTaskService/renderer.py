'''
Created on 6 Sep 2014

@author: podero

This helps the service to provide an API to which the client makes calls.

The API sends back image strings encoded in base64

'''

import json
import webapp2
import ops


class RPCMethods:
    def Echo(self, params):
        number = params['number']
        images = ops.getImage(number)
        image_data = ''
        comma = False
        
        for image in images:
            if comma:
                image_data = image_data + ","
            comma = True
            image_data = image_data + image.imageText
        return image_data

  
class RPCHandler(webapp2.RequestHandler):
    def __init__(self, request=None, response=None):
        webapp2.RequestHandler.__init__(self, request, response)
        self.methods = RPCMethods()
        
    def get(self):
        self.post()
        
    def post(self):
        action = self.request.params['action']
        params = self.request.params['params']
        key = self.request.params['key']

        if not key or key != 'mySecretKey':
            self.error(404) 
            return
    
        if not action:
            self.error(404) 
    
        if action[0] == '_':
            self.error(403) 
            return
            
        func = getattr(self.methods, action, None)
    
        if not func:
            self.error(404) 
            return
    
        result = func(json.loads(params))
        self.response.out.write(json.dumps(result))


app = webapp2.WSGIApplication([('/rpc', RPCHandler)],
                              debug=True)
