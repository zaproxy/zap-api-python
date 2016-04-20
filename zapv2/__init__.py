# Zed Attack Proxy (ZAP) and its related class files.
#
# ZAP is an HTTP/HTTPS proxy for assessing web application security.
#
# Copyright 2012 ZAP development team
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""
Client implementation for using the ZAP pentesting proxy remotely.
"""

try:
    # High performance json library
    import ujson as json
except ImportError:
    import json

import os
import six
import requests
import requests_cache
requests_cache.install_cache('zap_cache', backend="memory")

# Improving Python 2 & 3 compatibility
if six.PY2:
    from urllib import urlencode, urlopen
    from urlparse import urlparse, urljoin
else:
    from urllib.parse import urlparse, urlencode, urljoin
    from urllib.request import urlopen

from .acsrf import acsrf
from .ascan import ascan
from .ajaxSpider import ajaxSpider
from .authentication import authentication
from .autoupdate import autoupdate
from .brk import brk
from .context import context
from .core import core
from .forcedUser import forcedUser
from .httpSessions import httpSessions
from .importLogFiles import importLogFiles
from .params import params
from .pnh import pnh
from .pscan import pscan
from .reveal import reveal
from .script import script
from .search import search
from .selenium import selenium
from .sessionManagement import sessionManagement
from .spider import spider
from .users import users

__docformat__ = 'restructuredtext'


class ZapError(Exception):
    """
    Base ZAP exception.
    """
    pass


class ZAPv2(object):
    """
    Client API implementation for integrating with ZAP v2.
    """

    # base JSON api url
    base = 'http://zap/JSON/'
    # base OTHER api url
    base_other = 'http://zap/OTHER/'

    def __init__(self, proxies=None):
        """
        Creates an instance of the ZAP api client.

        Example:
        >>> z=ZAPv2()

        Example with custom proxies
        >>> my_proxies = {'http': 'http://10.0.1.1:9090', 'https': 'http://10.0.1.1:9009'}
        >>> z=ZAPv2(proxies=my_proxies)

        :param proxies: Dict with the scheme as key and PROXY url as value
        :type proxies: dict(str:str)

        """
        if proxies is None:
            # Set default
            proxies = {'http': 'http://127.0.0.1:8080',
                       'https': 'http://127.0.0.1:8080'}
        self.__proxies = proxies

        self.acsrf = acsrf(self)
        self.ajaxSpider = ajaxSpider(self)
        self.ascan = ascan(self)
        self.authentication = authentication(self)
        self.autoupdate = autoupdate(self)
        self.brk = brk(self)
        self.context = context(self)
        self.core = core(self)
        self.forcedUser = forcedUser(self)
        self.httpsessions = httpSessions(self)
        self.importLogFiles = importLogFiles(self)
        self.params = params(self)
        self.pnh = pnh(self)
        self.pscan = pscan(self)
        self.reveal = reveal(self)
        self.script = script(self)
        self.search = search(self)
        self.selenium = selenium(self)
        self.sessionManagement = sessionManagement(self)
        self.spider = spider(self)
        self.users = users(self)

    def _expect_ok(self, json_data):
        """
        Checks that we have an OK response, else raises an exception.

        :param json_data: the json data to look at.
        :type json_data: json
        """
        if isinstance(json_data, list) and json_data[0] == u'OK':
            return json_data

        raise ZapError(*json_data.values())

    def urlopen(self, *args, **kwargs):
        """
        Opens a url forcing the proxies to be used.

        :param args: all non-keyword arguments.
        :type args: list()

        :param kwarg: all non-keyword arguments.
        :type kwarg: dict()
        """
        # return urlopen(*args, **kwargs).read()
        return requests.get(*args, proxies=self.__proxies).text

    def status_code(self, *args, **kwargs):
        """
		Open a url forcing the proxies to be used.

        :param args: all non-keyword arguments.
        :type args: list()

        :param kwarg: all non-keyword arguments.
        :type kwarg: dict()
		"""
        # return urlopen(*args, **kwargs).getcode()
        return requests.get(*args, proxies=self.__proxies).status_code

    def _request(self, url, get=None):
        """
        Shortcut for a GET request.

        :param url: the url to GET at.
        :type url: str

        :param get: the dictionary to turn into GET variables.
        :type get: dict(str:str)
        """
        if get is None:
            get = {}

        return json.loads(self.urlopen("%s?%s" % (url, urlencode(get))))

    def _request_other(self, url, get=None):
        """
        Shortcut for an API OTHER GET request.

        :param url: the url to GET at.
        :type url: str

        :param get: the dictionary to turn into GET variables.
        :type get: dict(str:str)
        """
        if get is None:
            get = {}

        return self.urlopen("%s?%s" % (url, urlencode(get)))
