# Zed Attack Proxy (ZAP) and its related class files.
#
# ZAP is an HTTP/HTTPS proxy for assessing web application security.
#
# Copyright 2020 the ZAP development team
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


class exportreport(object):

    def __init__(self, zap):
        self.zap = zap

    @property
    def formats(self):
        """
        This component is optional and therefore the API will only work if it is installed
        """
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'exportreport/view/formats/')))

    def generate(self, absolutepath, fileextension, sourcedetails, alertseverity, alertdetails, scanid=None, includepassivealerts=None, apikey=''):
        """
        This component is optional and therefore the API will only work if it is installed
        """
        params = {'absolutePath': absolutepath, 'fileExtension': fileextension, 'sourceDetails': sourcedetails, 'alertSeverity': alertseverity, 'alertDetails': alertdetails, 'apikey': apikey}
        if scanid is not None:
            params['scanId'] = scanid
        if includepassivealerts is not None:
            params['includePassiveAlerts'] = includepassivealerts
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'exportreport/action/generate/', params)))
