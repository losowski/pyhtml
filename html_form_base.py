# Build HTML

# URL
#	https://docs.python.org/3/library/xml.etree.elementtree.html
#	https://www.programiz.com/html/form-elements

import logging

# Encoding base
import xml.etree.ElementTree as ET
from . import html_build_base


# Form Components
from .form import html_label
from .form import html_input
from .form import html_input_text
from .form import html_input_select
from .form import html_input_complex
from .form import html_input_button

class HTMLFormBase (html_build_base.HTMLBuildBase):
	def __init__(self, label):
		super().__init__(label)
		self.logger				=	logging.getLogger("HTMLFormBase")

	def __del__(self):
		super().__del__()


	## FORM DATA COMPONENTS
	def addLabel(self, inputName, labelName):
		hLabel = html_label.HTMLLabel(inputName, labelName)
		self.appendElement(hLabel.get())
		return hLabel

	def addPrettyLabel(self, inputName,):
		labelName = inputName.title().replace("_", " ")
		return self.addLabel(inputName, labelName)


	## INPUT
	def addInputText(self, name, value):
		hInput = html_input_text.HTMLInputText(name, value)
		self.appendElement(hInput.get())
		return hInput


	def addHidden(self, key, value):
		hHidden = html_input_text.HTMLInputHidden(key, value)
		self.appendElement(hHidden.get())
		return hHidden


	def addInputPassword(self, name):
		hPassword = html_input_text.HTMLInputPassword(name)
		self.appendElement(hPassword.get())
		return hPassword


	## SELECT
	def addInputSelect(self, name):
		hSelect = html_input_select.HTMLInputSelect(name)
		self.appendElement(hSelect.get())
		return hSelect


	## COMPLEX
	def addInputEmail(self, name, value):
		hEmail = html_input_complex.HTMLInputEmail(name)
		self.appendElement(hEmail.get())
		return hEmail

	def addInputTel(self, name, value):
		hTel = html_input_complex.HTMLInputTel(name, value)
		self.appendElement(hTel.get())
		return hTel

	def addInputNumber(self, name, value):
		hNumber = html_input_complex.HTMLInputNumber(name)
		self.appendElement(hNumber.get())
		return hNumber

	def addInputFile(self, name):
		hFile = html_input_complex.HTMLInputFile(name)
		self.appendElement(hFile.get())
		return hFile


	## BUTTON
	def addInputButton(self, name, value):
		hButton = html_input_button.HTMLInputButton(name, value)
		self.appendElement(hButton.get())
		return hButton


	def addInputSubmit(self, name):
		hSubmit = html_input_button.HTMLInputSubmit(name)
		self.appendElement(hSubmit.get())
		return hSubmit


	def addInputReset(self, name):
		hReset = html_input_button.HTMLInputReset(name)
		self.appendElement(hReset.get())
		return hReset


	def addInputImage(self, name, filename, action):
		hImage = html_input_button.HTMLInputImage(name, filename, action)
		self.appendElement(hImage.get())
		return hImage


	# TODO: add functions for EVERY type (16x)

