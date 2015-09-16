import urllib.request
import xml.etree.ElementTree as ElementTree
import webbrowser
import threading
import collections

import sys
import os
import re
from bs4 import BeautifulSoup
import html.parser

SALESFORCE_APEX_DOC_URL_BASE = "http://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/"
SALESFORCE_VISUALFORCE_DOC_URL_BASE = "http://developer.salesforce.com/docs/atlas.en-us.pages.meta/pages/"
SALESFORCE_SERVICECONSOLE_DOC_URL_BASE = "http://developer.salesforce.com/docs/atlas.en-us.api_console.meta/api_console/"

def __get_serviceconsole_doc():
    sf_html = urllib.request.urlopen(urllib.request.Request(SALESFORCE_SERVICECONSOLE_DOC_URL_BASE,None,{"User-Agent": "Mozilla/5.0"})).read().decode("utf-8")
    page_soup = BeautifulSoup(sf_html, "html.parser")
    reference_soup = page_soup.find_all("span", text=re.compile("Methods for \w"), class_="toc-text")
    for reference in reference_soup:
        span_list = reference.parent.parent.parent.find_all("span", class_="toc-text", text=re.compile("^(?!Methods for)"))
        for span in span_list:
            print (span.string)
            

__get_serviceconsole_doc();

print("done")
