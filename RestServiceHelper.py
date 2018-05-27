import requests
import json

def getResponseAsObject(url):
    """
    Returns a Python object representation of the JSON result of a REST web service call, given the service's URL.

    Args:
        url: The URL to retrieve a response from.
    
    Returns:
        A Python object representation of the JSON response received from the REST web service.
    """
    
    # Get the service response
    response = requests.get(url)

    # If the request was successful...
    if response.status_code == 200:
        return json.loads(response.content.decode('utf-8'))

    # If the request was not successful...
    return None