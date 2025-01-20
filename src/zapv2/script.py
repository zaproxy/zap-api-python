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


class script(object):

    def __init__(self, zap):
        self.zap = zap

    @property
    def list_engines(self):
        """
        Lists the script engines available
        This component is optional and therefore the API will only work if it is installed
        """
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'script/view/listEngines/')))

    @property
    def list_types(self):
        """
        Lists the script types available.
        This component is optional and therefore the API will only work if it is installed
        """
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'script/view/listTypes/')))

    @property
    def list_scripts(self):
        """
        Lists the scripts available, with its engine, name, description, type and error state.
        This component is optional and therefore the API will only work if it is installed
        """
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'script/view/listScripts/')))

    def global_var(self, varkey):
        """
        Gets the value of the global variable with the given key. Returns an API error (DOES_NOT_EXIST) if no value was previously set.
        This component is optional and therefore the API will only work if it is installed
        """
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'script/view/globalVar/', {'varKey': varkey})))

    def global_custom_var(self, varkey):
        """
        Gets the value (string representation) of a global custom variable. Returns an API error (DOES_NOT_EXIST) if no value was previously set.
        This component is optional and therefore the API will only work if it is installed
        """
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'script/view/globalCustomVar/', {'varKey': varkey})))

    @property
    def global_vars(self):
        """
        Gets all the global variables (key/value pairs).
        This component is optional and therefore the API will only work if it is installed
        """
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'script/view/globalVars/')))

    @property
    def global_custom_vars(self):
        """
        Gets all the global custom variables (key/value pairs, the value is the string representation).
        This component is optional and therefore the API will only work if it is installed
        """
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'script/view/globalCustomVars/')))

    def script_var(self, scriptname, varkey):
        """
        Gets the value of the variable with the given key for the given script. Returns an API error (DOES_NOT_EXIST) if no script with the given name exists or if no value was previously set.
        This component is optional and therefore the API will only work if it is installed
        """
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'script/view/scriptVar/', {'scriptName': scriptname, 'varKey': varkey})))

    def script_custom_var(self, scriptname, varkey):
        """
        Gets the value (string representation) of a custom variable. Returns an API error (DOES_NOT_EXIST) if no script with the given name exists or if no value was previously set.
        This component is optional and therefore the API will only work if it is installed
        """
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'script/view/scriptCustomVar/', {'scriptName': scriptname, 'varKey': varkey})))

    def script_vars(self, scriptname):
        """
        Gets all the variables (key/value pairs) of the given script. Returns an API error (DOES_NOT_EXIST) if no script with the given name exists.
        This component is optional and therefore the API will only work if it is installed
        """
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'script/view/scriptVars/', {'scriptName': scriptname})))

    def script_custom_vars(self, scriptname):
        """
        Gets all the custom variables (key/value pairs, the value is the string representation) of a script. Returns an API error (DOES_NOT_EXIST) if no script with the given name exists.
        This component is optional and therefore the API will only work if it is installed
        """
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'script/view/scriptCustomVars/', {'scriptName': scriptname})))

    def enable(self, scriptname, apikey=''):
        """
        Enables the script with the given name
        This component is optional and therefore the API will only work if it is installed
        """
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'script/action/enable/', {'scriptName': scriptname})))

    def disable(self, scriptname, apikey=''):
        """
        Disables the script with the given name
        This component is optional and therefore the API will only work if it is installed
        """
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'script/action/disable/', {'scriptName': scriptname})))

    def load(self, scriptname, scripttype, scriptengine, filename, scriptdescription=None, charset=None, apikey=''):
        """
        Loads a script into ZAP from the given local file, with the given name, type and engine, optionally with a description, and a charset name to read the script (the charset name is required if the script is not in UTF-8, for example, in ISO-8859-1).
        This component is optional and therefore the API will only work if it is installed
        """
        params = {'scriptName': scriptname, 'scriptType': scripttype, 'scriptEngine': scriptengine, 'fileName': filename}
        if scriptdescription is not None:
            params['scriptDescription'] = scriptdescription
        if charset is not None:
            params['charset'] = charset
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'script/action/load/', params)))

    def remove(self, scriptname, apikey=''):
        """
        Removes the script with the given name
        This component is optional and therefore the API will only work if it is installed
        """
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'script/action/remove/', {'scriptName': scriptname})))

    def run_stand_alone_script(self, scriptname, apikey=''):
        """
        Runs the stand alone script with the given name
        This component is optional and therefore the API will only work if it is installed
        """
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'script/action/runStandAloneScript/', {'scriptName': scriptname})))

    def clear_global_var(self, varkey, apikey=''):
        """
        Clears the global variable with the given key.
        This component is optional and therefore the API will only work if it is installed
        """
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'script/action/clearGlobalVar/', {'varKey': varkey})))

    def clear_global_custom_var(self, varkey, apikey=''):
        """
        Clears a global custom variable.
        This component is optional and therefore the API will only work if it is installed
        """
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'script/action/clearGlobalCustomVar/', {'varKey': varkey})))

    def clear_global_vars(self, apikey=''):
        """
        Clears the global variables.
        This component is optional and therefore the API will only work if it is installed
        """
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'script/action/clearGlobalVars/', {})))

    def clear_script_var(self, scriptname, varkey, apikey=''):
        """
        Clears the variable with the given key of the given script. Returns an API error (DOES_NOT_EXIST) if no script with the given name exists.
        This component is optional and therefore the API will only work if it is installed
        """
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'script/action/clearScriptVar/', {'scriptName': scriptname, 'varKey': varkey})))

    def clear_script_custom_var(self, scriptname, varkey, apikey=''):
        """
        Clears a script custom variable.
        This component is optional and therefore the API will only work if it is installed
        """
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'script/action/clearScriptCustomVar/', {'scriptName': scriptname, 'varKey': varkey})))

    def clear_script_vars(self, scriptname, apikey=''):
        """
        Clears the variables of the given script. Returns an API error (DOES_NOT_EXIST) if no script with the given name exists.
        This component is optional and therefore the API will only work if it is installed
        """
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'script/action/clearScriptVars/', {'scriptName': scriptname})))

    def set_script_var(self, scriptname, varkey, varvalue=None, apikey=''):
        """
        Sets the value of the variable with the given key of the given script. Returns an API error (DOES_NOT_EXIST) if no script with the given name exists.
        This component is optional and therefore the API will only work if it is installed
        """
        params = {'scriptName': scriptname, 'varKey': varkey}
        if varvalue is not None:
            params['varValue'] = varvalue
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'script/action/setScriptVar/', params)))

    def set_global_var(self, varkey, varvalue=None, apikey=''):
        """
        Sets the value of the global variable with the given key.
        This component is optional and therefore the API will only work if it is installed
        """
        params = {'varKey': varkey}
        if varvalue is not None:
            params['varValue'] = varvalue
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'script/action/setGlobalVar/', params)))
