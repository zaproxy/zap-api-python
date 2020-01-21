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


class autoupdate(object):

    def __init__(self, zap):
        self.zap = zap

    @property
    def latest_version_number(self):
        """
        Returns the latest version number
        """
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'autoupdate/view/latestVersionNumber/')))

    @property
    def is_latest_version(self):
        """
        Returns 'true' if ZAP is on the latest version
        """
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'autoupdate/view/isLatestVersion/')))

    @property
    def installed_addons(self):
        """
        Return a list of all of the installed add-ons
        """
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'autoupdate/view/installedAddons/')))

    @property
    def local_addons(self):
        """
        Returns a list with all local add-ons, installed or not.
        """
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'autoupdate/view/localAddons/')))

    @property
    def new_addons(self):
        """
        Return a list of any add-ons that have been added to the Marketplace since the last check for updates
        """
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'autoupdate/view/newAddons/')))

    @property
    def updated_addons(self):
        """
        Return a list of any add-ons that have been changed in the Marketplace since the last check for updates
        """
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'autoupdate/view/updatedAddons/')))

    @property
    def marketplace_addons(self):
        """
        Return a list of all of the add-ons on the ZAP Marketplace (this information is read once and then cached)
        """
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'autoupdate/view/marketplaceAddons/')))

    @property
    def option_addon_directories(self):
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'autoupdate/view/optionAddonDirectories/')))

    @property
    def option_day_last_checked(self):
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'autoupdate/view/optionDayLastChecked/')))

    @property
    def option_day_last_install_warned(self):
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'autoupdate/view/optionDayLastInstallWarned/')))

    @property
    def option_day_last_update_warned(self):
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'autoupdate/view/optionDayLastUpdateWarned/')))

    @property
    def option_download_directory(self):
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'autoupdate/view/optionDownloadDirectory/')))

    @property
    def option_check_addon_updates(self):
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'autoupdate/view/optionCheckAddonUpdates/')))

    @property
    def option_check_on_start(self):
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'autoupdate/view/optionCheckOnStart/')))

    @property
    def option_download_new_release(self):
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'autoupdate/view/optionDownloadNewRelease/')))

    @property
    def option_install_addon_updates(self):
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'autoupdate/view/optionInstallAddonUpdates/')))

    @property
    def option_install_scanner_rules(self):
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'autoupdate/view/optionInstallScannerRules/')))

    @property
    def option_report_alpha_addons(self):
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'autoupdate/view/optionReportAlphaAddons/')))

    @property
    def option_report_beta_addons(self):
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'autoupdate/view/optionReportBetaAddons/')))

    @property
    def option_report_release_addons(self):
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'autoupdate/view/optionReportReleaseAddons/')))

    def download_latest_release(self, apikey=''):
        """
        Downloads the latest release, if any 
        """
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'autoupdate/action/downloadLatestRelease/', {'apikey': apikey})))

    def install_addon(self, id, apikey=''):
        """
        Installs or updates the specified add-on, returning when complete (i.e. not asynchronously)
        """
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'autoupdate/action/installAddon/', {'id': id, 'apikey': apikey})))

    def install_local_addon(self, file, apikey=''):
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'autoupdate/action/installLocalAddon/', {'file': file, 'apikey': apikey})))

    def uninstall_addon(self, id, apikey=''):
        """
        Uninstalls the specified add-on 
        """
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'autoupdate/action/uninstallAddon/', {'id': id, 'apikey': apikey})))

    def set_option_check_addon_updates(self, boolean, apikey=''):
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'autoupdate/action/setOptionCheckAddonUpdates/', {'Boolean': boolean, 'apikey': apikey})))

    def set_option_check_on_start(self, boolean, apikey=''):
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'autoupdate/action/setOptionCheckOnStart/', {'Boolean': boolean, 'apikey': apikey})))

    def set_option_download_new_release(self, boolean, apikey=''):
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'autoupdate/action/setOptionDownloadNewRelease/', {'Boolean': boolean, 'apikey': apikey})))

    def set_option_install_addon_updates(self, boolean, apikey=''):
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'autoupdate/action/setOptionInstallAddonUpdates/', {'Boolean': boolean, 'apikey': apikey})))

    def set_option_install_scanner_rules(self, boolean, apikey=''):
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'autoupdate/action/setOptionInstallScannerRules/', {'Boolean': boolean, 'apikey': apikey})))

    def set_option_report_alpha_addons(self, boolean, apikey=''):
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'autoupdate/action/setOptionReportAlphaAddons/', {'Boolean': boolean, 'apikey': apikey})))

    def set_option_report_beta_addons(self, boolean, apikey=''):
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'autoupdate/action/setOptionReportBetaAddons/', {'Boolean': boolean, 'apikey': apikey})))

    def set_option_report_release_addons(self, boolean, apikey=''):
        return six.next(six.itervalues(self.zap._request(self.zap.base + 'autoupdate/action/setOptionReportReleaseAddons/', {'Boolean': boolean, 'apikey': apikey})))
