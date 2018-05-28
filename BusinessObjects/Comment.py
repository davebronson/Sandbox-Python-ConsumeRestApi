class Comment(object):
    '''
    Represents a user comment on a blog Post.

    Attributes:
        id: The unique identifier for the Comment.
        postId: The ID of the Post that this Comment belongs to.
        name: The name of the person commenting.
        email: The email address of the person commenting.
        body: The full text of the Comment.
    '''
    
    def __init__(self):
        '''
        Initializes Comment with default values.
        '''
        self.id = None
        self.postId = None
        self.name = None
        self.email = None
        self.body = None