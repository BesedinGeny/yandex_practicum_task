import pytest

from checkers import ExternalChecker
from common.entry_point import EntryPoint
from name_validotors import ExternalNameValidator, InternalNameValidator

test_input_params = [
	("docs/test1.py", True),  # проверка базового алгоритма
	("docs/test2.py", False),  # проверка базового алгоритма
	("docs/test3.py", False),  # объявление функции внутри if-a
	("docs/test4.py", True),  # пример из ТЗ
	("docs/test5.py", False),  # пример из ТЗ
	("docs/test6.py", False),  # некорректный python-код
	("docs/test7.py", True),  # объявление функции внутри for-a
	("docs/test8.py", False),  # большая вложенность
]


class TestCases:
	@pytest.mark.parametrize("document,expected_result", test_input_params)
	def test_run_app(self, document, expected_result):
		resources = dict(
			external_checker=ExternalChecker,
			external_name_validator=ExternalNameValidator,
			internal_name_validator=InternalNameValidator
		)
		main_service = EntryPoint(**resources)
		result = main_service(document)
		assert result == expected_result
