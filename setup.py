#
# Jinja2-Minify
#
# Copyright (C) 2018 Boris Raicheff
# All rights reserved
#


from setuptools import setup


setup(
    name='Jinja2-Minify',
    version='0.1.1',
    description='Jinja2-Minify',
    author='Boris Raicheff',
    author_email='b@raicheff.com',
    url='https://github.com/raicheff/jinja2-minify',
    install_requires=('jinja2', 'cssmin', 'htmlmin', 'jsmin'),
    py_modules=('jinja2_minify',),
)


# EOF
