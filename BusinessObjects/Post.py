from .Comment import Comment

class Post(object):
    '''
    Represents a blog Post belonging to a User.

    Attributes:
        id: The unique identifier for the Post.
        userId: The ID of the User that this Post belongs to.
        title: A headline or short description for the Post.
        body: The full text of the Post.
        comments: A list Comment objects that belong to the Post.
    '''
    
    def __init__(self):
        '''
        Initializes Post with default values.
        '''
        self.id = None
        self.userId = None
        self.title = None
        self.body = None

        # Collections
        self.comments = []