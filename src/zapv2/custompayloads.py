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


class custompayloads(object):

    def __init__(self, zap):
        self.zap = zap

    @property
    def custom_payloads_categories(self):
        """
        Lists all available categories.
        This component is optional and therefore the API will only work if it is installed
        """
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'custompayloads/view/customPayloadsCategories/')))

    def custom_payloads(self, category=None):
        """
        Lists all the payloads currently loaded (category, payload, enabled state). Optionally filtered by category.
        This component is optional and therefore the API will only work if it is installed
        """
        params = {}
        if category is not None:
            params['category'] = category
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'custompayloads/view/customPayloads/', params)))

    def disable_custom_payloads(self, category=None, apikey=''):
        """
        Disables payloads for a given category.
        This component is optional and therefore the API will only work if it is installed
        """
        params = {}
        if category is not None:
            params['category'] = category
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'custompayloads/action/disableCustomPayloads/', params)))

    def enable_custom_payloads(self, category=None, apikey=''):
        """
        Enables payloads for a given category.
        This component is optional and therefore the API will only work if it is installed
        """
        params = {}
        if category is not None:
            params['category'] = category
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'custompayloads/action/enableCustomPayloads/', params)))

    def remove_custom_payload(self, category, payload=None, apikey=''):
        """
        Removes a payload.
        This component is optional and therefore the API will only work if it is installed
        """
        params = {'category': category}
        if payload is not None:
            params['payload'] = payload
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'custompayloads/action/removeCustomPayload/', params)))

    def add_custom_payload(self, category, payload=None, apikey=''):
        """
        Adds a new payload.
        This component is optional and therefore the API will only work if it is installed
        """
        params = {'category': category}
        if payload is not None:
            params['payload'] = payload
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'custompayloads/action/addCustomPayload/', params)))

    def enable_custom_payload(self, category, payload=None, apikey=''):
        """
        Enables a given payload.
        This component is optional and therefore the API will only work if it is installed
        """
        params = {'category': category}
        if payload is not None:
            params['payload'] = payload
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'custompayloads/action/enableCustomPayload/', params)))

    def disable_custom_payload(self, category, payload=None, apikey=''):
        """
        Disables a given payload.
        This component is optional and therefore the API will only work if it is installed
        """
        params = {'category': category}
        if payload is not None:
            params['payload'] = payload
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'custompayloads/action/disableCustomPayload/', params)))
