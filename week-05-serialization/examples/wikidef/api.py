import bz2
import json
import urllib
import urllib2

import xml.etree.ElementTree as ET

from article import Article

class ParseError(Exception):
    pass

class Wikipedia(object):
    """Wikipedia API interface"""

    api_endpoint = "http://en.wikipedia.org/w/api.php?"

    @classmethod
    def article(cls, title):
        """Return contents of article

        arguments:

        title -- title of article
        """
        query_params = urllib.urlencode({'action': 'parse', 'format': 'json', 'prop':'text', 'page': title})
        url = cls.api_endpoint + query_params
        response = urllib2.urlopen(url)
        json_response = json.load(response)
        try:
            contents = json_response['parse']['text']['*']
        except KeyError:
            raise ParseError(json_response)

        return contents

class WikipediaStatic(object):

    @classmethod
    def article(cls, title):
        fname = "data/enwiki-latest-pages-articles1.xml-p000000010p000010000-shortened.bz2"

        f = bz2.BZ2File(fname)

        tree = ET.parse(f)
        root = tree.getroot()

        namespaces = {'xmlns': 'http://www.mediawiki.org/xml/export-0.8/'}
        for page in root.findall('xmlns:page', namespaces=namespaces):

            title_element = page.find('xmlns:title', namespaces=namespaces)
            body_element = page.find('xmlns:revision/xmlns:text', namespaces=namespaces)

            if title_element.text == title:
                return Article(title=title_element.text, body=body_element.text)