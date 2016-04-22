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

try:
	# High performance json library
	import ujson as json
except ImportError:
	import json

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


class _ZAP(object):
	"""
	Client API implementation for integrating with ZAP v2.
	"""

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
