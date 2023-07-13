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


class network(object):

    def __init__(self, zap):
        self.zap = zap

    @property
    def get_root_ca_cert_validity(self):
        """
        Gets the Root CA certificate validity, in days. Used when generating a new Root CA certificate.
        This component is optional and therefore the API will only work if it is installed
        """
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'network/view/getRootCaCertValidity/')))

    @property
    def get_server_cert_validity(self):
        """
        Gets the server certificate validity, in days. Used when generating server certificates.
        This component is optional and therefore the API will only work if it is installed
        """
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'network/view/getServerCertValidity/')))

    @property
    def get_aliases(self):
        """
        Gets the aliases used to identify the local servers/proxies.
        This component is optional and therefore the API will only work if it is installed
        """
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'network/view/getAliases/')))

    @property
    def get_local_servers(self):
        """
        Gets the local servers/proxies.
        This component is optional and therefore the API will only work if it is installed
        """
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'network/view/getLocalServers/')))

    @property
    def get_pass_throughs(self):
        """
        Gets the authorities that will pass-through the local proxies.
        This component is optional and therefore the API will only work if it is installed
        """
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'network/view/getPassThroughs/')))

    @property
    def get_connection_timeout(self):
        """
        Gets the connection timeout, in seconds.
        This component is optional and therefore the API will only work if it is installed
        """
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'network/view/getConnectionTimeout/')))

    @property
    def get_default_user_agent(self):
        """
        Gets the default user-agent.
        This component is optional and therefore the API will only work if it is installed
        """
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'network/view/getDefaultUserAgent/')))

    @property
    def get_dns_ttl_successful_queries(self):
        """
        Gets the TTL (in seconds) of successful DNS queries.
        This component is optional and therefore the API will only work if it is installed
        """
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'network/view/getDnsTtlSuccessfulQueries/')))

    @property
    def get_http_proxy(self):
        """
        Gets the HTTP proxy.
        This component is optional and therefore the API will only work if it is installed
        """
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'network/view/getHttpProxy/')))

    @property
    def get_http_proxy_exclusions(self):
        """
        Gets the HTTP proxy exclusions.
        This component is optional and therefore the API will only work if it is installed
        """
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'network/view/getHttpProxyExclusions/')))

    @property
    def get_socks_proxy(self):
        """
        Gets the SOCKS proxy.
        This component is optional and therefore the API will only work if it is installed
        """
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'network/view/getSocksProxy/')))

    @property
    def is_http_proxy_auth_enabled(self):
        """
        Tells whether or not the HTTP proxy authentication is enabled.
        This component is optional and therefore the API will only work if it is installed
        """
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'network/view/isHttpProxyAuthEnabled/')))

    @property
    def is_http_proxy_enabled(self):
        """
        Tells whether or not the HTTP proxy is enabled.
        This component is optional and therefore the API will only work if it is installed
        """
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'network/view/isHttpProxyEnabled/')))

    @property
    def is_socks_proxy_enabled(self):
        """
        Tells whether or not the SOCKS proxy is enabled.
        This component is optional and therefore the API will only work if it is installed
        """
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'network/view/isSocksProxyEnabled/')))

    @property
    def is_use_global_http_state(self):
        """
        Tells whether or not to use global HTTP state.
        This component is optional and therefore the API will only work if it is installed
        """
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'network/view/isUseGlobalHttpState/')))

    @property
    def get_rate_limit_rules(self):
        """
        List of rate limit rules.
        This component is optional and therefore the API will only work if it is installed
        """
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'network/view/getRateLimitRules/')))

    def generate_root_ca_cert(self, apikey=''):
        """
        Generates a new Root CA certificate, used to issue server certificates.
        This component is optional and therefore the API will only work if it is installed
        """
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'network/action/generateRootCaCert/', {'apikey': apikey})))

    def import_root_ca_cert(self, filepath, apikey=''):
        """
        Imports a Root CA certificate to be used to issue server certificates.
        This component is optional and therefore the API will only work if it is installed
        """
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'network/action/importRootCaCert/', {'filePath': filepath, 'apikey': apikey})))

    def set_root_ca_cert_validity(self, validity, apikey=''):
        """
        Sets the Root CA certificate validity. Used when generating a new Root CA certificate.
        This component is optional and therefore the API will only work if it is installed
        """
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'network/action/setRootCaCertValidity/', {'validity': validity, 'apikey': apikey})))

    def set_server_cert_validity(self, validity, apikey=''):
        """
        Sets the server certificate validity. Used when generating server certificates.
        This component is optional and therefore the API will only work if it is installed
        """
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'network/action/setServerCertValidity/', {'validity': validity, 'apikey': apikey})))

    def add_alias(self, name, enabled=None, apikey=''):
        """
        Adds an alias for the local servers/proxies.
        This component is optional and therefore the API will only work if it is installed
        """
        params = {'name': name, 'apikey': apikey}
        if enabled is not None:
            params['enabled'] = enabled
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'network/action/addAlias/', params)))

    def add_local_server(self, address, port, api=None, proxy=None, behindnat=None, decoderesponse=None, removeacceptencoding=None, apikey=''):
        """
        Adds a local server/proxy.
        This component is optional and therefore the API will only work if it is installed
        """
        params = {'address': address, 'port': port, 'apikey': apikey}
        if api is not None:
            params['api'] = api
        if proxy is not None:
            params['proxy'] = proxy
        if behindnat is not None:
            params['behindNat'] = behindnat
        if decoderesponse is not None:
            params['decodeResponse'] = decoderesponse
        if removeacceptencoding is not None:
            params['removeAcceptEncoding'] = removeacceptencoding
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'network/action/addLocalServer/', params)))

    def add_pass_through(self, authority, enabled=None, apikey=''):
        """
        Adds an authority to pass-through the local proxies.
        This component is optional and therefore the API will only work if it is installed
        """
        params = {'authority': authority, 'apikey': apikey}
        if enabled is not None:
            params['enabled'] = enabled
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'network/action/addPassThrough/', params)))

    def remove_alias(self, name, apikey=''):
        """
        Removes an alias.
        This component is optional and therefore the API will only work if it is installed
        """
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'network/action/removeAlias/', {'name': name, 'apikey': apikey})))

    def remove_local_server(self, address, port, apikey=''):
        """
        Removes a local server/proxy.
        This component is optional and therefore the API will only work if it is installed
        """
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'network/action/removeLocalServer/', {'address': address, 'port': port, 'apikey': apikey})))

    def remove_pass_through(self, authority, apikey=''):
        """
        Removes a pass-through.
        This component is optional and therefore the API will only work if it is installed
        """
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'network/action/removePassThrough/', {'authority': authority, 'apikey': apikey})))

    def set_alias_enabled(self, name, enabled, apikey=''):
        """
        Sets whether or not an alias is enabled.
        This component is optional and therefore the API will only work if it is installed
        """
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'network/action/setAliasEnabled/', {'name': name, 'enabled': enabled, 'apikey': apikey})))

    def set_pass_through_enabled(self, authority, enabled, apikey=''):
        """
        Sets whether or not a pass-through is enabled.
        This component is optional and therefore the API will only work if it is installed
        """
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'network/action/setPassThroughEnabled/', {'authority': authority, 'enabled': enabled, 'apikey': apikey})))

    def set_connection_timeout(self, timeout, apikey=''):
        """
        Sets the timeout, for reads and connects.
        This component is optional and therefore the API will only work if it is installed
        """
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'network/action/setConnectionTimeout/', {'timeout': timeout, 'apikey': apikey})))

    def set_default_user_agent(self, useragent, apikey=''):
        """
        Sets the default user-agent.
        This component is optional and therefore the API will only work if it is installed
        """
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'network/action/setDefaultUserAgent/', {'userAgent': useragent, 'apikey': apikey})))

    def set_dns_ttl_successful_queries(self, ttl, apikey=''):
        """
        Sets the TTL of successful DNS queries.
        This component is optional and therefore the API will only work if it is installed
        """
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'network/action/setDnsTtlSuccessfulQueries/', {'ttl': ttl, 'apikey': apikey})))

    def add_http_proxy_exclusion(self, host, enabled=None, apikey=''):
        """
        Adds a host to be excluded from the HTTP proxy.
        This component is optional and therefore the API will only work if it is installed
        """
        params = {'host': host, 'apikey': apikey}
        if enabled is not None:
            params['enabled'] = enabled
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'network/action/addHttpProxyExclusion/', params)))

    def remove_http_proxy_exclusion(self, host, apikey=''):
        """
        Removes an HTTP proxy exclusion.
        This component is optional and therefore the API will only work if it is installed
        """
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'network/action/removeHttpProxyExclusion/', {'host': host, 'apikey': apikey})))

    def set_http_proxy(self, host, port, realm=None, username=None, password=None, apikey=''):
        """
        Sets the HTTP proxy configuration.
        This component is optional and therefore the API will only work if it is installed
        """
        params = {'host': host, 'port': port, 'apikey': apikey}
        if realm is not None:
            params['realm'] = realm
        if username is not None:
            params['username'] = username
        if password is not None:
            params['password'] = password
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'network/action/setHttpProxy/', params)))

    def set_http_proxy_auth_enabled(self, enabled, apikey=''):
        """
        Sets whether or not the HTTP proxy authentication is enabled.
        This component is optional and therefore the API will only work if it is installed
        """
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'network/action/setHttpProxyAuthEnabled/', {'enabled': enabled, 'apikey': apikey})))

    def set_http_proxy_enabled(self, enabled, apikey=''):
        """
        Sets whether or not the HTTP proxy is enabled.
        This component is optional and therefore the API will only work if it is installed
        """
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'network/action/setHttpProxyEnabled/', {'enabled': enabled, 'apikey': apikey})))

    def set_http_proxy_exclusion_enabled(self, host, enabled, apikey=''):
        """
        Sets whether or not an HTTP proxy exclusion is enabled.
        This component is optional and therefore the API will only work if it is installed
        """
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'network/action/setHttpProxyExclusionEnabled/', {'host': host, 'enabled': enabled, 'apikey': apikey})))

    def set_socks_proxy(self, host, port, version=None, usedns=None, username=None, password=None, apikey=''):
        """
        Sets the SOCKS proxy configuration.
        This component is optional and therefore the API will only work if it is installed
        """
        params = {'host': host, 'port': port, 'apikey': apikey}
        if version is not None:
            params['version'] = version
        if usedns is not None:
            params['useDns'] = usedns
        if username is not None:
            params['username'] = username
        if password is not None:
            params['password'] = password
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'network/action/setSocksProxy/', params)))

    def set_socks_proxy_enabled(self, enabled, apikey=''):
        """
        Sets whether or not the SOCKS proxy is enabled.
        This component is optional and therefore the API will only work if it is installed
        """
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'network/action/setSocksProxyEnabled/', {'enabled': enabled, 'apikey': apikey})))

    def set_use_global_http_state(self, use, apikey=''):
        """
        Sets whether or not to use the global HTTP state.
        This component is optional and therefore the API will only work if it is installed
        """
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'network/action/setUseGlobalHttpState/', {'use': use, 'apikey': apikey})))

    def add_pkcs_12_client_certificate(self, filepath, password, index=None, apikey=''):
        """
        Adds a client certificate contained in a PKCS#12 file, the certificate is automatically set as active and used.
        This component is optional and therefore the API will only work if it is installed
        """
        params = {'filePath': filepath, 'password': password, 'apikey': apikey}
        if index is not None:
            params['index'] = index
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'network/action/addPkcs12ClientCertificate/', params)))

    def set_use_client_certificate(self, use, apikey=''):
        """
        Sets whether or not to use the active client certificate.
        This component is optional and therefore the API will only work if it is installed
        """
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'network/action/setUseClientCertificate/', {'use': use, 'apikey': apikey})))

    def add_rate_limit_rule(self, description, enabled, matchregex, matchstring, requestspersecond, groupby, apikey=''):
        """
        Adds a rate limit rule
        This component is optional and therefore the API will only work if it is installed
        """
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'network/action/addRateLimitRule/', {'description': description, 'enabled': enabled, 'matchRegex': matchregex, 'matchString': matchstring, 'requestsPerSecond': requestspersecond, 'groupBy': groupby, 'apikey': apikey})))

    def remove_rate_limit_rule(self, description, apikey=''):
        """
        Remove a rate limit rule
        This component is optional and therefore the API will only work if it is installed
        """
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'network/action/removeRateLimitRule/', {'description': description, 'apikey': apikey})))

    def set_rate_limit_rule_enabled(self, description, enabled, apikey=''):
        """
        Set enabled state for a rate limit rule.
        This component is optional and therefore the API will only work if it is installed
        """
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'network/action/setRateLimitRuleEnabled/', {'description': description, 'enabled': enabled, 'apikey': apikey})))

    def proxy_pac(self, apikey=''):
        """
        Provides a PAC file, proxying through the main proxy.
        This component is optional and therefore the API will only work if it is installed
        """
        return (self.zap._request_other(self.zap.base_other + 'network/other/proxy.pac/', {'apikey': apikey}))

    def set_proxy(self, proxy, apikey=''):
        """
        Sets the HTTP proxy configuration.
        This component is optional and therefore the API will only work if it is installed
        """
        return (self.zap._request_other(self.zap.base_other + 'network/other/setProxy/', {'proxy': proxy, 'apikey': apikey}))

    def root_ca_cert(self, apikey=''):
        """
        Gets the Root CA certificate used to issue server certificates. Suitable to import into client applications (e.g. browsers).
        This component is optional and therefore the API will only work if it is installed
        """
        return (self.zap._request_other(self.zap.base_other + 'network/other/rootCaCert/', {'apikey': apikey}))
