"""Main module of the Hack Assembler"""

import sys

from parser import Parser
from code import Code
from constants import *


def main():
	if len(sys.argv) != 2:
		print('Usage: program source.asm')
		exit(1)

	source_filename = '.'.join(sys.argv[1].split('.')[:-1:]) or sys.argv[1]

	with open(f'{source_filename}.asm', 'r') as source:
		with open(f'{source_filename}.hack', 'w') as output:
			parser = Parser(source)
			code = Code()
			instruction = ''

			while parser.advance():
				ins_type = parser.instruction_type()
				
				if ins_type == A_INSTRUCTION:
					symbol = parser.symbol()
					if symbol.isdigit():
						instruction = bin(int(symbol))[2::].zfill(16)

				elif ins_type == C_INSTRUCTION:
					# parse instruction fields
					dest_str = parser.dest()
					comp_str = parser.comp()
					jump_str = parser.jump()
					
					# translate instruction fields to binary machine code
					dest = code.dest(dest_str)
					comp = code.comp(comp_str)
					jump = code.jump(jump_str)
					
					# assemble codes into a single binary instruction
					instruction = '111' + comp + dest + jump 

				output.write(f'{instruction}\n')


if __name__ == '__main__':
	main()
