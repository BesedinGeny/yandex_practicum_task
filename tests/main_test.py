import pytest

from checkers import ExternalChecker
from common.entry_point import EntryPoint
from name_validotors import ExternalNameValidator, InternalNameValidator

test_input_params = [
	("docs/test1.py", True),
	("docs/test2.py", False),
	("docs/test3.py", False),
	("docs/test4.py", True),
	("docs/test5.py", False),
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
