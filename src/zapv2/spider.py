# Zed Attack Proxy (ZAP) and its related class files.
#
# ZAP is an HTTP/HTTPS proxy for assessing web application security.
#
# Copyright 2022 the ZAP development team
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


class spider(object):

    def __init__(self, zap):
        self.zap = zap

    def status(self, scanid=None):
        """
        
        This component is optional and therefore the API will only work if it is installed
        """
        params = {}
        if scanid is not None:
            params['scanId'] = scanid
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'spider/view/status/', params)))

    def results(self, scanid=None):
        """
        
        This component is optional and therefore the API will only work if it is installed
        """
        params = {}
        if scanid is not None:
            params['scanId'] = scanid
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'spider/view/results/', params)))

    def full_results(self, scanid):
        """
        
        This component is optional and therefore the API will only work if it is installed
        """
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'spider/view/fullResults/', {'scanId': scanid})))

    @property
    def scans(self):
        """
        
        This component is optional and therefore the API will only work if it is installed
        """
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'spider/view/scans/')))

    @property
    def excluded_from_scan(self):
        """
        Gets the regexes of URLs excluded from the spider scans.
        This component is optional and therefore the API will only work if it is installed
        """
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'spider/view/excludedFromScan/')))

    @property
    def all_urls(self):
        """
        Returns a list of unique URLs from the history table based on HTTP messages added by the Spider.
        This component is optional and therefore the API will only work if it is installed
        """
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'spider/view/allUrls/')))

    def added_nodes(self, scanid=None):
        """
        Returns a list of the names of the nodes added to the Sites tree by the specified scan.
        This component is optional and therefore the API will only work if it is installed
        """
        params = {}
        if scanid is not None:
            params['scanId'] = scanid
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'spider/view/addedNodes/', params)))

    @property
    def domains_always_in_scope(self):
        """
        Gets all the domains that are always in scope. For each domain the following are shown: the index, the value (domain), if enabled, and if specified as a regex.
        This component is optional and therefore the API will only work if it is installed
        """
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'spider/view/domainsAlwaysInScope/')))

    @property
    def option_domains_always_in_scope(self):
        """
        Use view domainsAlwaysInScope instead.
        This component is optional and therefore the API will only work if it is installed
        """
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'spider/view/optionDomainsAlwaysInScope/')))

    @property
    def option_domains_always_in_scope_enabled(self):
        """
        Use view domainsAlwaysInScope instead.
        This component is optional and therefore the API will only work if it is installed
        """
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'spider/view/optionDomainsAlwaysInScopeEnabled/')))

    @property
    def option_handle_parameters(self):
        """
        
        This component is optional and therefore the API will only work if it is installed
        """
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'spider/view/optionHandleParameters/')))

    @property
    def option_max_children(self):
        """
        Gets the maximum number of child nodes (per node) that can be crawled, 0 means no limit.
        This component is optional and therefore the API will only work if it is installed
        """
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'spider/view/optionMaxChildren/')))

    @property
    def option_max_depth(self):
        """
        Gets the maximum depth the spider can crawl, 0 if unlimited.
        This component is optional and therefore the API will only work if it is installed
        """
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'spider/view/optionMaxDepth/')))

    @property
    def option_max_duration(self):
        """
        
        This component is optional and therefore the API will only work if it is installed
        """
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'spider/view/optionMaxDuration/')))

    @property
    def option_max_parse_size_bytes(self):
        """
        Gets the maximum size, in bytes, that a response might have to be parsed.
        This component is optional and therefore the API will only work if it is installed
        """
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'spider/view/optionMaxParseSizeBytes/')))

    @property
    def option_max_scans_in_ui(self):
        """
        
        This component is optional and therefore the API will only work if it is installed
        """
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'spider/view/optionMaxScansInUI/')))

    @property
    def option_request_wait_time(self):
        """
        
        This component is optional and therefore the API will only work if it is installed
        """
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'spider/view/optionRequestWaitTime/')))

    @property
    def option_skip_url_string(self):
        """
        
        This component is optional and therefore the API will only work if it is installed
        """
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'spider/view/optionSkipURLString/')))

    @property
    def option_thread_count(self):
        """
        
        This component is optional and therefore the API will only work if it is installed
        """
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'spider/view/optionThreadCount/')))

    @property
    def option_user_agent(self):
        """
        
        This component is optional and therefore the API will only work if it is installed
        """
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'spider/view/optionUserAgent/')))

    @property
    def option_accept_cookies(self):
        """
        Gets whether or not a spider process should accept cookies while spidering.
        This component is optional and therefore the API will only work if it is installed
        """
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'spider/view/optionAcceptCookies/')))

    @property
    def option_handle_o_data_parameters_visited(self):
        """
        
        This component is optional and therefore the API will only work if it is installed
        """
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'spider/view/optionHandleODataParametersVisited/')))

    @property
    def option_parse_comments(self):
        """
        
        This component is optional and therefore the API will only work if it is installed
        """
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'spider/view/optionParseComments/')))

    @property
    def option_parse_ds_store(self):
        """
        This component is optional and therefore the API will only work if it is installed
        """
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'spider/view/optionParseDsStore/')))

    @property
    def option_parse_git(self):
        """
        
        This component is optional and therefore the API will only work if it is installed
        """
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'spider/view/optionParseGit/')))

    @property
    def option_parse_robots_txt(self):
        """
        
        This component is optional and therefore the API will only work if it is installed
        """
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'spider/view/optionParseRobotsTxt/')))

    @property
    def option_parse_svn_entries(self):
        """
        
        This component is optional and therefore the API will only work if it is installed
        """
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'spider/view/optionParseSVNEntries/')))

    @property
    def option_parse_sitemap_xml(self):
        """
        
        This component is optional and therefore the API will only work if it is installed
        """
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'spider/view/optionParseSitemapXml/')))

    @property
    def option_post_form(self):
        """
        
        This component is optional and therefore the API will only work if it is installed
        """
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'spider/view/optionPostForm/')))

    @property
    def option_process_form(self):
        """
        
        This component is optional and therefore the API will only work if it is installed
        """
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'spider/view/optionProcessForm/')))

    @property
    def option_send_referer_header(self):
        """
        Gets whether or not the 'Referer' header should be sent while spidering.
        This component is optional and therefore the API will only work if it is installed
        """
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'spider/view/optionSendRefererHeader/')))

    @property
    def option_show_advanced_dialog(self):
        """
        
        This component is optional and therefore the API will only work if it is installed
        """
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'spider/view/optionShowAdvancedDialog/')))

    def scan(self, url=None, maxchildren=None, recurse=None, contextname=None, subtreeonly=None, apikey=''):
        """
        Runs the spider against the given URL (or context). Optionally, the 'maxChildren' parameter can be set to limit the number of children scanned, the 'recurse' parameter can be used to prevent the spider from seeding recursively, the parameter 'contextName' can be used to constrain the scan to a Context and the parameter 'subtreeOnly' allows to restrict the spider under a site's subtree (using the specified 'url').
        This component is optional and therefore the API will only work if it is installed
        """
        params = {'apikey': apikey}
        if url is not None:
            params['url'] = url
        if maxchildren is not None:
            params['maxChildren'] = maxchildren
        if recurse is not None:
            params['recurse'] = recurse
        if contextname is not None:
            params['contextName'] = contextname
        if subtreeonly is not None:
            params['subtreeOnly'] = subtreeonly
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'spider/action/scan/', params)))

    def scan_as_user(self, contextid, userid, url=None, maxchildren=None, recurse=None, subtreeonly=None, apikey=''):
        """
        Runs the spider from the perspective of a User, obtained using the given Context ID and User ID. See 'scan' action for more details.
        This component is optional and therefore the API will only work if it is installed
        """
        params = {'contextId': contextid, 'userId': userid, 'apikey': apikey}
        if url is not None:
            params['url'] = url
        if maxchildren is not None:
            params['maxChildren'] = maxchildren
        if recurse is not None:
            params['recurse'] = recurse
        if subtreeonly is not None:
            params['subtreeOnly'] = subtreeonly
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'spider/action/scanAsUser/', params)))

    def pause(self, scanid, apikey=''):
        """
        
        This component is optional and therefore the API will only work if it is installed
        """
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'spider/action/pause/', {'scanId': scanid, 'apikey': apikey})))

    def resume(self, scanid, apikey=''):
        """
        
        This component is optional and therefore the API will only work if it is installed
        """
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'spider/action/resume/', {'scanId': scanid, 'apikey': apikey})))

    def stop(self, scanid=None, apikey=''):
        """
        
        This component is optional and therefore the API will only work if it is installed
        """
        params = {'apikey': apikey}
        if scanid is not None:
            params['scanId'] = scanid
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'spider/action/stop/', params)))

    def remove_scan(self, scanid, apikey=''):
        """
        
        This component is optional and therefore the API will only work if it is installed
        """
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'spider/action/removeScan/', {'scanId': scanid, 'apikey': apikey})))

    def pause_all_scans(self, apikey=''):
        """
        
        This component is optional and therefore the API will only work if it is installed
        """
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'spider/action/pauseAllScans/', {'apikey': apikey})))

    def resume_all_scans(self, apikey=''):
        """
        
        This component is optional and therefore the API will only work if it is installed
        """
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'spider/action/resumeAllScans/', {'apikey': apikey})))

    def stop_all_scans(self, apikey=''):
        """
        
        This component is optional and therefore the API will only work if it is installed
        """
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'spider/action/stopAllScans/', {'apikey': apikey})))

    def remove_all_scans(self, apikey=''):
        """
        
        This component is optional and therefore the API will only work if it is installed
        """
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'spider/action/removeAllScans/', {'apikey': apikey})))

    def clear_excluded_from_scan(self, apikey=''):
        """
        Clears the regexes of URLs excluded from the spider scans.
        This component is optional and therefore the API will only work if it is installed
        """
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'spider/action/clearExcludedFromScan/', {'apikey': apikey})))

    def exclude_from_scan(self, regex, apikey=''):
        """
        Adds a regex of URLs that should be excluded from the spider scans.
        This component is optional and therefore the API will only work if it is installed
        """
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'spider/action/excludeFromScan/', {'regex': regex, 'apikey': apikey})))

    def add_domain_always_in_scope(self, value, isregex=None, isenabled=None, apikey=''):
        """
        Adds a new domain that's always in scope, using the specified value. Optionally sets if the new entry is enabled (default, true) and whether or not the new value is specified as a regex (default, false).
        This component is optional and therefore the API will only work if it is installed
        """
        params = {'value': value, 'apikey': apikey}
        if isregex is not None:
            params['isRegex'] = isregex
        if isenabled is not None:
            params['isEnabled'] = isenabled
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'spider/action/addDomainAlwaysInScope/', params)))

    def modify_domain_always_in_scope(self, idx, value=None, isregex=None, isenabled=None, apikey=''):
        """
        Modifies a domain that's always in scope. Allows to modify the value, if enabled or if a regex. The domain is selected with its index, which can be obtained with the view domainsAlwaysInScope.
        This component is optional and therefore the API will only work if it is installed
        """
        params = {'idx': idx, 'apikey': apikey}
        if value is not None:
            params['value'] = value
        if isregex is not None:
            params['isRegex'] = isregex
        if isenabled is not None:
            params['isEnabled'] = isenabled
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'spider/action/modifyDomainAlwaysInScope/', params)))

    def remove_domain_always_in_scope(self, idx, apikey=''):
        """
        Removes a domain that's always in scope, with the given index. The index can be obtained with the view domainsAlwaysInScope.
        This component is optional and therefore the API will only work if it is installed
        """
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'spider/action/removeDomainAlwaysInScope/', {'idx': idx, 'apikey': apikey})))

    def enable_all_domains_always_in_scope(self, apikey=''):
        """
        Enables all domains that are always in scope.
        This component is optional and therefore the API will only work if it is installed
        """
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'spider/action/enableAllDomainsAlwaysInScope/', {'apikey': apikey})))

    def disable_all_domains_always_in_scope(self, apikey=''):
        """
        Disables all domains that are always in scope.
        This component is optional and therefore the API will only work if it is installed
        """
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'spider/action/disableAllDomainsAlwaysInScope/', {'apikey': apikey})))

    def set_option_handle_parameters(self, string, apikey=''):
        """
        
        This component is optional and therefore the API will only work if it is installed
        """
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'spider/action/setOptionHandleParameters/', {'String': string, 'apikey': apikey})))

    def set_option_skip_url_string(self, string, apikey=''):
        """
        
        This component is optional and therefore the API will only work if it is installed
        """
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'spider/action/setOptionSkipURLString/', {'String': string, 'apikey': apikey})))

    def set_option_user_agent(self, string, apikey=''):
        """
        
        This component is optional and therefore the API will only work if it is installed
        """
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'spider/action/setOptionUserAgent/', {'String': string, 'apikey': apikey})))

    def set_option_accept_cookies(self, boolean, apikey=''):
        """
        Sets whether or not a spider process should accept cookies while spidering.
        This component is optional and therefore the API will only work if it is installed
        """
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'spider/action/setOptionAcceptCookies/', {'Boolean': boolean, 'apikey': apikey})))

    def set_option_handle_o_data_parameters_visited(self, boolean, apikey=''):
        """
        
        This component is optional and therefore the API will only work if it is installed
        """
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'spider/action/setOptionHandleODataParametersVisited/', {'Boolean': boolean, 'apikey': apikey})))

    def set_option_max_children(self, integer, apikey=''):
        """
        Sets the maximum number of child nodes (per node) that can be crawled, 0 means no limit.
        This component is optional and therefore the API will only work if it is installed
        """
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'spider/action/setOptionMaxChildren/', {'Integer': integer, 'apikey': apikey})))

    def set_option_max_depth(self, integer, apikey=''):
        """
        Sets the maximum depth the spider can crawl, 0 for unlimited depth.
        This component is optional and therefore the API will only work if it is installed
        """
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'spider/action/setOptionMaxDepth/', {'Integer': integer, 'apikey': apikey})))

    def set_option_max_duration(self, integer, apikey=''):
        """
        
        This component is optional and therefore the API will only work if it is installed
        """
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'spider/action/setOptionMaxDuration/', {'Integer': integer, 'apikey': apikey})))

    def set_option_max_parse_size_bytes(self, integer, apikey=''):
        """
        Sets the maximum size, in bytes, that a response might have to be parsed. This allows the spider to skip big responses/files.
        This component is optional and therefore the API will only work if it is installed
        """
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'spider/action/setOptionMaxParseSizeBytes/', {'Integer': integer, 'apikey': apikey})))

    def set_option_max_scans_in_ui(self, integer, apikey=''):
        """
        
        This component is optional and therefore the API will only work if it is installed
        """
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'spider/action/setOptionMaxScansInUI/', {'Integer': integer, 'apikey': apikey})))

    def set_option_parse_comments(self, boolean, apikey=''):
        """
        
        This component is optional and therefore the API will only work if it is installed
        """
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'spider/action/setOptionParseComments/', {'Boolean': boolean, 'apikey': apikey})))

    def set_option_parse_ds_store(self, boolean, apikey=''):
        """
        This component is optional and therefore the API will only work if it is installed
        """
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'spider/action/setOptionParseDsStore/', {'Boolean': boolean, 'apikey': apikey})))

    def set_option_parse_git(self, boolean, apikey=''):
        """
        
        This component is optional and therefore the API will only work if it is installed
        """
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'spider/action/setOptionParseGit/', {'Boolean': boolean, 'apikey': apikey})))

    def set_option_parse_robots_txt(self, boolean, apikey=''):
        """
        
        This component is optional and therefore the API will only work if it is installed
        """
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'spider/action/setOptionParseRobotsTxt/', {'Boolean': boolean, 'apikey': apikey})))

    def set_option_parse_svn_entries(self, boolean, apikey=''):
        """
        
        This component is optional and therefore the API will only work if it is installed
        """
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'spider/action/setOptionParseSVNEntries/', {'Boolean': boolean, 'apikey': apikey})))

    def set_option_parse_sitemap_xml(self, boolean, apikey=''):
        """
        
        This component is optional and therefore the API will only work if it is installed
        """
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'spider/action/setOptionParseSitemapXml/', {'Boolean': boolean, 'apikey': apikey})))

    def set_option_post_form(self, boolean, apikey=''):
        """
        
        This component is optional and therefore the API will only work if it is installed
        """
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'spider/action/setOptionPostForm/', {'Boolean': boolean, 'apikey': apikey})))

    def set_option_process_form(self, boolean, apikey=''):
        """
        
        This component is optional and therefore the API will only work if it is installed
        """
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'spider/action/setOptionProcessForm/', {'Boolean': boolean, 'apikey': apikey})))

    def set_option_request_wait_time(self, integer, apikey=''):
        """
        
        This component is optional and therefore the API will only work if it is installed
        """
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'spider/action/setOptionRequestWaitTime/', {'Integer': integer, 'apikey': apikey})))

    def set_option_send_referer_header(self, boolean, apikey=''):
        """
        Sets whether or not the 'Referer' header should be sent while spidering.
        This component is optional and therefore the API will only work if it is installed
        """
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'spider/action/setOptionSendRefererHeader/', {'Boolean': boolean, 'apikey': apikey})))

    def set_option_show_advanced_dialog(self, boolean, apikey=''):
        """
        
        This component is optional and therefore the API will only work if it is installed
        """
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'spider/action/setOptionShowAdvancedDialog/', {'Boolean': boolean, 'apikey': apikey})))

    def set_option_thread_count(self, integer, apikey=''):
        """
        
        This component is optional and therefore the API will only work if it is installed
        """
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'spider/action/setOptionThreadCount/', {'Integer': integer, 'apikey': apikey})))
