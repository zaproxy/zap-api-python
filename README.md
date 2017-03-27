# OWASP ZAP Python API

The Python implementation to access the [OWASP ZAP API](https://github.com/zaproxy/zaproxy/wiki/ApiDetails). For more information
about OWASP ZAP consult the (main) [OWASP ZAP project](https://github.com/zaproxy/zaproxy/).

## How to Obtain

The latest released version can be downloaded from the [https://pypi.python.org/pypi/python-owasp-zap-v2.4](https://pypi.python.org/pypi/python-owasp-zap-v2.4) using:

    pip install python-owasp-zap-v2.4

## Getting Help

For help using OWASP ZAP API refer to:
  * [Examples](https://github.com/zaproxy/zap-api-python/tree/master/src/examples) - collection of examples using the library;
  * [Wiki](https://github.com/zaproxy/zaproxy/wiki/ApiPython)
  * [OWASP ZAP User Group](https://groups.google.com/group/zaproxy-users) - for asking questions;
  * IRC: irc.mozilla.org #websectools (eg [using Mibbit](http://chat.mibbit.com/?server=irc.mozilla.org%3A%2B6697&channel=%23websectools)) - chat with core ZAP developers (European office hours usually best)
  
## Issues

To report issues related to OWASP ZAP API, bugs and enhancements requests, use the [issue tracker of the main OWASP ZAP project](https://github.com/zaproxy/zaproxy/issues).

### Release to PyPi

To build and upload to PyPi you can run the following:

    python setup.py sdist upload

The user must have permissions to upload to the `python-owasp-zap-v2.4` package.
