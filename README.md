# OWASP ZAP Python API

[![Version](https://img.shields.io/pypi/v/python-owasp-zap-v2.4.svg)](https://pypi.python.org/pypi/python-owasp-zap-v2.4)
[![License](https://img.shields.io/badge/license-Apache%202-4EB1BA.svg)](https://www.apache.org/licenses/LICENSE-2.0.html)

The Python implementation to access the [OWASP ZAP API](https://www.zaproxy.org/docs/api/). For more information
about OWASP ZAP consult the (main) [OWASP ZAP project](https://github.com/zaproxy/zaproxy/).

## How to Obtain

The latest released version can be downloaded from the [https://pypi.python.org/pypi/python-owasp-zap-v2.4](https://pypi.python.org/pypi/python-owasp-zap-v2.4) using:

    pip install python-owasp-zap-v2.4

## Getting Help

For help using OWASP ZAP API refer to:
  * [Examples](https://github.com/zaproxy/zap-api-python/tree/master/src/examples) - collection of examples using the library;
  * [API Documentation](https://www.zaproxy.org/docs/api/)
  * [OWASP ZAP User Group](https://groups.google.com/group/zaproxy-users) - for asking questions;
  
## Issues

To report issues related to OWASP ZAP API, bugs and enhancements requests, use the [issue tracker of the main OWASP ZAP project](https://github.com/zaproxy/zaproxy/issues).

## Updating the Generated Files

Most of the API code is generated from the ZAP java source code.

To regenerate the API code you will need the repos [zaproxy](https://github.com/zaproxy/zaproxy) and [zap-extensions](https://github.com/zaproxy/zap-extensions) checked out at the same level as this one.

You should typically generate the core API calls from the latest release tag e.g.:

```
cd zaproxy
git fetch upstream -t
git checkout tags/v2.11.1
./gradlew generatePythonApiEndpoints
cd ..
```

The add-on APIs can be generated from the zap-extensions `main` branch:

```
cd zap-extensions
git pull upstream main
./gradle generatePythonZapApiClientFiles --continue
cd ..
```

The above commands will update the files in `src/zapv2`.

If any new files are created then they should be manually added to `src/zapv2/__init__.py` as per the existing files.

Note that you should also update the `CHANGELOG.md` file to state whatever has been changed.
