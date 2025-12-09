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


class client(object):

    def __init__(self, zap):
        self.zap = zap

    def report_object(self, objectjson, apikey=''):
        """
        This component is optional and therefore the API will only work if it is installed
        """
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'client/action/reportObject/', {'objectJson': objectjson})))

    def report_event(self, eventjson, apikey=''):
        """
        This component is optional and therefore the API will only work if it is installed
        """
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'client/action/reportEvent/', {'eventJson': eventjson})))

    def report_zest_statement(self, statementjson, apikey=''):
        """
        This component is optional and therefore the API will only work if it is installed
        """
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'client/action/reportZestStatement/', {'statementJson': statementjson})))

    def report_zest_script(self, scriptjson, apikey=''):
        """
        This component is optional and therefore the API will only work if it is installed
        """
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'client/action/reportZestScript/', {'scriptJson': scriptjson})))

    def export_client_map(self, pathyaml, apikey=''):
        """
        Exports the Client Map to a file.
        This component is optional and therefore the API will only work if it is installed
        """
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'client/action/exportClientMap/', {'pathYaml': pathyaml})))
