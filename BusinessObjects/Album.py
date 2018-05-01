from .Photo import Photo

class Album:
    def __init__(self):
        self.id = None
        self.userId = None
        self.title = None

        # Collections
        self.photos = []