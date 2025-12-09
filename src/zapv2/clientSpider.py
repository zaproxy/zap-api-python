# Zed Attack Proxy (ZAP) and its related class files.
#
# ZAP is an HTTP/HTTPS proxy for assessing web application security.
#
# Copyright 2025 the ZAP development team
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
This file was automatically generated.
"""

import six


class clientSpider(object):

    def __init__(self, zap):
        self.zap = zap

    def status(self, scanid):
        """
        Gets the status of a client spider scan.
        This component is optional and therefore the API will only work if it is installed
        """
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'clientSpider/view/status/', {'scanId': scanid})))

    def scan(self, browser=None, url=None, contextname=None, username=None, subtreeonly=None, maxcrawldepth=None, pageloadtime=None, numberofbrowsers=None, scopecheck=None, apikey=''):
        """
        Starts a client spider scan.
        This component is optional and therefore the API will only work if it is installed
        """
        params = {}
        if browser is not None:
            params['browser'] = browser
        if url is not None:
            params['url'] = url
        if contextname is not None:
            params['contextName'] = contextname
        if username is not None:
            params['userName'] = username
        if subtreeonly is not None:
            params['subtreeOnly'] = subtreeonly
        if maxcrawldepth is not None:
            params['maxCrawlDepth'] = maxcrawldepth
        if pageloadtime is not None:
            params['pageLoadTime'] = pageloadtime
        if numberofbrowsers is not None:
            params['numberOfBrowsers'] = numberofbrowsers
        if scopecheck is not None:
            params['scopeCheck'] = scopecheck
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'clientSpider/action/scan/', params)))

    def stop(self, scanid, apikey=''):
        """
        Stops a client spider scan.
        This component is optional and therefore the API will only work if it is installed
        """
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'clientSpider/action/stop/', {'scanId': scanid})))
