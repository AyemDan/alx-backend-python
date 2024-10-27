#!/usr/bin/env python3

from typing import Any, TypeVar, Mapping

T = TypeVar('T')


def safely_get_value(dct: Mapping[Any, T], key: Any, default: T = None) -> T:
    if key in dct:
        return dct[key]
    else:
        return default
