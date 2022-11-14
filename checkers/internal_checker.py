from checkers.base import BaseChecker
from _ast import FunctionDef


class InternalChecker(BaseChecker):
	def check(self) -> bool:
		for element in self._iter_inner_items():
			name_result = True
			if isinstance(element, FunctionDef):
				name_result = self._name_validator.validate(element.name)

			if not name_result:
				return False
			
			element_rule_result = self._continuous_check(element)
			
			if not element_rule_result:
				return False
		return True
	
	def _continuous_check(self, element) -> bool:
		checker = InternalChecker(element, self._name_validator)
		return checker.check()
