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


class context(object):

    def __init__(self, zap):
        self.zap = zap

    @property
    def context_list(self):
        """
        List context names of current session
        """
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'context/view/contextList/')))

    def exclude_regexs(self, contextname):
        """
        List excluded regexs for context
        """
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'context/view/excludeRegexs/', {'contextName': contextname})))

    def include_regexs(self, contextname):
        """
        List included regexs for context
        """
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'context/view/includeRegexs/', {'contextName': contextname})))

    def context(self, contextname):
        """
        List the information about the named context
        """
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'context/view/context/', {'contextName': contextname})))

    @property
    def technology_list(self):
        """
        Lists the names of all built in technologies
        """
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'context/view/technologyList/')))

    def included_technology_list(self, contextname):
        """
        Lists the names of all technologies included in a context
        """
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'context/view/includedTechnologyList/', {'contextName': contextname})))

    def excluded_technology_list(self, contextname):
        """
        Lists the names of all technologies excluded from a context
        """
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'context/view/excludedTechnologyList/', {'contextName': contextname})))

    def urls(self, contextname):
        """
        Lists the URLs accessed through/by ZAP, that belong to the context with the given name.
        """
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'context/view/urls/', {'contextName': contextname})))

    def exclude_from_context(self, contextname, regex, apikey=''):
        """
        Add exclude regex to context
        """
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'context/action/excludeFromContext/', {'contextName': contextname, 'regex': regex, 'apikey': apikey})))

    def include_in_context(self, contextname, regex, apikey=''):
        """
        Add include regex to context
        """
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'context/action/includeInContext/', {'contextName': contextname, 'regex': regex, 'apikey': apikey})))

    def set_context_regexs(self, contextname, incregexs, excregexs, apikey=''):
        """
        Set the regexs to include and exclude for a context, both supplied as JSON string arrays
        """
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'context/action/setContextRegexs/', {'contextName': contextname, 'incRegexs': incregexs, 'excRegexs': excregexs, 'apikey': apikey})))

    def set_context_checking_strategy(self, contextname, checkingstrategy, pollurl=None, polldata=None, pollheaders=None, pollfrequency=None, pollfrequencyunits=None, apikey=''):
        """
        Set the checking strategy for a context - this defines how ZAP checks that a request is authenticated
        """
        params = {'contextName': contextname, 'checkingStrategy': checkingstrategy, 'apikey': apikey}
        if pollurl is not None:
            params['pollUrl'] = pollurl
        if polldata is not None:
            params['pollData'] = polldata
        if pollheaders is not None:
            params['pollHeaders'] = pollheaders
        if pollfrequency is not None:
            params['pollFrequency'] = pollfrequency
        if pollfrequencyunits is not None:
            params['pollFrequencyUnits'] = pollfrequencyunits
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'context/action/setContextCheckingStrategy/', params)))

    def new_context(self, contextname, apikey=''):
        """
        Creates a new context with the given name in the current session
        """
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'context/action/newContext/', {'contextName': contextname, 'apikey': apikey})))

    def remove_context(self, contextname, apikey=''):
        """
        Removes a context in the current session
        """
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'context/action/removeContext/', {'contextName': contextname, 'apikey': apikey})))

    def export_context(self, contextname, contextfile, apikey=''):
        """
        Exports the context with the given name to a file. If a relative file path is specified it will be resolved against the "contexts" directory in ZAP "home" dir.
        """
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'context/action/exportContext/', {'contextName': contextname, 'contextFile': contextfile, 'apikey': apikey})))

    def import_context(self, contextfile, apikey=''):
        """
        Imports a context from a file. If a relative file path is specified it will be resolved against the "contexts" directory in ZAP "home" dir.
        """
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'context/action/importContext/', {'contextFile': contextfile, 'apikey': apikey})))

    def include_context_technologies(self, contextname, technologynames, apikey=''):
        """
        Includes technologies with the given names, separated by a comma, to a context
        """
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'context/action/includeContextTechnologies/', {'contextName': contextname, 'technologyNames': technologynames, 'apikey': apikey})))

    def include_all_context_technologies(self, contextname, apikey=''):
        """
        Includes all built in technologies in to a context
        """
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'context/action/includeAllContextTechnologies/', {'contextName': contextname, 'apikey': apikey})))

    def exclude_context_technologies(self, contextname, technologynames, apikey=''):
        """
        Excludes technologies with the given names, separated by a comma, from a context
        """
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'context/action/excludeContextTechnologies/', {'contextName': contextname, 'technologyNames': technologynames, 'apikey': apikey})))

    def exclude_all_context_technologies(self, contextname, apikey=''):
        """
        Excludes all built in technologies from a context
        """
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'context/action/excludeAllContextTechnologies/', {'contextName': contextname, 'apikey': apikey})))

    def set_context_in_scope(self, contextname, booleaninscope, apikey=''):
        """
        Sets a context to in scope (contexts are in scope by default)
        """
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'context/action/setContextInScope/', {'contextName': contextname, 'booleanInScope': booleaninscope, 'apikey': apikey})))
