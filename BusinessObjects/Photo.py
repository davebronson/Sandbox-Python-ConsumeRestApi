class Photo(object):
    '''
    Represents digital photographic image.

    Attributes:
        id: The unique identifier for the Photo.
        albumId: The ID of the Album that this Photo belongs to.
        title: A short description for the Photo.
        url: The internet address that points at the Photo image.
        thumbnailUrl: The internet address that points at the small thumbnail of the Photo image.
    '''
    
    def __init__(self):
        '''
        Initializes Photo with default values.
        '''
        self.id = None
        self.albumId = None
        self.title = None
        self.url = None
        self.thumbnailUrl = None