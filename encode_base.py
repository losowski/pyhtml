# Build HTML

# URL
#	https://docs.python.org/3/library/xml.etree.elementtree.html

import logging

# XML
import xml.etree.ElementTree as ET

class EncodeBase (object):
	def __init__(self, elementTitle):
		self.logger				=	logging.getLogger("EncodeBase")
		self.XMLObj				=	ET.Element(elementTitle)

	def __del__(self):
		pass

	# Get underlying object
	def get(self):
		return self.XMLObj

	## Modifiers
	def addSubElement(self, subElementXML, attrib={}):
		return ET.SubElement(self.XMLObj, subElementXML, attrib)

	# APPEND
	def appendElement(self, appendedElement):
		self.XMLObj.append(appendedElement)

	def appendToElement(self, elementObj, appendedElement):
		elementObj.append(appendedElement)

	# EXTEND
	def extendElement(self,elementObj, extendedElement):
		elementObj.extend(appendedElement)
