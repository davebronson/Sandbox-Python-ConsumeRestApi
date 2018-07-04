import json
import RestServiceHelper

from BusinessObjects.Address import Address
from BusinessObjects.Album import Album
from BusinessObjects.Comment import Comment
from BusinessObjects.Photo import Photo
from BusinessObjects.Post import Post
from BusinessObjects.ToDo import ToDo
from BusinessObjects.User import User

# https://jsonplaceholder.typicode.com << Faked REST service
# https://github.com/typicode/json-server << Details on querying the faked REST service
# http://google.github.io/styleguide/pyguide.html << Google's Python style guide

# TODO Use a Main()

userList = []

# Retrieve data from the REST service
users = RestServiceHelper.getResponseAsObject('https://jsonplaceholder.typicode.com/users?_sort=username&_order=asc')
todos = RestServiceHelper.getResponseAsObject('https://jsonplaceholder.typicode.com/todos?_sort=userId,title&_order=asc,asc')
posts = RestServiceHelper.getResponseAsObject('https://jsonplaceholder.typicode.com/posts?_sort=userId,title&_order=asc,asc')
comments = RestServiceHelper.getResponseAsObject('https://jsonplaceholder.typicode.com/comments?_sort=postId,name&_order=asc,asc')
albums = RestServiceHelper.getResponseAsObject('https://jsonplaceholder.typicode.com/albums?_sort=userId,title&_order=asc,asc')
photos = RestServiceHelper.getResponseAsObject('https://jsonplaceholder.typicode.com/photos?_sort=albumId,title&_order=asc,asc')

# Process Users
# *************
foundUser = None

for item in users:
    user = User()

    user.id = item['id']
    user.name = item['name']
    user.userName = item['username']
    user.email = item['email']
    user.phone = item['phone']
    user.website = item['website']
    user.companyName = item['company']['name']
    user.companyCatchPhrase = item['company']['catchPhrase']
    user.companyBs = item['company']['bs']

    user.address.id = 0 #  No ID provided
    user.address.userId = user.id
    user.address.street = item['address']['street']
    user.address.suite = item['address']['suite']
    user.address.city = item['address']['city']
    user.address.zipCode = item['address']['zipcode']
    user.address.geoLatitude = item['address']['geo']['lat']
    user.address.geoLongitude = item['address']['geo']['lng']

    userList.append(user)


# Process ToDos
# *************
foundUser = None

for item in todos:
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


# Process Posts
# *************
foundUser = None

for item in posts:
    post = Post()

    post.id = item['id']
    post.userId = item['userId']
    post.title = item['title']
    post.body = item['body']

    # Append Comments for this Post
    postsComments = [x for x in comments if x['postId'] == post.id]
    for c in postsComments:
        comment = Comment()

        comment.id = c['id']
        comment.postId = c['postId']
        comment.name = c['name']
        comment.email = c['email']
        comment.body = c['body']

        post.comments.append(comment)

    # Find the Post's user, and append
    if foundUser is None or post.userId != foundUser.id:
        foundUser = next((x for x in userList if x.id == post.userId), None)
    if foundUser is not None:
        foundUser.posts.append(post)


# Process Albums
# **************
foundUser = None

for item in albums:
    album = Album()

    album.id = item['id']
    album.userId = item['userId']
    album.title = item['title']

    # Append Photos for this Album
    albumsPhotos = [x for x in photos if x['albumId'] == album.id]
    for p in albumsPhotos:
        photo = Photo()

        photo.id = p['id']
        photo.albumId = p['albumId']
        photo.title = p['title']
        photo.url = p['url']
        photo.thumbnailUrl = p['thumbnailUrl']

        album.photos.append(photo)

    # Find the Album's user, and append
    if foundUser is None or album.userId != foundUser.id:
        foundUser = next((x for x in userList if x.id == album.userId), None)
    if foundUser is not None:
        foundUser.albums.append(album)