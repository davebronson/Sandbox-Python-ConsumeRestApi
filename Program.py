import requests
import json

from BusinessObjects.Address import Address
from BusinessObjects.Album import Album
from BusinessObjects.Comment import Comment
from BusinessObjects.Photo import Photo
from BusinessObjects.Post import Post
from BusinessObjects.ToDo import ToDo
from BusinessObjects.User import User

# https://code.tutsplus.com/articles/how-to-use-restful-web-apis-in-python--cms-29493
# https://jsonplaceholder.typicode.com

response = requests.get('https://jsonplaceholder.typicode.com/posts?userId=1')

if response.status_code == 200:
    responseAsJson = json.loads(response.content.decode('utf-8'))
    for item in responseAsJson:
        print(item["title"])