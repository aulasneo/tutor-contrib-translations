from __future__ import annotations

import os.path
from glob import glob

import click
import pkg_resources
from tutor import hooks

from .__about__ import __version__

########################################
# CONFIGURATION
########################################

config = {
    # Add here your new settings
    "defaults": {
        "VERSION": __version__,
    },
    "unique": {},
    "overrides": {},
}

hooks.Filters.CONFIG_DEFAULTS.add_items(
    [(f"TRANSLATIONS_{key}", value) for key, value in config["defaults"].items()]
)

hooks.Filters.CONFIG_UNIQUE.add_items(
    [(f"TRANSLATIONS_{key}", value) for key, value in config["unique"].items()]
)

hooks.Filters.CONFIG_OVERRIDES.add_items(
    list(config["overrides"].items())
)


########################################
# TEMPLATE RENDERING
########################################

hooks.Filters.ENV_TEMPLATE_ROOTS.add_items(
    # Root paths for template files, relative to the project root.
    [
        pkg_resources.resource_filename("tutortranslations", "templates"),
    ]
)

hooks.Filters.ENV_TEMPLATE_TARGETS.add_items(
    # For each pair (source_path, destination_path):
    # templates at ``source_path`` (relative to your ENV_TEMPLATE_ROOTS) will be
    # rendered to ``source_path/destination_path`` (relative to your Tutor environment).
    # For example, ``tutortranslations/templates/mfe/build``
    # will be rendered to ``$(tutor config printroot)/env/plugins/mfe/build``.
    [
        ("openedx/locale", "build"),
        ("mfe/i18n/", "plugins/mfe/build")
    ],
)
