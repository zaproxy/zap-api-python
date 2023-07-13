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


class ajaxSpider(object):

    def __init__(self, zap):
        self.zap = zap

    @property
    def allowed_resources(self):
        """
        Gets the allowed resources. The allowed resources are always fetched even if out of scope, allowing to include necessary resources (e.g. scripts) from 3rd-parties.
        This component is optional and therefore the API will only work if it is installed
        """
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'ajaxSpider/view/allowedResources/')))

    def excluded_elements(self, contextname):
        """
        Gets the excluded elements. The excluded elements are not clicked during crawling, for example, to prevent logging out.
        This component is optional and therefore the API will only work if it is installed
        """
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'ajaxSpider/view/excludedElements/', {'contextName': contextname})))

    @property
    def status(self):
        """
        Gets the current status of the crawler. Actual values are Stopped and Running.
        This component is optional and therefore the API will only work if it is installed
        """
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'ajaxSpider/view/status/')))

    def results(self, start=None, count=None):
        """
        Gets the current results of the crawler.
        This component is optional and therefore the API will only work if it is installed
        """
        params = {}
        if start is not None:
            params['start'] = start
        if count is not None:
            params['count'] = count
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'ajaxSpider/view/results/', params)))

    @property
    def number_of_results(self):
        """
        Gets the number of resources found.
        This component is optional and therefore the API will only work if it is installed
        """
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'ajaxSpider/view/numberOfResults/')))

    @property
    def full_results(self):
        """
        Gets the full crawled content detected by the AJAX Spider. Returns a set of values based on 'inScope' URLs, 'outOfScope' URLs, and 'errors' encountered during the last/current run of the AJAX Spider.
        This component is optional and therefore the API will only work if it is installed
        """
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'ajaxSpider/view/fullResults/')))

    @property
    def option_browser_id(self):
        """
        Gets the configured browser to use for crawling.
        This component is optional and therefore the API will only work if it is installed
        """
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'ajaxSpider/view/optionBrowserId/')))

    @property
    def option_event_wait(self):
        """
        Gets the time to wait after an event (in milliseconds). For example: the wait delay after the cursor hovers over an element, in order for a menu to display, etc.
        This component is optional and therefore the API will only work if it is installed
        """
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'ajaxSpider/view/optionEventWait/')))

    @property
    def option_max_crawl_depth(self):
        """
        Gets the configured value for the max crawl depth.
        This component is optional and therefore the API will only work if it is installed
        """
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'ajaxSpider/view/optionMaxCrawlDepth/')))

    @property
    def option_max_crawl_states(self):
        """
        Gets the configured value for the maximum crawl states allowed.
        This component is optional and therefore the API will only work if it is installed
        """
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'ajaxSpider/view/optionMaxCrawlStates/')))

    @property
    def option_max_duration(self):
        """
        Gets the configured max duration of the crawl, the value is in minutes.
        This component is optional and therefore the API will only work if it is installed
        """
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'ajaxSpider/view/optionMaxDuration/')))

    @property
    def option_number_of_browsers(self):
        """
        Gets the configured number of browsers to be used.
        This component is optional and therefore the API will only work if it is installed
        """
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'ajaxSpider/view/optionNumberOfBrowsers/')))

    @property
    def option_reload_wait(self):
        """
        Gets the configured time to wait after reloading the page, this value is in milliseconds.
        This component is optional and therefore the API will only work if it is installed
        """
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'ajaxSpider/view/optionReloadWait/')))

    @property
    def option_click_default_elems(self):
        """
        Gets the configured value for 'Click Default Elements Only', HTML elements such as 'a', 'button', 'input', all associated with some action or links on the page.
        This component is optional and therefore the API will only work if it is installed
        """
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'ajaxSpider/view/optionClickDefaultElems/')))

    @property
    def option_click_elems_once(self):
        """
        Gets the value configured for the AJAX Spider to know if it should click on the elements only once.
        This component is optional and therefore the API will only work if it is installed
        """
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'ajaxSpider/view/optionClickElemsOnce/')))

    @property
    def option_random_inputs(self):
        """
        Gets if the AJAX Spider will use random values in form fields when crawling, if set to true.
        This component is optional and therefore the API will only work if it is installed
        """
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'ajaxSpider/view/optionRandomInputs/')))

    def scan(self, url=None, inscope=None, contextname=None, subtreeonly=None, apikey=''):
        """
        Runs the AJAX Spider against a given target.
        This component is optional and therefore the API will only work if it is installed
        """
        params = {'apikey': apikey}
        if url is not None:
            params['url'] = url
        if inscope is not None:
            params['inScope'] = inscope
        if contextname is not None:
            params['contextName'] = contextname
        if subtreeonly is not None:
            params['subtreeOnly'] = subtreeonly
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'ajaxSpider/action/scan/', params)))

    def scan_as_user(self, contextname, username, url=None, subtreeonly=None, apikey=''):
        """
        Runs the AJAX Spider from the perspective of a User of the web application.
        This component is optional and therefore the API will only work if it is installed
        """
        params = {'contextName': contextname, 'userName': username, 'apikey': apikey}
        if url is not None:
            params['url'] = url
        if subtreeonly is not None:
            params['subtreeOnly'] = subtreeonly
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'ajaxSpider/action/scanAsUser/', params)))

    def stop(self, apikey=''):
        """
        Stops the AJAX Spider.
        This component is optional and therefore the API will only work if it is installed
        """
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'ajaxSpider/action/stop/', {'apikey': apikey})))

    def add_allowed_resource(self, regex, enabled=None, apikey=''):
        """
        Adds an allowed resource.
        This component is optional and therefore the API will only work if it is installed
        """
        params = {'regex': regex, 'apikey': apikey}
        if enabled is not None:
            params['enabled'] = enabled
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'ajaxSpider/action/addAllowedResource/', params)))

    def add_excluded_element(self, contextname, description, element, xpath=None, text=None, attributename=None, attributevalue=None, enabled=None, apikey=''):
        """
        Adds an excluded element to a context.
        This component is optional and therefore the API will only work if it is installed
        """
        params = {'contextName': contextname, 'description': description, 'element': element, 'apikey': apikey}
        if xpath is not None:
            params['xpath'] = xpath
        if text is not None:
            params['text'] = text
        if attributename is not None:
            params['attributeName'] = attributename
        if attributevalue is not None:
            params['attributeValue'] = attributevalue
        if enabled is not None:
            params['enabled'] = enabled
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'ajaxSpider/action/addExcludedElement/', params)))

    def modify_excluded_element(self, contextname, description, element, descriptionnew=None, xpath=None, text=None, attributename=None, attributevalue=None, enabled=None, apikey=''):
        """
        Modifies an excluded element of a context.
        This component is optional and therefore the API will only work if it is installed
        """
        params = {'contextName': contextname, 'description': description, 'element': element, 'apikey': apikey}
        if descriptionnew is not None:
            params['descriptionNew'] = descriptionnew
        if xpath is not None:
            params['xpath'] = xpath
        if text is not None:
            params['text'] = text
        if attributename is not None:
            params['attributeName'] = attributename
        if attributevalue is not None:
            params['attributeValue'] = attributevalue
        if enabled is not None:
            params['enabled'] = enabled
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'ajaxSpider/action/modifyExcludedElement/', params)))

    def remove_excluded_element(self, contextname, description, apikey=''):
        """
        Removes an excluded element from a context.
        This component is optional and therefore the API will only work if it is installed
        """
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'ajaxSpider/action/removeExcludedElement/', {'contextName': contextname, 'description': description, 'apikey': apikey})))

    def remove_allowed_resource(self, regex, apikey=''):
        """
        Removes an allowed resource.
        This component is optional and therefore the API will only work if it is installed
        """
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'ajaxSpider/action/removeAllowedResource/', {'regex': regex, 'apikey': apikey})))

    def set_enabled_allowed_resource(self, regex, enabled, apikey=''):
        """
        Sets whether or not an allowed resource is enabled.
        This component is optional and therefore the API will only work if it is installed
        """
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'ajaxSpider/action/setEnabledAllowedResource/', {'regex': regex, 'enabled': enabled, 'apikey': apikey})))

    def set_option_browser_id(self, string, apikey=''):
        """
        Sets the configuration of the AJAX Spider to use one of the supported browsers.
        This component is optional and therefore the API will only work if it is installed
        """
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'ajaxSpider/action/setOptionBrowserId/', {'String': string, 'apikey': apikey})))

    def set_option_click_default_elems(self, boolean, apikey=''):
        """
        Sets whether or not the the AJAX Spider will only click on the default HTML elements.
        This component is optional and therefore the API will only work if it is installed
        """
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'ajaxSpider/action/setOptionClickDefaultElems/', {'Boolean': boolean, 'apikey': apikey})))

    def set_option_click_elems_once(self, boolean, apikey=''):
        """
        When enabled, the crawler attempts to interact with each element (e.g., by clicking) only once.
        This component is optional and therefore the API will only work if it is installed
        """
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'ajaxSpider/action/setOptionClickElemsOnce/', {'Boolean': boolean, 'apikey': apikey})))

    def set_option_event_wait(self, integer, apikey=''):
        """
        Sets the time to wait after an event (in milliseconds). For example: the wait delay after the cursor hovers over an element, in order for a menu to display, etc.
        This component is optional and therefore the API will only work if it is installed
        """
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'ajaxSpider/action/setOptionEventWait/', {'Integer': integer, 'apikey': apikey})))

    def set_option_max_crawl_depth(self, integer, apikey=''):
        """
        Sets the maximum depth that the crawler can reach.
        This component is optional and therefore the API will only work if it is installed
        """
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'ajaxSpider/action/setOptionMaxCrawlDepth/', {'Integer': integer, 'apikey': apikey})))

    def set_option_max_crawl_states(self, integer, apikey=''):
        """
        Sets the maximum number of states that the crawler should crawl.
        This component is optional and therefore the API will only work if it is installed
        """
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'ajaxSpider/action/setOptionMaxCrawlStates/', {'Integer': integer, 'apikey': apikey})))

    def set_option_max_duration(self, integer, apikey=''):
        """
        The maximum time that the crawler is allowed to run.
        This component is optional and therefore the API will only work if it is installed
        """
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'ajaxSpider/action/setOptionMaxDuration/', {'Integer': integer, 'apikey': apikey})))

    def set_option_number_of_browsers(self, integer, apikey=''):
        """
        Sets the number of windows to be used by AJAX Spider.
        This component is optional and therefore the API will only work if it is installed
        """
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'ajaxSpider/action/setOptionNumberOfBrowsers/', {'Integer': integer, 'apikey': apikey})))

    def set_option_random_inputs(self, boolean, apikey=''):
        """
        When enabled, inserts random values into form fields.
        This component is optional and therefore the API will only work if it is installed
        """
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'ajaxSpider/action/setOptionRandomInputs/', {'Boolean': boolean, 'apikey': apikey})))

    def set_option_reload_wait(self, integer, apikey=''):
        """
        Sets the time to wait after the page is loaded before interacting with it.
        This component is optional and therefore the API will only work if it is installed
        """
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'ajaxSpider/action/setOptionReloadWait/', {'Integer': integer, 'apikey': apikey})))
