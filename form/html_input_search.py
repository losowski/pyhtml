# Build HTML

# URL
#	https://docs.python.org/3/library/xml.etree.elementtree.html
#	https://www.programiz.com/html/input

import logging

# Encoding base
import xml.etree.ElementTree as ET
from .. import html_input

## HTMLInputSearch
class HTMLInputSearch html_input.HTMLInputBase):
	def __init__(self, name):
		super().__init__(html_input.HTMLInputBase.SEARCH, name)
		self.logger				=	logging.getLogger("HTMLInputSearch")
		# Components
		self.setId(name)

	def __del__(self):
		super().__del__()
