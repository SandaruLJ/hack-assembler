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
		self.symbol_table = {}


	def add_entry(self, symbol, address):
		"""Add <symbol, address> to the table"""
		self.symbol_table[symbol] = address


	def contains(self, symbol):
		"""Return True if symbol table contains the given symbol, else False"""
		return True if self.symbol_table.get(symbol) else False


	def get_address(self, symbol):
		"""Return the address associated with the symbol"""
		return self.symbol_table[symbol]
