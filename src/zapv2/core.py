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


class core(object):

    def __init__(self, zap):
        self.zap = zap

    @property
    def hosts(self):
        """
        Gets the name of the hosts accessed through/by ZAP
        """
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'core/view/hosts/')))

    @property
    def sites(self):
        """
        Gets the sites accessed through/by ZAP (scheme and domain)
        """
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'core/view/sites/')))

    def urls(self, baseurl=None):
        """
        Gets the URLs accessed through/by ZAP, optionally filtering by (base) URL.
        """
        params = {}
        if baseurl is not None:
            params['baseurl'] = baseurl
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'core/view/urls/', params)))

    def child_nodes(self, url=None):
        """
        Gets the child nodes underneath the specified URL in the Sites tree
        """
        params = {}
        if url is not None:
            params['url'] = url
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'core/view/childNodes/', params)))

    def message(self, id):
        """
        Gets the HTTP message with the given ID. Returns the ID, request/response headers and bodies, cookies, note, type, RTT, and timestamp.
        """
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'core/view/message/', {'id': id})))

    def messages(self, baseurl=None, start=None, count=None):
        """
        Gets the HTTP messages sent by ZAP, request and response, optionally filtered by URL and paginated with 'start' position and 'count' of messages
        """
        params = {}
        if baseurl is not None:
            params['baseurl'] = baseurl
        if start is not None:
            params['start'] = start
        if count is not None:
            params['count'] = count
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'core/view/messages/', params)))

    def messages_by_id(self, ids):
        """
        Gets the HTTP messages with the given IDs.
        """
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'core/view/messagesById/', {'ids': ids})))

    def number_of_messages(self, baseurl=None):
        """
        Gets the number of messages, optionally filtering by URL
        """
        params = {}
        if baseurl is not None:
            params['baseurl'] = baseurl
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'core/view/numberOfMessages/', params)))

    @property
    def mode(self):
        """
        Gets the mode
        """
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'core/view/mode/')))

    @property
    def version(self):
        """
        Gets ZAP version
        """
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'core/view/version/')))

    @property
    def excluded_from_proxy(self):
        """
        Gets the regular expressions, applied to URLs, to exclude from the local proxies.
        """
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'core/view/excludedFromProxy/')))

    @property
    def home_directory(self):
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'core/view/homeDirectory/')))

    @property
    def session_location(self):
        """
        Gets the location of the current session file
        """
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'core/view/sessionLocation/')))

    @property
    def proxy_chain_excluded_domains(self):
        """
        Gets all the domains that are excluded from the outgoing proxy. For each domain the following are shown: the index, the value (domain), if enabled, and if specified as a regex.
        """
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'core/view/proxyChainExcludedDomains/')))

    @property
    def option_proxy_chain_skip_name(self):
        """
        Use view proxyChainExcludedDomains instead.
        """
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'core/view/optionProxyChainSkipName/')))

    @property
    def option_proxy_excluded_domains(self):
        """
        Use view proxyChainExcludedDomains instead.
        """
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'core/view/optionProxyExcludedDomains/')))

    @property
    def option_proxy_excluded_domains_enabled(self):
        """
        Use view proxyChainExcludedDomains instead.
        """
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'core/view/optionProxyExcludedDomainsEnabled/')))

    @property
    def zap_home_path(self):
        """
        Gets the path to ZAP's home directory.
        """
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'core/view/zapHomePath/')))

    @property
    def option_maximum_alert_instances(self):
        """
        Gets the maximum number of alert instances to include in a report.
        """
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'core/view/optionMaximumAlertInstances/')))

    @property
    def option_merge_related_alerts(self):
        """
        Gets whether or not related alerts will be merged in any reports generated.
        """
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'core/view/optionMergeRelatedAlerts/')))

    @property
    def option_alert_overrides_file_path(self):
        """
        Gets the path to the file with alert overrides.
        """
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'core/view/optionAlertOverridesFilePath/')))

    def alert(self, id):
        """
        Gets the alert with the given ID, the corresponding HTTP message can be obtained with the 'messageId' field and 'message' API method
        """
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'core/view/alert/', {'id': id})))

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
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'core/view/alerts/', params)))

    def alerts_summary(self, baseurl=None):
        """
        Gets number of alerts grouped by each risk level, optionally filtering by URL
        """
        params = {}
        if baseurl is not None:
            params['baseurl'] = baseurl
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'core/view/alertsSummary/', params)))

    def number_of_alerts(self, baseurl=None, riskid=None):
        """
        Gets the number of alerts, optionally filtering by URL or riskId
        """
        params = {}
        if baseurl is not None:
            params['baseurl'] = baseurl
        if riskid is not None:
            params['riskId'] = riskid
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'core/view/numberOfAlerts/', params)))

    @property
    def option_default_user_agent(self):
        """
        Gets the user agent that ZAP should use when creating HTTP messages (for example, spider messages or CONNECT requests to outgoing proxy).
        """
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'core/view/optionDefaultUserAgent/')))

    @property
    def option_dns_ttl_successful_queries(self):
        """
        Gets the TTL (in seconds) of successful DNS queries.
        """
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'core/view/optionDnsTtlSuccessfulQueries/')))

    @property
    def option_http_state(self):
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'core/view/optionHttpState/')))

    @property
    def option_proxy_chain_name(self):
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'core/view/optionProxyChainName/')))

    @property
    def option_proxy_chain_password(self):
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'core/view/optionProxyChainPassword/')))

    @property
    def option_proxy_chain_port(self):
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'core/view/optionProxyChainPort/')))

    @property
    def option_proxy_chain_realm(self):
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'core/view/optionProxyChainRealm/')))

    @property
    def option_proxy_chain_user_name(self):
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'core/view/optionProxyChainUserName/')))

    @property
    def option_timeout_in_secs(self):
        """
        Gets the connection time out, in seconds.
        """
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'core/view/optionTimeoutInSecs/')))

    @property
    def option_http_state_enabled(self):
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'core/view/optionHttpStateEnabled/')))

    @property
    def option_proxy_chain_prompt(self):
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'core/view/optionProxyChainPrompt/')))

    @property
    def option_single_cookie_request_header(self):
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'core/view/optionSingleCookieRequestHeader/')))

    @property
    def option_use_proxy_chain(self):
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'core/view/optionUseProxyChain/')))

    @property
    def option_use_proxy_chain_auth(self):
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'core/view/optionUseProxyChainAuth/')))

    @property
    def option_use_socks_proxy(self):
        """
        Gets whether or not the SOCKS proxy should be used.
        """
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'core/view/optionUseSocksProxy/')))

    def access_url(self, url, followredirects=None, apikey=''):
        """
        Convenient and simple action to access a URL, optionally following redirections. Returns the request sent and response received and followed redirections, if any. Other actions are available which offer more control on what is sent, like, 'sendRequest' or 'sendHarRequest'.
        """
        params = {'url': url, 'apikey': apikey}
        if followredirects is not None:
            params['followRedirects'] = followredirects
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'core/action/accessUrl/', params)))

    def shutdown(self, apikey=''):
        """
        Shuts down ZAP
        """
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'core/action/shutdown/', {'apikey': apikey})))

    def new_session(self, name=None, overwrite=None, apikey=''):
        """
        Creates a new session, optionally overwriting existing files. If a relative path is specified it will be resolved against the "session" directory in ZAP "home" dir.
        """
        params = {'apikey': apikey}
        if name is not None:
            params['name'] = name
        if overwrite is not None:
            params['overwrite'] = overwrite
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'core/action/newSession/', params)))

    def load_session(self, name, apikey=''):
        """
        Loads the session with the given name. If a relative path is specified it will be resolved against the "session" directory in ZAP "home" dir.
        """
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'core/action/loadSession/', {'name': name, 'apikey': apikey})))

    def save_session(self, name, overwrite=None, apikey=''):
        """
        Saves the session.
        """
        params = {'name': name, 'apikey': apikey}
        if overwrite is not None:
            params['overwrite'] = overwrite
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'core/action/saveSession/', params)))

    def snapshot_session(self, name=None, overwrite=None, apikey=''):
        """
        Snapshots the session, optionally with the given name, and overwriting existing files. If no name is specified the name of the current session with a timestamp appended is used. If a relative path is specified it will be resolved against the "session" directory in ZAP "home" dir.
        """
        params = {'apikey': apikey}
        if name is not None:
            params['name'] = name
        if overwrite is not None:
            params['overwrite'] = overwrite
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'core/action/snapshotSession/', params)))

    def clear_excluded_from_proxy(self, apikey=''):
        """
        Clears the regexes of URLs excluded from the local proxies.
        """
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'core/action/clearExcludedFromProxy/', {'apikey': apikey})))

    def exclude_from_proxy(self, regex, apikey=''):
        """
        Adds a regex of URLs that should be excluded from the local proxies.
        """
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'core/action/excludeFromProxy/', {'regex': regex, 'apikey': apikey})))

    def set_home_directory(self, dir, apikey=''):
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'core/action/setHomeDirectory/', {'dir': dir, 'apikey': apikey})))

    def set_mode(self, mode, apikey=''):
        """
        Sets the mode, which may be one of [safe, protect, standard, attack]
        """
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'core/action/setMode/', {'mode': mode, 'apikey': apikey})))

    def generate_root_ca(self, apikey=''):
        """
        Generates a new Root CA certificate for the local proxies.
        """
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'core/action/generateRootCA/', {'apikey': apikey})))

    def send_request(self, request, followredirects=None, apikey=''):
        """
        Sends the HTTP request, optionally following redirections. Returns the request sent and response received and followed redirections, if any. The Mode is enforced when sending the request (and following redirections), custom manual requests are not allowed in 'Safe' mode nor in 'Protected' mode if out of scope.
        """
        params = {'request': request, 'apikey': apikey}
        if followredirects is not None:
            params['followRedirects'] = followredirects
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'core/action/sendRequest/', params)))

    def run_garbage_collection(self, apikey=''):
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'core/action/runGarbageCollection/', {'apikey': apikey})))

    def delete_site_node(self, url, method=None, postdata=None, apikey=''):
        """
        Deletes the site node found in the Sites Tree on the basis of the URL, HTTP method, and post data (if applicable and specified). 
        """
        params = {'url': url, 'apikey': apikey}
        if method is not None:
            params['method'] = method
        if postdata is not None:
            params['postData'] = postdata
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'core/action/deleteSiteNode/', params)))

    def add_proxy_chain_excluded_domain(self, value, isregex=None, isenabled=None, apikey=''):
        """
        Adds a domain to be excluded from the outgoing proxy, using the specified value. Optionally sets if the new entry is enabled (default, true) and whether or not the new value is specified as a regex (default, false).
        """
        params = {'value': value, 'apikey': apikey}
        if isregex is not None:
            params['isRegex'] = isregex
        if isenabled is not None:
            params['isEnabled'] = isenabled
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'core/action/addProxyChainExcludedDomain/', params)))

    def modify_proxy_chain_excluded_domain(self, idx, value=None, isregex=None, isenabled=None, apikey=''):
        """
        Modifies a domain excluded from the outgoing proxy. Allows to modify the value, if enabled or if a regex. The domain is selected with its index, which can be obtained with the view proxyChainExcludedDomains.
        """
        params = {'idx': idx, 'apikey': apikey}
        if value is not None:
            params['value'] = value
        if isregex is not None:
            params['isRegex'] = isregex
        if isenabled is not None:
            params['isEnabled'] = isenabled
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'core/action/modifyProxyChainExcludedDomain/', params)))

    def remove_proxy_chain_excluded_domain(self, idx, apikey=''):
        """
        Removes a domain excluded from the outgoing proxy, with the given index. The index can be obtained with the view proxyChainExcludedDomains.
        """
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'core/action/removeProxyChainExcludedDomain/', {'idx': idx, 'apikey': apikey})))

    def enable_all_proxy_chain_excluded_domains(self, apikey=''):
        """
        Enables all domains excluded from the outgoing proxy.
        """
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'core/action/enableAllProxyChainExcludedDomains/', {'apikey': apikey})))

    def disable_all_proxy_chain_excluded_domains(self, apikey=''):
        """
        Disables all domains excluded from the outgoing proxy.
        """
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'core/action/disableAllProxyChainExcludedDomains/', {'apikey': apikey})))

    def set_option_maximum_alert_instances(self, numberofinstances, apikey=''):
        """
        Sets the maximum number of alert instances to include in a report. A value of zero is treated as unlimited.
        """
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'core/action/setOptionMaximumAlertInstances/', {'numberOfInstances': numberofinstances, 'apikey': apikey})))

    def set_option_merge_related_alerts(self, enabled, apikey=''):
        """
        Sets whether or not related alerts will be merged in any reports generated.
        """
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'core/action/setOptionMergeRelatedAlerts/', {'enabled': enabled, 'apikey': apikey})))

    def set_option_alert_overrides_file_path(self, filepath=None, apikey=''):
        """
        Sets (or clears, if empty) the path to the file with alert overrides.
        """
        params = {'apikey': apikey}
        if filepath is not None:
            params['filePath'] = filepath
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'core/action/setOptionAlertOverridesFilePath/', params)))

    def enable_pkcs_12_client_certificate(self, filepath, password, index=None, apikey=''):
        """
        Enables use of a PKCS12 client certificate for the certificate with the given file system path, password, and optional index.
        """
        params = {'filePath': filepath, 'password': password, 'apikey': apikey}
        if index is not None:
            params['index'] = index
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'core/action/enablePKCS12ClientCertificate/', params)))

    def disable_client_certificate(self, apikey=''):
        """
        Disables the option for use of client certificates.
        """
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'core/action/disableClientCertificate/', {'apikey': apikey})))

    def delete_all_alerts(self, apikey=''):
        """
        Deletes all alerts of the current session.
        """
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'core/action/deleteAllAlerts/', {'apikey': apikey})))

    def delete_alert(self, id, apikey=''):
        """
        Deletes the alert with the given ID. 
        """
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'core/action/deleteAlert/', {'id': id, 'apikey': apikey})))

    def set_option_default_user_agent(self, string, apikey=''):
        """
        Sets the user agent that ZAP should use when creating HTTP messages (for example, spider messages or CONNECT requests to outgoing proxy).
        """
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'core/action/setOptionDefaultUserAgent/', {'String': string, 'apikey': apikey})))

    def set_option_proxy_chain_name(self, string, apikey=''):
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'core/action/setOptionProxyChainName/', {'String': string, 'apikey': apikey})))

    def set_option_proxy_chain_password(self, string, apikey=''):
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'core/action/setOptionProxyChainPassword/', {'String': string, 'apikey': apikey})))

    def set_option_proxy_chain_realm(self, string, apikey=''):
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'core/action/setOptionProxyChainRealm/', {'String': string, 'apikey': apikey})))

    def set_option_proxy_chain_skip_name(self, string, apikey=''):
        """
        Use actions [add|modify|remove]ProxyChainExcludedDomain instead.
        """
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'core/action/setOptionProxyChainSkipName/', {'String': string, 'apikey': apikey})))

    def set_option_proxy_chain_user_name(self, string, apikey=''):
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'core/action/setOptionProxyChainUserName/', {'String': string, 'apikey': apikey})))

    def set_option_dns_ttl_successful_queries(self, integer, apikey=''):
        """
        Sets the TTL (in seconds) of successful DNS queries (applies after ZAP restart).
        """
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'core/action/setOptionDnsTtlSuccessfulQueries/', {'Integer': integer, 'apikey': apikey})))

    def set_option_http_state_enabled(self, boolean, apikey=''):
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'core/action/setOptionHttpStateEnabled/', {'Boolean': boolean, 'apikey': apikey})))

    def set_option_proxy_chain_port(self, integer, apikey=''):
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'core/action/setOptionProxyChainPort/', {'Integer': integer, 'apikey': apikey})))

    def set_option_proxy_chain_prompt(self, boolean, apikey=''):
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'core/action/setOptionProxyChainPrompt/', {'Boolean': boolean, 'apikey': apikey})))

    def set_option_single_cookie_request_header(self, boolean, apikey=''):
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'core/action/setOptionSingleCookieRequestHeader/', {'Boolean': boolean, 'apikey': apikey})))

    def set_option_timeout_in_secs(self, integer, apikey=''):
        """
        Sets the connection time out, in seconds.
        """
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'core/action/setOptionTimeoutInSecs/', {'Integer': integer, 'apikey': apikey})))

    def set_option_use_proxy_chain(self, boolean, apikey=''):
        """
        Sets whether or not the outgoing proxy should be used. The address/hostname of the outgoing proxy must be set to enable this option.
        """
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'core/action/setOptionUseProxyChain/', {'Boolean': boolean, 'apikey': apikey})))

    def set_option_use_proxy_chain_auth(self, boolean, apikey=''):
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'core/action/setOptionUseProxyChainAuth/', {'Boolean': boolean, 'apikey': apikey})))

    def set_option_use_socks_proxy(self, boolean, apikey=''):
        """
        Sets whether or not the SOCKS proxy should be used.
        """
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'core/action/setOptionUseSocksProxy/', {'Boolean': boolean, 'apikey': apikey})))

    def proxy_pac(self, apikey=''):
        return (self.zap._request_other(self.zap.base_other + 'core/other/proxy.pac/', {'apikey': apikey}))

    def rootcert(self, apikey=''):
        """
        Gets the Root CA certificate used by the local proxies.
        """
        return (self.zap._request_other(self.zap.base_other + 'core/other/rootcert/', {'apikey': apikey}))

    def setproxy(self, proxy, apikey=''):
        return (self.zap._request_other(self.zap.base_other + 'core/other/setproxy/', {'proxy': proxy, 'apikey': apikey}))

    def xmlreport(self, apikey=''):
        """
        Generates a report in XML format
        """
        return (self.zap._request_other(self.zap.base_other + 'core/other/xmlreport/', {'apikey': apikey}))

    def htmlreport(self, apikey=''):
        """
        Generates a report in HTML format
        """
        return (self.zap._request_other(self.zap.base_other + 'core/other/htmlreport/', {'apikey': apikey}))

    def jsonreport(self, apikey=''):
        """
        Generates a report in JSON format
        """
        return (self.zap._request_other(self.zap.base_other + 'core/other/jsonreport/', {'apikey': apikey}))

    def mdreport(self, apikey=''):
        """
        Generates a report in Markdown format
        """
        return (self.zap._request_other(self.zap.base_other + 'core/other/mdreport/', {'apikey': apikey}))

    def message_har(self, id, apikey=''):
        """
        Gets the message with the given ID in HAR format
        """
        return (self.zap._request_other(self.zap.base_other + 'core/other/messageHar/', {'id': id, 'apikey': apikey}))

    def messages_har(self, baseurl=None, start=None, count=None, apikey=''):
        """
        Gets the HTTP messages sent through/by ZAP, in HAR format, optionally filtered by URL and paginated with 'start' position and 'count' of messages
        """
        params = {'apikey': apikey}
        if baseurl is not None:
            params['baseurl'] = baseurl
        if start is not None:
            params['start'] = start
        if count is not None:
            params['count'] = count
        return (self.zap._request_other(self.zap.base_other + 'core/other/messagesHar/', params))

    def messages_har_by_id(self, ids, apikey=''):
        """
        Gets the HTTP messages with the given IDs, in HAR format.
        """
        return (self.zap._request_other(self.zap.base_other + 'core/other/messagesHarById/', {'ids': ids, 'apikey': apikey}))

    def send_har_request(self, request, followredirects=None, apikey=''):
        """
        Sends the first HAR request entry, optionally following redirections. Returns, in HAR format, the request sent and response received and followed redirections, if any. The Mode is enforced when sending the request (and following redirections), custom manual requests are not allowed in 'Safe' mode nor in 'Protected' mode if out of scope.
        """
        params = {'request': request, 'apikey': apikey}
        if followredirects is not None:
            params['followRedirects'] = followredirects
        return (self.zap._request_other(self.zap.base_other + 'core/other/sendHarRequest/', params))
