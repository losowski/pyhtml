# Build HTML

# URL
#	https://docs.python.org/3/library/xml.etree.elementtree.html

import logging

# Encoding base
import xml.etree.ElementTree as ET
from . import html_build_base

# Page components
from . import html_title
from . import html_meta
from . import html_stylesheet
from . import html_javascript



class HTMLPage (html_build_base.HTMLBuildBase):
	def __init__(self):
		super().__init__("html")
		self.logger				=	logging.getLogger("HTMLPage")
		# Page Components
		self.header				=	self.addSubElement("head")

	def __del__(self):
		super().__del__()

	# Generic Functions
	## HEADER
	def addToHeader(self, element):
		self.appendToElement(self.header, element)

	def addHTMLToHeader(self, htmlObj):
		self.addToHeader(htmlObj.get())


	# Header Specific Builders
	## TITLE
	def title(self, title):
		hTitle = html_title.HTMLTitle(title)
		self.addToHeader(hTitle.get())
		return hTitle


	## META
	def meta(self, key, value):
		hMeta = html_meta.HTMLMeta(title)
		self.addToHeader(hMeta.get())
		return hMeta

	## CSS StyleSheet
	def addStyleSheet(self, styleSheet):
		hStyle = html_stylesheet.HTMLStyleSheet(styleSheet)
		self.addToHeader(hStyle.get())
		return hStyle


	## JAVASCRIPT
	def addJavascript(self, javascript):
		hJavascript = html_javascript.HTMLJavaScript(javascript)
		self.addToHeader(hJavascript.get())
		return hJavascript
