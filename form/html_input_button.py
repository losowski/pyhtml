# Build HTML

# URL
#	https://docs.python.org/3/library/xml.etree.elementtree.html
#	https://www.programiz.com/html/input

import logging

# Encoding base
import xml.etree.ElementTree as ET
from . import html_input


## HTMLInputButton
class HTMLInputButton (html_input.HTMLInputBase):
	def __init__(self, name, value):
		super().__init__(html_input.HTMLInputBase.BUTTONGENERIC, name, name)
		self.logger				=	logging.getLogger("HTMLInputButton")

	def __del__(self):
		super().__del__()

	def setOnClick(self, functionName):
		name = "{name}()".format(name = functionName)
		self.setAttrib("onclick", name)


## HTMLInputSubmit
class HTMLInputSubmit (html_input.HTMLInputBase):
	def __init__(self, name):
		super().__init__(html_input.HTMLInputBase.BUTTONSUBMIT, name, name)
		self.logger				=	logging.getLogger("HTMLInputSubmit")
		self.setAttrib("name", "Submit")

	def __del__(self):
		super().__del__()




## HTMLInputReset
class HTMLInputReset (html_input.HTMLInputBase):
	def __init__(self, name):
		super().__init__(html_input.HTMLInputBase.BUTTONRESET, name, name)
		self.logger				=	logging.getLogger("HTMLInputReset")
		self.setAttrib("name", "reset")

	def __del__(self):
		super().__del__()




## HTMLInputImage
class HTMLInputImage (html_input.HTMLInputBase):
	def __init__(self, name, filename, action):
		super().__init__(html_input.HTMLInputBase.BUTTONIMAGE, name, name)
		self.logger				=	logging.getLogger("HTMLInputImage")
		self.setAttrib("src", "$CDN/image/{name}".format(name = filename))
		self.setAttrib("alt", "{action}".format(action = action))

	def __del__(self):
		super().__del__()
