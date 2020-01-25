from setuptools import setup
from CITIfile import __version__, __author__


with open('requirements.txt') as f:
    requirements = f.read().splitlines()


setup(
    name='CITIfile',
    version=__version__,
    author=__author__,
    author_email='titor.sun@gmail.com',
    py_modules=['CITIfile'],
    package_data={
        'CITIfile': ['README.md', 'LICENSE']
    },
    url='https://github.com/TitorX/CITIfile',
    description='To parse CITI format file to xarray.',
    long_description=open('README.md').read(),
    install_requires=requirements,
)
