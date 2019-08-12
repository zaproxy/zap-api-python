# Zed Attack Proxy (ZAP) and its related class files.
#
# ZAP is an HTTP/HTTPS proxy for assessing web application security.
#
# Copyright 2019 the ZAP development team
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


class localProxies(object):

    def __init__(self, zap):
        self.zap = zap

    @property
    def additional_proxies(self):
        """
        Gets all of the additional proxies that have been configured.
        """
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'localProxies/view/additionalProxies/')))

    def add_additional_proxy(self, address, port, behindnat=None, alwaysdecodezip=None, removeunsupportedencodings=None, apikey=''):
        """
        Adds an new proxy using the details supplied.
        """
        params = {'address': address, 'port': port, 'apikey': apikey}
        if behindnat is not None:
            params['behindNat'] = behindnat
        if alwaysdecodezip is not None:
            params['alwaysDecodeZip'] = alwaysdecodezip
        if removeunsupportedencodings is not None:
            params['removeUnsupportedEncodings'] = removeunsupportedencodings
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'localProxies/action/addAdditionalProxy/', params)))

    def remove_additional_proxy(self, address, port, apikey=''):
        """
        Removes the additional proxy with the specified address and port.
        """
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'localProxies/action/removeAdditionalProxy/', {'address': address, 'port': port, 'apikey': apikey})))
