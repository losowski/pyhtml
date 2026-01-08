# Build HTML

# URL
#	https://docs.python.org/3/library/xml.etree.elementtree.html

import logging

# Encoding base
import xml.etree.ElementTree as ET
from . import html_base

class HTMLStyleSheet (html_base.HTMLBase):
	def __init__(self, filename):
		super().__init__("link")
		self.logger			=	logging.getLogger("HTMLStyleSheet")
		self.setAttrib("rel", "stylesheet")
		self.setAttrib("href", "$CDN/style/{name}.css".format(name = filename))


	def __del__(self):
		super().__del__()
