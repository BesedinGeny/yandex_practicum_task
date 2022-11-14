import ast
import sys
from typing import Type

from checkers.base import BaseChecker
from name_validotors.base_validator import BaseNameValidator


class EntryPoint:
	"""Точка входа"""

	def __init__(
			self, *_,
			external_name_validator: Type[BaseNameValidator],
			internal_name_validator: Type[BaseNameValidator],
			external_checker: Type[BaseChecker]
	):
		self._external_name_validator = external_name_validator
		self._internal_name_validator = internal_name_validator
		self._external_checker = external_checker

	def __call__(self, doc_path):
		with open(doc_path) as code_file:
			code = code_file.read()
			return self._external_checker(
				ast.parse(code),
				self._external_name_validator,
				self._internal_name_validator
			).check()
		
	def get_arguments(self):
		try:
			doc_path = sys.argv[1]
		except IndexError:
			doc_path = "tests/docs/test1.py"
		return doc_path
