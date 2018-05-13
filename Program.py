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

userList = []
foundUser = None

response = requests.get('https://jsonplaceholder.typicode.com/users')
if response.status_code == 200:
    responseAsJson = json.loads(response.content.decode('utf-8'))

    for item in responseAsJson:
        user = User()

        user.id = item['id']
        user.name = item['name']
        user.userName = item['username']
        user.email = item['email']
        user.phone = item['phone']
        user.website = item['website']

        user.address.street = item['address']['street']
        user.address.suite = item['address']['suite']
        user.address.city = item['address']['city']
        user.address.zipCode = item['address']['zipcode']
        user.address.suite = item['address']['suite']

        user.address.geoLatitude = item['address']['geo']['lat']
        user.address.geoLongitude = item['address']['geo']['lng']

        user.companyName = item['company']['name']
        user.companyCatchPhrase = item['company']['catchPhrase']
        user.companyBs = item['company']['bs']

        userList.append(user)

response = requests.get('https://jsonplaceholder.typicode.com/todos')
if response.status_code == 200:
    responseAsJson = json.loads(response.content.decode('utf-8'))

    for item in responseAsJson:
        todo = ToDo()

        todo.id = item['id']
        todo.userId = item['userId']
        todo.title = item['title']
        todo.completed = item['completed']

        # Find the ToDo's user, and append
        if foundUser is None or todo.userId != foundUser.id:
            foundUser = next((x for x in userList if x.id == todo.userId), None)
        if foundUser is not None:
            foundUser.toDos.append(todo)

    print(len(userList))
    print(len(userList[2].toDos))