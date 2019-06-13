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


class alertFilter(object):

    def __init__(self, zap):
        self.zap = zap

    def alert_filter_list(self, contextid):
        """
        Lists the alert filters of the context with the given ID.
        This component is optional and therefore the API will only work if it is installed
        """
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'alertFilter/view/alertFilterList/', {'contextId': contextid})))

    def add_alert_filter(self, contextid, ruleid, newlevel, url=None, urlisregex=None, parameter=None, enabled=None, apikey=''):
        """
        Adds a new alert filter for the context with the given ID. 
        This component is optional and therefore the API will only work if it is installed
        """
        params = {'contextId': contextid, 'ruleId': ruleid, 'newLevel': newlevel, 'apikey': apikey}
        if url is not None:
            params['url'] = url
        if urlisregex is not None:
            params['urlIsRegex'] = urlisregex
        if parameter is not None:
            params['parameter'] = parameter
        if enabled is not None:
            params['enabled'] = enabled
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'alertFilter/action/addAlertFilter/', params)))

    def remove_alert_filter(self, contextid, ruleid, newlevel, url=None, urlisregex=None, parameter=None, enabled=None, apikey=''):
        """
        Removes an alert filter from the context with the given ID.
        This component is optional and therefore the API will only work if it is installed
        """
        params = {'contextId': contextid, 'ruleId': ruleid, 'newLevel': newlevel, 'apikey': apikey}
        if url is not None:
            params['url'] = url
        if urlisregex is not None:
            params['urlIsRegex'] = urlisregex
        if parameter is not None:
            params['parameter'] = parameter
        if enabled is not None:
            params['enabled'] = enabled
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'alertFilter/action/removeAlertFilter/', params)))
