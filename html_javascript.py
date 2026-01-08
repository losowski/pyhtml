# Build HTML

# URL
#	https://docs.python.org/3/library/xml.etree.elementtree.html

import logging

# Encoding base
import xml.etree.ElementTree as ET
from . import html_base

class HTMLJavaScript (html_base.HTMLBase):
	def __init__(self, filename):
		super().__init__("script")
		self.logger			=	logging.getLogger("HTMLJavaScript")
		self.setAttrib("src", "$CDN/script/{name}.js".format(name = filename))

	def __del__(self):
		super().__del__()
