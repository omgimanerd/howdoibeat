#!/usr/bin/python
# This file contains decorators used in the project.
# Author: alvin.lin.dev@gmail.com (Alvin Lin)

def cache(fn):
    cache = {}
    def wrapped_fn(*args, **kwargs):
        if repr(args) in cache:
            return cache[repr(args)]
        result = fn(*args, **kwargs)
        cache[repr(args)] = result
        return result
    return wrapped_fn
