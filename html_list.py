# Build HTML

# URL
#	https://docs.python.org/3/library/xml.etree.elementtree.html
#	https://www.programiz.com/html/input

import logging

# Encoding base
import xml.etree.ElementTree as ET
from . import html_input

from . import html_build_base

## HTMLListItem
class HTMLListItem (html_build_base.HTMLBuildBase):
	def __init__(self, value):
		super().__init__("li")
		self.logger				=	logging.getLogger("HTMLListItem")
		self.setValue(value)

	def __del__(self):
		super().__del__()


## HTML LIST BASE
class HTMLListBase (html_base.HTMLBase):
	def __init__(self, tag, className):
		super().__init__(tag)
		self.logger				=	logging.getLogger("HTMLList")
		self.setClass(className)


	def __del__(self):
		super().__del__()

	def addItem(self, name, value):
		hItem = HTMLListItem(name, value)
		self.appendElement(hItem.get())
		return hItem


## HTML ORDERED LIST
class HTMLOrderedList (HTMLListBase):
	def __init__(self, className):
		super().__init__("ol", className)
		self.logger				=	logging.getLogger("HTMLOrderedList")


	def __del__(self):
		super().__del__()

## HTML UNORDERED LIST
class HTMLUnOrderedList (HTMLListBase):
	def __init__(self, className):
		super().__init__("ul", className)
		self.logger				=	logging.getLogger("HTMLUnOrderedList")


	def __del__(self):
		super().__del__()

