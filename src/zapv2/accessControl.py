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


class accessControl(object):

    def __init__(self, zap):
        self.zap = zap

    def get_scan_progress(self, contextid):
        """
        Gets the Access Control scan progress (percentage integer) for the given context ID.
        This component is optional and therefore the API will only work if it is installed
        """
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'accessControl/view/getScanProgress/', {'contextId': contextid})))

    def get_scan_status(self, contextid):
        """
        Gets the Access Control scan status (description string) for the given context ID.
        This component is optional and therefore the API will only work if it is installed
        """
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'accessControl/view/getScanStatus/', {'contextId': contextid})))

    def scan(self, contextid, userid, scanasunauthuser=None, raisealert=None, alertrisklevel=None, apikey=''):
        """
        Starts an Access Control scan with the given context ID and user ID. (Optional parameters: user ID for Unauthenticated user, boolean identifying whether or not Alerts are raised, and the Risk level for the Alerts.) [This assumes the Access Control rules were previously established via ZAP gui and the necessary Context exported/imported.]
        This component is optional and therefore the API will only work if it is installed
        """
        params = {'contextId': contextid, 'userId': userid, 'apikey': apikey}
        if scanasunauthuser is not None:
            params['scanAsUnAuthUser'] = scanasunauthuser
        if raisealert is not None:
            params['raiseAlert'] = raisealert
        if alertrisklevel is not None:
            params['alertRiskLevel'] = alertrisklevel
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'accessControl/action/scan/', params)))

    def write_htm_lreport(self, contextid, filename, apikey=''):
        """
        Generates an Access Control report for the given context ID and saves it based on the provided filename (path). 
        This component is optional and therefore the API will only work if it is installed
        """
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'accessControl/action/writeHTMLreport/', {'contextId': contextid, 'fileName': filename, 'apikey': apikey})))
