"""
Setuptools file for tutor-contrib-translations.
"""
from __future__ import annotations

import importlib_resources
from tutor import hooks

from .__about__ import __version__

config = {
    # Add here your new settings
    "defaults": {
        "VERSION": __version__,
        "OPENEDX": {},
        "MFE_LEARNING": {},
        "MFE_ACCOUNT": {},
        "MFE_PROFILE": {}
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


# Add the "templates" folder as a template root
hooks.Filters.ENV_TEMPLATE_ROOTS.add_item(
    str(importlib_resources.files("tutortranslations") / "templates")
)

hooks.Filters.ENV_TEMPLATE_TARGETS.add_items(
    [
        ("openedx/locale", "build"),
        ("mfe/i18n/", "plugins/mfe/build")
    ],
)
