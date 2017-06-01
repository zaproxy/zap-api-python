# Zed Attack Proxy (ZAP) and its related class files.
#
# ZAP is an HTTP/HTTPS proxy for assessing web application security.
#
# Copyright 2016 the ZAP development team
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


class openapi(object):

    def __init__(self, zap):
        self.zap = zap

    def import_file(self, file, apikey=''):
        """
        Import an Open API definition from a local file.
        This component is optional and therefore the API will only work if it is installed
        """
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'openapi/action/importFile/', {'file': file, 'apikey': apikey})))

    def import_url(self, url, hostoverride=None, apikey=''):
        """
        Import an Open API definition from a URL, hostOverride allows the host to be replaced
        This component is optional and therefore the API will only work if it is installed
        """
        params = {'url': url, 'apikey': apikey}
        if hostoverride is not None:
            params['hostOverride'] = hostoverride
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'openapi/action/importUrl/', params)))
