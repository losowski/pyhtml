# Build HTML

# URL
#	https://docs.python.org/3/library/xml.etree.elementtree.html

import logging

# Encoding base
import xml.etree.ElementTree as ET
from . import html_build_base

class HTMLLink (html_build_base.HTMLBuildBase):
	def __init__(self, url, displayName):
		super().__init__("a")
		self.logger			=	logging.getLogger("HTMLLink")
		self.XMLObj.text	=	displayName
		self.XMLObj.set("href", "{url}".format(url = url))

	def __del__(self):
		super().__del__()

	def openNewTab(self):
		self.setAttrib("target", "_blank")

	def openParentFrame(self):
		self.setAttrib("target", "_parent")

	def openFullWindow(self):
		self.setAttrib("target", "_top")

	def openOwnFrame(self, frameName):
		self.setAttrib("target", frameName)
