# memcachier-django-ascii

This package provides a memcached cache backend for Django using
[pymemcache](https://github.com/pinterest/pymemcache). We generally
prefer [pylibmc](https://github.com/lericson/pylibmc) but it depends
on a [libmemcached](http://libmemcached.org) which can sometimes cause
issues. Pymemcache is a pure python client.

This package only works with the ASCII protocol and a single memcache
server.

*NOTE:* In general we recommend
[django-pylibmc](https://github.com/jbalogh/django-pylibmc/), but in
rare situations this package works better.

## MemCachier & Authentication

This backend only supports the memcached ASCII protocol, which
normally doesn't support authentication. MemCachier requires
authentication, and adds it in very simply by requiring all new
connections issue a set:

```
$ set <username> 0 0 <password length>\r\n
$ <password>\r\n
```

formatted as above to communicate credentials.

## Requirements

Requires Django 1.3+. It was written and tested on Python 2.7.

## Installation

Get it from pypi:

```
$ pip install memcachier-django-ascii
```

or github:

```
$ pip install -e git://github.com/memcachier/django-ascii.git
```

## Usage

Your cache backend should look something like this:

```
CACHES = {
    'default': {
        'BACKEND': 'memcache_fix.backend.PyMemcacheCache',
        'OPTIONS': {
            'no_delay': True,
            'connect_timeout': 2,
            'timeout': 2,
        }
    }
}
```

*NOTE*: The backend currently only supports connecting to one server.

## Configuration with Environment Variables

Optionally, the memcached connection can be configured with
environment variables (on platforms like Heroku). To do so, declare
the following variables:

```
MEMCACHE_SERVERS
MEMCACHE_USERNAME
MEMCACHE_PASSWORD
```

## Author

Forked from [django-pymemcache](https://github.com/jsocol/django-pymemcache).

## Get involved!

We are happy to receive bug reports, fixes, documentation enhancements,
and other improvements.

Please report bugs via the
[github issue tracker](http://github.com/memcachier/django-ascii/issues).

Master [git repository](http://github.com/memcachier/django-ascii):

* `git clone git://github.com/memcachier/django-ascii.git`

## Licensing

This library is licensed under the Apache Software License 2.0

