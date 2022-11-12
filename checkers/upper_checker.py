import ast
from _ast import AST, FunctionDef, ClassDef
from typing import Any, Callable, Type

from checkers.base import BaseChecker
from checkers.lower_checker import LowerChecker


class UpperChecker(BaseChecker):
	"""Класс для проверки объекта вне класса"""
	
	# todo: COR, composer
	def __init__(self, current_object):
		self._checkers_per_class = {
			FunctionDef: self._function_def_case,
			ClassDef: self._class_def_case
		}
		super().__init__(current_object)
	
	def check(self) -> bool:
		for element in self._iter_inner_items():
			current_checker_function: Callable = self._checkers_per_class.get(
				type(element), self._regular_check_case
			)
			current_result = current_checker_function(element)
			
			if not current_result:
				return False
		return True
		
	def _check_name(self, name: str):
		return not name[0].islower()
	
	def _function_def_case(self, element: Any) -> bool:
		if self._check_name(element.name):
			return self._regular_check_case(element)
		else:
			return False
	
	def _class_def_case(self, element: Any) -> bool:
		checker = LowerChecker(element)
		return checker.check()
		
	def _regular_check_case(self, element: Any) -> bool:
		current_element_checker = UpperChecker(element)
		return current_element_checker.check()
