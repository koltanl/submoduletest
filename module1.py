#!/usr/bin/env python3
"""
Submodule 1 - Basic functionality
"""

def hello_from_module1():
    """Return a greeting from module 1"""
    return "Hello from Submodule 1!"

def get_module_info():
    """Return information about this module"""
    return {
        "name": "submodule1",
        "version": "1.0.0",
        "description": "First test submodule"
    }

if __name__ == "__main__":
    print(hello_from_module1())
    print(f"Module info: {get_module_info()}") 