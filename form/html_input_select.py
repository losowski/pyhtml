# Build HTML

# URL
#	https://docs.python.org/3/library/xml.etree.elementtree.html
#	https://www.programiz.com/html/input

import logging

# Encoding base
import xml.etree.ElementTree as ET
from . import html_input

from .. import html_base

## HTMLInputSelectOption
class HTMLInputSelectOption (html_base.HTMLBase):
	def __init__(self, name, value):
		super().__init__("option")
		self.logger				=	logging.getLogger("HTMLInputSelectOption")
		self.setAttrib("value", "{value}".format(value = value))
		self.setValue(name)

	def __del__(self):
		super().__del__()

	# Mark as selected
	def setSelected(self):
		self.setAttrib("selected", self.value)


## HTMLInputSelect
class HTMLInputSelect (html_base.HTMLBase):
	def __init__(self, name):
		super().__init__(html_input.HTMLInputBase.SELECT)
		self.logger				=	logging.getLogger("HTMLInputSelect")


	def __del__(self):
		super().__del__()

	def addOption(self, name, value):
		hOption = HTMLInputSelectOption(name, value)
		self.appendElement(hOption.get())
		return hOption

	def addDefaultOption(self, name, value):
		hOption = HTMLInputSelectOption(name, value)
		hOption.setSelected()
		self.appendElement(hOption.get())
		return hOption

	# Number of options to display
	def setSize(self, number):
		self.setAttrib("size", number)
