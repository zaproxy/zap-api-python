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


class ascan(object):

    def __init__(self, zap):
        self.zap = zap

    def status(self, scanid=None):
        params = {}
        if scanid is not None:
            params['scanId'] = scanid
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'ascan/view/status/', params)))

    def scan_progress(self, scanid=None):
        params = {}
        if scanid is not None:
            params['scanId'] = scanid
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'ascan/view/scanProgress/', params)))

    def messages_ids(self, scanid):
        """
        Gets the IDs of the messages sent during the scan with the given ID. A message can be obtained with 'message' core view.
        """
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'ascan/view/messagesIds/', {'scanId': scanid})))

    def alerts_ids(self, scanid):
        """
        Gets the IDs of the alerts raised during the scan with the given ID. An alert can be obtained with 'alert' core view.
        """
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'ascan/view/alertsIds/', {'scanId': scanid})))

    @property
    def scans(self):
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'ascan/view/scans/')))

    @property
    def scan_policy_names(self):
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'ascan/view/scanPolicyNames/')))

    @property
    def excluded_from_scan(self):
        """
        Gets the regexes of URLs excluded from the active scans.
        """
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'ascan/view/excludedFromScan/')))

    def scanners(self, scanpolicyname=None, policyid=None):
        """
        Gets the scanners, optionally, of the given scan policy and/or scanner policy/category ID.
        """
        params = {}
        if scanpolicyname is not None:
            params['scanPolicyName'] = scanpolicyname
        if policyid is not None:
            params['policyId'] = policyid
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'ascan/view/scanners/', params)))

    def policies(self, scanpolicyname=None, policyid=None):
        params = {}
        if scanpolicyname is not None:
            params['scanPolicyName'] = scanpolicyname
        if policyid is not None:
            params['policyId'] = policyid
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'ascan/view/policies/', params)))

    @property
    def attack_mode_queue(self):
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'ascan/view/attackModeQueue/')))

    @property
    def excluded_params(self):
        """
        Gets all the parameters that are excluded. For each parameter the following are shown: the name, the URL, and the parameter type.
        """
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'ascan/view/excludedParams/')))

    @property
    def option_excluded_param_list(self):
        """
        Use view excludedParams instead.
        """
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'ascan/view/optionExcludedParamList/')))

    @property
    def excluded_param_types(self):
        """
        Gets all the types of excluded parameters. For each type the following are shown: the ID and the name.
        """
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'ascan/view/excludedParamTypes/')))

    @property
    def option_attack_policy(self):
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'ascan/view/optionAttackPolicy/')))

    @property
    def option_default_policy(self):
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'ascan/view/optionDefaultPolicy/')))

    @property
    def option_delay_in_ms(self):
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'ascan/view/optionDelayInMs/')))

    @property
    def option_handle_anti_csrf_tokens(self):
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'ascan/view/optionHandleAntiCSRFTokens/')))

    @property
    def option_host_per_scan(self):
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'ascan/view/optionHostPerScan/')))

    @property
    def option_max_chart_time_in_mins(self):
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'ascan/view/optionMaxChartTimeInMins/')))

    @property
    def option_max_results_to_list(self):
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'ascan/view/optionMaxResultsToList/')))

    @property
    def option_max_rule_duration_in_mins(self):
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'ascan/view/optionMaxRuleDurationInMins/')))

    @property
    def option_max_scan_duration_in_mins(self):
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'ascan/view/optionMaxScanDurationInMins/')))

    @property
    def option_max_scans_in_ui(self):
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'ascan/view/optionMaxScansInUI/')))

    @property
    def option_target_params_enabled_rpc(self):
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'ascan/view/optionTargetParamsEnabledRPC/')))

    @property
    def option_target_params_injectable(self):
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'ascan/view/optionTargetParamsInjectable/')))

    @property
    def option_thread_per_host(self):
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'ascan/view/optionThreadPerHost/')))

    @property
    def option_add_query_param(self):
        """
        Tells whether or not the active scanner should add a query parameter to GET request that don't have parameters to start with.
        """
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'ascan/view/optionAddQueryParam/')))

    @property
    def option_allow_attack_on_start(self):
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'ascan/view/optionAllowAttackOnStart/')))

    @property
    def option_inject_plugin_id_in_header(self):
        """
        Tells whether or not the active scanner should inject the HTTP request header X-ZAP-Scan-ID, with the ID of the scanner that's sending the requests.
        """
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'ascan/view/optionInjectPluginIdInHeader/')))

    @property
    def option_prompt_in_attack_mode(self):
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'ascan/view/optionPromptInAttackMode/')))

    @property
    def option_prompt_to_clear_finished_scans(self):
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'ascan/view/optionPromptToClearFinishedScans/')))

    @property
    def option_rescan_in_attack_mode(self):
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'ascan/view/optionRescanInAttackMode/')))

    @property
    def option_scan_headers_all_requests(self):
        """
        Tells whether or not the HTTP Headers of all requests should be scanned. Not just requests that send parameters, through the query or request body.
        """
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'ascan/view/optionScanHeadersAllRequests/')))

    @property
    def option_show_advanced_dialog(self):
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'ascan/view/optionShowAdvancedDialog/')))

    def scan(self, url=None, recurse=None, inscopeonly=None, scanpolicyname=None, method=None, postdata=None, contextid=None, apikey=''):
        """
        Runs the active scanner against the given URL and/or Context. Optionally, the 'recurse' parameter can be used to scan URLs under the given URL, the parameter 'inScopeOnly' can be used to constrain the scan to URLs that are in scope (ignored if a Context is specified), the parameter 'scanPolicyName' allows to specify the scan policy (if none is given it uses the default scan policy), the parameters 'method' and 'postData' allow to select a given request in conjunction with the given URL.
        """
        params = {'apikey': apikey}
        if url is not None:
            params['url'] = url
        if recurse is not None:
            params['recurse'] = recurse
        if inscopeonly is not None:
            params['inScopeOnly'] = inscopeonly
        if scanpolicyname is not None:
            params['scanPolicyName'] = scanpolicyname
        if method is not None:
            params['method'] = method
        if postdata is not None:
            params['postData'] = postdata
        if contextid is not None:
            params['contextId'] = contextid
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'ascan/action/scan/', params)))

    def scan_as_user(self, url=None, contextid=None, userid=None, recurse=None, scanpolicyname=None, method=None, postdata=None, apikey=''):
        """
        Active Scans from the perspective of a User, obtained using the given Context ID and User ID. See 'scan' action for more details.
        """
        params = {'apikey': apikey}
        if url is not None:
            params['url'] = url
        if contextid is not None:
            params['contextId'] = contextid
        if userid is not None:
            params['userId'] = userid
        if recurse is not None:
            params['recurse'] = recurse
        if scanpolicyname is not None:
            params['scanPolicyName'] = scanpolicyname
        if method is not None:
            params['method'] = method
        if postdata is not None:
            params['postData'] = postdata
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'ascan/action/scanAsUser/', params)))

    def pause(self, scanid, apikey=''):
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'ascan/action/pause/', {'scanId': scanid, 'apikey': apikey})))

    def resume(self, scanid, apikey=''):
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'ascan/action/resume/', {'scanId': scanid, 'apikey': apikey})))

    def stop(self, scanid, apikey=''):
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'ascan/action/stop/', {'scanId': scanid, 'apikey': apikey})))

    def remove_scan(self, scanid, apikey=''):
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'ascan/action/removeScan/', {'scanId': scanid, 'apikey': apikey})))

    def pause_all_scans(self, apikey=''):
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'ascan/action/pauseAllScans/', {'apikey': apikey})))

    def resume_all_scans(self, apikey=''):
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'ascan/action/resumeAllScans/', {'apikey': apikey})))

    def stop_all_scans(self, apikey=''):
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'ascan/action/stopAllScans/', {'apikey': apikey})))

    def remove_all_scans(self, apikey=''):
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'ascan/action/removeAllScans/', {'apikey': apikey})))

    def clear_excluded_from_scan(self, apikey=''):
        """
        Clears the regexes of URLs excluded from the active scans.
        """
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'ascan/action/clearExcludedFromScan/', {'apikey': apikey})))

    def exclude_from_scan(self, regex, apikey=''):
        """
        Adds a regex of URLs that should be excluded from the active scans.
        """
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'ascan/action/excludeFromScan/', {'regex': regex, 'apikey': apikey})))

    def enable_all_scanners(self, scanpolicyname=None, apikey=''):
        """
        Enables all scanners of the scan policy with the given name, or the default if none given.
        """
        params = {'apikey': apikey}
        if scanpolicyname is not None:
            params['scanPolicyName'] = scanpolicyname
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'ascan/action/enableAllScanners/', params)))

    def disable_all_scanners(self, scanpolicyname=None, apikey=''):
        """
        Disables all scanners of the scan policy with the given name, or the default if none given.
        """
        params = {'apikey': apikey}
        if scanpolicyname is not None:
            params['scanPolicyName'] = scanpolicyname
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'ascan/action/disableAllScanners/', params)))

    def enable_scanners(self, ids, scanpolicyname=None, apikey=''):
        """
        Enables the scanners with the given IDs (comma separated list of IDs) of the scan policy with the given name, or the default if none given.
        """
        params = {'ids': ids, 'apikey': apikey}
        if scanpolicyname is not None:
            params['scanPolicyName'] = scanpolicyname
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'ascan/action/enableScanners/', params)))

    def disable_scanners(self, ids, scanpolicyname=None, apikey=''):
        """
        Disables the scanners with the given IDs (comma separated list of IDs) of the scan policy with the given name, or the default if none given.
        """
        params = {'ids': ids, 'apikey': apikey}
        if scanpolicyname is not None:
            params['scanPolicyName'] = scanpolicyname
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'ascan/action/disableScanners/', params)))

    def set_enabled_policies(self, ids, scanpolicyname=None, apikey=''):
        params = {'ids': ids, 'apikey': apikey}
        if scanpolicyname is not None:
            params['scanPolicyName'] = scanpolicyname
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'ascan/action/setEnabledPolicies/', params)))

    def set_policy_attack_strength(self, id, attackstrength, scanpolicyname=None, apikey=''):
        params = {'id': id, 'attackStrength': attackstrength, 'apikey': apikey}
        if scanpolicyname is not None:
            params['scanPolicyName'] = scanpolicyname
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'ascan/action/setPolicyAttackStrength/', params)))

    def set_policy_alert_threshold(self, id, alertthreshold, scanpolicyname=None, apikey=''):
        params = {'id': id, 'alertThreshold': alertthreshold, 'apikey': apikey}
        if scanpolicyname is not None:
            params['scanPolicyName'] = scanpolicyname
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'ascan/action/setPolicyAlertThreshold/', params)))

    def set_scanner_attack_strength(self, id, attackstrength, scanpolicyname=None, apikey=''):
        params = {'id': id, 'attackStrength': attackstrength, 'apikey': apikey}
        if scanpolicyname is not None:
            params['scanPolicyName'] = scanpolicyname
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'ascan/action/setScannerAttackStrength/', params)))

    def set_scanner_alert_threshold(self, id, alertthreshold, scanpolicyname=None, apikey=''):
        params = {'id': id, 'alertThreshold': alertthreshold, 'apikey': apikey}
        if scanpolicyname is not None:
            params['scanPolicyName'] = scanpolicyname
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'ascan/action/setScannerAlertThreshold/', params)))

    def add_scan_policy(self, scanpolicyname, alertthreshold=None, attackstrength=None, apikey=''):
        params = {'scanPolicyName': scanpolicyname, 'apikey': apikey}
        if alertthreshold is not None:
            params['alertThreshold'] = alertthreshold
        if attackstrength is not None:
            params['attackStrength'] = attackstrength
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'ascan/action/addScanPolicy/', params)))

    def remove_scan_policy(self, scanpolicyname, apikey=''):
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'ascan/action/removeScanPolicy/', {'scanPolicyName': scanpolicyname, 'apikey': apikey})))

    def update_scan_policy(self, scanpolicyname, alertthreshold=None, attackstrength=None, apikey=''):
        params = {'scanPolicyName': scanpolicyname, 'apikey': apikey}
        if alertthreshold is not None:
            params['alertThreshold'] = alertthreshold
        if attackstrength is not None:
            params['attackStrength'] = attackstrength
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'ascan/action/updateScanPolicy/', params)))

    def import_scan_policy(self, path, apikey=''):
        """
        Imports a Scan Policy using the given file system path.
        """
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'ascan/action/importScanPolicy/', {'path': path, 'apikey': apikey})))

    def add_excluded_param(self, name, type=None, url=None, apikey=''):
        """
        Adds a new parameter excluded from the scan, using the specified name. Optionally sets if the new entry applies to a specific URL (default, all URLs) and sets the ID of the type of the parameter (default, ID of any type). The type IDs can be obtained with the view excludedParamTypes. 
        """
        params = {'name': name, 'apikey': apikey}
        if type is not None:
            params['type'] = type
        if url is not None:
            params['url'] = url
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'ascan/action/addExcludedParam/', params)))

    def modify_excluded_param(self, idx, name=None, type=None, url=None, apikey=''):
        """
        Modifies a parameter excluded from the scan. Allows to modify the name, the URL and the type of parameter. The parameter is selected with its index, which can be obtained with the view excludedParams.
        """
        params = {'idx': idx, 'apikey': apikey}
        if name is not None:
            params['name'] = name
        if type is not None:
            params['type'] = type
        if url is not None:
            params['url'] = url
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'ascan/action/modifyExcludedParam/', params)))

    def remove_excluded_param(self, idx, apikey=''):
        """
        Removes a parameter excluded from the scan, with the given index. The index can be obtained with the view excludedParams.
        """
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'ascan/action/removeExcludedParam/', {'idx': idx, 'apikey': apikey})))

    def skip_scanner(self, scanid, scannerid, apikey=''):
        """
        Skips the scanner using the given IDs of the scan and the scanner.
        """
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'ascan/action/skipScanner/', {'scanId': scanid, 'scannerId': scannerid, 'apikey': apikey})))

    def set_option_attack_policy(self, string, apikey=''):
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'ascan/action/setOptionAttackPolicy/', {'String': string, 'apikey': apikey})))

    def set_option_default_policy(self, string, apikey=''):
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'ascan/action/setOptionDefaultPolicy/', {'String': string, 'apikey': apikey})))

    def set_option_add_query_param(self, boolean, apikey=''):
        """
        Sets whether or not the active scanner should add a query param to GET requests which do not have parameters to start with.
        """
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'ascan/action/setOptionAddQueryParam/', {'Boolean': boolean, 'apikey': apikey})))

    def set_option_allow_attack_on_start(self, boolean, apikey=''):
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'ascan/action/setOptionAllowAttackOnStart/', {'Boolean': boolean, 'apikey': apikey})))

    def set_option_delay_in_ms(self, integer, apikey=''):
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'ascan/action/setOptionDelayInMs/', {'Integer': integer, 'apikey': apikey})))

    def set_option_handle_anti_csrf_tokens(self, boolean, apikey=''):
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'ascan/action/setOptionHandleAntiCSRFTokens/', {'Boolean': boolean, 'apikey': apikey})))

    def set_option_host_per_scan(self, integer, apikey=''):
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'ascan/action/setOptionHostPerScan/', {'Integer': integer, 'apikey': apikey})))

    def set_option_inject_plugin_id_in_header(self, boolean, apikey=''):
        """
        Sets whether or not the active scanner should inject the HTTP request header X-ZAP-Scan-ID, with the ID of the scanner that's sending the requests.
        """
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'ascan/action/setOptionInjectPluginIdInHeader/', {'Boolean': boolean, 'apikey': apikey})))

    def set_option_max_chart_time_in_mins(self, integer, apikey=''):
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'ascan/action/setOptionMaxChartTimeInMins/', {'Integer': integer, 'apikey': apikey})))

    def set_option_max_results_to_list(self, integer, apikey=''):
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'ascan/action/setOptionMaxResultsToList/', {'Integer': integer, 'apikey': apikey})))

    def set_option_max_rule_duration_in_mins(self, integer, apikey=''):
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'ascan/action/setOptionMaxRuleDurationInMins/', {'Integer': integer, 'apikey': apikey})))

    def set_option_max_scan_duration_in_mins(self, integer, apikey=''):
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'ascan/action/setOptionMaxScanDurationInMins/', {'Integer': integer, 'apikey': apikey})))

    def set_option_max_scans_in_ui(self, integer, apikey=''):
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'ascan/action/setOptionMaxScansInUI/', {'Integer': integer, 'apikey': apikey})))

    def set_option_prompt_in_attack_mode(self, boolean, apikey=''):
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'ascan/action/setOptionPromptInAttackMode/', {'Boolean': boolean, 'apikey': apikey})))

    def set_option_prompt_to_clear_finished_scans(self, boolean, apikey=''):
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'ascan/action/setOptionPromptToClearFinishedScans/', {'Boolean': boolean, 'apikey': apikey})))

    def set_option_rescan_in_attack_mode(self, boolean, apikey=''):
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'ascan/action/setOptionRescanInAttackMode/', {'Boolean': boolean, 'apikey': apikey})))

    def set_option_scan_headers_all_requests(self, boolean, apikey=''):
        """
        Sets whether or not the HTTP Headers of all requests should be scanned. Not just requests that send parameters, through the query or request body.
        """
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'ascan/action/setOptionScanHeadersAllRequests/', {'Boolean': boolean, 'apikey': apikey})))

    def set_option_show_advanced_dialog(self, boolean, apikey=''):
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'ascan/action/setOptionShowAdvancedDialog/', {'Boolean': boolean, 'apikey': apikey})))

    def set_option_target_params_enabled_rpc(self, integer, apikey=''):
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'ascan/action/setOptionTargetParamsEnabledRPC/', {'Integer': integer, 'apikey': apikey})))

    def set_option_target_params_injectable(self, integer, apikey=''):
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'ascan/action/setOptionTargetParamsInjectable/', {'Integer': integer, 'apikey': apikey})))

    def set_option_thread_per_host(self, integer, apikey=''):
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'ascan/action/setOptionThreadPerHost/', {'Integer': integer, 'apikey': apikey})))
