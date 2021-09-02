from typing import List, Any


def extract_path(obj, path: List[Any]) -> Any:
    item = object
    for path_el in path:
        item = item.get(path_el)
