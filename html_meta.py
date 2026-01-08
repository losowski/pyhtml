# Build HTML

# URL
#	https://docs.python.org/3/library/xml.etree.elementtree.html

import logging

# Encoding base
import xml.etree.ElementTree as ET
from . import html_base

class HTMLMeta (html_base.HTMLBase):
	def __init__(self, key, value):
		super().__init__("meta")
		self.logger			=	logging.getLogger("HTMLMeta")
		self.setAttrib("name", key)
		self.setAttrib("content", value)

	def __del__(self):
		super().__del__()
