# Build HTML

# URL
#	https://docs.python.org/3/library/xml.etree.elementtree.html
#	https://www.programiz.com/html/input

import logging

# Encoding base
import xml.etree.ElementTree as ET
from . import html_input

from .. import html_base

## HTMLInputText
class HTMLInputText (html_input.HTMLInputBase):
	def __init__(self, name, value):
		super().__init__(html_input.HTMLInputBase.TEXT, name, value)
		self.logger				=	logging.getLogger("HTMLInputText")
		# Components
		self.setId(name)
		self.setValue(value)

	def __del__(self):
		super().__del__()




## HTMLInputHidden
class HTMLInputHidden (html_input.HTMLInputBase):
	def __init__(self, name, value):
		super().__init__(html_input.HTMLInputBase.HIDDEN, name, value)
		self.logger				=	logging.getLogger("HTMLInputHidden")
		self.setId(name)
		self.setName(name)
		self.setValue(value)

	def __del__(self):
		super().__del__()




## HTMLInputPassword
class HTMLInputPassword (html_input.HTMLInputBase):
	def __init__(self, name):
		super().__init__(html_input.HTMLInputBase.PASSWORD, name, "")
		self.logger				=	logging.getLogger("HTMLInputPassword")
		self.setId(name)

	def __del__(self):
		super().__del__()

