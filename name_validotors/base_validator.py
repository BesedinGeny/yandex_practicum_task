from abc import ABC, abstractmethod


class BaseNameValidator(ABC):
	""" Базовый класс валидатора имени"""
	
	@classmethod
	@abstractmethod
	def validate(cls, name: str) -> bool:
		raise NotImplementedError
