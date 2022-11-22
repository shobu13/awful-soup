"""Python setup.py for awful_soup package"""
import io
import os
from setuptools import find_packages, setup


def read(*paths, **kwargs):
    """Read the contents of a text file safely.
    >>> read("awful_soup", "VERSION")
    '0.1.0'
    >>> read("README.md")
    ...
    """

    content = ""
    with io.open(
        os.path.join(os.path.dirname(__file__), *paths),
        encoding=kwargs.get("encoding", "utf8"),
    ) as open_file:
        content = open_file.read().strip()
    return content


def read_requirements(path):
    return [
        line.strip()
        for line in read(path).split("\n")
        if not line.startswith(('"', "#", "-", "git+"))
    ]


setup(
    name="awful_soup",
    version=read("awful_soup", "VERSION"),
    description="Awesome awful_soup created by shobu13",
    url="https://github.com/shobu13/awful-soup/",
    long_description=read("README.md"),
    long_description_content_type="text/markdown",
    author="shobu13",
    packages=find_packages(exclude=["tests", ".github"]),
    install_requires=read_requirements("requirements.txt"),
    entry_points={
        "console_scripts": ["awful_soup = awful_soup.__main__:main"]
    },
    extras_require={"test": read_requirements("requirements-test.txt")},
)
