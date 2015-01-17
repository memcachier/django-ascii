from setuptools import setup, find_packages

from memcachier_django import __version__

setup(
    name = 'memcachier-django-ascii',
    version = __version__,
    description = 'Django cache backend supporting MemCachier service',
    long_description = open('README.md').read(),
    author = 'MemCachier',
    author_email = 'support@memcachier.com',
    url = 'https://github.com/memcachier/django-ascii',
    packages = find_packages(),
    install_requires = ['pymemcache', 'Django>=1.3'],
    license = 'BSD',
    classifiers = [
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'Framework :: Django',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'License :: OSI Approved :: Apache Software License',
        'Topic :: Database'
    ],
)

