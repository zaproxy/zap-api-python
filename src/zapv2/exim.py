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


class exim(object):

    def __init__(self, zap):
        self.zap = zap

    def import_har(self, filepath, apikey=''):
        """
        Imports a HAR file.
        This component is optional and therefore the API will only work if it is installed
        """
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'exim/action/importHar/', {'filePath': filepath, 'apikey': apikey})))

    def import_urls(self, filepath, apikey=''):
        """
        Imports URLs (one per line) from the file with the given file system path.
        This component is optional and therefore the API will only work if it is installed
        """
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'exim/action/importUrls/', {'filePath': filepath, 'apikey': apikey})))

    def import_zap_logs(self, filepath, apikey=''):
        """
        Imports previously exported ZAP messages from the file with the given file system path.
        This component is optional and therefore the API will only work if it is installed
        """
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'exim/action/importZapLogs/', {'filePath': filepath, 'apikey': apikey})))

    def import_modsec_2_logs(self, filepath, apikey=''):
        """
        Imports ModSecurity2 logs from the file with the given file system path.
        This component is optional and therefore the API will only work if it is installed
        """
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'exim/action/importModsec2Logs/', {'filePath': filepath, 'apikey': apikey})))

    def export_har(self, baseurl=None, start=None, count=None, apikey=''):
        """
        Gets the HTTP messages sent through/by ZAP, in HAR format, optionally filtered by URL and paginated with 'start' position and 'count' of messages
        This component is optional and therefore the API will only work if it is installed
        """
        params = {'apikey': apikey}
        if baseurl is not None:
            params['baseurl'] = baseurl
        if start is not None:
            params['start'] = start
        if count is not None:
            params['count'] = count
        return (self.zap._request_other(self.zap.base_other + 'exim/other/exportHar/', params))

    def export_har_by_id(self, ids, apikey=''):
        """
        Gets the HTTP messages with the given IDs, in HAR format.
        This component is optional and therefore the API will only work if it is installed
        """
        return (self.zap._request_other(self.zap.base_other + 'exim/other/exportHarById/', {'ids': ids, 'apikey': apikey}))

    def send_har_request(self, request, followredirects=None, apikey=''):
        """
        Sends the first HAR request entry, optionally following redirections. Returns, in HAR format, the request sent and response received and followed redirections, if any. The Mode is enforced when sending the request (and following redirections), custom manual requests are not allowed in 'Safe' mode nor in 'Protected' mode if out of scope.
        This component is optional and therefore the API will only work if it is installed
        """
        params = {'request': request, 'apikey': apikey}
        if followredirects is not None:
            params['followRedirects'] = followredirects
        return (self.zap._request_other(self.zap.base_other + 'exim/other/sendHarRequest/', params))
