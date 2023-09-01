"""Parser module of the assembler.

Classes:
	Parser
"""

from constants import *


class Parser:
	"""Parser class of Hack Assembler.

	Encapsulates access to the input assembly code:

	Provides means for advancing through the source code,
	skipping comments and whitespace,
	and breaking each symbolic instruction into its underlying components.

	Properties:
		file: file object containing the source code
		current_instruction: the instruction currently being processed

	Methods:
		advance() -> None
		instruction_type() -> str
		symbol() -> str
	"""

	def __init__(self, file):
		self.file = file
		self.current_instruction = ''


	def advance(self):
		"""Advance to the next instruction, skipping white space and comments.
		Then, read it and make it the current instruction.
		"""
		self.current_instruction = ''
		
		while char := self.file.read(1):
			if char == ' ':
				# ignore whitespace
				continue
			elif char == '/':
				# ignore comments
				self.file.readline()
			elif char == '\n':
				if self.current_instruction:
					return
			else:
				self.current_instruction += char


	def instruction_type(self):
		"""Return the type of the current instruction"""
		first_char = self.current_instruction[0]

		if first_char == '@':
			return A_INSTRUCTION
		elif first_char == '(':
			return L_INSTRUCTION
		else:
			return C_INSTRUCTION


	def symbol(self):
		"""Return symbol in the current instruction, if there is one.
		In a label pseudo-instruction: (xxx), return symbol xxx.
		In an A-instruction: @xxx, return symbol or decimal xxx
		"""
		if self.instruction_type() == A_INSTRUCTION:
			return self.current_instruction[1::]
		elif self.instruction_type() == L_INSTRUCTION:			
			return self.current_instruction[1:-1:]
