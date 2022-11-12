from ast import FunctionDef, Module
from abc import abstractmethod
from typing import Any, List, Optional, Type, Union


class BaseChecker:
	# todo: Validator
	_current_object: Union[FunctionDef, Module, None] = None
	
	def __init__(self, current_object: Union[FunctionDef, Module, Any]):
		"""current_object - любой элемент AST"""
		self._current_object = current_object
	
	@abstractmethod
	def check(self) -> bool:
		""" Проверка элемента на соблюдения правилу"""
		raise NotImplementedError

	@abstractmethod
	def _check_name(self, name: str) -> bool:
		raise NotImplementedError
	
	def _iter_inner_items(self) -> List:
		"""Возвращает тело элемента, если такое возможно"""
		if hasattr(self._current_object, "body"):
			return self._current_object.body
		else:
			return []
