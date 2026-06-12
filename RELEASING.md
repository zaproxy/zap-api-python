## Releasing

Example commands use the version `0.x.0`, it should be replaced accordingly to the version being released.

### Update the Changelog

Change `## [Unreleased]` to `## [0.x.0] - yyyy-mm-dd` 

Change `[Unreleased]: <link>...HEAD` to `[0.x.0] <link>...0.x.0` 

Submit a PR and wait for it to be merged.

### Release to PyPi

Ensure the version is right in `pyproject.toml`.

Tag (and push) the new version:

    git tag -s 0.0.X -m "Version 0.x.0"
    git push upstream 0.x.0

The workflow [Release PyPI](https://github.com/zaproxy/zap-api-python/blob/main/.github/workflows/release.yml)
will be triggered by the tag push and release to PyPI.

### Update for the Next Version

Increment the version in `pyproject.toml`

Increment the version in `src/zapv2/__init__.py`

Add a new `## [Unreleased]` section at the top 

Add a new `[Unreleased]: <link>0.x.0...HEAD` section at the start of the last section 

Submit a PR and wait for it to be merged.
