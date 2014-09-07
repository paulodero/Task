Task
====

Solution
There solution has been developed in two different layers. There is the service and the client.

The service is deployed at http://ibmtask-service.appspot.com/
The client is deployed at http://ibmtask.appspot.com/ 

The service displays images found on twitpic and gives the user an option to scrap them off twitpic into the service datastore. The service them serves the pictures through an API accessed through 
http://ibmtask-service.appspot.com/rpc?action=Echo&params={“number”:”3”}&key=mySecretKey 

Parameters: 
action: is the function being called
params: parameters passed to the function. It is in key, value format. The parameter number specifies the number of images to be retrieved.
Response:
The API sends back a response in string format. A list of strings is sent back. These strings represents the images in base64 format. 

The client sends this request to the API and and receives back the strings. The client then uses this images strings which have been converted into base64 to set the src for <img > tag in html to display images.

Both the service and the client uses boostrap to render interface. 
