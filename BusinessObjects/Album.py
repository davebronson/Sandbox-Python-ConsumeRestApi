from .Photo import Photo

class Album(object):
    '''
    Represents a collection of related Photos belonging to a User.

    Attributes:
        id: The unique identifier for the Album.
        userId: The ID of the User that this Album belongs to.
        title: A short description for the Album.
        photos: A list Photo objects.
    '''

    def __init__(self):
        '''
        Initializes Album with default values.
        '''
        self.id = None
        self.userId = None
        self.title = None

        # Collections
        self.photos = []