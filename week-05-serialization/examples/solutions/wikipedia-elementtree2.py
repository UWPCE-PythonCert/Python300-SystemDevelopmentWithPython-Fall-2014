#!/usr/bin/env python

import bz2
from collections import defaultdict
import operator
import xml.etree.ElementTree as ET

from logging_config import logger

if __name__ == "__main__":
    fname = "data/enwiki-latest-pages-articles1.xml-p000000010p000010000-shortened.bz2"

    f = bz2.BZ2File(fname)

    tree = ET.parse(f)
    root = tree.getroot()
    
    seen = defaultdict(lambda: 0)

    namespaces = {'xmlns': 'http://www.mediawiki.org/xml/export-0.8/'}
    for title in root.findall('xmlns:page/xmlns:revision/xmlns:contributor/xmlns:username', namespaces=namespaces):
        seen[title.text] += 1

    for key, value in sorted(seen.iteritems(), key=operator.itemgetter(1)):
        logger.info("%s : %s" % (key, value))
