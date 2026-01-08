# Build HTML

# URL
#	https://docs.python.org/3/library/xml.etree.elementtree.html

import logging

# Encoding base
import xml.etree.ElementTree as ET
from . import html_build_base
from . import encode_base

# BReak
class HTMLBR (encode_base.EncodeBase):
	def __init__(self):
		self.logger			=	logging.getLogger("HTMLBR")
		super().__init__("br")

	def __del__(self):
		super().__del__()


# ORIGINAL DIV
class HTMLDiv (html_build_base.HTMLBuildBase):
	def __init__(self, className):
		super().__init__("div")
		self.logger			=	logging.getLogger("HTMLDiv")
		self.setClass(className)

	def __del__(self):
		super().__del__()


	def appendObject(self, parentObj):
		self.appendElement(parentObj)


# SPAN
class HTMLSpan (html_build_base.HTMLBuildBase):
	def __init__(self, className):
		self.logger			=	logging.getLogger("HTMLSpan")
		super().__init__("span")
		self.setClass(className)

	def __del__(self):
		super().__del__()
