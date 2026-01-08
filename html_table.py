# Build HTML

# URL
#	https://docs.python.org/3/library/xml.etree.elementtree.html
#	https://www.programiz.com/html/input

import logging

# Encoding base
import xml.etree.ElementTree as ET

from . import html_base
from . import html_build_base




## HTMLTableHeader
class HTMLTableHeader (html_build_base.HTMLBuildBase):
	def __init__(self, name):
		super().__init__("th")
		self.logger				=	logging.getLogger("HTMLTableHeader")
		self.setValue(name)

	def __del__(self):
		super().__del__()


## HTMLTableColumn
# NOTE: Use other functions or setValue() to create value
class HTMLTableColumn (html_build_base.HTMLBuildBase):
	def __init__(self):
		super().__init__("td")
		self.logger				=	logging.getLogger("HTMLTableColumn")

	def __del__(self):
		super().__del__()



## HTMLTableRow
class HTMLTableRow (html_base.HTMLBase):
	def __init__(self):
		super().__init__("tr")
		self.logger				=	logging.getLogger("HTMLTableRow")

	def __del__(self):
		super().__del__()


	def addHeader(self, name):
		hRow = HTMLTableHeader(name)
		self.appendElement(hRow.get())
		return hRow

	def addColumn(self):
		hRow = HTMLTableColumn()
		self.appendElement(hRow.get())
		return hRow



## HTML TABLE
class HTMLTable (html_build_base.HTMLBuildBase):
	def __init__(self, className):
		super().__init__("table")
		self.logger				=	logging.getLogger("HTMLTable")
		self.setClass(className)


	def __del__(self):
		super().__del__()

	def addRow(self):
		hRow = HTMLTableRow()
		self.appendElement(hRow.get())
		return hRow




