# Zed Attack Proxy (ZAP) and its related class files.
#
# ZAP is an HTTP/HTTPS proxy for assessing web application security.
#
# Copyright 2017 the ZAP development team
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


class stats(object):

    def __init__(self, zap):
        self.zap = zap

    def stats(self, keyprefix=None):
        """
        Statistics
        """
        params = {}
        if keyprefix is not None:
            params['keyPrefix'] = keyprefix
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'stats/view/stats/', params)))

    def all_sites_stats(self, keyprefix=None):
        """
        Gets all of the site based statistics, optionally filtered by a key prefix
        """
        params = {}
        if keyprefix is not None:
            params['keyPrefix'] = keyprefix
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'stats/view/allSitesStats/', params)))

    def site_stats(self, site, keyprefix=None):
        """
        Gets all of the global statistics, optionally filtered by a key prefix
        """
        params = {'site': site}
        if keyprefix is not None:
            params['keyPrefix'] = keyprefix
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'stats/view/siteStats/', params)))

    @property
    def option_statsd_host(self):
        """
        Gets the Statsd service hostname
        """
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'stats/view/optionStatsdHost/')))

    @property
    def option_statsd_port(self):
        """
        Gets the Statsd service port
        """
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'stats/view/optionStatsdPort/')))

    @property
    def option_statsd_prefix(self):
        """
        Gets the prefix to be applied to all stats sent to the configured Statsd service
        """
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'stats/view/optionStatsdPrefix/')))

    @property
    def option_in_memory_enabled(self):
        """
        Returns 'true' if in memory statistics are enabled, otherwise returns 'false'
        """
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'stats/view/optionInMemoryEnabled/')))

    @property
    def option_statsd_enabled(self):
        """
        Returns 'true' if a Statsd server has been correctly configured, otherwise returns 'false'
        """
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'stats/view/optionStatsdEnabled/')))

    def clear_stats(self, keyprefix=None, apikey=''):
        """
        Clears all of the statistics
        """
        params = {'apikey': apikey}
        if keyprefix is not None:
            params['keyPrefix'] = keyprefix
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'stats/action/clearStats/', params)))

    def set_option_statsd_host(self, string, apikey=''):
        """
        Sets the Statsd service hostname, supply an empty string to stop using a Statsd service
        """
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'stats/action/setOptionStatsdHost/', {'String': string, 'apikey': apikey})))

    def set_option_statsd_prefix(self, string, apikey=''):
        """
        Sets the prefix to be applied to all stats sent to the configured Statsd service
        """
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'stats/action/setOptionStatsdPrefix/', {'String': string, 'apikey': apikey})))

    def set_option_in_memory_enabled(self, boolean, apikey=''):
        """
        Sets whether in memory statistics are enabled
        """
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'stats/action/setOptionInMemoryEnabled/', {'Boolean': boolean, 'apikey': apikey})))

    def set_option_statsd_port(self, integer, apikey=''):
        """
        Sets the Statsd service port
        """
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'stats/action/setOptionStatsdPort/', {'Integer': integer, 'apikey': apikey})))
