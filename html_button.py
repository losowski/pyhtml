# Build HTML

# URL
#	https://docs.python.org/3/library/xml.etree.elementtree.html

import logging

# Encoding base
import xml.etree.ElementTree as ET
from . import html_base


class HTMLButton (html_base.HTMLBase):
	def __init__(self, className):
		super().__init__("button")
		self.logger			=	logging.getLogger("HTMLButton")
		self.setClass(className)


	def __del__(self):
		super().__del__()
