#!/usr/bin/env python

"""
Standard build script.
"""

from __future__ import print_function

from os.path import dirname, join

try:
    from setuptools import setup, find_packages
except ImportError:
    print("You must have setuptools installed to use setup.py. Exiting...")
    raise SystemExit(1)

__docformat__ = 'restructuredtext'

# Import requirements
with open(join(dirname(__file__), 'requirements.txt')) as f:
    required = f.read().splitlines()

# Import extra requirements
with open(join(dirname(__file__), 'requirements-extra.txt')) as f:
    extra_required = f.read().splitlines()

setup(
    name="python-owasp-zap",
    version="1.0.0",
    description="OWASP ZAP API client. Supported versions: 2.4",
    install_requires=required,
    extras_require={
        'performance': extra_required,
    },
    long_description="OWASP Zed Attack Proxy API python client",
    author="ZAP development team",
    author_email='',
    url="https://www.owasp.org/index.php/OWASP_Zed_Attack_Proxy_Project",
    download_url="https://github.com/zaproxy/zap-api-python/archive/master.zip",
    platforms=['any'],
    license="ASL2.0",
    packages=find_packages(),
    classifiers=[
        'License :: OSI Approved :: Apache Software License',
        'Topic :: Security',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Intended Audience :: Developers',
        'Intended Audience :: Information Technology',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python'],
)
