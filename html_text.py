# Build HTML

# URL
#	https://docs.python.org/3/library/xml.etree.elementtree.html

import logging

# Encoding base
import xml.etree.ElementTree as ET
from . import html_base


class HTMLText (html_base.HTMLBase):
	H1			=	"h1"
	H2			=	"h2"
	H3			=	"h3"
	H4			=	"h4"
	H5			=	"h5"
	H6			=	"h6"
	DEFAULT		=	"h4"

	def __init__(self, className, fmt):
		super().__init__(fmt)
		self.logger			=	logging.getLogger("HTMLText")
		self.setClass(className)


	def __del__(self):
		super().__del__()
