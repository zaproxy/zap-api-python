### Release to PyPi

Example commands use the version `0.0.X`, it should be replaced accordingly to the version being released.

Ensure the version is right in `pyproject.toml`.

Tag (and push) the new version:

    git tag -s 0.0.X -m "Version 0.0.X."
    git push upstream 0.0.X

The workflow [Release PyPI](https://github.com/zaproxy/zap-api-python/blob/main/.github/workflows/release.yml)
will be triggered by the tag push and release to PyPI.
