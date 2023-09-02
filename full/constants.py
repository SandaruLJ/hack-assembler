"""Module for storing constants used in the assembler"""

# instruction type
A_INSTRUCTION = 'A_INSTRUCTION'
C_INSTRUCTION = 'C_INSTRUCTION'
L_INSTRUCTION = 'L_INSTRUCTION'

# instruction set table
instruction_set = {
	'comp': {
		'0': '101010',
		'1': '111111',
		'-1': '111010',
		'D': '001100',
		'AM': '110000',
		'!D': '001101',
		'!AM': '110001',
		'-D': '001111',
		'-AM': '110011',
		'D+1': '011111',
		'AM+1': '110111',
		'D-1': '001110',
		'AM-1': '110010',
		'D+AM': '000010',
		'D-AM': '010011',
		'AM-D': '000111',
		'D&AM': '000000',
		'D|AM': '010101'
	},
	'jump': {
		'': '000',
		'JGT': '001',
		'JEQ': '010',
		'JGE': '011',
		'JLT': '100',
		'JNE': '101',
		'JLE': '110',
		'JMP': '111'
	}
}