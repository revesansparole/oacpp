#!/usr/bin/env python
# -*- coding: utf-8 -*-

# {# pkglts, pysetup.kwds
# format setup arguments

from setuptools import setup, find_packages


short_descr = "Test package for CPP Python interaction"
readme = open('README.rst').read()
history = open('HISTORY.rst').read().replace('.. :changelog:', '')


def parse_requirements(fname):
    with open(fname, 'r') as f:
        txt = f.read()

    reqs = []
    for line in txt.splitlines():
        line = line.strip()
        if len(line) > 0 and not line.startswith("#"):
            reqs.append(line)

    return reqs

# find version number in src/oacpp/version.py
version = {}
with open("src/oacpp/version.py") as fp:
    exec(fp.read(), version)


setup_kwds = dict(
    name='oacpp',
    version=version["__version__"],
    description=short_descr,
    long_description=readme + '\n\n' + history,
    author="revesansparole, ",
    author_email="revesansparole@gmail.com, ",
    url='https://github.com/revesansparole/oacpp',
    license='cecill-c',
    zip_safe=False,

    packages=find_packages('src'),
    package_dir={'': 'src'},
    install_requires=parse_requirements("requirements.txt"),
    tests_require=parse_requirements("dvlpt_requirements.txt"),
    entry_points={},
    keywords='',
    test_suite='nose.collector',
)
# #}
# change setup_kwds below before the next pkglts tag

sk = setup_kwds

bp = "build-scons"
# sk['build_prefix'] = bp
sk['scons_scripts'] = ['SConstruct']
sk['lib_dirs'] = {'lib': bp + '/lib'}
sk['inc_dirs'] = {'include': bp + '/include'}
sk['bin_dirs'] = {'bin': bp + '/bin'}

sk['include_package_data'] = True
sk['package_data'] = {'': ['*.pyd', '*.so']}

sk['entry_points']['wralea'] = ['oacpp = oacpp_wralea']

# do not change things below
# {# pkglts, pysetup.call
setup(**setup_kwds)
# #}
