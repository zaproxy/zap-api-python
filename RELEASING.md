### Release to PyPi

Example commands use the version `0.0.X`, it should be replaced accordingly to the version being released.

Ensure the description is right in `setup.py`.

Tag (and push) the new version:

    git tag -s 0.0.X -m "Version 0.0.X."
    git push upstream 0.0.X

(Checkout the tag and ensure the working copy is clean.)

Build the distribution (source and wheel) files:

    python setup.py sdist bdist_wheel --universal

Upload to PyPi:

     pip install twine
     
     twine upload \
         dist/zaproxy-0.0.X.tar.gz \
         dist/zaproxy-0.0.X-py2.py3-none-any.whl

The user must have permissions to upload to the `zaproxy` package.
