"""
This code was originally written by James Socol <me@jamessocol.com> and forked
by MemCachier to add in service specific functionality.

See the original here: https://github.com/jsocol/django-pymemcache
"""

try:
    import cPickle as pickle
except ImportError:
    import pickle
from threading import local
from django.core.cache.backends.memcached import BaseMemcachedCache

from . import client

def serialize_pickle(key, value):
    if isinstance(value, str):
        return value, 1
    return pickle.dumps(value), 2

def deserialize_pickle(key, value, flags):
    if flags == 1:
        return value
    if flags == 2:
        return pickle.loads(value)
    raise Exception('Unknown flags for value: {1}'.format(flags))


class MemcacheCache(BaseMemcachedCache):
    """An implementation of a cache binding using pymemcache."""

    def __init__(self, server, params, username=None, password=None):
        import os
        self._local = local()
        self._username = os.environ.get('MEMCACHE_USERNAME', username or params.get('USERNAME'))
        self._password = os.environ.get('MEMCACHE_PASSWORD', password or params.get('PASSWORD'))
        self._server = os.environ.get('MEMCACHE_SERVERS', server)
        if self._server.find(',') >= 0:
            self._server = self._server.split(',')
        else:
            self._server = self._server.split(';')
        super(MemcacheCache, self).__init__(self._server, params,
                                            library=client,
                                            value_not_found_exception=ValueError)

    @property
    def _cache(self):
        client = getattr(self._local, 'client', None)
        if client:
            return client

        # pymemcached uses cache options as kwargs to the __init__ method.
        options = {
            'serializer': serialize_pickle,
            'deserializer': deserialize_pickle,
        }
        if self._options:
            options.update(**self._options)
        host, port = self._servers[0].split(':')
        server = (host, int(port))

        client = self._lib.Client(server, **options)
        self._local.client = client

        if self._username is not None and self._password is not None:
            client.set_sasl_auth(self._username, self._password)
        return client

    def close(self, **kwargs): None

