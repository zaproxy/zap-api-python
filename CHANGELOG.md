# Changelog
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](http://keepachangelog.com/en/1.0.0/).

## [Unreleased]

## [0.4.0] - 2025-01-20
### Changed
- Update APIs for 2.16.

## [0.3.2] - 2024-06-04
### Fixed
- Return the whole response from `stats.stats`.

## [0.3.1] - 2024-05-20
### Fixed
- Return the whole response from `automation.plan_progress`.

## [0.3.0] - 2024-05-09
### Added
- Add the API of the following add-on:
  - Custom Payloads version 0.13.0.

### Changed
- Update core APIs for 2.15.

### Fixed
- Return the whole response from `users.get_user_by_id`.

## [0.2.0] - 2023-11-03
### Changed
- Update core APIs for 2.14.
- Update the APIs of the following add-on:
  - Selenium version 15.15.0.
- Allow to call the ZAP API with custom HTTP method and body (e.g. file upload).

### Deprecated
- The parameter `apikey` in the functions is no longer functional and will be removed in a future version.
  The API key should be set when creating the API client (i.e. `ZAPv2(apikey='MyApiKey')`), which was added in the version 0.0.9, seven years ago.
- The class `localProxies` will be removed in a future version, having been superseded by `network`.

### Removed
- The classes `exportreport`, `importLogFiles`, and `importurls` were removed as the corresponding add-ons no longer exist.

## [0.1.1] - 2023-08-09
### Fixed
- Correct module version.
- Use download link from PyPI.

## [0.1.0] - 2023-08-09
### Changed
- Rename package from `python-owasp-zap-v2.4` to `zaproxy`.

## [0.0.22] - 2023-07-13
### Changed
- Update core APIs for 2.13.
- Update the APIs of the following add-ons:
  - AJAX Spider version 23.15.0;
  - Alert Filters version 17;
  - GraphQL Support version 0.18.0;
  - Network version 0.10.0;
  - Selenium version 15.13.0;
  - Spider version 0.5.0.

## [0.0.21] - 2022-10-28
### Added
- Add the API of the following add-on:
  - Import/Export version 0.3.0.

### Changed
- Update core APIs for 2.12.
- Update the APIs of the following add-ons:
  - Network version 0.3.0;
  - Replacer version 11;
  - Selenium version 15.11.0;
  - Spider version 0.1.0.

## [0.0.20] - 2022-02-09
### Changed
- Update core APIs for 2.11.1
- Update all add-on APIs

## [0.0.19] - 2021-10-08
### Added
- Add the APIs of the following add-ons:
  - Automation Framework version 0.7.0;
  - Report Generation add-on, version 0.8.0;
  - Retest version 0.2.0.

### Changed
- Python 2.7 is no longer supported.
- Update core APIs for 2.11.
- Update the APIs of the following add-ons:
  - Ajax Spider version 23.6.0;
  - Alert Filters version 13;
  - GraphQL Support version 0.6.0;
  - OpenAPI Support version 23;
  - Replacer version 9.

## [0.0.18] - 2020-12-18
### Changed
- Core APIs updated for ZAP version 2.10.0.
- Update APIs from add-ons:
 - AJAX Spider;
 - GraphQL.

## [0.0.17] - 2020-10-14
### Added
- Add API for GraphQL add-on, version 0.2.0.

### Changed
- Fix typos in error messages.

## [0.0.16] - 2020-01-22
### Added
- Core APIs.
- APIs from add-ons:
 - Access Control Testing;
 - Export Report;
 - Revisit;
 - Wappalyzer - Technology Detection.

### Changed
- Core APIs updated for ZAP version 2.9.0.
- Update APIs from add-ons:
 - Alert Filters;
 - OpenAPI Support;
 - Replacer.

## [0.0.15] - 2019-06-14
### Added
- Add API for Context Alert Filters add-on, version 8.
- Add API for WebSockets add-on, version 19.
- Add API for SOAP Scanner add-on, version 3.

### Changed
- Minimum Python 3 version is now 3.4.
- Update Selenium API, per release of version 15.0.0.
- Update core APIs for ZAP 2.8.0.
- Allow to validate the status code returned by the ZAP API, to fail
sooner if the API request was not successful. This can be enabled when
instantiating the `ZAPv2` class with the argument `validate_status_code`
set to `True`.
- Update Replacer API, per release of version 7.
- Add description to Importurls API endpoint.

## [0.0.14] - 2017-12-04
### Changed
- Correct package descriptions for ZAP 2.7.0.

## [0.0.13] - 2017-11-29
### Changed
- Update core APIs for ZAP 2.7.0.
- Update APIs of the add-ons Ajax Spider, Reveal, and Selenium to update
its docs.

## [0.0.12] - 2017-06-27
### Changed
- Add `openaapi` to `ZAPv2` class.

## [0.0.11] - 2017-06-23
### Added
- Add API for Import files containing URLs add-on.
- Add API for Replacer add-on, version 1.

### Changed
- Update API of OpenAPI Support add-on, version 6.

## [0.0.10] - 2017-05-12
### Added
- Add `__version__`.
- Add API of OpenAPI Support add-on.

### Changed
- Update for Python 3.

## [0.0.9] - 2017-03-27
### Changed
- Update core APIs for ZAP 2.6.0.
- Allow to supply the API key when instantiating the class `ZAPv2`, to
ensure it's automatically sent in all API requests.

## [0.0.8] - 2016-06-03
### Changed
- Moved from the main `zaproxy` repository.

[Unreleased]: https://github.com/zaproxy/zap-api-python/compare/0.4.0...HEAD
[0.4.0]: https://github.com/zaproxy/zap-api-python/compare/0.3.2...0.4.0
[0.3.2]: https://github.com/zaproxy/zap-api-python/compare/0.3.1...0.3.2
[0.3.1]: https://github.com/zaproxy/zap-api-python/compare/0.3.0...0.3.1
[0.3.0]: https://github.com/zaproxy/zap-api-python/compare/0.2.0...0.3.0
[0.2.0]: https://github.com/zaproxy/zap-api-python/compare/0.1.1...0.2.0
[0.1.1]: https://github.com/zaproxy/zap-api-python/compare/0.1.0...0.1.1
[0.1.0]: https://github.com/zaproxy/zap-api-python/compare/0.0.22...0.1.0
[0.0.22]: https://github.com/zaproxy/zap-api-python/compare/0.0.21...0.0.22
[0.0.21]: https://github.com/zaproxy/zap-api-python/compare/0.0.20...0.0.21
[0.0.20]: https://github.com/zaproxy/zap-api-python/compare/0.0.19...0.0.20
[0.0.19]: https://github.com/zaproxy/zap-api-python/compare/0.0.18...0.0.19
[0.0.18]: https://github.com/zaproxy/zap-api-python/compare/0.0.17...0.0.18
[0.0.17]: https://github.com/zaproxy/zap-api-python/compare/0.0.16...0.0.17
[0.0.16]: https://github.com/zaproxy/zap-api-python/compare/0.0.15...0.0.16
[0.0.15]: https://github.com/zaproxy/zap-api-python/compare/0.0.14...0.0.15
[0.0.14]: https://github.com/zaproxy/zap-api-python/compare/0.0.13...0.0.14
[0.0.13]: https://github.com/zaproxy/zap-api-python/compare/0.0.12...0.0.13
[0.0.12]: https://github.com/zaproxy/zap-api-python/compare/0.0.11...0.0.12
[0.0.11]: https://github.com/zaproxy/zap-api-python/compare/0.0.10...0.0.11
[0.0.10]: https://github.com/zaproxy/zap-api-python/compare/0.0.9...0.0.10
[0.0.9]: https://github.com/zaproxy/zap-api-python/compare/0.0.8...0.0.9
[0.0.8]: https://github.com/zaproxy/zap-api-python/compare/98ce6066deba2c65eb992489311e146fff9b3430...0.0.8
