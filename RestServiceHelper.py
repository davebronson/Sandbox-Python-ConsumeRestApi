import requests
import json

def getResponseAsJson(url):
    # Returns a JSON representation of the result of a REST web service call, given the service's URL
    
    # Get the service response
    response = requests.get(url)

    # If the request was successful...
    if response.status_code == 200:
        return json.loads(response.content.decode('utf-8'))

    # If the request was not successful...
    return None