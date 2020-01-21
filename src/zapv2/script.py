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


class script(object):

    def __init__(self, zap):
        self.zap = zap

    @property
    def list_engines(self):
        """
        Lists the script engines available
        """
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'script/view/listEngines/')))

    @property
    def list_types(self):
        """
        Lists the script types available.
        """
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'script/view/listTypes/')))

    @property
    def list_scripts(self):
        """
        Lists the scripts available, with its engine, name, description, type and error state.
        """
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'script/view/listScripts/')))

    def global_var(self, varkey):
        """
        Gets the value of the global variable with the given key. Returns an API error (DOES_NOT_EXIST) if no value was previously set.
        """
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'script/view/globalVar/', {'varKey': varkey})))

    def global_custom_var(self, varkey):
        """
        Gets the value (string representation) of a global custom variable. Returns an API error (DOES_NOT_EXIST) if no value was previously set.
        """
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'script/view/globalCustomVar/', {'varKey': varkey})))

    @property
    def global_vars(self):
        """
        Gets all the global variables (key/value pairs).
        """
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'script/view/globalVars/')))

    @property
    def global_custom_vars(self):
        """
        Gets all the global custom variables (key/value pairs, the value is the string representation).
        """
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'script/view/globalCustomVars/')))

    def script_var(self, scriptname, varkey):
        """
        Gets the value of the variable with the given key for the given script. Returns an API error (DOES_NOT_EXIST) if no script with the given name exists or if no value was previously set.
        """
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'script/view/scriptVar/', {'scriptName': scriptname, 'varKey': varkey})))

    def script_custom_var(self, scriptname, varkey):
        """
        Gets the value (string representation) of a custom variable. Returns an API error (DOES_NOT_EXIST) if no script with the given name exists or if no value was previously set.
        """
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'script/view/scriptCustomVar/', {'scriptName': scriptname, 'varKey': varkey})))

    def script_vars(self, scriptname):
        """
        Gets all the variables (key/value pairs) of the given script. Returns an API error (DOES_NOT_EXIST) if no script with the given name exists.
        """
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'script/view/scriptVars/', {'scriptName': scriptname})))

    def script_custom_vars(self, scriptname):
        """
        Gets all the custom variables (key/value pairs, the value is the string representation) of a script. Returns an API error (DOES_NOT_EXIST) if no script with the given name exists.
        """
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'script/view/scriptCustomVars/', {'scriptName': scriptname})))

    def enable(self, scriptname, apikey=''):
        """
        Enables the script with the given name
        """
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'script/action/enable/', {'scriptName': scriptname, 'apikey': apikey})))

    def disable(self, scriptname, apikey=''):
        """
        Disables the script with the given name
        """
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'script/action/disable/', {'scriptName': scriptname, 'apikey': apikey})))

    def load(self, scriptname, scripttype, scriptengine, filename, scriptdescription=None, charset=None, apikey=''):
        """
        Loads a script into ZAP from the given local file, with the given name, type and engine, optionally with a description, and a charset name to read the script (the charset name is required if the script is not in UTF-8, for example, in ISO-8859-1).
        """
        params = {'scriptName': scriptname, 'scriptType': scripttype, 'scriptEngine': scriptengine, 'fileName': filename, 'apikey': apikey}
        if scriptdescription is not None:
            params['scriptDescription'] = scriptdescription
        if charset is not None:
            params['charset'] = charset
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'script/action/load/', params)))

    def remove(self, scriptname, apikey=''):
        """
        Removes the script with the given name
        """
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'script/action/remove/', {'scriptName': scriptname, 'apikey': apikey})))

    def run_stand_alone_script(self, scriptname, apikey=''):
        """
        Runs the stand alone script with the given name
        """
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'script/action/runStandAloneScript/', {'scriptName': scriptname, 'apikey': apikey})))

    def clear_global_var(self, varkey, apikey=''):
        """
        Clears the global variable with the given key.
        """
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'script/action/clearGlobalVar/', {'varKey': varkey, 'apikey': apikey})))

    def clear_global_custom_var(self, varkey, apikey=''):
        """
        Clears a global custom variable.
        """
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'script/action/clearGlobalCustomVar/', {'varKey': varkey, 'apikey': apikey})))

    def clear_global_vars(self, apikey=''):
        """
        Clears the global variables.
        """
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'script/action/clearGlobalVars/', {'apikey': apikey})))

    def clear_script_var(self, scriptname, varkey, apikey=''):
        """
        Clears the variable with the given key of the given script. Returns an API error (DOES_NOT_EXIST) if no script with the given name exists.
        """
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'script/action/clearScriptVar/', {'scriptName': scriptname, 'varKey': varkey, 'apikey': apikey})))

    def clear_script_custom_var(self, scriptname, varkey, apikey=''):
        """
        Clears a script custom variable.
        """
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'script/action/clearScriptCustomVar/', {'scriptName': scriptname, 'varKey': varkey, 'apikey': apikey})))

    def clear_script_vars(self, scriptname, apikey=''):
        """
        Clears the variables of the given script. Returns an API error (DOES_NOT_EXIST) if no script with the given name exists.
        """
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'script/action/clearScriptVars/', {'scriptName': scriptname, 'apikey': apikey})))

    def set_script_var(self, scriptname, varkey, varvalue=None, apikey=''):
        """
        Sets the value of the variable with the given key of the given script. Returns an API error (DOES_NOT_EXIST) if no script with the given name exists.
        """
        params = {'scriptName': scriptname, 'varKey': varkey, 'apikey': apikey}
        if varvalue is not None:
            params['varValue'] = varvalue
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'script/action/setScriptVar/', params)))

    def set_global_var(self, varkey, varvalue=None, apikey=''):
        """
        Sets the value of the global variable with the given key.
        """
        params = {'varKey': varkey, 'apikey': apikey}
        if varvalue is not None:
            params['varValue'] = varvalue
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'script/action/setGlobalVar/', params)))
