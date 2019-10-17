#!/usr/bin/python

from setuptools import setup, find_packages
from codecs import open

REQUIREMENTS = [
    'networkx==2.2',
    'elementals',
    'sark',
    'pydocstyle==3.0.0',
    'flake8',
    'click',
    'numpy==1.16.5',
    'scipy==1.2.2',
    'scikit-learn==0.20.3',
]

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='Karta',
    version='1.2.0',
    description='IDA plugin for identifying and matching open-source libraries in (huge) '
                'binaries',
    author='Eyal Itkin',
    author_email='eyalit@checkpoint.com',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/CheckPointSW/Karta',
    license='MIT',
    packages=find_packages(),
    install_requires=REQUIREMENTS,
    classifiers=[
        "Programming Language :: Python :: 2",
        "License :: OSI Approved :: MIT License (MIT License)",
        "Operating System :: OS Independent",
    ],
    zip_safe=False
)
