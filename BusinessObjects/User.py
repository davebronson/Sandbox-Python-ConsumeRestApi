from .Address import Address
from .Album import Album
from .ToDo import ToDo
from .Post import Post

class User:
    def __init__(self):
        self.id = None
        self.name = None
        self.userName = None
        self.email = None
        self.phone = None
        self.website = None
        self.address = Address()
        self.companyName = None
        self.companyCatchPhrase = None
        self.companyBs = None

        # Collections
        self.albums = []
        self.toDos = []
        self.posts = []