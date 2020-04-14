"""

Buildtest defaults, including environment variables and paths, are defined
or derived here.

"""

import pwd
import os

logID = "buildtest"

# each has a subfolder in buildtest/buildsystem/schemas/ with *.schema.json
supported_schemas = ["script"]

# global config sections that are known, added to buildbase.metadata
variable_sections = ["env"]
build_sections = ["pre_build", "build", "post_build", "pre_run", "run", "post_run"]
known_sections = variable_sections + build_sections

# Get user home based on effective uid, root of install to copy files
userhome = pwd.getpwuid(os.getuid())[5]
root = os.path.dirname(os.path.abspath(__file__))

# root of buildtest-framework user home, default shell
BUILDTEST_ROOT = os.path.join(userhome, ".buildtest")
BUILDTEST_SHELL = os.environ.get("SHELL", "/bin/bash")

# dictionary used for storing status of builds
BUILDTEST_SETTINGS_FILE = os.path.join(BUILDTEST_ROOT, "settings.yml")

# BUILDSPEC_DEFAULT_PATH is the root directory where Buildspec are found
# when using buildtest get to clone a buildtest test repo
BUILDSPEC_DEFAULT_PATH = os.path.join(BUILDTEST_ROOT, "site")
DEFAULT_SETTINGS_FILE = os.path.join(root, "settings", "settings.yml")
DEFAULT_SETTINGS_SCHEMA = os.path.join(root, "settings", "settings.schema.json")
EDITOR_LIST = ["vim", "emacs", "nano"]
