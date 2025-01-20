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


class pscan(object):

    def __init__(self, zap):
        self.zap = zap

    @property
    def scan_only_in_scope(self):
        """
        Tells whether or not the passive scan should be performed only on messages that are in scope.
        This component is optional and therefore the API will only work if it is installed
        """
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'pscan/view/scanOnlyInScope/')))

    @property
    def records_to_scan(self):
        """
        The number of records the passive scanner still has to scan.
        This component is optional and therefore the API will only work if it is installed
        """
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'pscan/view/recordsToScan/')))

    @property
    def scanners(self):
        """
        Lists all passive scan rules with their ID, name, enabled state, and alert threshold.
        This component is optional and therefore the API will only work if it is installed
        """
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'pscan/view/scanners/')))

    @property
    def current_rule(self):
        """
        Shows information about the passive scan rule currently being run (if any).
        This component is optional and therefore the API will only work if it is installed
        """
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'pscan/view/currentRule/')))

    @property
    def current_tasks(self):
        """
        Shows information about the passive scan tasks currently being run (if any).
        This component is optional and therefore the API will only work if it is installed
        """
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'pscan/view/currentTasks/')))

    @property
    def max_alerts_per_rule(self):
        """
        Gets the maximum number of alerts a passive scan rule should raise.
        This component is optional and therefore the API will only work if it is installed
        """
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'pscan/view/maxAlertsPerRule/')))

    def set_enabled(self, enabled, apikey=''):
        """
        Sets whether or not the passive scanning is enabled (Note: the enabled state is not persisted).
        This component is optional and therefore the API will only work if it is installed
        """
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'pscan/action/setEnabled/', {'enabled': enabled})))

    def set_scan_only_in_scope(self, onlyinscope, apikey=''):
        """
        Sets whether or not the passive scan should be performed only on messages that are in scope.
        This component is optional and therefore the API will only work if it is installed
        """
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'pscan/action/setScanOnlyInScope/', {'onlyInScope': onlyinscope})))

    def enable_all_scanners(self, apikey=''):
        """
        Enables all passive scan rules.
        This component is optional and therefore the API will only work if it is installed
        """
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'pscan/action/enableAllScanners/', {})))

    def disable_all_scanners(self, apikey=''):
        """
        Disables all passive scan rules.
        This component is optional and therefore the API will only work if it is installed
        """
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'pscan/action/disableAllScanners/', {})))

    def enable_scanners(self, ids, apikey=''):
        """
        Enables passive scan rules.
        This component is optional and therefore the API will only work if it is installed
        """
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'pscan/action/enableScanners/', {'ids': ids})))

    def disable_scanners(self, ids, apikey=''):
        """
        Disables passive scan rules.
        This component is optional and therefore the API will only work if it is installed
        """
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'pscan/action/disableScanners/', {'ids': ids})))

    def set_scanner_alert_threshold(self, id, alertthreshold, apikey=''):
        """
        Sets the alert threshold of a passive scan rule.
        This component is optional and therefore the API will only work if it is installed
        """
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'pscan/action/setScannerAlertThreshold/', {'id': id, 'alertThreshold': alertthreshold})))

    def set_max_alerts_per_rule(self, maxalerts, apikey=''):
        """
        Sets the maximum number of alerts a passive scan rule can raise.
        This component is optional and therefore the API will only work if it is installed
        """
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'pscan/action/setMaxAlertsPerRule/', {'maxAlerts': maxalerts})))

    def disable_all_tags(self, apikey=''):
        """
        Disables all passive scan tags.
        This component is optional and therefore the API will only work if it is installed
        """
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'pscan/action/disableAllTags/', {})))

    def enable_all_tags(self, apikey=''):
        """
        Enables all passive scan tags.
        This component is optional and therefore the API will only work if it is installed
        """
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'pscan/action/enableAllTags/', {})))

    def clear_queue(self, apikey=''):
        """
        Clears the passive scan queue.
        This component is optional and therefore the API will only work if it is installed
        """
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'pscan/action/clearQueue/', {})))
