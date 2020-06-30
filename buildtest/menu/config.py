import os
import sys
from jsonschema import ValidationError
from shutil import copy
from buildtest.config import get_default_settings, check_settings
from buildtest.defaults import (
    BUILDTEST_SETTINGS_FILE,
    DEFAULT_SETTINGS_FILE,
)


def func_config_validate(args=None):
    """This method implements ``buildtest config validate`` which attempts to
       validate buildtest settings with schema. If it not validate an exception
       an exception of type SystemError is raised. We invoke ``check_settings``
       method which will validate the configuration, if it fails we except an exception
       of type ValidationError which we catch and print message.
    """
    try:
        check_settings()
    except ValidationError as err:
        print(err)
        raise sys.exit(f"{BUILDTEST_SETTINGS_FILE} is not valid")

    print(f"{BUILDTEST_SETTINGS_FILE} is valid")


def func_config_edit(args=None):
    """Edit buildtest configuration in editor. This implements ``buildtest config edit``"""

    config_opts = get_default_settings()

    while True:
        success = True
        os.system(f"{config_opts['config']['editor']} {BUILDTEST_SETTINGS_FILE}")
        try:
            check_settings(run_init=False)
        except ValidationError as err:
            print(err)
            input("Press any key to continue")
            success = False

        if success:
            break


def func_config_view(args=None):
    """View buildtest configuration file. This implements ``buildtest config view``"""

    os.system(f"cat {BUILDTEST_SETTINGS_FILE}")


def func_config_reset(args=None):
    """Reset buildtest configuration by copying default configuration provided by buildtest to
       $HOME/.buildtest/settings.yml. This implements ``buildtest config reset`` command."""

    print(f"Restoring from default configuration: {DEFAULT_SETTINGS_FILE}")
    copy(DEFAULT_SETTINGS_FILE, BUILDTEST_SETTINGS_FILE)
