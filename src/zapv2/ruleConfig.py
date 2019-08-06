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


class ruleConfig(object):

    def __init__(self, zap):
        self.zap = zap

    def rule_config_value(self, key):
        """
        Show the specified rule configuration
        """
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'ruleConfig/view/ruleConfigValue/', {'key': key})))

    @property
    def all_rule_configs(self):
        """
        Show all of the rule configurations
        """
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'ruleConfig/view/allRuleConfigs/')))

    def reset_rule_config_value(self, key, apikey=''):
        """
        Reset the specified rule configuration, which must already exist
        """
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'ruleConfig/action/resetRuleConfigValue/', {'key': key, 'apikey': apikey})))

    def reset_all_rule_config_values(self, apikey=''):
        """
        Reset all of the rule configurations
        """
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'ruleConfig/action/resetAllRuleConfigValues/', {'apikey': apikey})))

    def set_rule_config_value(self, key, value=None, apikey=''):
        """
        Set the specified rule configuration, which must already exist
        """
        params = {'key': key, 'apikey': apikey}
        if value is not None:
            params['value'] = value
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'ruleConfig/action/setRuleConfigValue/', params)))
