# Build HTML

# URL
#	https://docs.python.org/3/library/xml.etree.elementtree.html
#	https://www.programiz.com/html/input

import logging

# Encoding base
import xml.etree.ElementTree as ET
from .. import html_base

## HTMLInputBase
class HTMLInputBase (html_base.HTMLBase):
	# Buttons
	BUTTONGENERIC	=	"button"
	BUTTONSUBMIT	=	"submit"
	BUTTONRESET		=	"reset"
	BUTTONIMAGE		=	"image"
	# Simple Input
	HIDDEN			=	"hidden"
	TEXT			=	"text"
	SELECT			=	"select"
	PASSWORD		=	"password"
	# Boxes
	CHECKBOX		=	"checkbox"
	RADIO			=	"radio"


	# Date and time
	DATE			=	"date"
	DATETIME		=	"datetime-local"
	TIME			=	"time"
	# Complex Data
	URL				=	"url"
	EMAIL			=	"email"
	TEL				=	"tel"
	NUMBER			=	"number"
	FILE			=	"file"
	# Call some function from the string
	SEARCH			=	"search"


	def __init__(self, inputType, name, value):
		super().__init__("input")
		self.logger				=	logging.getLogger("HTMLInputBase")
		self.setAttrib("type", "{inputType}".format(inputType = inputType))
		self.setAttrib("name", "{name}".format(name = name))
		self.setValue(value)


	def __del__(self):
		super().__del__()

	# Override the set value function for inputs
	def setValue(self, value):
		self.setAttrib("value", "{value}".format(value = value))
