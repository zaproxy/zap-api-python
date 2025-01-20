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


class selenium(object):

    def __init__(self, zap):
        self.zap = zap

    @property
    def option_browser_extensions(self):
        """
        This component is optional and therefore the API will only work if it is installed
        """
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'selenium/view/optionBrowserExtensions/')))

    @property
    def option_chrome_binary_path(self):
        """
        Returns the current path to Chrome binary
        This component is optional and therefore the API will only work if it is installed
        """
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'selenium/view/optionChromeBinaryPath/')))

    @property
    def option_chrome_driver_path(self):
        """
        Returns the current path to ChromeDriver
        This component is optional and therefore the API will only work if it is installed
        """
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'selenium/view/optionChromeDriverPath/')))

    @property
    def option_firefox_binary_path(self):
        """
        Returns the current path to Firefox binary
        This component is optional and therefore the API will only work if it is installed
        """
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'selenium/view/optionFirefoxBinaryPath/')))

    @property
    def option_firefox_default_profile(self):
        """
        This component is optional and therefore the API will only work if it is installed
        """
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'selenium/view/optionFirefoxDefaultProfile/')))

    @property
    def option_firefox_driver_path(self):
        """
        Returns the current path to Firefox driver (geckodriver)
        This component is optional and therefore the API will only work if it is installed
        """
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'selenium/view/optionFirefoxDriverPath/')))

    @property
    def option_ie_driver_path(self):
        """
        This component is optional and therefore the API will only work if it is installed
        """
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'selenium/view/optionIeDriverPath/')))

    @property
    def option_last_directory(self):
        """
        This component is optional and therefore the API will only work if it is installed
        """
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'selenium/view/optionLastDirectory/')))

    @property
    def option_phantom_js_binary_path(self):
        """
        This component is optional and therefore the API will only work if it is installed
        """
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'selenium/view/optionPhantomJsBinaryPath/')))

    def get_browser_arguments(self, browser):
        """
        Gets the browser arguments.
        This component is optional and therefore the API will only work if it is installed
        """
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'selenium/view/getBrowserArguments/', {'browser': browser})))

    def set_option_chrome_binary_path(self, string, apikey=''):
        """
        Sets the current path to Chrome binary
        This component is optional and therefore the API will only work if it is installed
        """
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'selenium/action/setOptionChromeBinaryPath/', {'String': string})))

    def set_option_chrome_driver_path(self, string, apikey=''):
        """
        Sets the current path to ChromeDriver
        This component is optional and therefore the API will only work if it is installed
        """
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'selenium/action/setOptionChromeDriverPath/', {'String': string})))

    def set_option_firefox_binary_path(self, string, apikey=''):
        """
        Sets the current path to Firefox binary
        This component is optional and therefore the API will only work if it is installed
        """
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'selenium/action/setOptionFirefoxBinaryPath/', {'String': string})))

    def set_option_firefox_default_profile(self, string, apikey=''):
        """
        This component is optional and therefore the API will only work if it is installed
        """
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'selenium/action/setOptionFirefoxDefaultProfile/', {'String': string})))

    def set_option_firefox_driver_path(self, string, apikey=''):
        """
        Sets the current path to Firefox driver (geckodriver)
        This component is optional and therefore the API will only work if it is installed
        """
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'selenium/action/setOptionFirefoxDriverPath/', {'String': string})))

    def set_option_ie_driver_path(self, string, apikey=''):
        """
        This component is optional and therefore the API will only work if it is installed
        """
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'selenium/action/setOptionIeDriverPath/', {'String': string})))

    def set_option_last_directory(self, string, apikey=''):
        """
        This component is optional and therefore the API will only work if it is installed
        """
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'selenium/action/setOptionLastDirectory/', {'String': string})))

    def set_option_phantom_js_binary_path(self, string, apikey=''):
        """
        This component is optional and therefore the API will only work if it is installed
        """
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'selenium/action/setOptionPhantomJsBinaryPath/', {'String': string})))

    def add_browser_argument(self, browser, argument, enabled=None, apikey=''):
        """
        Adds a browser argument.
        This component is optional and therefore the API will only work if it is installed
        """
        params = {'browser': browser, 'argument': argument}
        if enabled is not None:
            params['enabled'] = enabled
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'selenium/action/addBrowserArgument/', params)))

    def launch_browser(self, browser, apikey=''):
        """
        Launches a browser proxying through ZAP, for manual usage.
        This component is optional and therefore the API will only work if it is installed
        """
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'selenium/action/launchBrowser/', {'browser': browser})))

    def remove_browser_argument(self, browser, argument, apikey=''):
        """
        Removes a browser argument.
        This component is optional and therefore the API will only work if it is installed
        """
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'selenium/action/removeBrowserArgument/', {'browser': browser, 'argument': argument})))

    def set_browser_argument_enabled(self, browser, argument, enabled, apikey=''):
        """
        Sets whether or not a browser argument is enabled.
        This component is optional and therefore the API will only work if it is installed
        """
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'selenium/action/setBrowserArgumentEnabled/', {'browser': browser, 'argument': argument, 'enabled': enabled})))
