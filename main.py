import ast
import sys
import checkers

if __name__ == "__main__":
	print(sys.argv)
	with open("test_docs/test1.py") as code_file:
		code = code_file.read()
		print(checkers.UpperChecker(ast.parse(code)).check())
