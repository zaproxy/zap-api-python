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


class reports(object):

    def __init__(self, zap):
        self.zap = zap

    @property
    def templates(self):
        """
        View available templates.
        This component is optional and therefore the API will only work if it is installed
        """
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'reports/view/templates/')))

    def template_details(self, template):
        """
        View details of the specified template.
        This component is optional and therefore the API will only work if it is installed
        """
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'reports/view/templateDetails/', {'template': template})))

    def generate(self, title, template, theme=None, description=None, contexts=None, sites=None, sections=None, includedconfidences=None, includedrisks=None, reportfilename=None, reportfilenamepattern=None, reportdir=None, display=None, apikey=''):
        """
        Generate a report with the supplied parameters.
        This component is optional and therefore the API will only work if it is installed
        """
        params = {'title': title, 'template': template, 'apikey': apikey}
        if theme is not None:
            params['theme'] = theme
        if description is not None:
            params['description'] = description
        if contexts is not None:
            params['contexts'] = contexts
        if sites is not None:
            params['sites'] = sites
        if sections is not None:
            params['sections'] = sections
        if includedconfidences is not None:
            params['includedConfidences'] = includedconfidences
        if includedrisks is not None:
            params['includedRisks'] = includedrisks
        if reportfilename is not None:
            params['reportFileName'] = reportfilename
        if reportfilenamepattern is not None:
            params['reportFileNamePattern'] = reportfilenamepattern
        if reportdir is not None:
            params['reportDir'] = reportdir
        if display is not None:
            params['display'] = display
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'reports/action/generate/', params)))
