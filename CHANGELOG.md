# Changelog
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](http://keepachangelog.com/en/1.0.0/).

## [Unreleased]
### Changed
 - Python 2.7 is no longer supported.

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

[Unreleased]: https://github.com/zaproxy/zap-api-python/compare/0.0.18...HEAD
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
