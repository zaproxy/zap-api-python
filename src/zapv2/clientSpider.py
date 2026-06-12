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


class clientSpider(object):

    def __init__(self, zap):
        self.zap = zap

    def status(self, scanid):
        """
        Gets the status of a client spider scan.
        This component is optional and therefore the API will only work if it is installed
        """
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'clientSpider/view/status/', {'scanId': scanid})))

    @property
    def option_action_wait_time_in_secs(self):
        """
        Gets the action wait time option.
        This component is optional and therefore the API will only work if it is installed
        """
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'clientSpider/view/optionActionWaitTimeInSecs/')))

    @property
    def option_browser_id(self):
        """
        Gets the browser ID option.
        This component is optional and therefore the API will only work if it is installed
        """
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'clientSpider/view/optionBrowserId/')))

    @property
    def option_initial_load_time_in_secs(self):
        """
        Gets the initial page load time option.
        This component is optional and therefore the API will only work if it is installed
        """
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'clientSpider/view/optionInitialLoadTimeInSecs/')))

    @property
    def option_max_children(self):
        """
        Gets the maximum children option.
        This component is optional and therefore the API will only work if it is installed
        """
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'clientSpider/view/optionMaxChildren/')))

    @property
    def option_max_depth(self):
        """
        Gets the maximum crawl depth option.
        This component is optional and therefore the API will only work if it is installed
        """
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'clientSpider/view/optionMaxDepth/')))

    @property
    def option_max_duration(self):
        """
        Gets the maximum duration option.
        This component is optional and therefore the API will only work if it is installed
        """
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'clientSpider/view/optionMaxDuration/')))

    @property
    def option_max_scans_in_ui(self):
        """
        Gets the maximum scans in the UI option.
        This component is optional and therefore the API will only work if it is installed
        """
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'clientSpider/view/optionMaxScansInUi/')))

    @property
    def option_page_load_time_in_secs(self):
        """
        Gets the page load time option.
        This component is optional and therefore the API will only work if it is installed
        """
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'clientSpider/view/optionPageLoadTimeInSecs/')))

    @property
    def option_scope_check(self):
        """
        Gets the scope check option.
        This component is optional and therefore the API will only work if it is installed
        """
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'clientSpider/view/optionScopeCheck/')))

    @property
    def option_shutdown_time_in_secs(self):
        """
        Gets the shutdown time option.
        This component is optional and therefore the API will only work if it is installed
        """
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'clientSpider/view/optionShutdownTimeInSecs/')))

    @property
    def option_thread_count(self):
        """
        Gets the number of browser windows to open option.
        This component is optional and therefore the API will only work if it is installed
        """
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'clientSpider/view/optionThreadCount/')))

    @property
    def option_logout_avoidance(self):
        """
        Gets whether or not the spider avoids clicking logout elements.
        This component is optional and therefore the API will only work if it is installed
        """
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'clientSpider/view/optionLogoutAvoidance/')))

    def scan(self, browser=None, url=None, contextname=None, username=None, subtreeonly=None, maxcrawldepth=None, pageloadtime=None, actionwaittime=None, numberofbrowsers=None, scopecheck=None, logoutavoidance=None, apikey=''):
        """
        Starts a client spider scan.
        This component is optional and therefore the API will only work if it is installed
        """
        params = {}
        if browser is not None:
            params['browser'] = browser
        if url is not None:
            params['url'] = url
        if contextname is not None:
            params['contextName'] = contextname
        if username is not None:
            params['userName'] = username
        if subtreeonly is not None:
            params['subtreeOnly'] = subtreeonly
        if maxcrawldepth is not None:
            params['maxCrawlDepth'] = maxcrawldepth
        if pageloadtime is not None:
            params['pageLoadTime'] = pageloadtime
        if actionwaittime is not None:
            params['actionWaitTime'] = actionwaittime
        if numberofbrowsers is not None:
            params['numberOfBrowsers'] = numberofbrowsers
        if scopecheck is not None:
            params['scopeCheck'] = scopecheck
        if logoutavoidance is not None:
            params['logoutAvoidance'] = logoutavoidance
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'clientSpider/action/scan/', params)))

    def stop(self, scanid, apikey=''):
        """
        Stops a client spider scan.
        This component is optional and therefore the API will only work if it is installed
        """
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'clientSpider/action/stop/', {'scanId': scanid})))

    def set_option_browser_id(self, string, apikey=''):
        """
        Sets the browser ID option.
        This component is optional and therefore the API will only work if it is installed
        """
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'clientSpider/action/setOptionBrowserId/', {'String': string})))

    def set_option_scope_check(self, string, apikey=''):
        """
        Sets the scope check option.
        This component is optional and therefore the API will only work if it is installed
        """
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'clientSpider/action/setOptionScopeCheck/', {'String': string})))

    def set_option_action_wait_time_in_secs(self, integer, apikey=''):
        """
        Sets the action wait time option.
        This component is optional and therefore the API will only work if it is installed
        """
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'clientSpider/action/setOptionActionWaitTimeInSecs/', {'Integer': integer})))

    def set_option_initial_load_time_in_secs(self, integer, apikey=''):
        """
        Sets the initial page load time option.
        This component is optional and therefore the API will only work if it is installed
        """
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'clientSpider/action/setOptionInitialLoadTimeInSecs/', {'Integer': integer})))

    def set_option_logout_avoidance(self, boolean, apikey=''):
        """
        Sets whether or not the spider should avoid clicking logout elements.
        This component is optional and therefore the API will only work if it is installed
        """
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'clientSpider/action/setOptionLogoutAvoidance/', {'Boolean': boolean})))

    def set_option_max_children(self, integer, apikey=''):
        """
        Sets the maximum children option.
        This component is optional and therefore the API will only work if it is installed
        """
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'clientSpider/action/setOptionMaxChildren/', {'Integer': integer})))

    def set_option_max_depth(self, integer, apikey=''):
        """
        Sets the maximum crawl depth option.
        This component is optional and therefore the API will only work if it is installed
        """
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'clientSpider/action/setOptionMaxDepth/', {'Integer': integer})))

    def set_option_max_duration(self, integer, apikey=''):
        """
        Sets the maximum duration option.
        This component is optional and therefore the API will only work if it is installed
        """
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'clientSpider/action/setOptionMaxDuration/', {'Integer': integer})))

    def set_option_max_scans_in_ui(self, integer, apikey=''):
        """
        Sets the maximum scans in the UI option.
        This component is optional and therefore the API will only work if it is installed
        """
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'clientSpider/action/setOptionMaxScansInUi/', {'Integer': integer})))

    def set_option_page_load_time_in_secs(self, integer, apikey=''):
        """
        Sets the page load time option.
        This component is optional and therefore the API will only work if it is installed
        """
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'clientSpider/action/setOptionPageLoadTimeInSecs/', {'Integer': integer})))

    def set_option_shutdown_time_in_secs(self, integer, apikey=''):
        """
        Sets the shutdown time option.
        This component is optional and therefore the API will only work if it is installed
        """
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'clientSpider/action/setOptionShutdownTimeInSecs/', {'Integer': integer})))

    def set_option_thread_count(self, integer, apikey=''):
        """
        Sets the number of browser windows to open option.
        This component is optional and therefore the API will only work if it is installed
        """
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'clientSpider/action/setOptionThreadCount/', {'Integer': integer})))
