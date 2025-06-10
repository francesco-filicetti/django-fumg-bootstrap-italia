import os
from setuptools import find_packages, setup

with open(os.path.join(os.path.dirname(__file__), 'README.md')) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='django-fumg-bootstrap-italia',
    version='1.0.0',
    packages=find_packages(),
    include_package_data=True,
    license='Apache 2.0',
    description="Django theme for Fondazione Università Magna Graecia based on Bootstrap Italia theme",
    long_description=README,
    long_description_content_type='text/markdown',
    url='',
    author='Francesco Filicetti',
    author_email='easyweb.wa@gmail.com',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: 2.0',
        'Framework :: Django :: 3.0',
        'Framework :: Django :: 4.0',
        'Framework :: Django :: 5.0',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
    ],
    install_requires=[
        'design-django-theme',
    ]
)
