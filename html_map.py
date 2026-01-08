# Build HTML

# URL
#	https://docs.python.org/3/library/xml.etree.elementtree.html
#	https://www.programiz.com/html/input

import logging

# Encoding base
import xml.etree.ElementTree as ET
from . import html_input

from . import html_build_base

## HTMLMapArea
class HTMLMapArea (html_base.HTMLBase):
	def __init__(self, altDesc, linkHref):
		super().__init__("area")
		self.logger				=	logging.getLogger("HTMLMapArea")
		self.setDesc(altDesc)
		self.setHRef(linkHref)

	def __del__(self):
		super().__del__()

	def setHRef(self, href):
		self.setAttrib("href", href)

	def setDesc(self, desc):
		self.setAttrib("alt", desc)

	def setShape(self, shape):
		self.setAttrib("shape", shape)

	def setCoOrds(self, x, y, height, width):
		self.setAttrib("coords", "{x},{y},{height},{width}".format(
				x	=	x,
				y	=	y,
				height	=	height,
				width	=	width,
			)
		)


## HTML LIST BASE
class HTMLMap (html_base.HTMLBase):
	def __init__(self, className):
		super().__init__("map")
		self.logger				=	logging.getLogger("HTMLMap")
		self.setClass(className)

	def __del__(self):
		super().__del__()

	def addArea(self, altDesc, linkHref):
		hArea = HTMLMapArea(name, value)
		self.appendElement(hArea.get())
		return hArea



