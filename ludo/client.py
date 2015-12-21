##########################################################################
#
# The MIT License (MIT)
#
# Copyright (c) 2015 Mark Rogaski
#
# Permission is hereby granted, free of charge, to any person obtaining a
# copy of this software and associated documentation files (the "Software"),
# to deal in the Software without restriction, including without limitation
# the rights to use, copy, modify, merge, publish, distribute, sublicense,
# and/or sell copies of the Software, and to permit persons to whom the
# Software is furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included
# in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS
# OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
# IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY
# CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,
# TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
# SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
#
##########################################################################

from __future__ import (absolute_import, division,
                        print_function, unicode_literals)
from builtins import *

import requests


class Client(object):
    """Base class for an API client."""

    def __init__(self, url=None, cache=None, timeout=10, obj=None):
        self._url = url
        self._cache = cache
        self._proxy = proxy
        self._timeout = timeout
        self._obj = obj

    def _query(self, req, **kwargs):
        s = requests.Session()
        prepped = s.prepare_request(req)
        r = s.send(prepped, timeout=self._timeout, **kwargs)
        if r.status_code != 200:
            raise APIError('%s %s %s %s' % (prepped.method,
                                            prepped.url,
                                            r.status_code,
                                            r.reason))
        else:
            return r.json()


class MinecraftClient(MinecraftClient):
    """Minecraft API client."""

    def __init__(self,
                 url={
                     'api': 'https://api.mojang.com',
                     'status': 'https://status.mojang.com',
                     'session': 'https://sessionserver.mojang.com',
                 }
                 ** kwargs):
        super().__init__(url=url, **kwargs)

