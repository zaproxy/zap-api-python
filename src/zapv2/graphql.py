# Zed Attack Proxy (ZAP) and its related class files.
#
# ZAP is an HTTP/HTTPS proxy for assessing web application security.
#
# Copyright 2020 the ZAP development team
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


class graphql(object):

    def __init__(self, zap):
        self.zap = zap

    @property
    def option_args_type(self):
        """
        Returns how arguments are currently specified.
        This component is optional and therefore the API will only work if it is installed
        """
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'graphql/view/optionArgsType/')))

    @property
    def option_max_args_depth(self):
        """
        Returns the current maximum arguments generation depth.
        This component is optional and therefore the API will only work if it is installed
        """
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'graphql/view/optionMaxArgsDepth/')))

    @property
    def option_max_query_depth(self):
        """
        Returns the current maximum query generation depth.
        This component is optional and therefore the API will only work if it is installed
        """
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'graphql/view/optionMaxQueryDepth/')))

    @property
    def option_optional_args_enabled(self):
        """
        Returns whether or not optional arguments are currently specified.
        This component is optional and therefore the API will only work if it is installed
        """
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'graphql/view/optionOptionalArgsEnabled/')))

    @property
    def option_query_split_type(self):
        """
        Returns the current level for which a single query is generated.
        This component is optional and therefore the API will only work if it is installed
        """
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'graphql/view/optionQuerySplitType/')))

    @property
    def option_request_method(self):
        """
        Returns the current request method.
        This component is optional and therefore the API will only work if it is installed
        """
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'graphql/view/optionRequestMethod/')))

    def import_file(self, endurl, file, apikey=''):
        """
        Imports a GraphQL Schema from a File.
        This component is optional and therefore the API will only work if it is installed
        """
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'graphql/action/importFile/', {'endurl': endurl, 'file': file, 'apikey': apikey})))

    def import_url(self, endurl, url=None, apikey=''):
        """
        Imports a GraphQL Schema from a URL.
        This component is optional and therefore the API will only work if it is installed
        """
        params = {'endurl': endurl, 'apikey': apikey}
        if url is not None:
            params['url'] = url
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'graphql/action/importUrl/', params)))

    def set_option_args_type(self, string, apikey=''):
        """
        Sets how arguments are specified.
        This component is optional and therefore the API will only work if it is installed
        """
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'graphql/action/setOptionArgsType/', {'String': string, 'apikey': apikey})))

    def set_option_query_split_type(self, string, apikey=''):
        """
        Sets the level for which a single query is generated.
        This component is optional and therefore the API will only work if it is installed
        """
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'graphql/action/setOptionQuerySplitType/', {'String': string, 'apikey': apikey})))

    def set_option_request_method(self, string, apikey=''):
        """
        Sets the request method.
        This component is optional and therefore the API will only work if it is installed
        """
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'graphql/action/setOptionRequestMethod/', {'String': string, 'apikey': apikey})))

    def set_option_max_args_depth(self, integer, apikey=''):
        """
        Sets the maximum arguments generation depth.
        This component is optional and therefore the API will only work if it is installed
        """
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'graphql/action/setOptionMaxArgsDepth/', {'Integer': integer, 'apikey': apikey})))

    def set_option_max_query_depth(self, integer, apikey=''):
        """
        Sets the maximum query generation depth.
        This component is optional and therefore the API will only work if it is installed
        """
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'graphql/action/setOptionMaxQueryDepth/', {'Integer': integer, 'apikey': apikey})))

    def set_option_optional_args_enabled(self, boolean, apikey=''):
        """
        Sets whether or not Optional Arguments should be specified.
        This component is optional and therefore the API will only work if it is installed
        """
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'graphql/action/setOptionOptionalArgsEnabled/', {'Boolean': boolean, 'apikey': apikey})))
