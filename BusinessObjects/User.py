from .Address import Address
from .Album import Album
from .ToDo import ToDo
from .Post import Post

class User(object):
    '''
    Represents a person.

    Attributes:
        id: The unique identifier for the User.
        name: The full name of the User.
        userName: The login username of the User.
        email: The User's email address.
        phone: The User's phone number.
        website: The User's personal website URL.
        address: An Address object that provides information about the User's
            place of residence.
        companyName: The name of the company that the User is employed by.
        companyCatchPhrase: The catch-phrase of the company that the User is
            employed by.
        companyBs: Some random baloney about the company that the User is
            employed by.
        albums: A list Album objects.
        toDos: A list ToDo objects.
        posts: A list Post objects.
    '''
    
    def __init__(self):
        '''
        Initializes User with default values.
        '''
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