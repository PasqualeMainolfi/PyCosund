from setuptools import setup, find_packages


NAME = "PyCsound"
VERSION = "1.1.0"
DESCRIPTION = "Working with Csound in Python..."

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

license = "LICENSE.txt"

setup(
    name=NAME,
    version=VERSION,
    author="Pasquale Mainolfi",
    author_email="<mnlpql@gmail.com>",
    description=DESCRIPTION,
    long_description=long_description,
    long_description_content_type="text/markdown",
    keywords=["csound", "sound", "sound synthesis", "python"],
    packages=find_packages(exclude=("test")),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
        "License :: OSI Approved :: MIT License",
    ],
    install_requires=["numpy", "matplotlib"],
    license_file=license
)
