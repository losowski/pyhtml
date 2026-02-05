# Build HTML

# URL
#	https://docs.python.org/3/library/xml.etree.elementtree.html

import logging

# Encoding base
import xml.etree.ElementTree as ET
from . import html_form_base

## HTML LEGEND
class HTMLLegend (html_form_base.HTMLFormBase):
	def __init__(self, className, name):
		super().__init__("legend")
		self.logger				=	logging.getLogger("HTMLLegend")
		self.XMLObj.text		=	name
		self.setId(name)

	def __del__(self):
		super().__del__()


## HTML FIELDSET
class HTMLFieldSet (html_form_base.HTMLFormBase):
	def __init__(self, className):
		super().__init__("fieldset")
		self.logger				=	logging.getLogger("HTMLFieldSet")
		self.className 			=	className
		self.setClass(className)
		

	def __del__(self):
		super().__del__()
	
	def setLegend(self, name):
		hLegend = HTMLLegend(self.className, name)
		self.addElement(hLegend.get())		



## HTML FORM
class HTMLForm (html_form_base.HTMLFormBase):
	def __init__(self, className):
		super().__init__("form")
		self.logger				=	logging.getLogger("HTMLForm")
		self.setClass(className)

	def __del__(self):
		super().__del__()

	## CONTAINING COMPONENTS
	def addFieldSet(self, className):
		hFieldSet = HTMLFieldSet(className)
		self.addElement(hFieldSet.get())
		return hFieldSet


	def setAction(self, action):
		self.setAttrib("action", "{action}".format(action = action))

	def setMethod(self, method):
		self.setAttrib("method", "{method}".format(method = method))

	def setTarget(self, target):
		self.setAttrib("target", "{target}".format(target = target))
