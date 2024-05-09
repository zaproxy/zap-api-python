# Contributing to zap-api-python

## Updating the Generated Files

Most of the API code is generated from the ZAP java source code.

To regenerate the API code you will need the repos [zaproxy](https://github.com/zaproxy/zaproxy) and [zap-extensions](https://github.com/zaproxy/zap-extensions) checked out at the same level as this one.

You should typically generate the core API calls from the latest release tag e.g.:

```
cd zaproxy
git fetch upstream -t
git checkout tags/v2.13.0
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

## Changelog

Note that you should also update the `CHANGELOG.md` file to state whatever has been changed.