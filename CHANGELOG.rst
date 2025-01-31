Change Log
----------

..
   All enhancements and patches to openedx_events will be documented
   in this file.  It adheres to the structure of https://keepachangelog.com/ ,
   but in reStructuredText instead of Markdown (for ease of incorporation into
   Sphinx documentation and the PyPI description).

   This project adheres to Semantic Versioning (https://semver.org/).

.. There should always be an "Unreleased" section for changes pending release.

Unreleased
~~~~~~~~~~

[0.6.0] - 2021-09-15
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Added
_____
* Add custom formatting class for events responses.
* Add a way to use send method instead of send_robust while testing.

Changed
_______
* Remove unnecessary InstantiationError exception.
* Default is send_robust instead of send unless specified otherwise.

[0.5.1] - 2021-08-26
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Changed
_______
* Remove TestCase inheritance from OpenEdxTestMixin.

[0.5.0] - 2021-08-24
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Added
_____
* Utilities to use while testing in other platforms.

[0.4.1] - 2021-08-18
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Changed
_______
* Remove raise_exception assignment in events metadata.

[0.4.0] - 2021-08-18
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Added
_____
* Preliminary Open edX events definitions.

[0.3.0] - 2021-08-18
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Added
_____
* Add tooling needed to create and trigger events in Open edX platform.
* Add Data Attribute classes used as arguments by Open edX Events.


[0.2.0] - 2021-07-28
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Changed
_______

* Update reposirtory purpose.
* Changed max-doc-length from 79 to 120 following community recommendation.

[0.1.3] - 2021-07-01
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Changed
_______

* Update setup.cfg with complete bumpversion configuration.

[0.1.2] - 2021-06-29
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Changed
_______

* Update documentation with current organization info.

[0.1.1] - 2021-06-29
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Added
_____

* Add Django testing configuration.

[0.1.0] - 2021-04-07
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Added
_____

* First release on PyPI.
