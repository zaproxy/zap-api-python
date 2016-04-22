# Zed Attack Proxy (ZAP) and its related class files.
#
# ZAP is an HTTP/HTTPS proxy for assessing web application security.
#
# Copyright 2016 ZAP development team
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

from ..base import _ZAP


class ZAPv24(_ZAP):
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
		>>> z=ZAPv24()

		Example with custom proxies
		>>> my_proxies = {'http': 'http://10.0.1.1:9090', 'https': 'http://10.0.1.1:9090'}
		>>> z=ZAPv24(proxies=my_proxies)

		:param proxies: Dict with the scheme as key and PROXY url as value
		:type proxies: dict(str:str)

		"""
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
