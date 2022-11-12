from ast import FunctionDef, Module
from abc import abstractmethod
from typing import Any, List, Optional, Type, Union

from name_validotors.base_validator import BaseNameValidator


class BaseChecker:
	_current_object: Union[FunctionDef, Module, None] = None
	_name_validator: Optional[Type[BaseNameValidator]] = None
	
	def __init__(self, current_object: Any, name_validator: Type[BaseNameValidator]):
		"""current_object - любой элемент AST"""
		self._current_object = current_object
		self._name_validator = name_validator
	
	@abstractmethod
	def check(self) -> bool:
		""" Проверка элемента на соблюдения правилу"""
		raise NotImplementedError
	
	def _iter_inner_items(self) -> List:
		"""Возвращает тело элемента, если такое возможно"""
		return getattr(self._current_object, "body", [])
