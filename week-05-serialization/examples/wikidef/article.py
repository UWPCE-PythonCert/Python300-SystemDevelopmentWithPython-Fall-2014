import json

class Article(object):
    def __init__(self, title=None, body=None, authors=None):
        self.title = title
        self.body = body
        self.authors= authors

    def __str__(self):
        return json.dumps(self.__dict__)

