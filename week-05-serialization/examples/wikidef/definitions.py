from api import Wikipedia, WikipediaStatic

class Definitions(object):

    @classmethod
    def article(cls, title):
        response = WikipediaStatic.article(title)
        return response
