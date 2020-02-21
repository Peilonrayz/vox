#!/usr/bin/env python
from setuptools import find_packages, setup

try:
    import ConfigParser as configparser
except ImportError:
    import configparser

with open("README.rst") as f:
    LONG_DESCRIPTION = f.read()

config = configparser.ConfigParser()
config.read("setup.cfg")

setup(
    name="vox",
    version=config.get("src", "version"),
    license="MIT",
    description="Runs linters seperately and outputs them as one.",
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/x-rst",
    author="Peilonrayz",
    author_email="peilonrayz@gmail.com",
    url="https://peilonrayz.github.io/vox",
    project_urls={
        "Bug Tracker": "https://github.com/Peilonrayz/vox/issues",
        "Documentation": "https://peilonrayz.github.io/vox",
        "Source Code": "https://github.com/Peilonrayz/vox",
    },
    packages=find_packages("src"),
    package_dir={"": "src"},
    include_package_data=True,
    zip_safe=False,
    install_requires=["nox", "parse", "typing_extensions", "mypy_extensions"],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
    keywords="linter",
    # entry_points={"console_scripts": ["vox=vox.__main__:main"]},
)
