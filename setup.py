#!/usr/bin/env python

import os
from setuptools import find_packages, setup

with open(os.path.join(os.path.dirname(__file__), 'README.md')) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='voltaire.website',
    version='0.0.0+git',
    packages=find_packages(exclude=['ez_setup']),
    namespace_packages=['voltaire'],
    include_package_data=True,
    license='MIT',
    description='website',
    long_description=README,
    url='https://github.com/voltaire/website',
    author='Jon Chen',
    author_email='bsd@voltaire.sh',
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
    ],
    install_requires=[
        'alembic==0.7.6',
        'Flask==0.10.1',
        'Flask-Migrate==1.4.0',
        'Flask-OpenID==1.2.4',
        'Flask-Script==2.0.5',
        'Flask-SQLAlchemy==2.0',
        'itsdangerous==0.24',
        'Jinja2==2.7.3',
        'Mako==1.0.1',
        'MarkupSafe==0.23',
        'SQLAlchemy==1.0.4',
        'Werkzeug==0.10.4',
        'podhub.meh==0.1.12',
        'psycopg2==2.6',
    ],
    scripts=[
        'scripts/voltairemc_site',
    ],
)
