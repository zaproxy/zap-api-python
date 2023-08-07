from setuptools import setup
import os

VERSION = "0.1.0"


def get_long_description():
    with open(
        os.path.join(os.path.dirname(os.path.abspath(__file__)), "README.md"),
        encoding="utf8",
    ) as fp:
        return fp.read()


setup(
    name="python-owasp-zap-v2.4",
    description="python-owasp-zap-v2.4 is now zaproxy",
    long_description=get_long_description(),
    long_description_content_type="text/markdown",
    version=VERSION,
    packages=[],
    install_requires=["zaproxy"],
    classifiers=["Development Status :: 7 - Inactive"],
)
