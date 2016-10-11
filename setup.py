#!/usr/bin/env python
from setuptools import setup, find_packages
import itertools

options = dict(
    name='boaphys',
    version='0.0',
    packages=find_packages(),
    # package_data={'': ['LICENSE', 'MANIFEST.in', 'README.md', 'HISTORY.txt']},
    license='MIT',
    description='Some physics relations.',
    # long_description=open('README.md').read(),
    author='Jan Pipek',
    author_email='jan.pipek@gmail.com',
    url='https://github.com/janpipek/boaphys',
    install_requires = ['numpy'],
    #extras_require = {
    #    'all' : ['dask', 'matplotlib', 'bokeh']
    #},
    entry_points = {
        'console_scripts' : [
        ]
    },
    classifiers=[
        "Development Status :: 3 - Alpha",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Intended Audience :: Developers",
        "Intended Audience :: Information Technology",
        "Intended Audience :: Science/Research",
        "Topic :: Scientific/Engineering",
        "Topic :: Software Development :: Libraries :: Python Modules"
    ]
)

#extras = options['extras_require']
#extras['full'] = list(set(itertools.chain.from_iterable(extras.values())))
setup(**options)
