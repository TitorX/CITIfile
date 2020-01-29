from setuptools import setup
from CITIfile import __version__, __author__


setup(
    name='CITIfile',
    version=__version__,
    author=__author__,
    author_email='titor.sun@gmail.com',
    py_modules=['CITIfile'],
    url='https://github.com/TitorX/CITIfile',
    description='To parse CITI format file to xarray.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    install_requires=[
        "xarray>=0.14.1"
    ],
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3"
    ],
)
