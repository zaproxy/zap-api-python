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


class selenium(object):

    def __init__(self, zap):
        self.zap = zap

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
    def option_phantom_js_binary_path(self):
        """
        Returns the current path to PhantomJS binary
        This component is optional and therefore the API will only work if it is installed
        """
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'selenium/view/optionPhantomJsBinaryPath/')))

    def set_option_chrome_driver_path(self, string, apikey=''):
        """
        Sets the current path to ChromeDriver
        This component is optional and therefore the API will only work if it is installed
        """
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'selenium/action/setOptionChromeDriverPath/', {'String': string, 'apikey': apikey})))

    def set_option_firefox_binary_path(self, string, apikey=''):
        """
        Sets the current path to Firefox binary
        This component is optional and therefore the API will only work if it is installed
        """
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'selenium/action/setOptionFirefoxBinaryPath/', {'String': string, 'apikey': apikey})))

    def set_option_firefox_driver_path(self, string, apikey=''):
        """
        Sets the current path to Firefox driver (geckodriver)
        This component is optional and therefore the API will only work if it is installed
        """
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'selenium/action/setOptionFirefoxDriverPath/', {'String': string, 'apikey': apikey})))

    def set_option_ie_driver_path(self, string, apikey=''):
        """
        This component is optional and therefore the API will only work if it is installed
        """
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'selenium/action/setOptionIeDriverPath/', {'String': string, 'apikey': apikey})))

    def set_option_phantom_js_binary_path(self, string, apikey=''):
        """
        Sets the current path to PhantomJS binary
        This component is optional and therefore the API will only work if it is installed
        """
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'selenium/action/setOptionPhantomJsBinaryPath/', {'String': string, 'apikey': apikey})))
