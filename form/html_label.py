# Build HTML

# URL
#	https://docs.python.org/3/library/xml.etree.elementtree.html

import logging

# Encoding base
import xml.etree.ElementTree as ET
from .. import html_base


class HTMLLabel (html_base.HTMLBase):
	def __init__(self, inputName, labelName):
		super().__init__("label")
		self.logger				=	logging.getLogger("HTMLLabel")
		self.XMLObj.text		=	labelName
		self.setAttrib("for", "{inputName}".format(inputName = inputName))

	def __del__(self):
		super().__del__()

