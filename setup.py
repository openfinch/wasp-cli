
from setuptools import setup, find_packages
from wasp.core.version import get_version

VERSION = get_version()

f = open('README.md', 'r')
LONG_DESCRIPTION = f.read()
f.close()

setup(
    name='wasp',
    version=VERSION,
    description='Web Application Stinger Proxy',
    long_description=LONG_DESCRIPTION,
    long_description_content_type='text/markdown',
    author='Josh Finch',
    author_email='finch@ologist.io',
    url='https://github.com/ologist/wasp',
    license='unlicensed',
    packages=find_packages(exclude=['ez_setup', 'tests*']),
    package_data={'wasp': ['templates/*']},
    include_package_data=True,
    entry_points="""
        [console_scripts]
        wasp = wasp.main:main
    """,
)
