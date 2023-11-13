### Release to PyPi

Example commands use the version `0.0.X`, it should be replaced accordingly to the version being released.

Ensure the version is right in `pyproject.toml`.

Tag (and push) the new version:

    git tag -s 0.0.X -m "Version 0.0.X."
    git push upstream 0.0.X

(Checkout the tag and ensure the working copy is clean.)

Build the distribution (source and wheel) files:

     poetry build

Upload to PyPi:

     poetry publish

The user must have permissions to upload to the `zaproxy` package.
