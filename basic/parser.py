class Parser:
	"""Parser class of Hack Assembler.

	Encapsulates access to the input assembly code:

	Provides means for advancing through the source code,
	skipping comments and whitespace,
	and breaking each symbolic instruction into its underlying components.

	Methods:
		advance() -> None
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
