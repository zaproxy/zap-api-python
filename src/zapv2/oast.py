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


class oast(object):

    def __init__(self, zap):
        self.zap = zap

    @property
    def get_active_scan_service(self):
        """
        Gets the service used with the active scanner, if any.
        This component is optional and therefore the API will only work if it is installed
        """
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'oast/view/getActiveScanService/')))

    @property
    def get_services(self):
        """
        Gets all of the services.
        This component is optional and therefore the API will only work if it is installed
        """
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'oast/view/getServices/')))

    @property
    def get_boast_options(self):
        """
        Gets the BOAST options.
        This component is optional and therefore the API will only work if it is installed
        """
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'oast/view/getBoastOptions/')))

    @property
    def get_callback_options(self):
        """
        Gets the Callback options.
        This component is optional and therefore the API will only work if it is installed
        """
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'oast/view/getCallbackOptions/')))

    @property
    def get_interactsh_options(self):
        """
        Gets the Interactsh options.
        This component is optional and therefore the API will only work if it is installed
        """
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'oast/view/getInteractshOptions/')))

    @property
    def get_days_to_keep_records(self):
        """
        Gets the number of days the OAST records will be kept for.
        This component is optional and therefore the API will only work if it is installed
        """
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'oast/view/getDaysToKeepRecords/')))

    def set_active_scan_service(self, name, apikey=''):
        """
        Sets the service used with the active scanner.
        This component is optional and therefore the API will only work if it is installed
        """
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'oast/action/setActiveScanService/', {'name': name})))

    def set_boast_options(self, server, pollinsecs, apikey=''):
        """
        Sets the BOAST options.
        This component is optional and therefore the API will only work if it is installed
        """
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'oast/action/setBoastOptions/', {'server': server, 'pollInSecs': pollinsecs})))

    def set_callback_options(self, localaddress, remoteaddress, port, apikey=''):
        """
        Sets the Callback options.
        This component is optional and therefore the API will only work if it is installed
        """
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'oast/action/setCallbackOptions/', {'localAddress': localaddress, 'remoteAddress': remoteaddress, 'port': port})))

    def set_interactsh_options(self, server, pollinsecs, authtoken, apikey=''):
        """
        Sets the Interactsh options.
        This component is optional and therefore the API will only work if it is installed
        """
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'oast/action/setInteractshOptions/', {'server': server, 'pollInSecs': pollinsecs, 'authToken': authtoken})))

    def set_days_to_keep_records(self, days, apikey=''):
        """
        Sets the number of days the OAST records will be kept for.
        This component is optional and therefore the API will only work if it is installed
        """
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'oast/action/setDaysToKeepRecords/', {'days': days})))
