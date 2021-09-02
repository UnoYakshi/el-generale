"""
General-purpose utility methods that can be applied to any project.
"""

from typing import Any

# import Singleton as Singleton


def is_primitive(obj: Any) -> bool:
    """
    Checks if the given object is of primitive type or not...
    Primitive types are: string, integer, float, boolean, `type`, `function`...
    """
    return isinstance(obj, (str, int, float, bool, type)) or (callable(obj) and not isclass(obj))


def noneptr(*args, **kwargs) -> None:
    """Callable None..."""
    return None


