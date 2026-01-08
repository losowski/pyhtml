# Build HTML

# URL
#	https://docs.python.org/3/library/xml.etree.elementtree.html
#	https://www.programiz.com/html/input

import logging

# Encoding base
import xml.etree.ElementTree as ET
from . import html_input

## HTMLInputURL
class HTMLInputURL (html_input.HTMLInputBase):
	def __init__(self, name, value):
		super().__init__(html_input.HTMLInputBase.URL, name)
		self.logger				=	logging.getLogger("HTMLInputURL")
		# Components
		self.setId(name)
		self.setAttrib("placeholder", "https://example.com")
		#TODO: Better Regex for HTTP too
		self.setAttrib("pattern", "https://.*")

	def __del__(self):
		super().__del__()




## HTMLInputEmail
class HTMLInputEmail (html_input.HTMLInputBase):
	def __init__(self, name, value):
		super().__init__(html_input.HTMLInputBase.EMAIL, name)
		self.logger				=	logging.getLogger("HTMLInputEmail")
		# Components
		self.setId(name)

	def __del__(self):
		super().__del__()



## HTMLInputTel
class HTMLInputTel (html_input.HTMLInputBase):
	def __init__(self, name, value):
		super().__init__(html_input.HTMLInputBase.TEL, name, value)
		self.logger				=	logging.getLogger("HTMLInputTel")
		# Components
		self.setId(name)
		# TODO: add REGEX code

	def __del__(self):
		super().__del__()



## HTMLInputNumber
class HTMLInputNumber (html_input.HTMLInputBase):
	def __init__(self, name, value):
		super().__init__(html_input.HTMLInputBase.NUMBER, name)
		self.logger				=	logging.getLogger("HTMLInputNumber")
		# Components
		self.setId(name)


	def __del__(self):
		super().__del__()

	def setMin(self, minValue):
		self.setAttrib("min", minValue)

	def setMax(self, maxValue):
		self.setAttrib("max", maxValue)

	def setStep(self, stepValue):
		self.setAttrib("step", stepValue)


## HTMLInputFile
class HTMLInputFile (html_input.HTMLInputBase):
	def __init__(self, name):
		super().__init__(html_input.HTMLInputBase.FILE, name)
		self.logger				=	logging.getLogger("HTMLInputFile")

	def __del__(self):
		super().__del__()
