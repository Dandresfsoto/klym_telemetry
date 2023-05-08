import importlib
from typing import Any

def import_module(package: str, classname: str):
    try:
        print(f"Importing module: {package}.{classname}")
        module = __get_optional_module(package)
        print(module)
        if module:
            return getattr(module, classname)
    except Exception:
        # Do something additional with the exception
        return None


def __get_optional_module(module_path: str) -> Any:
    try:
        return importlib.import_module(module_path)
    except Exception as e:
        print(f"Error importing module {module_path}. Exception: {e}")
        raise