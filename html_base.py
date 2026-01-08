# Build HTML

# URL
#	https://docs.python.org/3/library/xml.etree.elementtree.html

import logging

# Encoding base
import xml.etree.ElementTree as ET
from . import encode_base

class HTMLBase (encode_base.EncodeBase):

	def __init__(self, elementTitle):
		super().__init__(elementTitle)
		self.logger				=	logging.getLogger("HTMLBase")

	def __del__(self):
		super().__del__()

	# Output HTML
	def writeToFile(self, fileObj):
		return self.XMLObj.write(fileObj, method='html')

	def toString(self):
		return ET.tostring(self.XMLObj, method='html')

	def getHTML(self):
		return self.toString().decode()


	def debugHTML(self):
		rawHTML = self.toString().decode()
		self.logger.debug("HTML:\n%s", rawHTML)

	## Generic Functions
	def addElement(self, element):
		self.appendToElement(self.XMLObj, element)

	def addHTMLtoElement(self, htmlObj):
		self.addElement(htmlObj)


	# GENERIC ADDITIONS
	def setAttrib(self, attrib, value):
		self.XMLObj.set(attrib, value)

	def setValue(self, value):
		self.XMLObj.text = value

	# SPECIFIC ADDITIONS
	def setClass(self, className):
		self.setAttrib("class", className)

	def setId(self, Id):
		self.setAttrib("id", Id)

	def setName(self, name):
		self.setAttrib("name", "{name}".format(name = name))

	def setReadonly(self):
		self.setAttrib("readonly", "true")

	def setDisabled(self):
		self.setAttrib("disabled", "true")

	def setHidden(self):
		self.setAttrib("hidden", "true")

	def setChecked(self):
		self.setAttrib("checked", "true")

	def setRequired(self):
		self.setAttrib("required", "true")

	def setRegex(self, regex):
		self.setAttrib("pattern", regex)
