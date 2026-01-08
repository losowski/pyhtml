# Build HTML

# URL
#	https://docs.python.org/3/library/xml.etree.elementtree.html
#	https://www.programiz.com/html/input

import logging

# Encoding base
import xml.etree.ElementTree as ET
from .. import html_input

## HTMLInputCheckbox
class HTMLInputCheckbox (html_input.HTMLInputBase):
	def __init__(self, name):
		super().__init__(html_input.HTMLInputBase.CHECKBOX, name)
		self.logger				=	logging.getLogger("HTMLInputCheckbox")
		self.setAttrib("value", "{name}".format(name = name))

	def __del__(self):
		super().__del__()



## HTMLInputRadio
class HTMLInputRadio (html_input.HTMLInputBase):
	def __init__(self, name):
		super().__init__(html_input.HTMLInputBase.RADIO, name)
		self.logger				=	logging.getLogger("HTMLInputRadio")
		self.setAttrib("value", "{name}".format(name = name))

	def __del__(self):
		super().__del__()
