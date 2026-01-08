# Build HTML

# URL
#	https://docs.python.org/3/library/xml.etree.elementtree.html

import logging

# Encoding base
import xml.etree.ElementTree as ET
from . import html_base

class HTMLTitle (html_base.HTMLBase):
	def __init__(self, title):
		super().__init__("title")
		self.logger			=	logging.getLogger("HTMLTitle")
		self.setValue(title)

	def __del__(self):
		super().__del__()
