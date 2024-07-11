from typing import Optional

METADATA =\
{
	'name': 'V-TURN Demo',
	'description': 'Next generation face swapper and enhancer',
	'version': '0.3.0',
	'license': 'V-TURN',
	'author': '',
	'url': 'https://vturn.ir/eng/'
}


def get(key : str) -> Optional[str]:
	if key in METADATA:
		return METADATA.get(key)
	return None
