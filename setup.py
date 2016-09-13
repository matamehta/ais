from setuptools import setup, find_packages
from ais import __version__

setup(
    name='ais',
    version=__version__,
    packages=find_packages(),
    entry_points='''
       [console_scripts]
       ais = ais.cli:cli
    ''',
)
