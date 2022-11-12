from name_validotors.base_validator import BaseNameValidator


class InternalNameValidator(BaseNameValidator):
	""" Валидатор имени функции внутри класса """
	
	@classmethod
	def validate(cls, name: str) -> bool:
		return name[0].islower()
