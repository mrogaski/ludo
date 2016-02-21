##########################################################################
#
# The MIT License (MIT)
#
# Copyright (c) 2015-2016 Mark Rogaski
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
import json

from requests import Request

import ludo


class Client(ludo.Client):
    """Minecraft API client."""

    def status(self, url='https://status.mojang.com/check'):
        request = Request('GET', url)
        response = self._query(request)
        return { k: v for d in response for k, v in d.items() }

    def user(self, name_list, url='https://api.mojang.com/profiles/minecraft'):
        request = Request('POST', url, json=name_list)
        response = self._query(request)
        lookup = {d['name'].lower(): d for d in response}
        return {k: lookup[k.lower()] for k in name_list}
    
    