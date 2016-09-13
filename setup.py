from setuptools import setup, find_packages
from ais import version

setup(
    name='ais',
    version=version,
    packages=find_packages(),
    entry_points='''
       [console_scripts]
       ais = ais.cli:cli
    ''',
)
