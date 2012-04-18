#!/usr/bin/env python
from setuptools import setup, find_packages

import nested_formsets

CLASSIFIERS = [
    'Intended Audience :: Developers',    
    'Natural Language :: English',
    'Operating System :: OS Independent',
    'Programming Language :: Python'    
]

KEYWORDS = 'django admin formset nested inline'


setup(name = 'Django nested formsets',
    version = nested_formsets.__version__,
    description = """Manage formsets in formsets""",
    author = nested_formsets.__author__,
    url = "https://github.com/oxys-net/django-nested-formsets",
    packages = find_packages(),
    classifiers = CLASSIFIERS,
    keywords = KEYWORDS,
    zip_safe = True
)