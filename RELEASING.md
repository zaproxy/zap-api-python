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
