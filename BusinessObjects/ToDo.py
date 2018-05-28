class ToDo(object):
    '''
    Represents a statused task belonging to a User.

    Attributes:
        id: The unique identifier for the ToDo.
        userId: The ID of the User that this ToDo belongs to.
        title: A headline or short description for the ToDo.
        completed: a boolean value that indcated whether the ToDo is in a
            completed state.
    '''
    
    def __init__(self):
        '''
        Initializes ToDo with default values.
        '''
        self.id = None
        self.userId = None
        self.title = None
        self.completed = False