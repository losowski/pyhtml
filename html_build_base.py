# Build HTML

# URL
#	https://docs.python.org/3/library/xml.etree.elementtree.html

import logging

# Encoding base
import xml.etree.ElementTree as ET
from . import html_base

# Page components
from . import html_image
#from . import html_div
#from . import html_link
from . import html_text
from . import html_button
#from . import html_table
#from . import html_form


class HTMLBuildBase (html_base.HTMLBase):
	def __init__(self, className):
		super().__init__(className)
		self.logger				=	logging.getLogger("HTMLBuilderBase")

	def __del__(self):
		super().__del__()

	# Body Specific Builders
	## BODY
	## DIV
	def addDiv(self, className, identifier):
		# Import
		from . import html_div
		# Function
		hDiv = html_div.HTMLDiv(className)
		hDiv.setId(identifier)
		self.addHTMLtoElement(hDiv.get())
		return hDiv


	## SPAN
	def addSpan(self, className, identifier):
		# Import
		from . import html_div
		# Function
		hSpan = html_div.HTMLSpan(className)
		hSpan.setId(identifier)
		self.addHTMLtoElement(hSpan.get())
		return hSpan

	### DIV An OBJECT
	def addDivObject(self, className, identifier, parentObj):
		hDiv = self.addDiv(className, identifier)
		hDiv.appendObject(parentObj)
		return hDiv


	def mkDiv(self, hObject, name, identifier, div):
		if (div):
			self.addDivObject(name, identifier, hObject.get())
		else:
			self.addHTMLtoElement(hObject.get())


	## IMAGE
	def addImage(self, className, filename, desc ="", div=False):
		hImage = html_image.HTMLImage(filename)
		hImage.setDesc(desc)
		# Make it Div
		self.mkDiv(hImage, "image", className, div )
		return hImage


	## LINK
	def addLink(self, className, url, displayName, div=False):
		# Import
		from . import html_link
		hLink = html_link.HTMLLink(url, displayName)
		# Make it Div
		self.mkDiv(hLink, "link", className, div)
		return hLink

	## TEXT
	#	Implements:
	#		-	Navigation
	#		-	Text
	def addText(self, className, textToAdd, fmt=html_text.HTMLText.DEFAULT):
		# Function
		hText = html_text.HTMLText(className, fmt)
		hText.setValue(textToAdd)
		self.addHTMLtoElement(hText.get())
		return hText


	## BUTTON
	def addButton(self, className, textToAdd, div=False):
		hButton = html_button.HTMLButton(className)
		hButton.setValue(textToAdd)
		# Make it Div
		self.mkDiv(hButton, "button", className, div)
		return hButton


	## TABLE
	def addTable(self, className, div=False):
		# Import
		from . import html_table
		# Function
		hTable = html_table.HTMLTable(className)
		# Make it Div
		self.mkDiv(hTable, "table", className, div)
		return hTable



	## FORM
	def addForm(self, className):
		# Import
		from . import html_form
		# Function
		hForm = html_Form.HTMLForm(className)
		# Make it Div
		self.mkDiv(hForm, "form", className, div)
		return hForm
