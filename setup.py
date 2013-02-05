#!/usr/bin/env python
#
# Copyright (C) 2007 SIOS Technology, Inc.
# Copyright (C) 2011 Umea Universitet, Sweden
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
#
import sys

from distutils.core import  Command
from setuptools import setup

install_requires=[
    # core dependencies
    'decorator',
    'paste',
    'zope.interface',
    'repoze.who == 1.0.18'
    ]

# only for Python 2.6
if sys.version_info < (2,7):
    install_requires.append('importlib')

setup(
    name='pysaml2',
    version='1.0.0dev',
    description='Python implementation of SAML Version 2 to for instance be used in a WSGI environment',
    author='Roland Hedberg',
    author_email='roland.hedberg@adm.umu.se',
    license='Apache 2.0',
    url='https://github.com/rohe/pysaml2',

    packages=['saml2', 'xmldsig', 'xmlenc', 's2repoze', 's2repoze.plugins',
              "saml2/profile", "saml2/schema", "saml2/extension"],

    package_dir = {'':'src'},
    package_data={'': ['xml/*.xml']},

    classifiers = ["Development Status :: 4 - Beta",
        "License :: OSI Approved :: Apache Software License",
        "Topic :: Software Development :: Libraries :: Python Modules"],

    scripts=["tools/parse_xsd2.py", "tools/make_metadata.py"],

    tests_require=[
        'pyasn1',
        'pymongo',
        'python-memcached',
        'pytest',
        ],

    install_requires=install_requires,

    extras_require={
        'cjson': ['python-cjson'],
        'pyasn1': ['pyasn1'],
        'pymongo': ['pymongo'],
        'python-memcached': ['python-memcached']
    },

    zip_safe=False,

    cmdclass = {},
)
