# OWASP ZAP Python API

[![Version](https://img.shields.io/pypi/v/python-owasp-zap-v2.4.svg)](https://pypi.python.org/pypi/python-owasp-zap-v2.4)
[![License](https://img.shields.io/badge/license-Apache%202-4EB1BA.svg)](https://www.apache.org/licenses/LICENSE-2.0.html)
[![Build Status](https://api.travis-ci.org/zaproxy/zap-api-python.svg?branch=master)](https://travis-ci.org/zaproxy/zap-api-python)

The Python implementation to access the [OWASP ZAP API](https://github.com/zaproxy/zaproxy/wiki/ApiDetails). For more information
about OWASP ZAP consult the (main) [OWASP ZAP project](https://github.com/zaproxy/zaproxy/).

## How to Obtain

The latest released version can be downloaded from the [https://pypi.python.org/pypi/python-owasp-zap-v2.4](https://pypi.python.org/pypi/python-owasp-zap-v2.4) using:

    pip install python-owasp-zap-v2.4

## Getting Help

For help using OWASP ZAP API refer to:
  * [Examples](https://github.com/zaproxy/zap-api-python/tree/master/src/examples) - collection of examples using the library;
  * [Wiki](https://github.com/zaproxy/zaproxy/wiki/ApiDetails)
  * [OWASP ZAP User Group](https://groups.google.com/group/zaproxy-users) - for asking questions;
  * IRC: irc.mozilla.org #websectools (eg [using Mibbit](http://chat.mibbit.com/?server=irc.mozilla.org%3A%2B6697&channel=%23websectools)) - chat with core ZAP developers (European office hours usually best)
  
## Issues

To report issues related to OWASP ZAP API, bugs and enhancements requests, use the [issue tracker of the main OWASP ZAP project](https://github.com/zaproxy/zaproxy/issues).

### Release to PyPi

Example commands use the version `0.0.1`, it should be replaced accordingly to the version being released.

Tag (and push) the new version:

    git tag -s 0.0.1 -m "Version 0.0.1."
    git push upstream 0.0.1

(Checkout the tag and ensure the working copy is clean.)

Build the distribution (source and wheel) files:

    python setup.py sdist bdist_wheel --universal

Sign the distribution files:

    gpg --detach-sign -a dist/python-owasp-zap-v2.4-0.0.1.tar.gz
    gpg --detach-sign -a dist/python_owasp_zap_v2.4-0.0.1-py2.py3-none-any.whl

Upload to PyPi:

     twine upload \
         dist/python-owasp-zap-v2.4-0.0.1.tar.gz python-owasp-zap-v2.4-0.0.1.tar.gz.asc \
         dist/python_owasp_zap_v2.4-0.0.1-py2.py3-none-any.whl python_owasp_zap_v2.4-0.0.1-py2.py3-none-any.whl.asc

The user must have permissions to upload to the `python-owasp-zap-v2.4` package.
