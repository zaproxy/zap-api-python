# Zed Attack Proxy (ZAP) and its related class files.
#
# ZAP is an HTTP/HTTPS proxy for assessing web application security.
#
# Copyright 2018 the ZAP development team
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


class websocket(object):

    def __init__(self, zap):
        self.zap = zap

    @property
    def channels(self):
        """
        Returns all of the registered web socket channels
        This component is optional and therefore the API will only work if it is installed
        """
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'websocket/view/channels/')))

    def message(self, channelid, messageid):
        """
        Returns full details of the message specified by the channelId and messageId
        This component is optional and therefore the API will only work if it is installed
        """
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'websocket/view/message/', {'channelId': channelid, 'messageId': messageid})))

    def messages(self, channelid=None, start=None, count=None, payloadpreviewlength=None):
        """
        Returns a list of all of the messages that meet the given criteria (all optional), where channelId is a channel identifier, start is the offset to start returning messages from (starting from 0), count is the number of messages to return (default no limit) and payloadPreviewLength is the maximum number bytes to return for the payload contents
        This component is optional and therefore the API will only work if it is installed
        """
        params = {}
        if channelid is not None:
            params['channelId'] = channelid
        if start is not None:
            params['start'] = start
        if count is not None:
            params['count'] = count
        if payloadpreviewlength is not None:
            params['payloadPreviewLength'] = payloadpreviewlength
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'websocket/view/messages/', params)))

    @property
    def break_text_message(self):
        """
        Returns a text representation of an intercepted websockets message
        This component is optional and therefore the API will only work if it is installed
        """
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'websocket/view/breakTextMessage/')))

    def send_text_message(self, channelid, outgoing, message, apikey=''):
        """
        Sends the specified message on the channel specified by channelId, if outgoing is 'True' then the message will be sent to the server and if it is 'False' then it will be sent to the client
        This component is optional and therefore the API will only work if it is installed
        """
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'websocket/action/sendTextMessage/', {'channelId': channelid, 'outgoing': outgoing, 'message': message, 'apikey': apikey})))

    def set_break_text_message(self, message, outgoing, apikey=''):
        """
        Sets the text message for an intercepted websockets message
        This component is optional and therefore the API will only work if it is installed
        """
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'websocket/action/setBreakTextMessage/', {'message': message, 'outgoing': outgoing, 'apikey': apikey})))
