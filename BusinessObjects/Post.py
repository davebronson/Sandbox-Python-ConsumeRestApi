from .Comment import Comment

class Post:
    def __init__(self):
        self.id = None
        self.userId = None
        self.title = None
        self.body = None

        # Collections
        self.comments = []