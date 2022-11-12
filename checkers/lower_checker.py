from checkers.base import BaseChecker
from _ast import FunctionDef


class LowerChecker(BaseChecker):
	def check(self) -> bool:
		for element in self._iter_inner_items():
			name_result = True
			if isinstance(element, FunctionDef):
				name_result = self._check_name(element.name)

			if not name_result:
				return False
			
			element_rule_result = self._continuous_check(element)
			
			if not element_rule_result:
				return False
		return True
	
	def _check_name(self, name: str) -> bool:
		return name[0].islower()
	
	def _continuous_check(self, element) -> bool:
		checker = LowerChecker(element)
		return checker.check()
