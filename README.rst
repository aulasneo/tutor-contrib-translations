translations plugin for `Tutor <https://docs.tutor.overhang.io>`__
===================================================================================

This plugin allows adding or overriding translations strings easily from the ``config.yml``.

.. image:: https://img.shields.io/badge/linting-pylint-yellowgreen
    :target: https://github.com/pylint-dev/pylint

Installation
------------

::

    pip install tutor-contrib-translations

Usage
-----

First, enable the plugin with

::

    tutor plugins enable translations


Translations are handled in a different way in the legacy Django HTML pages and
and in the MFEs.

Translating DJANGO legacy pages
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Add a ``TRANSLATIONS_OPENEDX`` entry to the configuration file.
Then add a key for each language in lower case. Finally add as many items as needed
using the original string in english as key and the translated text as value.

E.g.:

::

    TRANSLATIONS_OPENEDX:
        es:
            "Courses": "Cursos"
            "Certificate": "Certificado"

Translating MFE
~~~~~~~~~~~~~~~

Similarly, create an entry named ``TRANSLATIONS_MFE_<mfe name>``.
Then add a key for each language in lower case. Finally add as many items as needed
using the original string in english as key and the translated text as value.

E.g.:

::

    TRANSLATIONS_MFE_LEARNING:
        es:
            "Courses": "Cursos"
            "Certificate": "Certificado"

Save the configuration to apply the translations.
Finally, rebuild the ``openedx`` and or ``mfe`` images where the translations
have changed.


License
-------

This software is licensed under the terms of the AGPLv3.