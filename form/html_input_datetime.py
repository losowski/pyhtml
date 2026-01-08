# Build HTML

# URL
#	https://docs.python.org/3/library/xml.etree.elementtree.html
#	https://www.programiz.com/html/input

import logging

# Encoding base
import xml.etree.ElementTree as ET
from .. import html_input

## HTMLInputDate
class HTMLInputDate html_input.HTMLInputBase):
	def __init__(self, name):
		super().__init__(html_input.HTMLInputBase.DATE, name)
		self.logger				=	logging.getLogger("HTMLInputDate")
		# Components
		self.setId(name)

	def __del__(self):
		super().__del__()




## HTMLInputTime
class HTMLInputTime html_input.HTMLInputBase):
	def __init__(self, name):
		super().__init__(html_input.HTMLInputBase.TIME, name)
		self.logger				=	logging.getLogger("HTMLInputTime")
		# Components
		self.setId(name)

	def __del__(self):
		super().__del__()




## HTMLInputDateTime
class HTMLInputDateTime html_input.HTMLInputBase):
	def __init__(self, name):
		super().__init__(html_input.HTMLInputBase.DATETIME, name)
		self.logger				=	logging.getLogger("HTMLInputDateTime")
		# Components
		self.setId(name)

	def __del__(self):
		super().__del__()
