"""
This code was originally written by James Socol <me@jamessocol.com> and forked
by MemCachier to add in service specific functionality.

See the original here: https://github.com/jsocol/django-pymemcache
"""

try:
    from pymemcache import client
except ImportError:
    raise InvalidCacheBackendError('Could not import pymemcache.')

""" Compatability layer for pymemcache and python-memcache """
class Client(client.Client):
    # this just fixes some API holes between python-memcached and pymemcache
    set_multi = client.Client.set_many
    get_multi = client.Client.get_many
    delete_multi = client.Client.delete_many
    disconnect_all = client.Client.quit

    def __init__(self, server, **params):
        self._username = None
        self._password = None
        super(Client, self).__init__(server, **params)

    def _connect(self):
        super(Client, self)._connect()
        if self._username is not None and self._password is not None:
            self.set(self._username, self._password)

    def set_sasl_auth(self, username, password):
        self._username = username
        self._password = password


