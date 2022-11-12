import ast
from _ast import AST, FunctionDef, ClassDef
from typing import Any, Callable, Type

from checkers.base import BaseChecker
from checkers.lower_checker import LowerChecker
from name_validotors.base_validator import BaseNameValidator


class UpperChecker(BaseChecker):
	"""Класс для проверки объекта вне класса"""
	
	def __init__(
			self,
			current_object: Any,
			external_name_validator: Type[BaseNameValidator],
			internal_name_validator: Type[BaseNameValidator],
	):
		self._checkers_per_class = {
			FunctionDef: self._function_def_case,
			ClassDef: self._class_def_case
		}
		self._internal_name_validator = internal_name_validator
		super().__init__(current_object, external_name_validator)
	
	def check(self) -> bool:
		for element in self._iter_inner_items():
			current_checker_function: Callable = self._checkers_per_class.get(
				type(element), self._regular_check_case
			)
			current_result = current_checker_function(element)
			
			if not current_result:
				return False
		return True
	
	def _function_def_case(self, element: Any) -> bool:
		if self._name_validator.validate(element.name):
			return self._regular_check_case(element)
		else:
			return False
	
	def _class_def_case(self, element: Any) -> bool:
		checker = LowerChecker(element, self._internal_name_validator)
		return checker.check()
		
	def _regular_check_case(self, element: Any) -> bool:
		current_element_checker = UpperChecker(
			element,
			self._name_validator,
			self._internal_name_validator
		)
		return current_element_checker.check()
