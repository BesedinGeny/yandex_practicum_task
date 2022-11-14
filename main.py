from checkers import *
from common.entry_point import EntryPoint
from name_validotors import *


if __name__ == "__main__":
	resources = dict(
		external_checker=ExternalChecker,
		external_name_validator=ExternalNameValidator,
		internal_name_validator=InternalNameValidator
	)
	main_service = EntryPoint(**resources)
	doc_path = main_service.get_arguments()
	print(main_service(doc_path))
