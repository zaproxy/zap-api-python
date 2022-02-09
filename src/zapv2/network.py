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

    def root_ca_cert(self, apikey=''):
        """
        Gets the Root CA certificate used to issue server certificates. Suitable to import into client applications (e.g. browsers).
        This component is optional and therefore the API will only work if it is installed
        """
        return (self.zap._request_other(self.zap.base_other + 'network/other/rootCaCert/', {'apikey': apikey}))
