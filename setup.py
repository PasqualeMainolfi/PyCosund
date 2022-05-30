from setuptools import setup, find_packages


NAME = "PyCsound"
VERSION = "1.0.0"
DESCRIPTION = "Working with Csound in python..."


setup(
    name=NAME,
    version=VERSION,
    author="Pasquale Mainolfi",
    author_email="<mnlpql@gmail.com>",
    description=DESCRIPTION,
    keywords=["csound", "sound", "sound synthesis", "python"],
    packages=find_packages(exclude=("test")),
    classifiers=[
        "Programming Language :: Python :: 3"
    ],
    install_requires=["numpy", "matplotlib"]
)
