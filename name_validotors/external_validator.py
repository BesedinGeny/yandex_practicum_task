from name_validotors.base_validator import BaseNameValidator


class ExternalNameValidator(BaseNameValidator):
	""" Валидатор имени функции вне класса"""
	
	@classmethod
	def validate(cls, name: str) -> bool:
		return not name[0].islower()
