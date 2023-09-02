"""Symbol table module of the assembler.

Classes:
	SymbolTable
"""

class SymbolTable:
	"""SymbolTable class of Hack Assembler.

	Handles the resolving of symbolic references into actual addresses:

	Creates and maintains the correspondence between symbols and their meaning.
	Implemented using a dictionary.

	Properties:
		symbol_table: dictionary containing the mapping between symbols and addresses

	Methods:
		add_entry(str, int) -> None
		contains(str) -> bool
		get_address(str) -> int
	"""

	def __init__(self):
		self.symbol_table = {
			'R0': 0,
			'R1': 1,
			'R2': 2,
			'R3': 3,
			'R4': 4,
			'R5': 5,
			'R6': 6,
			'R7': 7,
			'R8': 8,
			'R9': 9,
			'R10': 10,
			'R11': 11,
			'R12': 12,
			'R13': 13,
			'R14': 14,
			'R15': 15,
			'SP': 0,
			'LCL': 1,
			'ARG': 2,
			'THIS': 3,
			'THAT': 4,
			'SCREEN': 16384,
			'KBD': 24576
		}


	def add_entry(self, symbol, address):
		"""Add <symbol, address> to the table"""
		self.symbol_table[symbol] = address


	def contains(self, symbol):
		"""Return True if symbol table contains the given symbol, else False"""
		return True if self.symbol_table.get(symbol, -1) != -1 else False


	def get_address(self, symbol):
		"""Return the address associated with the symbol"""
		return self.symbol_table[symbol]
