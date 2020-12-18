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


class alert(object):

    def __init__(self, zap):
        self.zap = zap

    def alert(self, id):
        """
        Gets the alert with the given ID, the corresponding HTTP message can be obtained with the 'messageId' field and 'message' API method
        """
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'alert/view/alert/', {'id': id})))

    def alerts(self, baseurl=None, start=None, count=None, riskid=None):
        """
        Gets the alerts raised by ZAP, optionally filtering by URL or riskId, and paginating with 'start' position and 'count' of alerts
        """
        params = {}
        if baseurl is not None:
            params['baseurl'] = baseurl
        if start is not None:
            params['start'] = start
        if count is not None:
            params['count'] = count
        if riskid is not None:
            params['riskId'] = riskid
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'alert/view/alerts/', params)))

    def alerts_summary(self, baseurl=None):
        """
        Gets number of alerts grouped by each risk level, optionally filtering by URL
        """
        params = {}
        if baseurl is not None:
            params['baseurl'] = baseurl
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'alert/view/alertsSummary/', params)))

    def number_of_alerts(self, baseurl=None, riskid=None):
        """
        Gets the number of alerts, optionally filtering by URL or riskId
        """
        params = {}
        if baseurl is not None:
            params['baseurl'] = baseurl
        if riskid is not None:
            params['riskId'] = riskid
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'alert/view/numberOfAlerts/', params)))

    def alerts_by_risk(self, url=None, recurse=None):
        """
        Gets a summary of the alerts, optionally filtered by a 'url'. If 'recurse' is true then all alerts that apply to urls that start with the specified 'url' will be returned, otherwise only those on exactly the same 'url' (ignoring url parameters)
        """
        params = {}
        if url is not None:
            params['url'] = url
        if recurse is not None:
            params['recurse'] = recurse
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'alert/view/alertsByRisk/', params)))

    def alert_counts_by_risk(self, url=None, recurse=None):
        """
        Gets a count of the alerts, optionally filtered as per alertsPerRisk
        """
        params = {}
        if url is not None:
            params['url'] = url
        if recurse is not None:
            params['recurse'] = recurse
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'alert/view/alertCountsByRisk/', params)))

    def delete_all_alerts(self, apikey=''):
        """
        Deletes all alerts of the current session.
        """
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'alert/action/deleteAllAlerts/', {'apikey': apikey})))

    def delete_alert(self, id, apikey=''):
        """
        Deletes the alert with the given ID. 
        """
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'alert/action/deleteAlert/', {'id': id, 'apikey': apikey})))

    def update_alerts_confidence(self, ids, confidenceid, apikey=''):
        """
        Update the confidence of the alerts.
        """
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'alert/action/updateAlertsConfidence/', {'ids': ids, 'confidenceId': confidenceid, 'apikey': apikey})))

    def update_alerts_risk(self, ids, riskid, apikey=''):
        """
        Update the risk of the alerts.
        """
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'alert/action/updateAlertsRisk/', {'ids': ids, 'riskId': riskid, 'apikey': apikey})))

    def update_alert(self, id, name, riskid, confidenceid, description, param=None, attack=None, otherinfo=None, solution=None, references=None, evidence=None, cweid=None, wascid=None, apikey=''):
        """
        Update the alert with the given ID, with the provided details.
        """
        params = {'id': id, 'name': name, 'riskId': riskid, 'confidenceId': confidenceid, 'description': description, 'apikey': apikey}
        if param is not None:
            params['param'] = param
        if attack is not None:
            params['attack'] = attack
        if otherinfo is not None:
            params['otherInfo'] = otherinfo
        if solution is not None:
            params['solution'] = solution
        if references is not None:
            params['references'] = references
        if evidence is not None:
            params['evidence'] = evidence
        if cweid is not None:
            params['cweId'] = cweid
        if wascid is not None:
            params['wascId'] = wascid
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'alert/action/updateAlert/', params)))

    def add_alert(self, messageid, name, riskid, confidenceid, description, param=None, attack=None, otherinfo=None, solution=None, references=None, evidence=None, cweid=None, wascid=None, apikey=''):
        """
        Add an alert associated with the given message ID, with the provided details. (The ID of the created alert is returned.)
        """
        params = {'messageId': messageid, 'name': name, 'riskId': riskid, 'confidenceId': confidenceid, 'description': description, 'apikey': apikey}
        if param is not None:
            params['param'] = param
        if attack is not None:
            params['attack'] = attack
        if otherinfo is not None:
            params['otherInfo'] = otherinfo
        if solution is not None:
            params['solution'] = solution
        if references is not None:
            params['references'] = references
        if evidence is not None:
            params['evidence'] = evidence
        if cweid is not None:
            params['cweId'] = cweid
        if wascid is not None:
            params['wascId'] = wascid
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'alert/action/addAlert/', params)))
