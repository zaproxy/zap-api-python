#!/usr/bin/env python
"""
Standard build script.
"""

from setuptools import setup, find_packages

__docformat__ = "restructuredtext"
ZAP_VERSION = "2.13"
PACKAGE_VERSION = "0.1.0"

install_dependencies = ("requests", "six")
test_requirements = ("mock", "pyhamcrest", "pylama", "pytest", "requests_mock")
setup(
    name="zaproxy",
    version=PACKAGE_VERSION,
    description=f"ZAP {ZAP_VERSION} API client",
    long_description=f"Zed Attack Proxy {ZAP_VERSION} API Python client",
    author="ZAP Development Team",
    author_email="zaproxy-develop@googlegroups.com",
    url="https://www.zaproxy.org/",
    download_url=f"https://github.com/zaproxy/zap-api-python/releases/tag/{PACKAGE_VERSION}",
    platforms=["any"],
    license="ASL2.0",
    package_dir={
        "": "src",
    },
    packages=find_packages("src"),
    classifiers=[
        "License :: OSI Approved :: Apache Software License",
        "Development Status :: 5 - Production/Stable",
        "Topic :: Security",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Intended Audience :: Developers",
        "Intended Audience :: Information Technology",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
    install_requires=install_dependencies,
    tests_require=test_requirements,
    extras_require={"tests": test_requirements},
)
