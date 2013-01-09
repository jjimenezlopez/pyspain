# -*- coding: utf-8 -*-

from distutils.core import setup

version = __import__('pyspain').get_version()

setup(
    name = "pyspain",
    version = version,
    #url = '',
    author = 'Jose Jiménez',
    author_email = 'jjimenezlopez@gmail.com',
    description = 'A XML based database that stores provinces and localities from Spain.',
    #download_url = '',
    packages = ['pyspain'],
    package_data={'': ['db/*']},
    include_package_data=True,
    license = 'GPL',
    classifiers = [
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries :: Python Modules',
   ],
)                                                                                          
