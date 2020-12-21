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

__docformat__ = 'restructuredtext'
__version__ = '0.0.19'

import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning

from .accessControl import accessControl
from .acsrf import acsrf
from .alert import alert
from .alertFilter import alertFilter
from .ascan import ascan
from .ajaxSpider import ajaxSpider
from .authentication import authentication
from .authorization import authorization
from .autoupdate import autoupdate
from .brk import brk
from .context import context
from .core import core
from .exportreport import exportreport
from .forcedUser import forcedUser
from .graphql import graphql
from .httpSessions import httpSessions
from .importLogFiles import importLogFiles
from .importurls import importurls
from .localProxies import localProxies
from .openapi import openapi
from .params import params
from .pnh import pnh
from .pscan import pscan
from .replacer import replacer
from .reveal import reveal
from .revisit import revisit
from .ruleConfig import ruleConfig
from .script import script
from .search import search
from .selenium import selenium
from .sessionManagement import sessionManagement
from .soap import soap
from .spider import spider
from .stats import stats
from .users import users
from .wappalyzer import wappalyzer
from .websocket import websocket


class ZAPv2(object):
    """
    Client API implementation for integrating with ZAP v2.
    """
    base = 'http://zap/JSON/'
    base_other = 'http://zap/OTHER/'

    def __init__(self, proxies=None, apikey=None, validate_status_code=False):
        """
        Creates an instance of the ZAP api client.

        :Parameters:
           - `proxies`: dictionary of ZAP proxies to use.

        Note that all of the other classes in this directory are generated
        new ones will need to be manually added to this file
        """
        self.__proxies = proxies or {
            'http': 'http://127.0.0.1:8080',
            'https': 'http://127.0.0.1:8080'
        }
        self.__apikey = apikey
        self.__validate_status_code=validate_status_code

        self.accessControl = accessControl(self)
        self.acsrf = acsrf(self)
        self.alert = alert(self)
        self.alertFilter = alertFilter(self)
        self.ajaxSpider = ajaxSpider(self)
        self.ascan = ascan(self)
        self.authentication = authentication(self)
        self.authorization = authorization(self)
        self.autoupdate = autoupdate(self)
        self.brk = brk(self)
        self.context = context(self)
        self.core = core(self)
        self.exportreport = exportreport(self)
        self.forcedUser = forcedUser(self)
        self.graphql = graphql(self)
        self.httpsessions = httpSessions(self)
        self.importLogFiles = importLogFiles(self)
        self.importurls = importurls(self)
        self.localProxies = localProxies(self)
        self.openapi = openapi(self)
        self.params = params(self)
        self.pnh = pnh(self)
        self.pscan = pscan(self)
        self.replacer = replacer(self)
        self.reveal = reveal(self)
        self.revisit = revisit(self)
        self.ruleConfig = ruleConfig(self)
        self.script = script(self)
        self.search = search(self)
        self.selenium = selenium(self)
        self.sessionManagement = sessionManagement(self)
        self.soap = soap(self)
        self.spider = spider(self)
        self.stats = stats(self)
        self.users = users(self)
        self.wappalyzer = wappalyzer(self)
        self.websocket = websocket(self)

        # not very nice, but prevents warnings when accessing the ZAP API via https
        requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

        # Currently create a new session for each request to prevent request failing
        # e.g. when polling the spider status
        #self.session = requests.Session()
        #if apikey is not None:
        #  self.session.headers['X-ZAP-API-Key'] = apikey

    def urlopen(self, url, *args, **kwargs):
        """
        Opens a url forcing the proxies to be used.

        :Parameters:
           - `args`:  all non-keyword arguments.
           - `kwargs`: all other keyword arguments.
        """
        # Must never leak the API key via proxied requests
        return requests.get(url, proxies=self.__proxies, verify=False, *args, **kwargs).text

    def _request_api(self, url, query=None):
        """
        Shortcut for an API request. Will always add the apikey (if defined)

        :Parameters:
           - `url`: the url to GET at.
        """
        if not url.startswith('http://zap/'):
          # Only allow requests to the API so that we never leak the apikey
          raise ValueError('A non ZAP API url was specified ' + url)

        # In theory we should be able to reuse the session,
        # but there have been problems with that
        self.session = requests.Session()
        if self.__apikey is not None:
          self.session.headers['X-ZAP-API-Key'] = self.__apikey

        query = query or {}
        if self.__apikey is not None:
          # Add the apikey to get params for backwards compatibility
          if not query.get('apikey'):
            query['apikey'] = self.__apikey

        response = self.session.get(url, params=query, proxies=self.__proxies, verify=False)

        if (self.__validate_status_code and response.status_code >= 300 and response.status_code < 500):
            raise Exception("Non-successful status code returned from ZAP, which indicates a bad request: "
                                + str(response.status_code)
                                + "response: " + response.text )
        elif (self.__validate_status_code and response.status_code >= 500):
            raise Exception("Non-successful status code returned from ZAP, which indicates a ZAP internal error: "
                                + str(response.status_code)
                                + "response: " + response.text )
        return response

    def _request(self, url, get=None):
        """
        Shortcut for a GET request.

        :Parameters:
           - `url`: the url to GET at.
           - `get`: the dictionary to turn into GET variables.
        """
        data = self._request_api(url, get)
        return data.json()

    def _request_other(self, url, get=None):
        """
        Shortcut for an API OTHER GET request.

        :Parameters:
           - `url`: the url to GET at.
           - `get`: the dictionary to turn into GET variables.
        """
        data = self._request_api(url, get)
        return data.text
