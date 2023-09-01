"""Code module of the assembler.

Classes:
	Code
"""

from constants import instruction_set


class Code:
	"""Code class of Hack Assembler.

	Translates symbolic Hack mnemonics into corresponding binary codes.

	Methods:
		dest(str) -> str
		comp(str) -> str
		jump(str) -> str
	"""

	def dest(self, mnemonic):
		"""Return the binary code of the 'dest' mnemonic."""
		dest_binary = ['0', '0', '0']

		if 'A' in mnemonic:
			dest_binary[0] = '1'
		if 'D' in mnemonic:
			dest_binary[1] = '1'
		if 'M' in mnemonic:
			dest_binary[2] = '1'

		return ''.join(dest_binary)


	def comp(self, mnemonic):
		"""Return the binary code of the 'comp' mnemonic."""
		comp_binary = ''

		if 'A' in mnemonic or 'M' in mnemonic:
			if 'A' in mnemonic:
				comp_binary += '0'
				mnemonic = mnemonic.replace('A', 'AM')
			elif 'M' in mnemonic:
				comp_binary += '1'
				mnemonic = mnemonic.replace('M', 'AM')

		comp_binary += instruction_set['comp'][mnemonic]
		return comp_binary


	def jump(self, mnemonic):
		"""Return the binary code of the 'jump' mnemonic."""
		return instruction_set['jump'][mnemonic]
