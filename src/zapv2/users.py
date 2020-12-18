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


class users(object):

    def __init__(self, zap):
        self.zap = zap

    def users_list(self, contextid=None):
        """
        Gets a list of users that belong to the context with the given ID, or all users if none provided.
        """
        params = {}
        if contextid is not None:
            params['contextId'] = contextid
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'users/view/usersList/', params)))

    def get_user_by_id(self, contextid, userid):
        """
        Gets the data of the user with the given ID that belongs to the context with the given ID.
        """
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'users/view/getUserById/', {'contextId': contextid, 'userId': userid})))

    def get_authentication_credentials_config_params(self, contextid):
        """
        Gets the configuration parameters for the credentials of the context with the given ID.
        """
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'users/view/getAuthenticationCredentialsConfigParams/', {'contextId': contextid})))

    def get_authentication_credentials(self, contextid, userid):
        """
        Gets the authentication credentials of the user with given ID that belongs to the context with the given ID.
        """
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'users/view/getAuthenticationCredentials/', {'contextId': contextid, 'userId': userid})))

    def get_authentication_state(self, contextid, userid):
        """
        Gets the authentication state information for the user identified by the Context and User Ids.
        """
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'users/view/getAuthenticationState/', {'contextId': contextid, 'userId': userid})))

    def get_authentication_session(self, contextid, userid):
        """
        Gets the authentication session information for the user identified by the Context and User Ids, e.g. cookies and realm credentials.
        """
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'users/view/getAuthenticationSession/', {'contextId': contextid, 'userId': userid})))

    def new_user(self, contextid, name, apikey=''):
        """
        Creates a new user with the given name for the context with the given ID.
        """
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'users/action/newUser/', {'contextId': contextid, 'name': name, 'apikey': apikey})))

    def remove_user(self, contextid, userid, apikey=''):
        """
        Removes the user with the given ID that belongs to the context with the given ID.
        """
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'users/action/removeUser/', {'contextId': contextid, 'userId': userid, 'apikey': apikey})))

    def set_user_enabled(self, contextid, userid, enabled, apikey=''):
        """
        Sets whether or not the user, with the given ID that belongs to the context with the given ID, should be enabled.
        """
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'users/action/setUserEnabled/', {'contextId': contextid, 'userId': userid, 'enabled': enabled, 'apikey': apikey})))

    def set_user_name(self, contextid, userid, name, apikey=''):
        """
        Renames the user with the given ID that belongs to the context with the given ID.
        """
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'users/action/setUserName/', {'contextId': contextid, 'userId': userid, 'name': name, 'apikey': apikey})))

    def set_authentication_credentials(self, contextid, userid, authcredentialsconfigparams=None, apikey=''):
        """
        Sets the authentication credentials for the user with the given ID that belongs to the context with the given ID.
        """
        params = {'contextId': contextid, 'userId': userid, 'apikey': apikey}
        if authcredentialsconfigparams is not None:
            params['authCredentialsConfigParams'] = authcredentialsconfigparams
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'users/action/setAuthenticationCredentials/', params)))

    def authenticate_as_user(self, contextid, userid, apikey=''):
        """
        Tries to authenticate as the identified user, returning the authentication request and whether it appears to have succeeded.
        """
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'users/action/authenticateAsUser/', {'contextId': contextid, 'userId': userid, 'apikey': apikey})))

    def poll_as_user(self, contextid, userid, apikey=''):
        """
        Tries to poll as the identified user, returning the authentication request and whether it appears to have succeeded. This will only work if the polling verification strategy has been configured.
        """
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'users/action/pollAsUser/', {'contextId': contextid, 'userId': userid, 'apikey': apikey})))

    def set_authentication_state(self, contextid, userid, lastpollresult=None, lastpolltimeinms=None, requestssincelastpoll=None, apikey=''):
        """
        Sets fields in the authentication state for the user identified by the Context and User Ids.
        """
        params = {'contextId': contextid, 'userId': userid, 'apikey': apikey}
        if lastpollresult is not None:
            params['lastPollResult'] = lastpollresult
        if lastpolltimeinms is not None:
            params['lastPollTimeInMs'] = lastpolltimeinms
        if requestssincelastpoll is not None:
            params['requestsSinceLastPoll'] = requestssincelastpoll
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'users/action/setAuthenticationState/', params)))

    def set_cookie(self, contextid, userid, domain, name, value, path=None, secure=None, apikey=''):
        """
        Sets the specified cookie for the user identified by the Context and User Ids.
        """
        params = {'contextId': contextid, 'userId': userid, 'domain': domain, 'name': name, 'value': value, 'apikey': apikey}
        if path is not None:
            params['path'] = path
        if secure is not None:
            params['secure'] = secure
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'users/action/setCookie/', params)))
