# Build HTML

# URL
#	https://docs.python.org/3/library/xml.etree.elementtree.html

import logging

# Encoding base
import xml.etree.ElementTree as ET
from . import html_base

class HTMLImage (html_base.HTMLBase):
	def __init__(self, filename):
		super().__init__("img")
		self.logger					=	logging.getLogger("HTMLImage")
		self.setAttrib("src", "$CDN/image/{filename}".format(filename = filename))

	def __del__(self):
		super().__del__()


	def setDesc(self, desc):
		self.setAttrib("alt", desc)


	def setUseMap(self, mapName):
		self.setAttrib("usemap", "#{name}".format(name = mapName))
