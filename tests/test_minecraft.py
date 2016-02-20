"""

The MIT License (MIT)

Copyright (c) 2015-2016 Mark Rogaski.

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

"""

from json import loads

from .context import ludo
from .context import minecraft

def test_init():
    c = minecraft.Client()
    assert  isinstance(c, ludo.Client)

def test_status(monkeypatch):
    def query(self, request, **kwargs):
        return loads("""[
                            {"minecraft.net":"green"},
                            {"session.minecraft.net":"green"},
                            {"account.mojang.com":"green"},
                            {"auth.mojang.com":"green"},
                            {"skins.minecraft.net":"green"},
                            {"authserver.mojang.com":"green"},
                            {"sessionserver.mojang.com":"green"},
                            {"api.mojang.com":"green"},
                            {"textures.minecraft.net":"green"}
                        ]""") 

    monkeypatch.setattr('ludo.Client._query', query)
    c = minecraft.Client()
    r = c.status()
    assert r['minecraft.net'] == 'green'
    assert r['session.minecraft.net'] == 'green'
    assert r['account.mojang.com'] == 'green'
    assert r['auth.mojang.com'] == 'green'
    assert r['skins.minecraft.net'] == 'green'
    assert r['authserver.mojang.com'] == 'green'
    assert r['sessionserver.mojang.com'] == 'green'
    assert r['api.mojang.com'] == 'green'
    assert r['textures.minecraft.net'] == 'green'

