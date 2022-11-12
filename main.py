import ast
import sys
import checkers
from name_validotors import *

if __name__ == "__main__":
	print(sys.argv)
	with open("test_docs/test1.py") as code_file:
		code = code_file.read()
		print(checkers.UpperChecker(ast.parse(code), ExternalNameValidator, InternalNameValidator).check())
