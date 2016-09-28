#!/usr/bin/env python
"""
Standard build script.
"""

__docformat__ = 'restructuredtext'


try:
    from setuptools import setup, find_packages
except ImportError:
    print "You must have setuptools installed to use setup.py. Exiting..."
    raise SystemExit(1)


setup(
    name="python-owasp-zap-v2.4",
    version="0.0.9.dev1",
    description="OWASP ZAP 2.5 API client",
    long_description="OWASP Zed Attack Proxy 2.5 API python client",
    author="ZAP development team",
    author_email='',
    url="https://www.owasp.org/index.php/OWASP_Zed_Attack_Proxy_Project",
    download_url="https://github.com/zaproxy/zaproxy/releases/tag/2.5.0",
    platforms=['any'],

    license="ASL2.0",

    package_dir={
        '': 'src',
    },
    packages=find_packages('src'),

    classifiers=[
        'License :: OSI Approved :: Apache Software License',
        'Development Status :: 5 - Production/Stable',
        'Topic :: Security',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Intended Audience :: Developers',
        'Intended Audience :: Information Technology',
        'Programming Language :: Python'],
)
